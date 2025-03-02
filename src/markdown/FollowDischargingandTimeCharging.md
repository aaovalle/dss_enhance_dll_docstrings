# Follow (Discharging) and Time (Charging)

As explained in [*5.1.3*](<DispatchModes1.md>), the controller operation in Follow mode is similar to the PeakShave mode. The difference is that there is no fixed target value. The target varies according to the power measured at the time specified in *TimeDischargeTrigger* property.

The discharge trigger has been set to 6pm. [Figure 14](<OpenDSSDocumentation.md#\_bookmark23>) shows that the controller regulates the power measured at 6pm indeed. &nbsp; &nbsp; &nbsp;

&nbsp;

New StorageController.SC element=Line.ln5815900-1 terminal=1 modedis=follow

\~ MonPhase=AVG kwtarget=10200 modecharge=Time timeChargeTrigger=2 %rateCharge=50

\~ timeDischargeTrigger=18 %reserve=20 eventlog=yes

&nbsp;

Note that the corresponding band (in kW) also varies depending on the target set at TimeDischargeTrigger.

A fixed band can also be set with property *kWBand*. In this situation, the automatic update of the band as percentage of the varying target is disabled.

![A graph with a line going up

Description automatically generated](<lib/NewItem394.png>)

**Figure 14: Powers at the monitored element in Follow mode with *DischargeTrigger* set to 6pm**


***
_Created with the Standard Edition of HelpNDoc: [Keep Your Sensitive PDFs Safe with These Easy Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
