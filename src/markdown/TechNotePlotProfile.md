# TechNote Plot Profile

&nbsp;

A new type has been added to the Plot command:

&nbsp;

Plot \[type=\]Profile

&nbsp;

This plot is designed to show the voltage profile along the feeder. It plots selected voltages vs distance from the substation (actually Energymeter object upline from the bus). It requires an EnergyMeter object, which should be placed at the head of a feeder.

&nbsp;

The command uses the "Phases" property of the Plot command to determine which voltages to plot.

&nbsp;

The following are examples for the IEEE 8500node test feeder (unbalanced).

&nbsp;

***The Default***

&nbsp;

Plot Profile \[phases=default\]

&nbsp;

This form of the command plots only phases 1, 2, or 3 of buses having at least 3 phases.

&nbsp;

![Image](<lib/NewItem58.png>)

&nbsp;

***Primary Only***

&nbsp;

Plot Profile Phases=primary

&nbsp;

Plots only voltages at buses where the kV base is greater than 1 kV. This picks up some 1phase buses and nodes that are isolated through open switches (zero voltage)

&nbsp;

![Image](<lib/NewItem59.png>)

&nbsp;

***All Nodes***

&nbsp;

Plot Profile Phases=all

&nbsp;

Plots all node voltages. Secondaries are shown with dashed lines and usually appear nearly vertical on this scale. The secondaries are generally short so that the lines are nearly vertical. This clearly shows the voltage drop across the secondary service drop.

&nbsp;

![Image](<lib/NewItem60.png>)

&nbsp;

***One Phase Only***

&nbsp;

Plot Profile Phases=1

&nbsp;

Plots only those voltages at nodes designated as "1". (This shows some secondaries that are actually connected to other primary phases, but are designated as phase 1. Note that you may designate the secondary node numbers to match the primary node numbers if your want this to look differently.)

&nbsp;

![Image](<lib/NewItem61.png>)

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Easily create iPhone documentation](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
