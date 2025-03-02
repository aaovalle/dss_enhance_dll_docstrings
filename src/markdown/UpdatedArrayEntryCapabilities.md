# Updated Array Entry Capabilities

&nbsp;

*Update: Mods to File=... Option for Array Properties*

&nbsp;

In preparation for some upcoming new capabilities and to make it easier to import general CSV files, some features have been added to the options for defining array properties with the 'file=...' syntax.

&nbsp;

***Standard Ways to Define Array Properties***

&nbsp;

Arrays can be defined by the following methods:

&nbsp;

•Entering the numeric values directly

&nbsp;

...mult=\[1, 2, 3, 4, ...\]

&nbsp;

•Entering the numbers from a single column text file:

&nbsp;

...mult=\[File=MyTextDataFile.CSV\]

&nbsp;

•Entering the data from a packed binary file of doubles:

&nbsp;

...mult=\[dblFile=MyFileOfDoubles.dbl\]

&nbsp;

•Entering the data from a packed binary file of singles:

&nbsp;

...mult=\[sngFile=MyFileOfDoubles.sng\]

&nbsp;

***Enhanced Syntax***

&nbsp;

The 'File=...' capability has been enhanced. Two options may be added if you want to extract a column of data from a multicolumn CSV file (like you might get from Excel or the OpenDSS Export command). The complete syntax is:

&nbsp;

...mult=\[File=myMultiColumnFile.CSV, Column=n, Header=Yes/No\]

&nbsp;

Enter n for the column number you want. The default is always set to 1 for each array.

&nbsp;

Specifying Header=Yes causes the first record in the CSV file to be skipped. This allows for a single line of non-numeric data in the first line, as is common in OpenDSS Export files. Default is No.

&nbsp;

***Example***

&nbsp;

New Loadshape.Ramp2 npts=4000 sInterval=1 mult=(file=MultiChannelTest.csv, column=3, header=yes)

&nbsp;

***Reserved File Name***

&nbsp;

The name %result% is now used to designate the last result file. For example, if you want to export a file (such as a monitor file) and then immediately read in column 5 to do something with, you could do it with the following syntax:

&nbsp;

...mult=\[File=%result%, Column=5, Header=Yes\]

&nbsp;

This must be executed before another command is issued that writes a result file.

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Revolutionize your documentation process with HelpNDoc's online capabilities](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
