# TSensorObj

| ***TSensorObj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description* |
| **Implements the following properties/methods as in 3.3.15:** **MakePosSequence** **RecalcElementData** **CalcYPrim** **GetCurrents** **GetInjCurrents** **GetPropertyValue** **InitPropertyValues** **DumpProperties** |  |  |
| **Method-private** | Set\_Conn | Interpret the Connection. |
| **Method-private** | Set\_Action | Interpret Action Property. Not implemented. |
| **Method-private** | ZeroSensorArrays | Resets all the sensor arrays (0). |
| **Method-private** | AllocateSensorObjArrays | Allocates the sensor arrays in memory. |
| **Method-private** | RecalcVbase | Recalculates the voltage base for the monitored buses. |
| **Method-private** | RotatePhases | For Delta connections or Line-Line voltages. |
| **Property-private** | LimitToPlusMinusOne | Returns +/- 1 accroding to the sign of the given integer. |
| **Method-private** | ClearSensor | Clears the sensor registers and flags. |
| **Method-private** | UpdateCurrentVector | Updates the current vector when P and Q are defined as the input vectors for the sensor. |
| **Property-private** | Get\_WLSCurrentError | Return the WLS Error for Currents.&nbsp; Get Square error and weight it. |
| **Property-private** | Get\_WLSVoltageError | Return the WLS Error for Voltages.&nbsp; Get Square error and weight it. |
| **Method-public** | TakeSample | Go add a sample to the buffer. Overrides the more generic class. |
| **Method-public** | ResetIt | Resets the monitor. |
| **Method-public** | Save | Saves present buffer to file. |
| **Property-public** | Conn | PA Fconn (variable) and Set\_Conn. |
| **Property-public** | Action | PA Set\_Action. |
| **Property-public** | WLSCurrentError | PA Get\_WLSCurrentError. |
| **Property-public** | WLSVoltageError | PA Get\_WLSVoltageError. |
| **Property-public** | BaseKV | PA kvbase (variable). |
| **Property-public** | DeltaDirection | PA FDeltaDirection (variable). |
| **Property-public** | SensorP | PA SensorKW (variable). |
| **Property-public** | SensorQ | PA SensorKVAR (variable). |



***
_Created with the Standard Edition of HelpNDoc: [Say Goodbye to Documentation Headaches with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
