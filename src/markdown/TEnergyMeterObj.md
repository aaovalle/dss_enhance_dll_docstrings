# TEnergyMeterObj

| ***TEnergyMeterObj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Implements the following properties/methods as in 3.3.15:** **MakePosSequence** **RecalcElementData** **CalcYPrim** **GetCurrents** **GetInjCurrents** **GetPropertyValue** **InitPropertyValues** **DumpProperties** |  |  |
| **Method-private** | Integrate | Performs the integration of the demand interval registers. |
| **Method-private** | SetDragHandRegister | Stores data in the shift registers for DI. |
| **Property-private** | Accumulate\_Load | Accumulate load in meter’s zone. |
| **Method-private** | Accumulate\_Gen | Accumulate generation in meter’s zone. |
| **Method-private** | CalcBusCoordinates | Calculates bus coordinates using interpolation. |
| **Property-private** | AddToVoltBaseList | Add to VoltBase list if not already there and return index. |
| **Property-private** | MakeDIFileName | Creates and returns the name for the DI report file. |
| **Property-private** | MakeVPhaseReportFileName | Creates and returns the name for the phase voltage report file. |
| **Method-private** | AssignVoltBaseRegisterNames | Assigns voltage base to register names (DI) |
| **Method-private** | TotalupDownstreamCustomers | Totalizes the number of customers in the zone. |
| **Method-protected** | OpenDemandIntervalFile | Opends DI file. |
| **Method-protected** | WriteDemandIntervalData | Writes in DI file. |
| **Method-protected** | CloseDemandIntervalFile | Closes in DI file. |
| **Method-protected** | AppendDemandIntervalFile | Appends to DI file. |
| **Method-public** | ResetRegisters | Resets the meter registers. |
| **Method-public** | TakeSample | Update registers from metered zone. Assumes one time has taken place since last sample. Overrides the more generic class. |
| **Method-public** | SaveRegisters | Saves the meter register in the meter file. |
| **Method-public** | MakeMeterZoneLists | This gets fired off whenever the bus lists are rebuilt. Must be updated whenever there is a change in the circuit. |
| **Method-public** | ZoneDump | Dumps the elements within the zone into the meter file assigned. |
| **Method-public** | InterpolateCoordinates | Completes the missing bus coordinates by interpolation. |
| **Method-public** | EnableFeeder | HasFeeder must be true before feederObj will be re-enabled. Not implemented. |
| **Method-public** | AllocateLoad | Allocates load across the feeder model using allocation factors. |
| **Method-public** | ReduceZone | Reduce Zone by eliminating buses and merging lines. |
| **Method-public** | SaveZone | Run down the zone and write each element into a file. |
| **Method-public** | GetPCEatZone | Gets all the PCE within the meter zone. |
| **Method-public** | CalcReliabilityIndices | Calculates the feeder’s reliability indices using backward forward sweep. |



***
_Created with the Standard Edition of HelpNDoc: [Why Microsoft Word Isn't Cut Out for Documentation: The Benefits of a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
