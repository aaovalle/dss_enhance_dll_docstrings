# TLoadObj

| ***TLoadObj*** |  |  |
| --- | --- | --- |
| ***Type-access*** | *Command* | *Description – (Specific class) otherwise generic* |
| **Property- private** | AllTerminalsClosed | Gets a Boolean flag indicating if all the terminals for the active element are closed (true). |
| **Method- private** | Set\_CalcDailyMult | Calculates the multiplier for daily simulation at the simulation time step given in the argument, using the given load shape for daily simulation if any. |
| **Method- private** | CalcDutyMult | Calculates the multiplier for duty simulation at the simulation time step given in the argument, using the given load shape for duty simulation if any. |
| **Method- private** | CalcInjCurrentArray | Fills the Injection Current array with the current values to use for injections. |
| **Method- private** | CalcLoadModelContribution | Calculates total load current and adds it properly into the Injection Current array. |
| **Method- private** | CalcVTerminalPhase | Establishes the phase voltages and stick them into Vtemp (local voltage array). |
| **Method- private** | CalcYearlyMult | Calculates the multiplier for yearly simulation at the simulation time step given in the argument, using the given load shape for yearly simulation if any. |
| **Method- private** | CalcCVRMult | Calculates the multiplier for yearly simulation using the CVR curve. CVR curve is assumed to be used in a yearly simulation. |
| **Method- private** | CalcYPrimMatrix | Calculates the Y primitive matrix for the model. |
| **Method- private** | DoConstantILoad | Implements the routine for calculating the contribution of the load as a constant current load model. |
| **Method- private** | DoConstantPQLoad | Implements the routine for calculating the contribution of the load as a constant PQ load model. |
| **Method- private** | DoConstantZLoad | Implements the routine for calculating the contribution of the load as a constant impedance load model. |
| **Method- private** | DoFixedQ | Implements the routine for calculating the contribution of the load as a Constant P, Fixed Q load model. Q is always kvarBase. |
| **Method- private** | DoFixedQZ | Implements the routine for calculating the contribution of the load as a Constant P, Fixed Q load model. Q is always a fixed Z derived from kvarBase. |
| **Method- private** | DoHarmonicMode | Implements the routine for calculating the injection currents for the model in harmonics simulation mode. |
| **Method- private** | DoCVRModel | Implements the routine for calculating the contribution of the load as a Linear P, quadratic Q load model. |
| **Method- private** | DoZIPVModel | Implements the routine for calculating the contribution of the load as a ZIP model. |
| **Method- private** | SetZIPVSize | Allocates the memory needed for storing the ZIP coefficients for the load. |
| **Method- private** | DoMotorTypeLoad | Implements the routine for calculating the contribution of the load as a motor load model. |
| **Property- private** | GrowthFactor | Returns the multiplier for the year given in the argument to be used as load growth in time-based simulation modes. |
| **Method- private** | StickCurrInTerminalArray | Puts the current into the proper location according to connection. |
| **Property- private** | InterpolateY95\_YLow | Routine for Vmag between V95 and Vlow, interpolate for equivalent Y. |
| **Property- private** | InterpolateY95I\_YLow | Routine for Vmag between V95 and Vlow, interpolate for equivalent Y.&nbsp; |
| **Property- private** | Get\_Unserved | Returns the number of unserved customers at this load. |
| **Method- private** | Set\_kVAAllocationFactor | Sets the KVA allocation factor for the active load. |
| **Method- private** | Set\_ConnectedkVA | Sets the amount of KVA represented by this load. |
| **Method- private** | ComputeAllocatedLoad | Calculates the amount of load allocated at the current connection point. Fixed loads defined by kW, kvar or kW, pf are ignored. |
| **Method- private** | Set\_CFactor | Sets the kWh billed spec. Computes the allocated load. |
| **Method- private** | Set\_kWh | Sets the amount of kWh for the load at present. Computes the allocated load. |
| **Method- private** | Set\_kWhDays | Sets the amount of kWh days for the load at present. Computes the allocated load. |
| **Method- private** | Set\_AllocationFactor | Sets the allocation factor for the load. |
| **Method- private** | SetkWkvar | Sets kW and kvar for the load, both given in the arguments. |
| **Method- private** | set\_nZIPV | Reallocates memory for ZIP coefficients.&nbsp; |
| **Method- protected** | GetTerminalCurrents | Overrides the more generic foundation.&nbsp; Obtains the present current values at the active terminal. |
| **Property- public** | Get\_ExceedsNormal | Routine for determining if the voltage values at present for the load exceed the normal limits. |
| **Method- public** | RecalcElementData | Overrides the more generic function. Recalculates the values required for the element. |
| **Method- public** | CalcYPrim | Overrides the more generic function. Recalculates the YPrim.&nbsp; |
| **Property- public** | InjCurrents | Overrides the more generic function. Gets the injection currents and add them directly into the Currents array. |
| **Method- public** | GetInjCurrents | Overrides the more generic function. Gets the injection currents for the last solution performed. |
| **Method- public** | InitHarmonics | Overrides the more generic function. Initializes the load values for harmonic simulation. |
| **Method- public** | MakePosSequence | Overrides the more generic function. Makes the positive sequence model for the element. |
| **Method- public** | SetNominalLoad | Sets nominal load for different simulation modes. |
| **Method- public** | Randomize | Randomizes the load multiplier value locally using 3 distribution options (0=none, 1=Gaussian, 2=Uniform). |
| **Property- public** | GetPropertyValue | Overrides the more generic function. Returns the value (string) for the property indicated by index in the argument. |
| **Method- public** | InitPropertyValues | Overrides the more generic function. Initializes the local property array with the default values. |
| **Method- public** | DumpProperties | Overrides the more generic function. Implements the routine for writing the local properties down into a plain text file at the end. |
| **Method- public** | UpdateVoltageBases | Updates the voltage bases for the load. |
| **Property- public** | Unserved | PA Get\_Unserved. |
| **Property- public** | AllocationFactor | PA FAllocationFactor (variable) and Set\_AllocationFactor. |
| **Property- public** | kVAAllocationFactor | PA FkVAAllocationFactor (variable) and Set\_kVAAllocationFactor. |
| **Property- public** | ConnectedkVA | PA FConnectedkVA (variable) Set\_ConnectedkVA. |
| **Property- public** | kWh | PA FkWh (variable) and Set\_kWh. |
| **Property- public** | kWhDays | PA FkWhDays (variable) and Set\_kWhDays. |
| **Property- public** | CFactor | PA FCFactor (variable) and Set\_CFactor. |
| **Property- public** | puMean | PA FpuMean (variable). |
| **Property- public** | puStdDev | PA FpuStdDev (variable). |
| **Property- public** | CVRwatts | PA FCVRwattFactor (variable). |
| **Property- public** | CVRvars | PA FCVRvarFactor (variable). |
| **Property- public** | MaxPU | PA Vmaxpu (variable). |
| **Property- public** | MinEmerg | PA VminEmerg (variable). |
| **Property- public** | MinNormal | PA VminNormal (variable). |
| **Property- public** | MinPU | PA Vminpu (variable). |
| **Property- public** | ExemptLoad | PA ExemptFromLDCurve (variable). |
| **Property- public** | FixedLoad | PA Fixed (variable). |
| **Property- public** | nZIPV | PA FnZIPV (variable) and set\_nZIPV. |
| **Property- public** | IsPFSpecified | PA PFSpecified (variable). |



***
_Created with the Standard Edition of HelpNDoc: [Don't Let Unauthorized Users View Your PDFs: Learn How to Set Passwords](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
