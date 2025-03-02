# Schedule

In Schedule mode, a trapezoidal-shaped discharge schedule is specified through *Tup* (up ramp dura- tion), *TFlat* (flat duration), and *Tdn* (down ramp duration) properties, as shown in [*Figure 5*](<PeakShaveLow.md>). The schedule start time is set by *TimeDischargeTrigger* and the rate of discharge for the flat part is determined by %*RatekW* .

In this mode, whenever the simulation time advances and it is within the trapezoidal-shaped dis- charged schedule, a new request is sent by the controller to each storage element in the fleet.

&nbsp;

![A graph with a line and text

Description automatically generated with medium confidence](<lib/NewItem405.png>)

**Figure 3: Operation in Follow Mode**

![A graph of a band

Description automatically generated](<lib/NewItem404.png>)

**Figure 4: Operation in Support Mode**

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Support Your Windows Applications with HelpNDoc's CHM Generation](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
