# Calculation of the monitored voltage in Volts

The voltages sampled by InvControl can be the nodal voltages of the controlled element or line-to-line and/or line-to-ground voltages of monitored bus or buses.

&nbsp;

&nbsp;

![A diagram of a control system

Description automatically generated](<lib/NewItem474.png>)

**Figure 8: Block diagram of the control loop when only *InvControl* elements are considered**

&nbsp;

By default the InvControl samples the nodal voltages of the controlled element. For example, for a three-phase element, the voltages monitored in *V* can be written according to [Equation 29](<Calculationofthemonitoredvoltage.md#\_bookmark33>).

&nbsp;

![Image](<lib/NewItem512.png>)

In order to sample voltages of monitored bus or buses, the *monBus* and *monBusesVbase* properties of InvControl must be used. The *monBus* property stores the monitored buses and their nodes defined in a list and the *monBusesVbase* property stores the list with the corresponding base voltages for each of these monitored buses. For instance, [Equation 30](<OpenDSSDocumentation.md#\_bookmark34>) shows the list with two monitored voltages (resulted from power flow) and [Equation 31](<OpenDSSDocumentation.md#\_bookmark35>) the list with their respective base voltages.

&nbsp;

![Image](<lib/NewItem513.png>)

&nbsp;

![Image](<lib/NewItem514.png>)

&nbsp;

Where:

* *VmonBusA*1 \[*t*\]*j* corresponds to the line-to-ground voltage of the node 1 of the bus *A*;
* *VmonBusB*12 \[*t*\]*j* corresponds to the line-to-line voltage between the nodes 1 and 2 of the bus *B*.

The values of the voltages of [Equation 30](<OpenDSSDocumentation.md#\_bookmark34>) can present base voltages with distinct values and therefore, this list must have its values corrected to the same base voltage, which correspond to the rated voltage of the controlled element, as presented in [Equation 32](<Calculationofthemonitoredvoltage.md#\_bookmark36>). This is necessary so that the calculation of the monitored voltage in *V* is made considering voltages of the same order of magnitude.

&nbsp;

![Image](<lib/NewItem515.png>)

&nbsp;

Where:

* *Velementbase* corresponds to the rated voltage of the controlled element which is the *kV* property value of the *PVSystem*.

A unique monitored voltage in *V* is calculated from one of the two lists present in Equations [29](<Calculationofthemonitoredvoltage.md#\_bookmark33>) or [32](<Calculationofthemonitoredvoltage.md#\_bookmark36>). The options for this selection are present in the *monVoltageCalc* property and are applied in the list to calculate the maximum, minimum or average value, according to the options described below:

* For *AVG*, the average monitored voltage is calculated by applying the mean in the list;
* For *MAX*, the monitored voltage is the maximum value present in the list;
* For *MIN*, the monitored voltage is the minimum value present in the list.

Thus, as a result, the monitored voltage in *V* is defined as *Vmon*\[*t*\]*j*.

***
_Created with the Standard Edition of HelpNDoc: [Leave the tedious WinHelp HLP to CHM conversion process behind with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
