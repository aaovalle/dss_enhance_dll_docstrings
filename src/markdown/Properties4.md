# Properties

&nbsp;

The property list for this device is listed as follows:

&nbsp;

&nbsp;

| **Property** | **Description**&nbsp; |
| --- | --- |
| *Bus1* &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Name of bus to which the UPFC's first terminal (input terminal *“Vin”*) is connected. Remember to specify the node order if the terminals are connected in some unusual manner.&nbsp; |
| *Bus2* &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Name of bus to which the UPFC's second terminal (output terminal *“Vout”*) is connected. Remember to specify the node order if the terminals are connected in some unusual manner.&nbsp; |
| *RefkV*&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | The set point in kV for the voltage regulation controller. The default value is 0.24&nbsp; |
| *PF*&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | The desired power factor to be compensated by the UPFC. The default value is 1.&nbsp; |
| *Frequency*&nbsp; &nbsp; | Frequency of the system. Defaults to circuit fundamental frequency . |
| *Phases* &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Number of phases of the device, the default value is 1.&nbsp; |
| *Xs* &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Impedance in ohms of the series transformer of the UPFC (2πfL). By default, is 0.745 Ω (2mH – 60Hz)&nbsp; |
| *Tol1* &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Corresponds to the desired tolerance for the control algorithms of the UPFC, the default value is 0.02 (2%)&nbsp; |
| *Mode* &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Number (integer) specifying the operation mode. The UPFC has 4 modes of operation: 0: The controllers are turned off; this means that the UPFC will behave as a series impedance with value Xs for all the phases.&nbsp; 1: Voltage regulation mode. In this mode the UPFC only regulates the output voltage; however, there is no reactive compensation. The set point is the one specified in the property RefkV.&nbsp; 2: Reactive power compensation. In this mode the UPFC will compensate reactive power and try to fix the PF programmed in the property PF. There will be no voltage regulation.&nbsp; 3: Dual control mode. In this mode the UPFC performs voltage regulation and reactive power compensation. Both controllers will follow the set points programmed in the properties RefkV and PF.&nbsp; 4: It is a control mode where the user can set two different set points to create a secure GAP, these references must be defined in the parameters *RefkV* and *RefkV2*. The only restriction when setting these values is that *RefkV* must be higher than *RefkV2*. &nbsp; 5: In this mode the user can define the same GAP using two set points as in control mode 4. The only difference between mode 5 and mode 4 is that in mode 5, the UPFC controller performs dual control actions just as in control mode 3.&nbsp; |
| *VpqMax* &nbsp; &nbsp; &nbsp; &nbsp; | It is the maximum voltage (in Volts) that the series voltage source (Vpq) can provide. By default, is 24 V.&nbsp; |
| *LossCurve*&nbsp; &nbsp; | It is the name of the XY curve that describes the losses as a function of the input voltage.&nbsp; |
| *BaseFreq* &nbsp; &nbsp; | Base Frequency for impedance specifications. Default is 60 Hz.&nbsp; |
| *enabled* &nbsp; &nbsp; | {Yes\|No or True\|False} Indicates whether this element is enabled&nbsp; |
| *Like*&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Name of an existing UPFC object on which to base this one.&nbsp; |
| *VHLimit*&nbsp; &nbsp; &nbsp; | High limit for the voltage at the input of the UPFC, if the voltage is above this value the UPFC turns off. This value is specified in Volts (default 300 V)&nbsp; |
| *VLLimit* &nbsp; &nbsp; &nbsp; | Low limit for the voltage at the input of the UPFC, if voltage is below this value the UPFC turns off. This value is specified in Volts (default 125 V)’;&nbsp; |
| *CLImit* &nbsp; &nbsp; &nbsp; &nbsp; | Current Limit for the UPFC, if the current passing through the UPFC is higher than this value the UPFC turns off. This value is specified in Amps (Default 265 A)&nbsp; |
| *RefkV2* &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | The set point in kV for the voltage regulation controller for control modes 4 and 5. The default value is 0&nbsp; |
| *kvarLimit* &nbsp; &nbsp; | This value is the maximum amount of reactive power (kvar) that the UPFC can compensate. (Default 5kvar)&nbsp; |
| *Element* &nbsp; &nbsp; &nbsp; | The name of the PD element monitored when operating with reactive power compensation. Normally, it should be the PD element immediately upstream the UPFC. The element must be defined including the class, e.g. Line.myline. |



***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Output with HelpNDoc's Stunning User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
