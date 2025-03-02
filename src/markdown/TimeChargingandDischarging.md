# Time (Charging) and (Discharging)

Time discharging mode works the same way as charging, i.e., the fleet is set to charge at the time instant set by the respective time trigger and the fleet remains in the desired dispatch state until fully discharged.

&nbsp;

New StorageController.SC element=Line.ln5815900-1 terminal=1 modedis=time

\~ timeDischargeTrigger=17 %ratekW=100 modecharge=time timeChargeTrigger=2

\~ %rateCharge=50 %reserve=20 eventlog=yes

*&nbsp;*&nbsp; &nbsp; &nbsp;

&nbsp;

![A graph with red lines

Description automatically generated](<lib/NewItem386.png>)

**Figure 23: Powers at the monitored element in example [7.8**](<References2.md#\_bookmark35>)

&nbsp;

Note that the fleet takes 4 hours to charge 30% of its energy capacity (the initial state of charge of each element of the fleet is 70%), whereas it takes only 5 hours to discharge 80% down to %reserve. This is given the charging rate is 50% whereas the discharging rate has been set to 100%.


***
_Created with the Standard Edition of HelpNDoc: [Revolutionize your documentation process with HelpNDoc's online capabilities](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
