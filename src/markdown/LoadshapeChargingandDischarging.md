# Loadshape (Charging and Discharging)

In loadshape mode, both charging and discharging of the fleet follows a dispatch curve defined in a loadshape object, as follows.

*&nbsp;*&nbsp; &nbsp; &nbsp; &nbsp;

New LoadShape.SCloadshape interval=1 npts=24 mult=\[0,0,-0.3,-0.45,-0.5,-0.45,-0.3,0,0,0,0,0,0,0,0,0.3,0.5,0.8,0.9,0.8,0.5,0.3,0,0\]

&nbsp;

New StorageController.SC element=Line.ln5815900-1 terminal=1 modedis=loadshape

\~ daily=SCloadshape %rateCharge=50 %reserve=20 eventlog=yes

*&nbsp;*&nbsp; &nbsp; &nbsp;

Note that it is not needed to set *ModeCharge* to Loadshape. This happens automatically when the discharge mode is set to Loadshape. [Figure 22](<OpenDSSDocumentation.md#\_bookmark34>) shows the dispatch curve and the power measured at the beginning of the feeder with and without the controller.

![A graph with lines and numbers

Description automatically generated](<lib/NewItem387.png>)

**Figure 22: Powers at the monitored element and dispatch curve**


***
_Created with the Standard Edition of HelpNDoc: [Revolutionize your documentation process with HelpNDoc's online capabilities](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
