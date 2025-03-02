import glob, os, re, copy, json


class docstring_enhancer:
    """ Class to autogenerate a Python wrapper and JSON formatted interface to the OpenDSS DLL.
    Uses regular expressions to extract as much information as possible from the DDLL PAS files.
    """

    def __init__(self, path_ddll: str=r"C:\EPRI\OpenDSS\Version8\Source\DDLL"):

        self.classes = {} # Where the relevant data from the PAS files is stored
        self.update_interface_documentation(path_ddll)

    def update_interface_documentation(self, path_ddll: str):
        """ Function to loop through the DDLL classes to collect the relevant information for the interface and update
        the modes description. """

        # Load documentation JSON
        with open("docs.json") as f:
            docs = json.load(f)

        # file_struct = {dictionary['title'].lower() : {'file': dictionary['file'], 'functions': {child['title'].lower(): child['file'] for child in dictionary['children']}} for dictionary in docs["sections"][8]['children'][1:]}
        file_struct = {dictionary['title'].lower() : {'file': dictionary['file'], 'functions': {child['title'].lower(): child['file'] for child in dictionary['children']}} for dictionary in docs["sections"][9]['children']}

        pas_files = glob.glob(os.path.join(path_ddll, "*.pas"))
        for pas_file in pas_files:
            # Read through and get what is needed


            with open(pas_file) as f:
                all = f.read()
                doc_string = self.extract_text_between_markers(all, pattern=r'unit\s+\w+;\s*\r?\n((?://.*\r?\n)+)\s*interface').strip()
                has_doc_string = len(doc_string) > 0

            with open(pas_file) as f:
                current_unit_name = None
                current_function_name = None
                found_unit_name = False
                found_implementation = False
                found_interface = False
                new_lines = []
                files = None

                for line_old in f.readlines():
                    line_new = line_old
                    line = line_old.strip()
                    unit_name = self.find_pattern(line, r"unit\s+([A-Za-z]\w*);")
                    interface = "interface" in line.lower() and "//" not in line.lower()
                    implementation = "implementation" in line.lower() and "//" not in line.lower()
                    lines_to_add = []

                    if not found_unit_name and len(unit_name) > 0 and unit_name[0][0] == "D":
                        found_unit_name = True
                        current_unit_name = unit_name[0]
                        self.classes[current_unit_name] = {}

                        try:
                            if current_unit_name == "DDSSExecutive":
                                files = file_struct[f"DSS_Executive Interface".lower()]
                            elif current_unit_name == "DIDSSProperty":
                                files = file_struct[f"DSSProperties Interface".lower()]
                            elif current_unit_name in ("DISource", "DLoadShape"):
                                files = file_struct[f"{current_unit_name[1:]}s Interface".lower()]
                            elif current_unit_name == "DWindGens":
                                files = file_struct[f"{current_unit_name[1:]}".lower()]
                            elif current_unit_name in ("DYMatrix",):
                                new_lines.append(line_new)
                                continue
                            else:
                                files = file_struct[f"{current_unit_name[1:].lower()} interface"]
                            with open(fr"markdown\{files['file']}", encoding='utf-8') as doc:
                                doc_string = doc.read()
                            doc_string = self.extract_text_between_markers(doc_string, pattern = r'(?s)(#.*?)(?=\n\*\*\*)')
                            doc_string = doc_string[1:].replace("\n\n&nbsp;\n\n", "\n").strip().split("\n")
                            if not has_doc_string:
                                for descr in doc_string:
                                    descr = descr.replace('\u201C', '"')  # Replace left double quote
                                    descr = descr.replace('\u201D', '"')  # Replace right double quote  # Replace right double quote
                                    descr = descr.replace('\u2018', "'")  # Replace left single quote
                                    descr = descr.replace('\u2019', "'")  # Replace right single quote
                                    lines_to_add.append(f"// {descr}\n")
                        except:
                            print(f"Unable to find data for {current_unit_name}")
                        new_lines.append(line_new)
                        new_lines.extend(lines_to_add)
                        continue

                    elif found_unit_name and not found_interface and interface is True:
                        found_interface = True

                    elif found_unit_name and not found_implementation and implementation is True:
                        found_implementation = True

                    elif found_interface and not found_implementation:
                        # Find the patterns for each function or procedure declarations
                        func_proc_name = self.find_function_names(line)
                        if len(func_proc_name) > 0:
                            self.classes[current_unit_name][func_proc_name[0][1]] = {'details': {}, 'modes': []}
                    elif found_implementation:
                        # Find the patterns for each function or procedure
                        func_proc_name = self.find_function_names(line)
                        func_proc_details = self.find_function_details(line)
                        if len(func_proc_name) > 0 and len(func_proc_details) > 0:

                            if current_function_name != func_proc_name[0]:
                                current_function_name = func_proc_name[0]
                                if current_function_name[1] in self.classes[current_unit_name].keys():
                                    self.classes[current_unit_name][current_function_name[1]]['details'] = copy.deepcopy(func_proc_details[0])

                        elif len(func_proc_name) > 0 and len(func_proc_details) == 0:
                            print(func_proc_name, "Lacks details")

                        mode_output = self.find_numbered_begins(line)

                        mode_done = False
                        if len(mode_output) > 0 and any([mode_output[0]["number"] == existing["number"] for existing in self.classes[current_unit_name][current_function_name[1]]['modes']]):
                            if current_unit_name != 'DDSSProgress':
                                mode_done = True

                        if len(mode_output) > 0 and not mode_done:
                            if len(mode_output[0]["comment"].split(": ")) >= 3:  # Pas file has been updated with "Mode #: ClassNAme.Attribute: Description text"
                                mode_output[0]["comment"] = mode_output[0]["comment"].split(": ")[1]

                            sub_file = None
                            try:
                                type_interf = current_function_name[1][-1]
                                type_interf = "Int" if type_interf == "I" else ("Float" if type_interf == "F" else ("String" if type_interf == "S" else ("Array" if type_interf == "V" else "")))
                                try:
                                    sub_file = files['functions'][f"{current_function_name[1]} ({type_interf}) interface".lower()]
                                except:
                                    if type_interf == "Array":
                                        try:
                                            sub_file = files['functions'][f"{current_function_name[1]} (variant) interface".lower()]
                                        except:
                                            sub_file = files['functions'][f"{current_function_name[1]}(variant) interface".lower()]
                                    else:
                                        raise(f"Unable to find data for {current_unit_name} {current_function_name}")
                            except:
                                type_interf = current_function_name[1][-1]
                                type_interf = "Int" if type_interf == "I" else ("Float" if type_interf == "F" else ("String" if type_interf == "S" else ("Array" if type_interf == "V" else "")))
                                if current_unit_name == "DParallel":
                                    type_interf = "Integer" if type_interf == "Int" else type_interf
                                    sub_file = files['functions'][f"{current_function_name[1]} ({type_interf}) interface".lower()]
                                elif current_unit_name == "DIDSSProperty":
                                    sub_file = files['functions'][f"dssproperties interface"]
                                elif current_unit_name == "DDSSExecutive":
                                    type_interf = "Float" if type_interf == "String" else type_interf
                                    sub_file = files['functions'][f"DSS_Executive{current_function_name[1][-1]} ({type_interf}) interface".lower()]
                                elif current_unit_name == "DTopology":
                                    type_interf = "Variant" if type_interf == "Array" else type_interf
                                    sub_file = files['functions'][f"tolopolgy{current_function_name[1][-1]} ({type_interf}) interface".lower()]
                                elif current_unit_name == "DISource":
                                    type_interf = "Variant" if type_interf == "Array" else type_interf
                                    sub_file = files['functions'][f"{current_function_name[1][:-1]}s{current_function_name[1][-1]} ({type_interf}) interface".lower()]
                                elif current_unit_name == "DLoads":
                                    type_interf = "Variant" if type_interf == "Array" else ("Int" if current_function_name[1] == "DSSLoads" else type_interf)
                                    type_interf = "Integers" if type_interf == "Int" else type_interf
                                    extra = "nt" if type_interf == "Integers" else ""
                                    func_start = current_function_name[1][3:] if type_interf == "Integers" else current_function_name[1][3:-1]
                                    func_end = "I" if type_interf == "Integers" else current_function_name[1][-1]
                                    sub_file = files['functions'][f"{func_start} {func_end + extra} ({type_interf}) interface".lower()]
                                else:
                                    print(f"Unable to find data for {current_unit_name} {current_function_name}")

                            self.classes[current_unit_name][current_function_name[1]]['modes'].append(copy.deepcopy(mode_output[0]))

                            # open file and extract description for mode
                            if sub_file is not None:
                                with open(fr"markdown\{sub_file}", encoding='utf-8') as doc_sub:
                                    doc_string = doc_sub.read()
                                    mode_doc = self.extract_text_between_markers(doc_string, pattern=fr'(?s)(### Parameter {mode_output[0]["number"]}.*?)(### Parameter {int(mode_output[0]["number"]) + 1}.*?)')
                                    if not mode_doc:
                                        mode_doc = self.extract_text_between_markers(doc_string, pattern=fr'(?s)(### \*Parameter {mode_output[0]["number"]}.*?)(### \*Parameter {int(mode_output[0]["number"]) + 1}.*?)')
                                        if mode_doc:
                                            print(f"update docs for ### *Parameter in {sub_file}")
                                    if not mode_doc:
                                        mode_doc = self.extract_text_between_markers(doc_string, pattern=fr'(?s)(## Parameter {mode_output[0]["number"]}.*?)(## Parameter {int(mode_output[0]["number"]) + 1}.*?)')
                                        if mode_doc:
                                            print(f"update docs for ## Parameter in {sub_file}")
                                    if not mode_doc:
                                        mode_doc = self.extract_text_between_markers(doc_string, pattern=fr'(?s)(### Parameter {mode_output[0]["number"]}.*?)(?=\n\*\*\*)')
                                    if not mode_doc:
                                        mode_doc = self.extract_text_between_markers(doc_string, pattern=fr'(?s)(### \*Parameter {mode_output[0]["number"]}.*?)(?=\n\*\*\*)')
                                    if not mode_doc:
                                        mode_doc = self.extract_text_between_markers(doc_string, pattern=fr'(?s)(## Parameter {mode_output[0]["number"]}.*?)(?=\n\*\*\*)')
                                    if not mode_doc:
                                        mode_doc = self.extract_text_between_markers(doc_string, pattern=fr'(?s)(\*\*Parameter {mode_output[0]["number"]}.*?)(?=\n\*\*\*)')
                                        if mode_doc:
                                            print(f"update docs for **Parameter in {sub_file}")

                                    mode_doc = mode_doc.replace("\n\n&nbsp;\n\n", "\n").replace("\n", " ").replace("### Parameter", "Mode").replace("## Parameter", "Mode").replace("## Parameter", "Mode").replace("*Parameter", "Mode").replace("*", "").strip()
                                    mode_doc = mode_doc.replace("  ", ": ")
                                    mode_doc = mode_doc.replace("\\_", "_")
                                    if mode_output[0]["number"] in ("22", "23") and sub_file == "TransformersFFloatInterface1.md":
                                        if mode_output[0]["number"] == "22":
                                            mode_doc = f"Mode {mode_output[0]['number']}: {mode_output[0]['comment']}: This parameter gets the Winding dc resistance in OHMS."
                                        else:
                                            mode_doc = f"Mode {mode_output[0]['number']}: {mode_output[0]['comment']}: This parameter sets the Winding dc resistance in OHMS."

                                    if not mode_doc:
                                        print(f"Missing mode {mode_output[0]['number']} for {sub_file}")

                                    # Here we attempt to correct all that was foudn to be wrong on the documentation before passing along to the PAS files
                                    try:
                                        mode_name_doc = mode_doc.split(":")[1]
                                    except:
                                        print()
                                    if "(read)" in mode_name_doc or "(write)" in mode_name_doc:
                                        pass
                                    else:
                                        mode_name_doc = mode_name_doc.replace("read", "(read)").replace("write", "(write)")
                                        mode_name_doc = mode_name_doc.replace("Read", "(read)").replace("Write", "(write)")

                                    if "ActiveClass.ActiveClassName" in mode_name_doc and "sets" in mode_doc:
                                        mode_doc = mode_doc.replace(" sets ", " gets ")

                                    mode_name_doc = mode_name_doc.replace("-", "")
                                    mode_name_doc = mode_name_doc.replace(" ", "")
                                    mode_name_doc = mode_name_doc.replace("(", " (")
                                    mode_name_doc = mode_name_doc.replace("– ", " ")
                                    mode_name_doc = mode_name_doc.strip()
                                    mode_name_doc = mode_name_doc.replace("Load.", "Loads.") if mode_name_doc[:5] == "Load." else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("Circuit.AllBusVMagPu", "Circuit.AllBusVMagPu (read)") if mode_name_doc == "Circuit.AllBusVMagPu" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("CktElement.VoltagesMagAng", "CktElement.VoltagesMagAng (read)") if mode_name_doc == "CktElement.VoltagesMagAng" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("CktElement.TotalPowers", "CktElement.TotalPowers (read)") if mode_name_doc == "CktElement.TotalPowers" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("CtrlQueue.QueueSize", "CtrlQueue.QueueSize (read)") if mode_name_doc == "CtrlQueue.QueueSize" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("CtrlQueue.CtrlQueue", "CtrlQueue.ClearQueue") if mode_name_doc == "CtrlQueue.CtrlQueue" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("DSSElement.Name", "DSSElement.Name (read)") if mode_name_doc == "DSSElement.Name" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("Fuses.AllNames", "Fuses.AllNames (read)") if mode_name_doc == "Fuses.AllNames" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("Sensors.AllocationFactor", "Sensors.AllocationFactors (read)") if mode_name_doc == "Sensors.AllocationFactor" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("Parser.ResetDelimeters","Parser.ResetDelimiters") if mode_name_doc == "Parser.ResetDelimeters" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("Meters.CalCurrent","Meters.CalcCurrent") if mode_name_doc == "Meters.CalCurrent (read)" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("Meters.CustInterrupts","Meters.CustInterrupts (read)") if mode_name_doc == "Meters.CustInterrupts" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("Executive.NumCommands", "Executive.NumCommands (read)") if mode_name_doc == "Executive.NumCommands" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("Executive.NumOptions", "Executive.NumOptions (read)") if mode_name_doc == "Executive.NumOptions" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("DSSElement.Name", "DSSElement.Name (read)") if mode_name_doc == "DSSElement.Name" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("DSSElement.Name", "DSSElement.Name (read)") if mode_name_doc == "DSSElement.Name" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("GICSources.AllNames", "GICSources.AllNames (read)") if mode_name_doc == "GICSources.AllNames" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("Lines.IsZ1Z0","LineCodes.IsZ1Z0 (read)") if mode_name_doc == "Lines.IsZ1Z0" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("Meters.MeterdTerminal (write)","Meters.MeteredTerminal (write)") if mode_name_doc == "Meters.MeterdTerminal (write)" else mode_name_doc
                                    mode_name_doc = mode_name_doc.replace("LineCodes.Phasess","LineCodes.Phases") if "LineCodes.Phasess" in mode_name_doc else mode_name_doc

                                    if ".allnames" in mode_name_doc.lower() and ".allnames (read)" not in mode_name_doc.lower():
                                        mode_name_doc = mode_name_doc + " (read)"

                                    mode_doc = f"{mode_doc.split(':', 2)[0].strip()}: {mode_name_doc}: {mode_doc.split(':', 2)[2].strip()}"

                                    if mode_name_doc == "Storages.ControloMode (read)":
                                        mode_name_doc = mode_name_doc.replace("Storages.ControloMode", "Storages.ControlMode")
                                        mode_doc = f"{mode_doc.split(': ',2)[0]}: {mode_name_doc}: {mode_doc.split(': ',2)[2]}"

                                    if "LinesCode" in mode_name_doc:
                                        mode_name_doc = mode_name_doc.replace("LinesCode", "LineCodes")
                                        mode_doc = f"{mode_doc.split(': ',2)[0]}: {mode_name_doc}: {mode_doc.split(': ',2)[2]}"

                                    if mode_name_doc == "Storages.ControloMode (read)":
                                        mode_name_doc = mode_name_doc.replace("Storages.ControloMode", "Storages.ControlMode")
                                        mode_doc = f"{mode_doc.split(': ',2)[0]}: {mode_name_doc}: {mode_doc.split(': ',2)[2]}"

                                    if mode_name_doc == "Bus.Name":
                                        mode_name_doc = mode_name_doc.replace("Bus.Name", "Bus.Name (read)")
                                        mode_doc = f"{mode_doc.split(': ',2)[0]}: {mode_name_doc}: {mode_doc.split(': ',2)[2]}"
                                    if mode_name_doc == "Bus.Zsc1":
                                        mode_name_doc = mode_name_doc.replace("Bus.Zsc1", "Bus.Zsc1 (read)")
                                        mode_doc = f"{mode_doc.split(': ',2)[0]}: {mode_name_doc}: {mode_doc.split(': ',2)[2]}"

                                    if mode_name_doc == "CktElement.ActiveVariableidx":
                                        if "read" in mode_output[0]['comment'].lower():
                                            mode_name_doc = mode_name_doc.replace("CktElement.ActiveVariableidx", "CktElement.ActiveVariableidx (read)")
                                        mode_doc = f"{mode_doc.split(': ',2)[0]}: {mode_name_doc}: {mode_doc.split(': ',2)[2]}"

                                    if mode_name_doc in "Parallel.NumCPUs":
                                        if "read" in mode_output[0]['comment'].lower():
                                            mode_name_doc = mode_name_doc.replace("Parallel.NumCPUs", "Parallel.NumCPUs (read)")
                                        elif "write" in mode_output[0]['comment'].lower():
                                            mode_name_doc = mode_name_doc.replace("Parallel.NumCPUs", "Parallel.NumCPUs (write)")
                                        mode_doc = f"{mode_doc.split(': ',2)[0]}: {mode_name_doc}: {mode_doc.split(': ',2)[2]}"

                                    if mode_name_doc == "Parallel.NumCores":
                                        if "read" in mode_output[0]['comment'].lower():
                                            mode_name_doc = mode_name_doc.replace("Parallel.NumCores", "Parallel.NumCores (read)")
                                        elif "write" in mode_output[0]['comment'].lower():
                                            mode_name_doc = mode_name_doc.replace("Parallel.NumCores", "Parallel.NumCores (write)")
                                        mode_doc = f"{mode_doc.split(': ',2)[0]}: {mode_name_doc}: {mode_doc.split(': ',2)[2]}"

                                    if mode_name_doc == "Parallel.NumActors":
                                        if "read" in mode_output[0]['comment'].lower():
                                            mode_name_doc = mode_name_doc.replace("Parallel.NumActors", "Parallel.NumActors (read)")
                                        elif "write" in mode_output[0]['comment'].lower():
                                            mode_name_doc = mode_name_doc.replace("Parallel.NumActors", "Parallel.NumActors (write)")
                                        mode_doc = f"{mode_doc.split(': ',2)[0]}: {mode_name_doc}: {mode_doc.split(': ',2)[2]}"

                                    if mode_name_doc == "Parallel.ActorProgress":
                                        if "read" in mode_output[0]['comment'].lower():
                                            mode_name_doc = mode_name_doc.replace("Parallel.ActorProgress", "Parallel.ActorProgress (read)")
                                        elif "write" in mode_output[0]['comment'].lower():
                                            mode_name_doc = mode_name_doc.replace("Parallel.ActorProgress", "Parallel.ActorProgress (write)")
                                        mode_doc = f"{mode_doc.split(': ',2)[0]}: {mode_name_doc}: {mode_doc.split(': ',2)[2]}"

                                    if mode_name_doc == "Parallel.ActorStatus":
                                        if "read" in mode_output[0]['comment'].lower():
                                            mode_name_doc = mode_name_doc.replace("Parallel.ActorStatus", "Parallel.ActorStatus (read)")
                                        elif "write" in mode_output[0]['comment'].lower():
                                            mode_name_doc = mode_name_doc.replace("Parallel.ActorStatus", "Parallel.ActorStatus (write)")
                                        mode_doc = f"{mode_doc.split(': ',2)[0]}: {mode_name_doc}: {mode_doc.split(': ',2)[2]}"

                                    if mode_name_doc == "Loads.Sensor":
                                        if "read" in mode_output[0]['comment'].lower():
                                            mode_name_doc = mode_name_doc.replace("Loads.Sensor", "Loads.Sensor (read)")
                                        elif "write" in mode_output[0]['comment'].lower():
                                            mode_name_doc = mode_name_doc.replace("Loads.Sensor", "Loads.Sensor (write)")
                                        mode_doc = f"{mode_doc.split(': ',2)[0]}: {mode_name_doc}: {mode_doc.split(': ',2)[2]}"

                                    if mode_name_doc == "PVSystems.Sensor":
                                        if "read" in mode_output[0]['comment'].lower():
                                            mode_name_doc = mode_name_doc.replace("PVSystems.Sensor", "PVSystems.Sensor (read)")
                                        elif "write" in mode_output[0]['comment'].lower():
                                            mode_name_doc = mode_name_doc.replace("PVSystems.Sensor", "PVSystems.Sensor (write)")
                                        mode_doc = f"{mode_doc.split(': ',2)[0]}: {mode_name_doc}: {mode_doc.split(': ',2)[2]}"

                                    if mode_name_doc == "Sensors.AllocationFactor":
                                        if "read" in mode_output[0]['comment'].lower():
                                            mode_name_doc = mode_name_doc.replace("Sensors.AllocationFactor", "Sensors.AllocationFactor (read)")
                                        elif "write" in mode_output[0]['comment'].lower():
                                            mode_name_doc = mode_name_doc.replace("Sensors.AllocationFactor", "Sensors.AllocationFactor (write)")
                                        mode_doc = f"{mode_doc.split(': ',2)[0]}: {mode_name_doc}: {mode_doc.split(': ',2)[2]}"

                                    if mode_name_doc == "Lines.R0 (read)" and mode_output[0]["number"] == "7" and sub_file == 'LinesFFloatInterface1.md':
                                        mode_name_doc = mode_name_doc.replace("(read)", "(write)")
                                        mode_doc = f"{mode_doc.split(': ',2)[0]}: {mode_name_doc}: {mode_doc.split(': ',2)[2]}"

                                    if mode_name_doc == "RegControls.IsReversible (read)" and mode_output[0]["number"] == "7" and sub_file == 'RegControlsIIntInterface1.md':
                                        mode_name_doc = mode_name_doc.replace("(read)", "(write)")
                                        mode_doc = f"{mode_doc.split(': ',2)[0]}: {mode_name_doc}: {mode_doc.split(': ',2)[2]}"

                                    if mode_name_doc == "XYCurves.Npts (read)" and mode_output[0]["number"] == "4" and sub_file == 'XYCurvesIIntInterface1.md':
                                        mode_name_doc = mode_name_doc.replace("(read)", "(write)")
                                        mode_doc = f"{mode_doc.split(': ',2)[0]}: {mode_name_doc}: {mode_doc.split(': ',2)[2]}"

                                    name_mode_pas = mode_output[0]['comment']
                                    if "(read)" in name_mode_pas or "(write)" in name_mode_pas:
                                        pass
                                    else:
                                        name_mode_pas = name_mode_pas.replace("read", "(read)").replace("write", "(write)")
                                        name_mode_pas = name_mode_pas.replace("Read", "(read)").replace("Write", "(write)")
                                        name_mode_pas = name_mode_pas.replace("-", "")
                                        name_mode_pas = name_mode_pas.replace(" ", "")
                                        name_mode_pas = name_mode_pas.replace("(", " (")
                                    name_mode_pas = name_mode_pas.replace("//TODO", "")

                                    # Add "read" flag to variables that lack it in the documentation
                                    if ((" gets " in mode_doc or " returns " in mode_doc or " will deliver " in mode_doc) and "read" not in mode_name_doc) and \
                                            (
                                                (".Count" in mode_name_doc or "NumElements" in mode_name_doc) or
                                                mode_name_doc in (
                                                    "ActiveClass.ActiveClassName",
                                                    "Capacitors.AvailableSteps",
                                                    "CtrlQueue.NumActions",
                                                    "CtrlQueue.ActionCode",
                                                    "CtrlQueue.DeviceHandle",
                                                    'DSS.NumCircuits',
                                                    'DSS.NumClasses',
                                                    'DSS.NumUserClasses',
                                                    'DSS.Version',
                                                    'DSS.DefaultEditor',
                                                    'DSSElement.NumProperties',
                                                    'Fuses.NumPhases',
                                                    'GICSources.Bus1',
                                                    'GICSources.Bus2',
                                                    'Lines.NumCust',
                                                    'Lines.Parent',
                                                    'Parser.NextParam',
                                                    'PDElements.NumCustomers',
                                                    'PDElements.TotalCustomers',
                                                    'PDElements.ParentPDElement',
                                                    'PDElements.FromTerminal',
                                                    'PDElements.SectionID',
                                                    'PDElements.Lambda',
                                                    'PDElements.AccumulatedL',
                                                    'PDElements.RepairTime',
                                                    'PDElements.TotalMiles',
                                                    'PVSystems.kW',
                                                    'Topology.NumLoops',
                                                    'Topology.NumIsolatedBranches',
                                                    'Topology.NumIsolatedLoads',
                                                    'Topology.ActiveLevel',
                                                    'Transformers.StrWdgVoltages',
                                                    'ActiveClass.ActiveClassParent',
                                                    'Bus.NumNodes',
                                                    'Bus.Coorddefined',
                                                    'Bus.N_Customers',
                                                    'Bus.SectionID',
                                                    'Bus.kVBase',
                                                    'Bus.Distance',
                                                    'Bus.Lambda',
                                                    'Bus.N_Interrupts',
                                                    'Bus.Int_Duration',
                                                    'Bus.Cust_interrupts',
                                                    'Bus.Cust_duration',
                                                    'Bus.Totalmiles',
                                                    'Bus.Voltages',
                                                    'Bus.SeqVoltages',
                                                    'Bus.Nodes',
                                                    'Bus.Voc',
                                                    'Bus.Isc',
                                                    'Bus.PuVoltages',
                                                    'Bus.ZscMatrix',
                                                    'Bus.Zsc0',
                                                    'Bus.YscMatrix',
                                                    'Bus.CplxSeqVoltages',
                                                    'Bus.VLL',
                                                    'Bus.PuVLL',
                                                    'Bus.VMagAngle',
                                                    'Bus.PuVMagAngle',
                                                    'Bus.LineList',
                                                    'Bus.LoadList',
                                                    'Circuit.Name',
                                                    'Circuit.Losses',
                                                    'Circuit.LineLosses',
                                                    'Circuit.SubstationLosses',
                                                    'Circuit.TotalPower',
                                                    'Circuit.AllBusVolts',
                                                    'Circuit.AllBusVMag',
                                                    'Circuit.AllElementNames',
                                                    'Circuit.AllBusNames',
                                                    'Circuit.AllElementLosses',
                                                    'Circuit.AllNodeNames',
                                                    'Circuit.SystemY',
                                                    'Circuit.AllBusDistances',
                                                    'Circuit.AllNodeDistances',
                                                    'Circuit.YNodeVArray',
                                                    'Circuit.YNodeOrder',
                                                    'Circuit.YCurrents',
                                                    'CktElement.Voltages',
                                                    'CktElement.Currents',
                                                    'CktElement.powers',
                                                    'CktElement.Losses',
                                                    'CktElement.PhaseLosses',
                                                    'CktElement.SeqVoltages',
                                                    'CktElement.SeqCurrents',
                                                    'CktElement.SeqPowers',
                                                    'CktElement.AllPropertyNames',
                                                    'CktElement.Residuals',
                                                    'CktElement.YPrim',
                                                    'CktElement.CplxSeqVoltages',
                                                    'CktElement.CplxSeqCurrents',
                                                    'CktElement.AllVariableNames',
                                                    'CktElement.AllVariableValues',
                                                    'CktElement.Nodeorder',
                                                    'CktElement.CurrentsMagAng',
                                                    'DSS.Classes',
                                                    'DSS.UserClasses',
                                                    'DSSElement.AllPropertyNames',
                                                    'Fuses.IsBlown',
                                                    'Generators.RegisterNames',
                                                    'Generators.RegisterValues',
                                                    'Lines.SeasonRating',
                                                    'Meters.DIFilesAreopen',
                                                    'Meters.SeqListSize',
                                                    'Meters.TotalCustomers',
                                                    'Meters.NumSections',
                                                    'Meters.OCPDeviceType',
                                                    'Meters.NumSectionCustomers',
                                                    'Meters.NumSectionBranches',
                                                    'Meters.SectSeqIdx',
                                                    'Meters.SectTotalCust',
                                                    'Meters.SAIFI',
                                                    'Meters.SAIFIkW',
                                                    'Meters.SAIDI',
                                                    'Meters.AvgRepairTime',
                                                    'Meters.FaultRateXRepairHrs',
                                                    'Meters.SumBranchFltRates',
                                                    'Meters.RegisterNames',
                                                    'Meters.RegisterValues',
                                                    'Meters.Totals',
                                                    'Meters.AllEndElements',
                                                    'Meters.AllBranchesInZone',
                                                    'Meters.AllPCEinZone',
                                                    'Monitors.SampleCount',
                                                    'Monitors.FileVersion',
                                                    'Monitors.RecordSize',
                                                    'Monitors.NumChannels',
                                                    'Monitors.FileName',
                                                    'Monitors.Header',
                                                    'Monitors.dblHour',
                                                    'Monitors.dblFreq',
                                                    'PVSystems.IrradianceNow',
                                                    'Reclosers.RecloseIntervals',
                                                    'Solution.Iterations',
                                                    'Solution.TotalIterations',
                                                    'Solution.MostIterationsDone',
                                                    'Solution.ModeID',
                                                    'Solution.EventLog',
                                                    'Solution.IncMatrix',
                                                    'Solution.BusLevels',
                                                    'Solution.IncMatrixRows',
                                                    'Solution.IncMatrixCols',
                                                    'Solution.Laplacian',
                                                    'Storages.RegisterNames',
                                                    'Storages.RegisterValues',
                                                    'Topology.ActiveBranch',
                                                    'Topology.AllLoopedPairs',
                                                    'Topology.AllIsolatedBranches',
                                                    'Topology.AllIsolatedLoads',
                                                    'Transformers.WdgVoltages',
                                                    'Transformers.WdgCurrents',
                                                    'WindGens.RegisterNames',
                                                    'WindGens.RegisterValues',
                                                    'Circuit.NumCktElements',
                                                    'Circuit.NumBuses',
                                                    'Circuit.NumNodes',
                                                    'CktElement.NumTerminals',
                                                    'CktElement.NumConductors',
                                                    'CktElement.NumPhases',
                                                )
                                            ):
                                        mode_name_doc = mode_name_doc + " (read)"
                                        mode_doc = f"{mode_doc.split(': ', 2)[0]}: {mode_name_doc}: {mode_doc.split(': ', 2)[2]}"

                                    # Add "write" flag to variables that lack it in the documentation
                                    if ((" sets " in mode_doc) and "write" not in mode_name_doc) and \
                                            (
                                                mode_name_doc in (
                                                    'CtrlQueue.Action',
                                                    'Meters.SetActiveSection',
                                                    'Settings.AllocationFactors',
                                                    'Solution.StepSizeMin',
                                                    'Solution.StepSizeHr',
                                                    'DSSProgress.Caption',
                                                    'DSSProgress.PctProgress',
                                                )
                                            ):
                                        mode_name_doc = mode_name_doc + " (write)"
                                        mode_doc = f"{mode_doc.split(': ', 2)[0]}: {mode_name_doc}: {mode_doc.split(': ', 2)[2]}"

                                    # Remove the "write" flag from variables that should be treated as functions because they return something
                                    if 'PDElements.Name (write)' in mode_name_doc:
                                        mode_name_doc = mode_name_doc.replace(" (write)", "")
                                        mode_doc = f"{mode_doc.split(': ', 2)[0]}: {mode_name_doc}: {mode_doc.split(': ', 2)[2]}"

                                    # Display remaining conflicts for reference
                                    if "read" in mode_name_doc.lower() and "read" not in name_mode_pas.lower() and "allnames" not in mode_name_doc.lower():
                                        print(f"Read-None conflict: {mode_name_doc} {name_mode_pas}")

                                    if "write" in mode_name_doc.lower() and "write" not in name_mode_pas.lower():
                                        print(f"Write-None conflict: {mode_name_doc} {name_mode_pas}")

                                    if "read" not in mode_name_doc.lower() and "read" in name_mode_pas.lower():
                                        print(f"None-Read conflict: {mode_name_doc} {name_mode_pas}")
                                    if "write" not in mode_name_doc.lower() and "write" in name_mode_pas.lower():
                                        print(f"None-Write conflict: {mode_name_doc} {name_mode_pas}")

                                    if "read" in mode_name_doc.lower() and "write" in name_mode_pas.lower():
                                        print(f"Read-Write conflict: {mode_name_doc} {name_mode_pas}")

                                    if "write" in mode_name_doc.lower() and "read" in name_mode_pas.lower():
                                        print(f"Write-Read conflict: {mode_name_doc} {name_mode_pas}")

                                    if mode_name_doc.lower() == name_mode_pas.lower() or (mode_name_doc.split(".")[0][:-1] + "." + mode_name_doc.split(".")[1]).lower() == name_mode_pas.lower():
                                        pass
                                    else:
                                        print(mode_name_doc, name_mode_pas)

                                    line_new = line_new.split("//", 2)[0] + "//" + mode_doc.replace("\\", "").replace("\xa0", "") + "\n"
                                    line_new = line_new.replace('\u201C', '"')  # Replace left double quote
                                    line_new = line_new.replace('\u201D', '"')  # Replace right double quote  # Replace right double quote
                                    line_new = line_new.replace('\u2018', "'")  # Replace left single quote
                                    line_new = line_new.replace('\u2019', "'")  # Replace right single quote


                    new_lines.append(line_new)
                    new_lines.extend(lines_to_add)

            with open(pas_file, "w") as f:
                f.write("".join(new_lines))

    @staticmethod
    def clean_modes(mode_comment: str):
        """ Function to remove characters that may cause issues """

        try:
            clean_mode = mode_comment.split(".", 1)[1]
        except:
            clean_mode = mode_comment + ""

        clean_mode = clean_mode.replace('/', '').replace('TODO', '').strip().replace(' - ', ' ').replace(' -', ' ').replace('- ', ' ').replace(
            ' ', '_').replace('.', '_').replace(' -', '_').replace('(', '').replace(')', '')
        return clean_mode

    @staticmethod
    def extract_text_between_markers(text, pattern = r'(?s)(#.*?)(?=\n\*\*\*)'):
        # Pattern to match text between a line with # and a line with ***
        # (?s) enables DOTALL mode, making . match newlines
        # The pattern captures from the line with # up to but not including the line with ***

        match = re.search(pattern, text)

        if match:
            return match.group(1)
        else:
            return ""

    @staticmethod
    def find_pattern(text: str, pattern: str=r"unit\s+([A-Za-z]\w*);"):
        # Pattern explanation:
        # unit\s+         - matches the literal 'unit' followed by whitespace
        # ([A-Za-z]\w*)   - captures a word starting with a letter followed by any word characters
        # ;               - matches semicolon and closing quote
        # pattern = r"unit\s+([A-Za-z]\w*);"

        # Find all matches
        matches = re.findall(pattern, text, re.IGNORECASE)
        return matches

    @staticmethod
    def find_function_names(text):
        # Pattern explanation:
        # (function|procedure) - matches either "function" or "procedure"
        # \s+ - matches whitespace
        # ([A-Za-z]\w*) - captures the function/procedure name
        # \( - matches opening parenthesis
        # .*? - non-greedy match of any characters
        # \) - matches closing parenthesis
        # .*? - non-greedy match of any characters
        # ;cdecl; - matches the cdecl declaration
        pattern = r'(function|procedure)\s+([A-Za-z]\w*)\(.*?\).*?(;cdecl;|;)'

        # Find all matches
        matches = re.finditer(pattern, text, re.IGNORECASE)

        # Extract function/procedure names and their types
        results = []
        for match in matches:
            func_type = match.group(1)  # 'function' or 'procedure'
            func_name = match.group(2)  # name of the function/procedure
            results.append((func_type, func_name))

        return results

    @staticmethod
    def parse_parameters(param_str):
        # Split parameters by semicolon and parse each one
        params = param_str.split(';')
        parsed_params = []

        for param in params:
            param = param.strip()
            if not param:
                continue

            # Handle 'var' parameters
            is_var = param.lower().startswith('var')
            if is_var:
                param = param[4:].strip()  # Remove 'var' and extra spaces

            # Split parameter into name and type
            if ':' in param:
                name_part, type_part = param.split(':', 1)
                names = [n.strip() for n in name_part.split(',')]
                param_type = type_part.strip()

                for name in names:
                    parsed_params.append({
                        'name': name,
                        'type': param_type,
                        'is_var': is_var
                    })

        return parsed_params

    def find_function_details(self, text):
        pattern = r'(function|procedure)\s+([A-Za-z]\w*)\((.*?)\)(?:\s*:\s*([A-Za-z]\w*))?\s*(?:;cdecl;|;)'
        pattern = r'(?i)(function|procedure)\s+([A-Za-z]\w*)\((.*?)\)(?:\s*:\s*([A-Za-z]\w*))?\s*(?:;cdecl;|;)'

        matches = re.finditer(pattern, text, re.MULTILINE)

        results = []
        for match in matches:
            func_type = match.group(1)  # 'function' or 'procedure'
            func_name = match.group(2)  # name of the function/procedure
            parameters = match.group(3)  # parameter list
            return_type = match.group(4) if match.group(4) else None  # return type (if function)

            # Parse parameters
            parsed_params = self.parse_parameters(parameters)

            # Create function info dictionary
            func_info = {
                'type': func_type,
                'name': func_name,
                'parameters': parsed_params,
                'return_type': return_type
            }

            results.append(func_info)

        return results

    @staticmethod
    def find_numbered_begins(text):
        # Pattern explanation:
        # ^\s*            - start of line and any whitespace
        # (\d+)          - one or more digits (captured)
        # \s*:\s*        - colon with optional whitespace around it
        # begin          - literal 'begin'
        # \s*            - any whitespace before possible comment
        # (?:\/\/\s*(.+?))?\s*$ - optional comment and trailing whitespace
        pattern = r'^\s*(\d+)\s*:\s*begin\s*(?:\/\/\s*(.+?))?\s*$'

        matches = re.finditer(pattern, text, re.IGNORECASE)

        results = []
        for match in matches:
            number = match.group(1)
            comment = match.group(2) if match.group(2) else ''
            results.append({
                'number': number,
                'comment': comment.strip()
            })

        return results

if __name__ == "__main__":
    docstring_enhancer(path_ddll=r"C:\EPRI\OpenDSS\Version8\Source\DDLL")



