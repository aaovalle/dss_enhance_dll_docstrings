# PeakShaveLow

In PeakShaveLow mode, the fleet is set to charge when the power at a monitored element is below a specified target (*kWTargetLow*). The controller will request as much power as necessary, limited by the inverter rated kW (*kWrated* property) of each element of the fleet, to keep the power within the bandwith (%*kWBandLow* or *kWBandLow*) around *kWTargetLow*. [Figure 6](<OpenDSSDocumentation.md#\_bookmark8>) illustrates the operation of the controller in this mode assuming that the fleet has enough energy and power capacity to completely fill the valley below *kWTargetLow*.

&nbsp;

&nbsp;

![A diagram of a diagram

Description automatically generated](<lib/NewItem403.png>)

**Figure 5: Dispatch shape as defined by *Tup*, *Tflat*, *Tdn* and *timeDischargeTrigger* properties in Schedule Mode**

&nbsp;

![A graph of a band

Description automatically generated with medium confidence](<lib/NewItem402.png>)

**Figure 6: Operation in PeakShaveLow/I-PeakShaveLow Mode**


***
_Created with the Standard Edition of HelpNDoc: [Full-featured Documentation generator](<https://www.helpndoc.com>)_
