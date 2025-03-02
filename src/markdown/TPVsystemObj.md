# TPVsystemObj

| ***TPVsystemObj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description – (Specific class) otherwise generic* |
| **Implements the following properties/methods as in TLoadObj, *TIndMach012Obj and TGeneratorObj*:** **RecalcElementData** **CalcYPrim** **MakePosSequence** **InjCurrents** **GetInjCurrents** **GetCurrents** **InitPropertyValues** **DumpProperties** **CalcDailyMult** **CalcDutyMult** **CalcYearlyMult** **GetPropertyValue** **CalcYPrimMatrix** **CalcInjCurrentArray** **GetTerminalCurrents** **DoHarmonicMode** **InitHarmonics** **Integrate** **StickCurrInTerminalArray** **WriteTraceRecord** **Set\_ConductorClosed** **VariableName** **NumVariables** **GetAllVariables** **Get\_Variable** **Set\_Variable** **VariableName** **Randomize** **InitStateVars** **IntegrateStates** **CalcVTerminalPhase** **DoDynamicMode** **DoUserModel** **SetDragHandRegister** **Get\_PresentkW** **Get\_Presentkvar** **Get\_PresentkV** **Set\_PresentkV** **Set\_Presentkvar** **Set\_PresentkW** **Set\_PowerFactor** |  |  |
| **Method- private** | CalcDailyTemperature | Calculates the temperature for the present simulation time in daily simulation mode. |
| **Method- private** | CalcDutyTemperature | Calculates the temperature for the present simulation time in duty cycle simulation mode. |
| **Method- private** | CalcYearlyTemperature | Calculates the temperature for the present simulation time in Yearly cycle simulation mode. |
| **Method- private** | CalcYearlyTemperature | Calculates the temperature for the present simulation time in Yearly cycle simulation mode. |
| **Method- private** | ComputePanelPower | Calculates the total PV power production. |
| **Method- private** | ComputeInverterPower | Calculates the total inverter power. |
| **Method- private** | ComputekWkvar | Calculates the total P and Q contributions of the inverter. |
| **Method- private** | CalcPVSystemModelContribution | Implements the routine for calculating the PV panel power injection. |
| **Method- private** | DoConstantPQPVSystemObj | Routine for calculating PV contribution as model 1. |
| **Method- private** | DoConstantZPVSystemObj | Routine for calculating PV contribution as model 2. |
| **Method- private** | DoConstantZPVSystemObj | Routine for calculating PV contribution as model 2. |
| **Method- private** | UpdatePVSystem | Updates PVSystem elements based on present kW and IntervalHrs variable. |
| **Property-private** | Get\_PresentIrradiance | Returns the present irradiance (pu). |
| **Method- private** | Set\_PresentIrradiance | Sets the present irradiance (pu). |
| **Method- private** | Set\_pf\_wp\_nominal | Sets the variable Fpf\_wp\_nominal with the given value. |
| **Method- private** | Set\_kVARating | Sets the KVA rating for the model. |
| **Method- private** | Set\_Pmpp | Sets the DC power rating for the model. |
| **Method- private** | Set\_puPmpp | Sets the DC power rating for the model (pu). |
| **Method- private** | Get\_Varmode/Set\_Varmode | Sets/gets the var control mode. |
| **Method- private** | Get\_VWmode/Set\_VWmode | Sets/gets the volt-watt control mode. |
| **Method- private** | Get\_WPmode/Set\_WPmode | Sets/gets if PV is in WP mode. |
| **Method- private** | Get\_WVmode/Set\_WVmode | Sets/gets if PV is in WV mode. |
| **Method- private** | Get\_DRCmode/Set\_DRCmode | Sets/gets if PV is in DRC mode. |
| **Method- private** | Get\_AVRmode/Set\_AVRmode | Sets/gets if PV is in AVR mode. |
| **Method- private** | kWOut\_Calc | Calculates the kW production. |
| **Property-public** | Get\_InverterON/ Set\_InverterON | Sets/gets ON/OFF the inverter output. |
| **Method- public** | Get\_VarFollowInverter/ Set\_VarFollowInverter | Sets/gets ON/OFF the inverter var following functionality of the inverter. |
| **Method- public** | Set\_Maxkvar | Sets the maximum kvar for the inverter. |
| **Method- public** | Set\_Maxkvarneg | Sets the minimum limit for kvar production/ absorption. |
| **Method- public** | SetNominalPVSystemOuput | Implements the routine for setting the nominal PV power output. |
| **Property-public** | PresentIrradiance | PA Get\_PresentIrradiance and Set\_PresentIrradiance. |
| **Property-public** | PresentkW | PA Get\_PresentkW and Set\_PresentkW. |
| **Property-public** | Presentkvar | PA Get\_Presentkvar and Set\_Presentkvar. |
| **Property-public** | PresentkV | PA Get\_PresentkV and Set\_PresentkV. |
| **Property-public** | PowerFactor | PA PFnominal (variable) and Set\_PowerFactor. |
| **Property-public** | kVARating | PA PVSystemVars.FkVARating (variable) and Set\_kVARating. |
| **Property-public** | Pmpp | PA PVSystemVars.FPmpp and Set\_pmpp. |
| **Property-public** | puPmpp | PA PVSystemVars.FpuPmpp and Set\_puPmpp. |
| **Property-public** | Varmode | PA Get\_Varmode and Set\_Varmode. |
| **Property-public** | VWmode | PA Get\_VWmode and Set\_VWmode. |
| **Property-public** | VVmode | PA Get\_VVmode and Set\_VVmode. |
| **Property-public** | WPmode | PA Get\_WPmode and Set\_WPmode. |
| **Property-public** | WVmode | PA Get\_WVmode and Set\_WVmode. |
| **Property-public** | AVRmode | PA Get\_AVRmode and Set\_AVRmode. |
| **Property-public** | DRCmode | PA Get\_DRCmode and Set\_DRCmode. |
| **Property-public** | InverterON | PA Get\_InverterON and Set\_InverterON. |
| **Property-public** | VarFollowInverter | PA Get\_VarFollowInverter and Set\_VarFollowInverter. |
| **Property-public** | kvarLimit | PA PVSystemVars.Fkvarlimit (variable) and Set\_Maxkvar. |
| **Property-public** | kvarLimitneg | PA PVSystemVars.Fkvarlimitneg (variable) and Set\_Maxkvarneg. |
| **Property-public** | MinModelVoltagePU | PA VminPu. |
| **Property-public** | pf\_wp\_nominal | PA Set\_pf\_wp\_nominal. |
| **Property-public** | IrradianceNow | PA ShapeFactor.re. |
| **Property-public** | Pmin | PA Get\_Pmin. |
| **Property-public** | Pmax | PA Get\_Pmax. |
| **Property-public** | qMaxInj | PA Get\_qMaxInj. |
| **Property-public** | qMaxAbs | PA Get\_qMaxAbs. |
| **Property-public** | acVmin | PA Get\_acVmin. |
| **Property-public** | acVmax | PA Get\_acVmax. |
| **Property-public** | acVnom | PA Get\_acVnom. |
| **Property-public** | pMaxUnderPF | PA Get\_pMaxUnderPF. |
| **Property-public** | pMaxOverPF | PA Get\_pMaxOverPF. |
| **Property-public** | pMaxCharge | PA Get\_Zero. |
| **Property-public** | apparentPowerChargeMax | PA Get\_Zero. |
| **Property-public** | UsingCIMDynamics | PA Get\_CIMDynamicMode. |



***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create High-Quality Help Documentation with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
