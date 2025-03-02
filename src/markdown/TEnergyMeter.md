# TEnergyMeter

| ***TEnergyMeter*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Implements the following properties/methods as in TMeterClass and 3.1.4:** **DefineProperties** **MakeLike** **Edit** **Init** **NewObject** |  |  |
| **Method-private** | ProcessOptions | Parses the options for the energy meter. |
| **Method-private** | Set\_SaveDemandInterval | Sets the demand interval flag using the given value. |
| **Method-private** | Get\_SaveDemandInterval | Gets the demand interval flag. |
| **Method-private** | CreateMeterTotals | Allocates in memory for the meter totals registers. |
| **Method-private** | CreateFDI\_Totals | Allocates in memory for the FDI totals registers. |
| **Method-private** | ClearDI\_Totals | Clears the DI totals registers. |
| **Method-private** | WriteTotalsFile | Sum up all registers of all meters and write to Totals.CSV. |
| **Method-private** | OpenOverloadReportFile | Allocates memory for the overload report, initializes the memory space with headers. |
| **Method-private** | OpenVoltageReportFile | Allocates memory for the voltage violations report, initializes the memory space with headers. |
| **Method-private** | WriteOverloadReport | Scans the active circuit for overloaded PD elements and writes each to a file. This is called only if in Demand Interval (DI) mode and the file is open. |
| **Method-private** | WriteVoltageReport | For any bus with a defined voltage base, test for \> Vmax or \< Vmin and writes each to a file. This is called only if in Demand Interval (DI) mode and the file is open. |
| **Method-private** | InterpretRegisterMaskArray | Interprets the registry mask array using the given reference. |
| **Method-private** | Set\_DI\_Verbose | Sets the DI verbose flag. |
| **Method-private** | Get\_DI\_Verbose | Gets the DI verbose flag. |
| **Method-protected** | SetHasMeterFlag | Set the HasMeter Flag for all cktElement. |
| **Method-public** | ResetMeterZonesAll | Force all EnergyMeters in the circuit to reset their meter zones. |
| **Method-public** | ResetAll | Reset all meters in active circuit to zero. Overrides the more generic class. |
| **Method-public** | SampleAll | Forces all meters in active circuit to sample. Overrides the more generic class. |
| **Method-public** | SaveAll | Forces all meters in the circuit to take a sample. Overrides the more generic class. |
| **Method-public** | AppendAllDIFiles | Appends the DI files for all the energy meters. |
| **Method-public** | OpenAllDIFiles | Opens the DI files for all the energy meters. |
| **Method-public** | CloseAllDIFiles | Closes the DI files for all the energy meters. |
| **Property-public** | SaveDemandInterval | PA Get\_SaveDemandInterval and Set\_SaveDemandInterval. |
| **Property-public** | DI\_Verbose | PA Get\_DI\_Verbose and Set\_DI\_Verbose. |



***
_Created with the Standard Edition of HelpNDoc: [Make Help Documentation a Breeze with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
