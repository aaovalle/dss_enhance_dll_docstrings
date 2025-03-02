# Default Circuit

&nbsp;

\
When a new circuit is instantiated, it is created as a 3-phase voltage source named "Source" connected to a bus named "SourceBus" with a reasonable short circuit strength for transmission systems feeding distribution substations.

&nbsp;

![Image](<lib/NewItem134.png>)

Figure 1. Default Circuit

&nbsp;

The default values for the source are (see Vsource object definition):

&nbsp;

•115 kV

&nbsp;

•3000 MVA short circuit

&nbsp;

Thus, the circuit can be immediately solved, albeit with a trivial result.\
\
The circuit is also immediately available for adding a substation and/or lines for a quick manual circuit modeling task.

&nbsp;

The default circuit model does not include a substation transformer because the user may wish to study more than one substation connected by a non-trivial transmission or sub-transmission network.


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your CHM Help File Capabilities with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
