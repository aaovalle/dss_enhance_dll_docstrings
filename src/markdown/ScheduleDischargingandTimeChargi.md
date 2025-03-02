# Schedule (Discharging) and Time (Charging)

In Schedule mode, the power requested by the controller to the fleet does not directly depend on a previous power flow solution. However, previous power flow solutions may *indirectly* affect the available energy at the storage, which in turns may impede the fleet to follow the specified schedule, as shown in this example. The storage controller has been specified as follows:&nbsp;

*&nbsp;*&nbsp; &nbsp;

New StorageController.SC element=Line.ln5815900-1 terminal=1 modedis=schedule

\~ tup=3 tflat=4 tdn=2 timeDischargeTrigger=14 modecharge=Time

\~ timeChargeTrigger=2 %ratekW=100 %rateCharge=50 %reserve=20 eventlog=yes

*&nbsp;*&nbsp;

Note that even though the controller does not utilize any power/current reference in this mode, it requires an element to be specified.

&nbsp;

![A graph with numbers and lines

Description automatically generated](<lib/NewItem391.png>)

**Figure 18: Dispatch shape as defined by *Tup*, *Tflat*, *Tdn* and *timeDischargeTrigger* properties**

&nbsp;

[Figure 19](<ScheduleDischargingandTimeChargi.md#\_bookmark29>) shows the power measured at the feeder head along with the total power dispatched by the fleet. Note that during discharging, it precisely follows the schedule until 6pm. However, at 7pm some elements of the fleet are fully depleted, as shown in [Figure 20](<OpenDSSDocumentation.md#\_bookmark30>). The elements that still have energy stored continue following the schedule, until 9pm, when the entire fleet has reached the specified %*reserve*.

&nbsp;

![A graph with red lines and numbers

Description automatically generated](<lib/NewItem390.png>)

**Figure 19: Powers at the monitored element and the total power dispatched by the fleet**

&nbsp;

![A graph of a line graph

Description automatically generated with medium confidence](<lib/NewItem389.png>)

**Figure 20: State of charge of each element of the fleet**
***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Output with HelpNDoc's Stunning User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
