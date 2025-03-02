# Enhanced Syntax

\
The 'File=...' capability for text files has been enhanced to allow you to extract a column of data from a multi-column CSV file (like you might get from an Excel spreadsheet or the OpenDSS Export command). The complete syntax is:

&nbsp;

...mult=\[File=myMultiColumnFile.CSV, Column=n, Header=Yes/No\]

&nbsp;

Enter n for the column number you want. The default is always set to 1 for each array.

&nbsp;

Specifying Header=Yes causes the first record in the CSV file to be skipped. This allows for a single line of non-numeric data in the first line, as is common in OpenDSS Export files. Default is “Header=No”.

&nbsp;

*Example*

&nbsp;

New Loadshape.Ramp2 npts=4000 sInterval=1

\~ mult= (file=MultiChannelTest.csv, column=3, header=yes)

***
_Created with the Standard Edition of HelpNDoc: [Make Help Documentation a Breeze with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
