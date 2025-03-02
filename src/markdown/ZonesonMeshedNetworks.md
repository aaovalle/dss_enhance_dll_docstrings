# Zones on Meshed Networks

\
While the concept of zones nominally applies to radial circuits, judicious placement of energy meters can make the concept useful for meshed networks as well. Keep in mind that there can be many EnergyMeter objects defined in the circuit. Their placement does not necessarily have to represent reality; they are for the reporting of power and energy quantities throughout the system.

&nbsp;

The automatic algorithm for determining zones will determine zones consistently for meshed networks, although the zones themselves may not be radial. If there are several meters on the network that could be monitoring the same zone, the first one defined will have access to all the elements except the ones containing the other meters. The others will have only one element in their zone, as in Figure 52.

&nbsp;

![Image](<lib/NewItem132.png>)\
Figure 52. Default Meter Zones for a Simple Network

&nbsp;

Don't put any load at tie point or take care in processing meter information so that it isn't counted more than once. All three of the meters added would see the center-most bus in Figure 53.

&nbsp;

![Image](<lib/NewItem133.png>)\
Figure 53. Using Additional Meters to Control the Definition of Meter Zones

***
_Created with the Standard Edition of HelpNDoc: [Enhance Your Documentation with HelpNDoc's Advanced Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
