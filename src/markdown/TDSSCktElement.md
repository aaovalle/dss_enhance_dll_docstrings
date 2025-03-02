# TDSSCktElement

| ***TDSSCktElement*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description – (Specific class) otherwise generic* |
| **Method- private** | Set\_Freq | Set frequency and recompute YPrim. |
| **Method- private** | Set\_Nconds | Sets the number of conductors and creates the conductor array within the class for the caller. |
| **Method- private** | Set\_NPhases | Sets the number of phases for the device. |
| **Method- private** | Set\_ActiveTerminal | Activates the given terminal for future queries/operations. |
| **Property- private** | Get\_ConductorClosed | Evaluates if the conductor given by index is closed. |
| **Method- private** | Set\_YprimInvalid | Sets the YPrim invalid flag (Boolean) in the value given in the argument. |
| **Property- private** | Get\_YprimInvalid | Returns the value of the YPrim invalid Boolean flag. |
| **Property- private** | Get\_FirstBus | Returns the name of bus 1 for the element. |
| **Property- private** | Get\_NextBus | Returns the name of next bus of the element. |
| **Property- private** | Get\_Losses | Returns the total losses for the caller. |
| **Property- private** | Get\_Power | Gets total complex power in active terminal. |
| **Property- private** | Get\_MaxPower | Gets equivalent total complex power in active terminal based on phase with max current. |
| **Property- private** | Get\_MaxCurrent | Gets equivalent total complex current on phase with max current. Uses the terminal number given in the argument. |
| **Property- private** | Get\_MaxCurrentAng | Gets equivalent angle of the total complex current on phase with max current. Uses the terminal number given in the argument. |
| **Property- private** | Get\_MaxVoltage | Gets equivalent total complex voltage on phase using the terminal index given in the argument. |
| **Property- private** | Get\_MaxVoltageAng | Gets equivalent total complex voltage phase angle on phase using the terminal index given in the argument. |
| **Property- private** | Get\_PCE\_Value | Gets a value for the active PCE such as P, Q, Vmag, IMag, etc. The value type is given in the argument as an integer number. |
| **Method- private** | DoYprimCalcs | Calculates the YPrim matrix for the caller. |
| **Method- protected** | Set\_Enabled | Sets the enabled flag using the Boolean value given in the argument. |
| **Method- protected** | Set\_ConductorClosed | Sets the conductor closed flag using the index and Boolean values given in the argument. |
| **Method- protected** | Set\_NTerms | Sets the number of terminals for the calling object. |
| **Method- protected** | Set\_Handle | Sets a handle in the form of an integer number for the calling object. |
| **Property- public** | GetYPrim | Returns a handler to the object’s YPrim depending on the type of matrix specified in the argument (series, shunt, full). |
| **Property- public** | GetYPrimValues | Returns the values of the object’s YPrim specified in the argument (series, shunt, full). |
| **Property- public** | MaxTerminalOneIMag | Get max of phase currents on the first terminal; Requires computing Iterminal. |
| **Method- public** | ComputeIterminal | Computes Iterminal for this device and put them into a local array. |
| **Method - public** | ComputeVterminal | Extracts the voltages in the active terminal of the calling object and put terminal voltages in an array. |
| **Method - public** | ZeroITerminal | Sets the local current array to 0. |
| **Method - public** | GetCurrents | Get present value of terminal Currents for reports. |
| **Method- public** | GetInjCurrents | Returns last Injection currents calculated for this object (caller). |
| **Property- public** | InjCurrents | Applies to PC Elements. Puts the injection currents locally calculated straight into the Solution Array. |
| **Property- public** | GetBus | Returns the name of the bus addressed using the index in the argument. |
| **Method- public** | SetBus | Sets the name of the bus addressed using the index in the argument. |
| **Method- public** | SetNodeRef | Set NodeRef Array for fast solution with intrinsics. |
| **Method- public** | RecalcElementData | Default for recalculating the foundation of the calling element. It is expected to be override by a more specific class. If not overridden, when called it will trigger an error message.&nbsp; |
| **Method- public** | CalcYPrim | Calculates the YPrim type given in the argument (series, shunt, full). |
| **Method- public** | MakePosSequence | Make a positive Sequence Model for the calling object. |
| **Method- public** | GetTermVoltages | Fills Vbuffer array which must be adequately allocated by calling routine. Vbuffer is the local array for storing the element voltages. |
| **Method- public** | GetPhasePower | Gets the power in each phase (complex losses) of active terminal neutral conductors are ignored by this routine. |
| **Method- public** | GetPhaseLosses | Gets the losses in each phase (complex losses); Power difference coming out each phase. Note: This can be misleading if the nodev voltage is greatly unbalanced. Neutral conductors are ignored by this routine. |
| **Method- public** | GetLosses | Returns total losses and set LoadLosses=total losses and noload losses =0. |
| **Method- public** | GetSeqLosses | For the base class, just return Complex ZERO. |
| **Property- public** | GetPropertyValue | Returns the value (string) for the property indicated by index in the argument. |
| **Method- public** | InitPropertyValues | Initializes the property values for the class with the default values. |
| **Method- public** | DumpProperties | Implements the routine for writing the local properties down into a plain text file at the end. |
| **Property- public** | Handle | PA FHandle (local handle) and Set\_Handle. |
| **Property- public** | Enabled | PA FEnabled (variable) and Set\_Enabled. |
| **Property- public** | YPrimInvalid | PA get\_YprimInvalid and set\_YprimInvalid. |
| **Property- public** | YPrimFreq | PA FYprimFreq (variable)&nbsp; and Set\_Freq. |
| **Property- public** | NTerms | PA Fnterms (variable) and Set\_NTerms. |
| **Property- public** | NConds | PA Fnconds (variable) and Set\_Nconds. |
| **Property- public** | NPhases | PA Fnphases (variable) and Set\_NPhases. |
| **Property- public** | FirstBus | PA Get\_FirstBus. |
| **Property- public** | NextBus | PA Get\_NextBus. |
| **Property- public** | Losses | PA Get\_Losses. |
| **Property- public** | Power | PA Get\_Power. |
| **Property- public** | MaxPower | PA Get\_MaxPower. |
| **Property- public** | MaxCurrent | PA Get\_MaxCurrent. |
| **Property- public** | MaxVoltage | PA Get\_MaxVoltage. |
| **Property- public** | MaxCurrentAng | PA Get\_MaxCurrentAng. |
| **Property- public** | MaxVoltageAng | PA Get\_MaxVoltageAng. |
| **Property- public** | ActiveTerminalIdx | PA FActiveTerminal (variable) and Set\_ActiveTerminal. |
| **Property- public** | Closed | PA Get\_ConductorClosed and Set\_ConductorClosed. |
| **Property- public** | PCEValue | PA Get\_PCE\_Value. |
| **Method- public** | SumCurrents | Sums the terminal Currents into System Currents Array primarily for Newton Iteration. |
| **Method- public** | Get\_Current\_Mags | Returns the Currents vector in magnitude. |



***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
