# Putting it all Together

&nbsp;

This section s dedicated to describe the power flow solution methods implemented in OpenDSS. OpenDSS uses three solution methods for solving the power flow problem:

&nbsp;

1. [The Normal method (floating-point iterative)](<TheNormalSolutionmethod.md>)

&nbsp;

set algorithm=Normal

&nbsp;

2. [The Newton method](<TheNewtonmethod.md>)

&nbsp;

set algorithm=Newton

&nbsp;

3. [NCIM](<NCIM.md>)&nbsp;

&nbsp;

set algorithm=NCIM

&nbsp;

&nbsp;

Figure 1 depicts the general solution algorithm in which the power flow solution goes first, and then the control actions to operate over the latest solution found.

&nbsp;

![Image](<lib/NewItem 43.png>)

Figure 1

Solution algorithm in OpenDSS

***
_Created with the Standard Edition of HelpNDoc: [Upgrade your help files and your workflow with HelpNDoc's WinHelp HLP to CHM conversion](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
