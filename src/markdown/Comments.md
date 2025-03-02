# Comments

&nbsp;

Comments can be added to scripts using // or \! as demonstrated below:

&nbsp;

// Edit the voltage regulator control

RegControl.Ctrl1. maxtapchange=1 \! Limit to one tap change

&nbsp;

Multi‐line comments are notated via /\* … \*/. Note that /\* must be on the first column of the line. For example:

&nbsp;

/\* comment out the next two monitors

New Monitor.Source-PQ Vsource.source 1 mode=1 ppolar=no

New Monitor.source-VI Vsource.source 1 mode=0 VIpolar=Yes

\*/

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Spot and Fix Problems in Your Documentation with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
