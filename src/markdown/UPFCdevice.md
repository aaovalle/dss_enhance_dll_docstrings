# UPFC device

&nbsp;

&nbsp;

The Universal Power Flow Controller (UPFC) model developed for EPRI’s OpenDSS corresponds to an equivalent representation for applications on Distribution Systems (DS), where the aim is to regulate voltage for a part of the system and to compensate reactive power to fix a desired power factor (PF). In the current version, the UPFC control actions have been moved into the control queue in OpenDSS, this to make it more stable and improve the accuracy of the model when widely deployed across a medium/large-scale circuit model.

&nbsp;

![Image](<lib/NewItem580.png>)

&nbsp;

Figure 1. General architecture of the UPFC device

&nbsp;

This model is a steady state model and can be used for simulations in sequential-time mode.&nbsp; The variables defined to configure this device allows to configure the set point in terms of the output voltage and PF. Additionally, this generalized model allows to specify the maximum rating for the compensating voltage source (Vpq) and the losses behavior as a function of the input voltage by using XY curves.&nbsp;

&nbsp;

After defining the UPFC device(s) in the model, it is necessary to define an UPFC controller to coordinate the control actions. If the UPFC controller is not defined, the UPFC device(s) will not perform any control action. The UPFC Controller has just a few properties, the only one to consider is UPFCList, in which the user can define the UPFCs that will operate. If this property (UPFCList) is not defined, all the UPFCs in the model will operate. Define the UPFCControl after defining the UPFCs as follows:

&nbsp;

New UPFCControl.myUPFCCtrl

&nbsp;

Or in case the list of UPFCs will be defined:

&nbsp;

New UPFCControl.myUPFCCtrl UPFCList=\[myupfc1, myupfc2, …\]

&nbsp;

For more information, check the example located here:

&nbsp;[https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Version8/Distrib/Examples/UPFC\_Test/](<https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Version8/Distrib/Examples/UPFC\_Test/>)


***
_Created with the Standard Edition of HelpNDoc: [Elevate Your CHM Help Files with HelpNDoc's Advanced Customization Options](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
