# TStorageControllerObj

| ***TStorageControllerObj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Implements the following properties/methods as in TCapControlObj, TStorageObj and TExpControlObj:** **RecalcElementData** **CalcYPrim** **GetLosses** **GetPropertyValue** **InitPropertyValues** **DumpProperties** **SaveWrite** **MakePosSequence** **Sample** **DoPendingAction** **Reset** **Set\_PendingChange** **Get\_PendingChange** **GetCurrents** **GetInjCurrents** **CalcYearlyMult** **CalcDailyMult** **CalcDutyMult** |  |  |
| **Method-private** | SetAllFleetValues | Sets the dispatch values for all the storage devices in the fleet. |
| **Method-private** | SetFleetkWRate | Sets the kW values for all the storage devices in the fleet. |
| **Method-private** | SetFleetChargeRate | Sets the charging rate for all the storage devices in the fleet. |
| **Method-private** | SetFleetToCharge | Commands the fleet to enter in charging mode. |
| **Method-private** | SetFleetToDisCharge | Commands the fleet to enter in discharging mode. |
| **Method-private** | SetFleetToIdle | Commands the fleet to enter in Idle mode. |
| **Method-private** | SetFleetToExternal | Commands the fleet to enter in external mode. |
| **Method-private** | SetFleetDesiredState | Commands the fleet to enter in desired mode. |
| **Property-private** | InterpretMode | Interprets the mode embedded in the given string. |
| **Property-private** | GetModeString | Returns the present mode for the fleet. |
| **Property-private** | GetkWTotal | Returns the total kW. |
| **Property-private** | GetkWhTotal | Returns the total kWh. |
| **Property-private** | GetkWhActual | Returns the present kWh. |
| **Property-private** | GetkWActual | Returns the present kW. |
| **Property-private** | GetkWActual | Returns the present kW. |
| **Property-private** | ReturnSeasonTarget | Returns the seasonal target. |
| **Property-private** | ReturnElementsList | Returns the list of controlled elements as string. |
| **Property-private** | ReturnWeightsList | Returns the weigh list as string. |
| **Property-private** | MakeFleetList | Allocates the list of storage devices controlled by this control. |
| **Method-private** | DoLoadFollowMode | Implements the control routine for follow control mode. |
| **Method-private** | DoLoadShapeMode | Implements the control routine for load shape control mode. |
| **Method-private** | DoTimeMode | Implements the control routine for time control mode. |
| **Method-private** | DoScheduleMode | Implements the control routine for schedule control mode. |
| **Method-private** | DoPeakShaveModeLow | Implements the control routine for peak shave control mode. |
| **Method-private** | PushTimeOntoControlQueue | Push present time onto control queue to force re solve at new dispatch value. |
| **Property-private** | NormalizeToTOD | Normalize time to a floating-point number representing time of day If Hour \> 24 time should be 0 to 23.999999. |
| **Property-private** | GetControlPower | Returns the total power of the fleet. |
| **Property-private** | GetControlCurrent | Returns the control current. |
| **Property-private** | Get\_FleetkW | Returns the fleet kW. |
| **Property-private** | Get\_FleetkWh | Returns the fleet kWh. |
| **Property-private** | Get\_FleetkWhRating | Returns the fleet kWh rating. |
| **Property-private** | Get\_FleetReservekWh | Returns the fleet kWh reserve. |
| **Property-private** | Get\_DynamicTarget | Returns the target considering the seasonal ratings. |
| **Property-public** | FleetkW | PA Get\_FleetkW. |
| **Property-public** | FleetkWh | PA Get\_FleetkWh. |
| **Property-public** | FleetkWhRating | PA Get\_FleetkWhRating. |
| **Property-public** | FleetReservekWh | PA Get\_FleetReservekWh. |



***
_Created with the Standard Edition of HelpNDoc: [Converting Word Docs to eBooks Made Easy with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
