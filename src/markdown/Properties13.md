# Properties

&nbsp;

Following are presented the commands and properties of the GICTransformer Model

&nbsp;

| %R1 | Optional. Percent Resistance, each phase, for H winding (1), (Series winding, if Auto). Default is 0.2. &nbsp; Alternative way to enter R1 value. It is the actual resistances in ohmns that matter. MVA and kV should be specified. |
| --- | --- |
| %R2 | Optional. Percent Resistance, each phase, for H winding (1), (Series winding, if Auto). Default is 0.2. &nbsp; Alternative way to enter R1 value. It is the actual resistances in ohmns that matter. MVA and kV should be specified. |
| basefreq | Base Frequency for ratings. |
| busH | Name of High-side(H) bus. Examples: BusH=busname BusH=busname.1.2.3 |
| busNH | Name of Neutral bus for H, or first, winding. Defaults to all phases connected to H-side bus, node 0, if not specified and transformer type is either GSU or YY. (Shunt Wye Connection to ground reference)For Auto, this is automatically set to the X bus. |
| busNX | Name of Neutral bus for X, or Second, winding. Defaults to all phases connected to X-side bus, node 0, if not specified. (Shunt Wye Connection to ground reference) |
| busX | Name of Low-side(X) bus, if type=Auto or YY.&nbsp; |
| emergamps | Maximum or emerg current. |
| enabled | {Yes\|No or True\|False} Indicates whether this element is enabled. |
| faultrate | Failure rate per year. |
| K | Mvar K factor. Default way to convert GIC Amps in H winding (winding 1) to Mvar. Default is 2.2. Commonly-used simple multiplier for estimating Mvar losses for power flow analysis. &nbsp; Mvar = K \* kvLL \* GIC per phase / 1000 &nbsp; Mutually exclusive with using the VarCurve property and pu curves.If you specify this (default), VarCurve is ignored. |
| KVLL1 | Optional. kV LL rating for H winding (winding 1). Default is 500. Required if you are going to export vars for power flow analysis or enter winding resistances in percent. |
| KVLL2 | Optional. kV LL rating for X winding (winding 2). Default is 138. Required if you are going to export vars for power flow analysis or enter winding resistances in percent.. |
| like | Make like another object |
| MVA | Optional. MVA Rating assumed Transformer. Default is 100. Used for computing vars due to GIC and winding resistances if kV and MVA ratings are specified. |
| normaamps | Normal rated current. |
| pctperm | Percent of failures that become permanent. |
| phases | Number of Phases. Default is 3. |
| R1 | Resistance, each phase, ohms for H winding, (Series winding, if Auto). Default is 0.0001. |
| R2 | Resistance, each phase, ohms for X winding, (Common winding, if Auto). Default is 0.0001.&nbsp; |
| repair | Hours to repair. |
| Type | Type of transformer: {GSU\* \| Auto \| YY}. Default is GSU. |
| VarCurve | Optional. XYCurve object name. Curve is expected as TOTAL pu vars vs pu GIC amps/phase. Vars are in pu of the MVA property. No Default value. Required only if you are going to export vars for power flow analysis. See K property. |


&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Make your documentation accessible on any device with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
