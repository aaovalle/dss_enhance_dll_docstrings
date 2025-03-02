# AutoTrans

&nbsp;

&nbsp;

&nbsp;

A three-phase model of an autotransformer used in determining GIC flow is shown in Figure 1. Note that the delta tertiary winding (if applicable) is not included in the DSS model since it does not have any physical connection to ground. The common autotransformer neutral (H0/X0) is modeled explicitly.

&nbsp;

![Image](<lib/NewItem127.png>)

Figure 1 Three-phase Model of a Three-Winding Autotransformer

&nbsp;

&nbsp;

Rw1 and Rw2 are defined as the dc resistance values of the series and common windings, respectively. Transformer windings are modeled in DSS with resistive branch circuits as shown in Figure 2.

&nbsp;

![Image](<lib/NewItem128.png>)\
Figure 2. Two-winding and Three-winding Autotransformer model in DSS

&nbsp;

The winding terminals designated as NX.1, NX.2, and NX.3 in Figure 48 must be connected together to construct the neutral connection. The bus numbers are arbitrary, but typically the name of the high side bus with the next available terminal number is used to designate the neutral bus. An example OpenDSS script with high voltage bus named ‘Bus1’, low voltage bus named ‘Bus2’, dc winding resistance of 0.1 Ω/phase for the series winding and 0.2 Ω/phase for the common winding is as follows:

&nbsp;

New GICTransformer.T1 busH=Bus1.1.2.3 busX=Bus2.1.2.3 busNX=Bus1.4.4.4 R1=0.1 R2=0.2 type=auto

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Streamline Your CHM Help File Creation with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
