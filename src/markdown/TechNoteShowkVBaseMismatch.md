# TechNote Show kVBaseMismatch

&nbsp;

Debugging Aid: Show kVBaseMismatch Command

&nbsp;

As a circuit debugging aid, the Show kVBaseMismatch command has been added. This may be abbreviated to "show k" for now until something else is added that starts with "k".&nbsp;

&nbsp;

Help now has the Show command separated from the rest of the commands. Help for the Plot and Export commands has also been separated.&nbsp;

&nbsp;

This command will let you know after the bus base voltages have been established if the loads and generators match the kV base of the bus to which they are connected. The report shows you the mismatch found and two possible fixes. Since either the bus base kV or the Load kV may be in error, the report provides commands to correct either.

&nbsp;

\!\!\! LOAD VOLTAGE BASE MISMATCHES

\!\!\!\!\! Voltage Base Mismatch, Load.s100c.kV=12, Bus 100.3 LN kvBase = 2.40178

\!setkvbase bus=100 kVLN=12

\!Load.s100c.kV=2.40178

&nbsp;

Just remove the "\!" (inline comment) from the line you want to keep and the report becomes a script for correcting the errors (unless you have the Loads or Generators on the wrong bus).

&nbsp;

Sort the script file and copy only the lines you want. Keep them in a separate script file to be executed from your main script probably after the CalcVoltageBases command in the usual script.

***
_Created with the Standard Edition of HelpNDoc: [Qt Help documentation made easy](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
