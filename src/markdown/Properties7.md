# Properties

&nbsp;

The properties, in order, are:

&nbsp;

| bus1 | Name of bus to which the load is connected. Include node definitions if the terminal conductors are connected abnormally. 3-phase Wye-connected loads have 4 conductors; Delta-connected have 3. Wye-connected loads, in general, have one more conductor than phases. 1-phase Delta has 2 conductors; 2-phase has 3. The remaining Delta, or line-line, connections have the same number of conductors as phases. |
| --- | --- |
| Phases | No. of phases this load. |
| Kv | Base voltage for load. For 2- or 3-phase loads, specified in phase-to-phase kV. For all other loads, the actual kV across the load branch. If wye (star) connected, then specify phase-to-neutral (L-N). If delta or phase-to-phase connected, specify the phase-to-phase (L-L) kV. |
| Kw | nominal active power, kW, for the load. Total of all phases. See kVA. |
| Pf | nominal Power Factor for load. Negative PF is leading. Specify either PF or kvar (see below). If both are specified, the last one specified takes precedence. |
| Model | Integer defining how the load will vary with voltage (see “Power Conversion Elements” for more details). The load models currently implemented are: 1: Constant P and constant Q (Default): Commonly used for power flow studies 2: Constant Z (or constant impedance) 3: Constant P and quadratic Q 4: Exponential:&nbsp; ![Image](<lib/eq61.png>) and&nbsp; ![Image](<lib/eq66.png>) (See CVRwars ans CVRvar) 5: Constant I (or constant current magnitude) Sometimes used for rectifier load 6: Constant P and fixed Q (at the nominal value) 7: Constant P and quadratic Q (i.e., fixed reactance) 8: ZIP (see ZIPV) "Constant" power value (either P or Q) may be modified by loadshape multipliers. "Fixed" power values are always the same -- at nominal, or base, value.&nbsp; |
| Yearly | Name of Yearly load shape. |
| Daily | Name of Daily load shape. |
| Duty | name of Duty cycleload shape. Defaults to Daily load shape if not defined. |
| Growth | Name of Growth Shape Growth factor defaults to the circuit's default growth rate if not defined. (see Set %Growth command) |
| Conn | {wye \| y \| LN} for Wye (Line-Neutral) connection; {delta \| LL} for Delta (Line-Line) connection. Default = wye. |
| kvar | Base kvar. If this is specified, supercedes PF. (see PF) |
| Rneut | Neutral resistance, ohms. If entered as negative, non-zero number, neutral is assumed open, or ungrounded. Ignored for delta or line-line connected loads. |
| Xneut | Neutral reactance, ohms. Ignored for delta or line-line connected loads. Assumed to be in series with Rneut value. |
| Status | {fixed\| variable}. Default is variable. If fixed, then the load is not modified by multipliers; it is fixed at its defined base value. |
| Class | Integer number segregating the load according to a particular class. |
| Vminpu | Default = 0.95. Minimum per unit voltage for which the MODEL is assumed to apply. Below this value, the load model reverts to a constant impedance model. |
| Vmaxpu | Default = 1.05. Maximum per unit voltage for which the MODEL is assumed to apply. Above this value, the load model reverts to a constant impedance model. |
| VminNorm | Minimum per unit voltage for load EEN evaluations, Normal limit. Default = 0, which defaults to system "vminnorm" property (see Set Command under Executive). If this property is specified, it ALWAYS overrides the system specification. This allows you to have different criteria for different loads. Set to zero to revert to the default system value. |
| VminEmerg | Minimum per unit voltage for load UE evaluations, Emergency limit. Default = 0, which defaults to system "vminemerg" property (see Set Command under Executive). If this property is specified, it ALWAYS overrides the system specification. This allows you to have different criteria for different loads. Set to zero to revert to the default system value. |
| XfkVA | Default = 0.0. Rated kVA of service transformer for allocating loads based on connected kVA at a bus. Side effect: kW, PF, and kvar are modified. See PeakCurrent property of EnergyMeter. See also AllocateLoads Command. See kVA property below. |
| AllocationFactor | Default = 0.5. Allocation factor for allocating loads based on connected kVA at a bus. Side effect: kW, PF, and kvar are modified by multiplying this factor times the XFKVA (if \> 0). See also AllocateLoads Command. |
| kVA | Definition of the Base load in kVA, total all phases. This is intended to be used in combination with the power factor (PF) to determine the actual load. Legal ways to define base load (kW and kvar):&nbsp; kW, PF kW, kvar kVA, PF XFKVA \* Allocationfactor, PF kWh/(kWhdays\*24) \* Cfactor, PF |
| %mean | Percent mean value for load to use for monte carlo studies if no loadshape is assigned to this load. Default is 50. |
| %stddev | Percent Std deviation value for load to use for monte carlo studies if no loadshape is assigned to this load. Default is 10. |
| CVRwatts | Exponential paramater that defines the relationship between voltage (𝑉) and active power (𝑃) based on the following:&nbsp; ![Image](<lib/eq61.png>) P0 is the nominal power of the load at the base voltage V0. &nbsp; CVRwatts default=1 (linear relationship between voltage and active power). Typical values range from 0.4 to 0.8. Applies to Model=4 only. |
| CVRvars | Exponential paramater that defines the relationship between voltage (𝑉) and reactive power (Q) based on the following:&nbsp; ![Image](<lib/eq66.png>)&nbsp; Q0 is the nominal power of the load at the base voltage V0. CVRvars default=2 (quadratic relationship between voltage and reactive power). Typical values range from 2 to 3. Applies to Model=4 only. |
| kWh | kWh billed for this period. Default is 0. See help on kVA and Cfactor and kWhDays. |
| kWhDays | Length of kWh billing period in days (24 hr days). Default is 30. Average demand is computed using this value. |
| CFactor | Factor relating average kW to peak kW. Default is 4.0. See kWh and kWhdays. See kVA. |
| CVRCurve | Default is NONE. Curve describing both watt and var factors as a function of time. Refers to a LoadShape object with both Mult and Qmult defined. Define a Loadshape to agree with yearly or daily curve according to the type of analysis being done. If NONE, the CVRwatts and CVRvars factors are used and assumed constant for the simulation period. |
| NumCust | Number of customers, this load. Default is 1. |
| spectrum | Name of harmonic current spectrum for this load. Default is "defaultload", which is defined when the DSS starts. |
| ZIPV | Array of 7 coefficients: 1. First 3 are ZIP weighting factors for active power (should sum to 1) 2. Next 3 are ZIP weighting factors for reactive power (should sum to 1) 3. Last 1 is cut-off voltage in p.u. of base kV; load is 0 below this cut-off No defaults; all coefficients must be specified if using model=8. |
| %SeriesRL | Percent of load that is series R-L for Harmonic studies. Default is 50. Remainder is assumed to be parallel R and L. This has a significant impact on the amount of damping observed in Harmonics solutions. |
| RelWeight | Relative weighting factor for reliability calcs. Default = 1. Used to designate high priority loads such as hospitals, etc.&nbsp; Is multiplied by number of customers and load kW during reliability calcs. |
| Vlowpu | Default = 0.50. Per unit voltage at which the model switches to same as constant Z model (model=2). This allows more consistent convergence at very low voltages due to opening switches or solving for fault situations. |
| puXharm | Special reactance, pu (based on kVA, kV properties), for the series impedance branch in the load model for HARMONICS analysis. Generally used to represent motor load blocked rotor reactance. If not specified (that is, set =0, the default value), the series branch is computed from the percentage of the nominal load at fundamental frequency specified by the %SERIESRL property. Applies to load model in HARMONICS mode only. A typical value would be approximately 0.20 pu based on kVA \* %SeriesRL / 100.0. |
| XRharm | X/R ratio of the special harmonics mode reactance specified by the puXHARM property at fundamental frequency. Default is 6. |


&nbsp;

Inherited Properties

&nbsp;

| Spectrum | Name of harmonic current spectrum for this load. Default is "defaultload", which is defined when the DSS starts. |
| --- | --- |
| Basefreq | Base frequency for which this load is defined. Default is 60.0 |
| Like | Name of another Load object on which to base this one. |



***
_Created with the Standard Edition of HelpNDoc: [Streamline your documentation process with HelpNDoc's HTML5 template](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
