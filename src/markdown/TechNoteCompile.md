# TechNote Compile

&nbsp;

The Compile and Redirect commands are similar but have key different behaviors:

&nbsp;

***Compile:*** Leaves the current directory at the directory of the last file "compiled".

***Redirect:*** Returns to the directory from which it was issued.

&nbsp;

You can redirect to a relative pathname such as

&nbsp;

Redirect Beachhaven\\master.DSS

&nbsp;

or to a full pathname such as:

&nbsp;

Redirect C:\\MyProject\\Beachhaven\\master.DSS

&nbsp;

The file Master.DSS may contain many other Redirect commands with only local file reference.

&nbsp;

When done with Master.DSS, the DSS resets the current directory to where it started.

***
_Created with the Standard Edition of HelpNDoc: [Save time and frustration with HelpNDoc's WinHelp HLP to CHM conversion feature](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
