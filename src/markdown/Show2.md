# Show

&nbsp;

The following properties are part of the command show

&nbsp;

| *Show option* | *Description* |
| :---: | --- |
| Autoadded |  Shows auto added capacitors or generators. See AutoAdd solution mode.&nbsp; |
| buses |  Report showing all buses and nodes currently defined.&nbsp; |
| busflow |  Creates a report showing power and current flows as well as voltages around a selected bus. Syntax: &nbsp; &nbsp; Show BUSFlow busname \[MVA\|kVA\*\] \[Seq\* \| Elements\] &nbsp; &nbsp; Show busflow busxxx kVA elem&nbsp; &nbsp; Show busflow busxxx MVA seq&nbsp; NOTE: The Show menu will prompt you for these values.&nbsp; |
| Controlled |  Show Controlled elements and the names of the controls connected to them in CSV format.&nbsp; |
| controlqueue |  Shows the present contents of the control queue.&nbsp; |
| convergence |  Report on the convergence of each node voltage.&nbsp; |
| currents | Report showing currents from most recent solution. syntax:&nbsp; &nbsp; &nbsp; Show Currents&nbsp; \[\[residual=\]yes\|no\*\] \[Seq\* \| Elements\]&nbsp; If "residual" flag is yes, the sum of currents in all conductors is reported. Default is to report Sequence currents; otherwise currents in all conductors are reported. |
| deltaV |  Show voltages ACROSS each 2-terminal element, phase-by-phase. &nbsp; |
| elements |  Shows names of all elements in circuit or all elements of a specified class. Syntax:&nbsp; &nbsp; &nbsp; Show ELements \[Classname\] &nbsp; Useful for creating scripts that act on selected classes of elements. &nbsp; |
| eventlog |  Shows the present event log. (Regulator tap changes, capacitor switching, etc.)&nbsp; |
| faults |  After fault study solution, shows fault currents.&nbsp; |
| generators |  Report showing generator elements currently defined and the values of the energy meters&nbsp; associated with each generator.&nbsp; |
| isolated |  Report showing buses and elements that are isolated from the main source.&nbsp; |
| kvbasemismatch |  Creates a report of Load and Generator elements for which the base voltage does not match the Bus base voltage. Scripts for correcting the voltage base are suggested.&nbsp; |
| lineconstants |  Creates two report files for the line constants (impedances) of every LINEGEOMETRY element currently defined. One file shows the main report with the matrices. The other file contains corresponding LINECODE definitions that you may use in subsequent simulations.&nbsp; Syntax: &nbsp; &nbsp; Show LIneConstants \[frequency\] \[none\|mi\|km\|kft\|m\|me\|ft\|in\|cm\] \[rho\]&nbsp; Specify the frequency, length units and earth resistivity (meter-ohms). Examples: &nbsp; &nbsp; Show Lineconstants 60 kft 100&nbsp; &nbsp; Show Linecon 50 km 1000&nbsp; |
| loops |  Shows closed loops detected by EnergyMeter elements that are possibly unwanted. Otherwise, loops are OK.&nbsp; |
| losses |  Reports losses in each element and in the entire circuit.&nbsp; |
| meters |  Shows the present values of the registers in the EnergyMeter elements.&nbsp; |
| mismatch |  Shows the current mismatches at each node in amperes and percent of max currents at node.&nbsp; |
| monitor |  Shows the contents of a selected monitor. Syntax:&nbsp; &nbsp; &nbsp; Show Monitor&nbsp; monitorname&nbsp; |
| overloads |  Shows overloaded power delivery elements.&nbsp; |
| panel |  Shows control panel. (not necessary for standalone version)&nbsp; |
| powers | Report on powers flowing in circuit from most recent solution.&nbsp; Powers may be reported in kVA or MVA and in sequence quantities or in every conductor of each element. Syntax: &nbsp; &nbsp; Show Powers \[MVA\|kVA\*\] \[Seq\* \| Elements\]&nbsp; Sequence powers in kVA is the default. Examples: &nbsp; &nbsp; Show powers&nbsp; &nbsp; Show power kva element&nbsp; &nbsp; Show power mva elem&nbsp; |
| PV2PQ\_Conversions |  Show the list of generators converted from PV bus to PQ during the last solution step (NCIM).&nbsp; |
| QueryLog |  Show Query Log file. &nbsp; |
| ratings |  Shows ratings of power delivery elements.&nbsp; |
| Result |  Show last result (in @result variable).&nbsp; |
| taps |  Shows the regulator/LTC taps from the most recent solution.&nbsp; |
| topology |  Shows the topology as seen by the SwtControl elements.&nbsp; |
| unserved |  Shows loads that are "unserved". That is, loads for which the voltage is too low, or a branch on the source side is overloaded. If UEonly is specified, shows only those loads in which the emergency rating has been exceeded. Syntax: &nbsp; &nbsp; Show Unserved \[UEonly\] (unserved loads)&nbsp; |
| variables |  Shows internal state variables of devices (Power conversion elements) that report them.&nbsp; |
| voltages |  Reports voltages from most recent solution. Voltages are reported with respect to&nbsp; system reference (Node 0) by default (LN option), but may also be reported Line-Line (LL option). The voltages are normally reported by bus/node, but may also be reported by circuit element. Syntax: &nbsp; &nbsp; Show Voltages \[LL \|LN\*\]&nbsp; \[Seq\* \| Nodes \| Elements\] &nbsp; &nbsp; Show Voltages&nbsp; &nbsp; Show Voltage LN Nodes&nbsp; &nbsp; Show Voltages LL Nodes&nbsp; &nbsp; Show Voltage LN Elem&nbsp; |
| y |  Show the system Y matrix. Could be a large file\!&nbsp; |
| yprim |  Show the primitive admittance (y) matrix for the active element.&nbsp; |
| zone |  Shows the zone for a selected EnergyMeter element. Shows zone either in a text file or in a graphical tree view. &nbsp; &nbsp; Show Zone&nbsp; energymetername \[Treeview\]&nbsp; |



***
_Created with the Standard Edition of HelpNDoc: [Easy EPub and documentation editor](<https://www.helpndoc.com>)_
