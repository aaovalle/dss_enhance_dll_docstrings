# PeakShave (Discharging) and PeakShaveLow (Charging)

In this example, PeakShave and PeakShaveLow modes are applied simultaneously. For the PeakShave mode, the target has been set to 10.2MW and for the PeakShaveLow, it has been set to 8.5MW. The initial stored energy of each element of the fleet has been reduced to 20% of the respective rated capacity, *kWhrated*, such that the fleet operates in charging mode from 1 to 8am. &nbsp;

&nbsp;

BatchEdit Storage..\* %stored=20

New StorageController.SC element=Line.ln5815900-1 terminal=1 modedis=peakShave

\~ MonPhase=AVG kwtarget=10200 modecharge=peakShaveLow kwtargetLow=8500

\~ eventlog=yes %reserve=20

*&nbsp;*&nbsp; &nbsp; &nbsp;

The fleet can shave both peaks, as shown in [Figure 21](<OpenDSSDocumentation.md#\_bookmark32>). Note that the charging of the fleet starts at midnight, as the system’s loading drops below *kWTargetLow* at this time step.

![A graph with red line

Description automatically generated](<lib/NewItem388.png>)

**Figure 21: Powers at the monitored element**

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Don't Let Unauthorized Users View Your PDFs: Learn How to Set Passwords](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
