# TechNote Export and Plot Updates

&nbsp;

This Tech Note describes recent updates to the Export, Show and Plot commands. Due to the complexity of the some of these commands, the EXE version now has additional aids and prompts in the menus (You actually get some bus names to choose from, etc.).

&nbsp;

***EXPORT Updates***

There is now an Export menu in the DSS EXE user interface to help you remember the commands The voltage and current exports were updated to be more consistent and useful when you load them into Excel or whatever.

&nbsp;

• The output tables now stretch out horizontally instead of vertically. This is also done to fit in better with modifications to the Plot command

• Note: Current exports are keyed on device name

• Note: Voltage exports are keyed on bus name

• Residual values were added (sum of all conductors or nodes at a branch or bus). (This is also true for the seq currents and seq voltage exports because the residuals can be different than the zero-sequence values.)

&nbsp;

Here are the export options:

&nbsp;

Export Voltages \[Filename\] (EXP\_VOLTAGES.CSV)

Export SeqVoltages \[Filename\] (EXP\_SEQVOLTAGES.CSV)

Export Currents \[Filename\] (EXP\_CURRENTS.CSV)

Export Overloads \[Filename\] EXP\_OVERLOADS.CSV)

Export Unserved \[UEonly\] \[Filename\] EXP\_UNSERVED.CSV)

Export SeqCurrents \[Filename\] (EXP\_SEQCURRENTS.CSV)

Export Powers \[MVA\] \[Filename\](EXP\_POWERS.CSV)

Export SeqPowers \[MVA\] \[Filename\](EXP\_SEQPOWERS.CSV)

Export Faultstudy \[Filename\] (EXP\_FAULTS.CSV)

Export Generators \[Filename \| /m \] (EXP\_GENMETERS.CSV)

Export Loads \[Filename\] (EXP\_LOADS.CSV)

Export Meters \[Filename \| /m \] (EXP\_METERS.CSV)

Export Monitors monitorname (file name is assigned)

Export Yprims \[Filename\] (EXP\_Yprims.CSV) (all YPrim matrices)

Export Y \[Filename\] (EXP\_Y.CSV) (system Y matrix)

&nbsp;

The circuit name is prepended onto the file names above.

&nbsp;

***Edit Result File***

At the conclusion of an Export operation (as well as any other DSS operation that writes a file) the name of the output file appears in the Result window. You can quickly display/edit the file by:

&nbsp;

&#49;. Edit \| Result File menu item

&#50;. ctrl-R

&#51;. There is a new button on the tool bar for this purpose

&nbsp;

You can also set the option ShowExport to YES/TRUE and the export result file will automatically appear. For Example:

&nbsp;

Set ShowExport=Yes

Export Yprims

&nbsp;

***SHOW Command Updates***

From the EXE version, you now get some more options on the Show menu. In particular, on the Show BusFlow and Show LineConstants, you get additional prompts to help you with the options. PLOT Command Updates For several years there has been the capability to display various things on circuit plots: The existing “circuit plot” creates displays on which the thicknesses of LINE elements are varied according to :

• Power

• Current

• Voltage

• Losses

• Capacity (remaining)

This plot is a unicolor plot (specified by color C1). The following example will display the circuit with the line thickness propotional to POWER relative to a max scale of 2000 kW:

&nbsp;

plot circuit Power Max=2000 dots=n labels=n subs=n C1=$00FF0000

&nbsp;

The existing “general plot” creates displays on which the color of bus dots are varied according to an arbitrary quantity entered through a CSV file . The following gives a nice yellowred variation of data field 1 (the bus name is assumed to be in the first column of the csv file) with the min displayed as color C1 (yellow) and the max=0.003 being C2 (red). Values in between are various shades of orange.

&nbsp;

plot General 1 Max=.003 dots=n labels=n subs=y object=filename.csv C1=$0080FFFF C2=$000000FF

&nbsp;

Example results: This plot clearly shows the extent of harmonic resonance involving the residual current (likely, the zero sequence, too) on the circuit.

&nbsp;

For more recent information see TechNote Using the General Plot and the latest User Manual.

&nbsp;

***New General Line Data Feature in Plot Command***

There is now an option on the plot circuit command that will permit you to draw the circuit with lines proportional to some arbitrary quantity imported from a CSV file. The first column in the file should be the LINE name specified either by complete specification “line.elementname” or simply “elementname”. If the command can find a line by that name in the present circuit, it will plot it. The usual thing you would do is to export a file that is keyed on branch name, such as

&nbsp;

Export currents, or Export seqcurrents

&nbsp;

Then you would issue the plot command, for example:

&nbsp;

Plot circuit quantity=1 Max=.001 dots=n labels=n Object=feeder\_exp\_currents.CSV

&nbsp;

The DSS differentiates this from the standard circuit plot by:

&#49;. A numeric value for “quantity” (representing the field number) instead of “Power”, etc

&#50;. A non-null specification for “Object” ( the specified file must exist for the command to proceed). The **Plot \> Circuit Plots \> General Line Data** menu will guide you through the creation of this command with menus and list prompts (turn the recorder on). The first line in the CSV file is assumed to contain the field names, which is common for CSV files. For example, the same plot as above with line thicknesses instead of colored dots.

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Productivity with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
