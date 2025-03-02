# PeakShave

&nbsp;

PeakShave is the default discharge mode. The control attempts to discharge the storage fleet to keep power in the monitored element within a bandwidth (specified by either *%kWBand* or *kWBand* properties) of, or below, the kW value specified by the *kWTarget* property. The controller will request as much power as necessary, limited by the inverter rated kW (*kWrated* property) of each element of the fleet, to accomplish this. The fleet turns itself off when it runs out of stored energy. The basic concept is to follow the load by keeping the load in the monitored terminal at or below the value. [Figure 2](<OpenDSSDocumentation.md#\_bookmark2>) illustrates the operation of the controller in this mode assuming that the fleet has enough energy and power capacity to completely shave the peak. The monitored branch would typically be a line or transformer that might be considered overloaded at the target value. Note that it is possible to change *kWtarget* on the fly for real time control simulation.

&nbsp;

&nbsp;

![A graph with a line and a line](<lib/NewItem406.png>)

**Figure 2: Operation in PeakShave/I-PeakShave Mode**


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Publish Your Word Document as an eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
