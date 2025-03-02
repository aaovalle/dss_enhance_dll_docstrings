# TUPFCObj

| ***TUPFCObj*** |  |  |  |  |
| --- | --- | --- | --- | --- |
| ***Type-access*** |  | *Command* | *Description – (Specific class) otherwise generic* |  |
| **Implements the following properties/methods as in TLoadObj, *TIndMach012Obj, TPVSystemObj and TGeneratorOb*:** **RecalcElementData** **CalcYPrim** **MakePosSequence** **InjCurrents** **GetInjCurrents** **GetCurrents** **InitPropertyValues** **DumpProperties** **Get\_Variable** **Set\_Variable** **GetPropertyValue** **NumVariables** **GetAllVariables** **VariableName** |  |  |  |  |
| **Property- private** | GetinputCurr |  |  | Calculates the input current to absorb reactive power from UPFC. |
| **Property- private** | GetOutputCurr |  |  | Calculates the output current for the UPFC device. |
| **Property- private** | CalcUPFCPowers |  |  | Calculates the equivalent power output for the UPFC device. |
| **Property- private** | CalcUPFCLosses |  |  | Calculates the Active power losses at the input of the device by using the Load powers, the approach is based in the data provided. |
| **Method- public** | UploadCurrents |  |  | Uploads the input/output currents when commanded by the controller. |
| **Property- public** | CheckStatus |  |  | Checks if the UPFC control needs an update, returns true if so. |



***
_Created with the Standard Edition of HelpNDoc: [Create Professional CHM Help Files with HelpNDoc's Easy-to-Use Tool](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
