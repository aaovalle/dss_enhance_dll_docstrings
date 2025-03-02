# TDSSCircuit

| ***TDSSCircuit*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Method-private** | AddDeviceHandle | Adds a handle Index into CktElements. |
| **Method-private** | AddABus | Reallocates the bus array for adding a new element. |
| **Method-private** | AddANodeBus | Reallocates the MapNodeToBus array for adding a new element. |
| **Property-private** | AddBus | Adds a new bus to the bus list, reallocates memory if needed. |
| **Method-private** | Set\_ActiveCktElement | Sets the given ckt element active in the actor context. |
| **Method-private** | Set\_BusNameRedefined | Force Rebuilding of SystemY if bus def has changed so controls will know buses redefined. |
| **Property-private** | Get\_Losses | Gets the total Circuit losses. |
| **Property-private** | Set\_LoadMultiplier | Sets the load multiplier in the actor context. |
| **Property-private** | SaveBusInfo | Save existing bus definitions and names for info that needs to be restored. |
| **Property-private** | RestoreBusInfo | Restore kV bases, other values to buses still in the list. |
| **Property-private** | SaveMasterFile | Write Redirect for all populated DSS Classes Except Solution Class. |
| **Property-private** | SaveDSSObjects | Write Files for all populated DSS Classes Except Solution Class. |
| **Property-private** | SaveFeeders | Write out all energy meter zones to separate subdirectories. |
| **Property-private** | SaveBusCoords | Writes the circuit’s buscoords into the file assigned. |
| **Property-private** | SaveGISCoords | Writes the circuit’s GIS coordinates into the file assigned. |
| **Property-private** | SaveVoltageBases | Writes the circuit’s bus voltage bases into the file assigned. |
| **Method-private** | ReallocDeviceList | Reallocate the device list to improve the performance of searches. |
| **Method-private** | Set\_CaseName | Stores in memory the case name assigned by the user. |
| **Property-private** | Get\_Name | Gets the circuit name. |
| **Method-public** | AddCktElement | Adds last DSS object created to circuit. |
| **Method-public** | ClearBusMarkers | Clears all the bus marker objects in the model. |
| **Method-public** | TotalizeMeters | Totalize all energymeters in the problem. |
| **Property-public** | ComputeCapacity | Calculates the system total capacity. |
| **Property-public** | Save | Save the present circuit - Enabled devices only. |
| **Method-public** | ProcessBusDefs | Processes the bus definitions in the circuit. |
| **Method-public** | ReProcessBusDefs | Redo all Buslists, nodelists. Includes memory reallocation if needed. |
| **Method-public** | DoResetMeterZones | Do this only if meterzones unlocked.&nbsp; Normally, Zones will remain unlocked so that all changes to the circuit will result in rebuilding the lists. |
| **Property-public** | SetElementActive | Sets the given element active in the global context for the active actor. |
| **Method-public** | InvalidateAllPCElements | Forces rebuild of matrix on next solution. |
| **Method-public** | DebugDump | Writes the debug file in the active folder. |
| **Property-public** | GetTopology | Access to topology from the first source. |
| **Method-public** | FreeTopology | Frees all the elements within the topology object. |
| **Property-public** | GetBusAdjacentPDLists | Returns the PD list adjacent to the active point in the topology tree. |
| **Property-public** | GetBusAdjacentPCLists | Returns the PC list adjacent to the active point in the topology tree. |
| **Property-public** | Tear\_Circuit | Tears the circuit considering the number of Buses of the original Circuit. |
| **Property-public** | Create\_MeTIS\_graph | Generates the graph describing the model for MeTiS. |
| **Property-public** | Create\_MeTIS\_Zones | Executes MeTiS and loads the zones into memory for further use. |
| **Method-public** | AggregateProfiles | Aggregates profiles using the number of zones defined by the user. |
| **Method-public** | Disable\_All\_DER | Disables all DER present in the model. |
| **Method-public** | Save\_SubCircuits | Saves the subcircuits created in memory into the hard drive. |
| **Property-public** | getPCEatBus | Returns the list of all PCE connected to the bus name given at BusName. |
| **Property-public** | getPDEatBus | Returns the list of all PDE connected to the bus name given at BusName. |
| **Property-public** | ReportPCEatBus | Gets all PCE at given bus and returns the list as string. |
| **Property-public** | ReportPDEatBus | Gets all PDE at given bus and returns the list as string. |
| **Property-public** | get\_Line\_Bus | Delivers the name of the bus at the specific line and terminal. |
| **Method-public** | get\_longest\_path | This routine calculates the longest path within a linearized graph considering the zero level buses as the beginning of new path. |
| **Property-public** | Append2PathsArray | Appends a new path to the array and returns the index(1D). |
| **Method-public** | Normalize\_graph | This routine normalizes the Inc\_matrix levels. |
| **Method-public** | Get\_paths\_4\_Coverage | Calculates the paths inside the graph to guarantee the desired coverage when tearing the system. |
| **Method-public** | Format\_SubCircuits | Arrange the files of the subcircuits to make them independent. |
| **Method-public** | AppendIsources | Appends single phase ISources to each node of bus specified if the given linkBranch. These actions take place within the given file. |
| **Property-public** | Name | PA Get\_Name. |
| **Property-public** | CaseName | PA FCaseName (variable) and Set\_CaseName. |
| **Property-public** | ActiveCktElement | PA FActiveCktElement (variable) and Set\_ActiveCktElement. |
| **Property-public** | Losses | PA Get\_Losses. |
| **Property-public** | BusNameRedefined | PA FBusNameRedefined (variable) and Set\_BusNameRedefined. |
| **Property-public** | LoadMultiplier | PA FLoadMultiplier (variable) and Set\_LoadMultiplier. |



***
_Created with the Standard Edition of HelpNDoc: [Make Your PDFs More Secure with Encryption and Password Protection](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
