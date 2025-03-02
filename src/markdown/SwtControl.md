# SwtControl

&nbsp;

The SwtControl was modified at the end of May 2016 to correct some deficiencies and get it to work better in QSTS calculations.

&nbsp;

The Normal property was added to define the normal state of the switch after a mode change or other reset. It defaults to the Action value defined during the initial New command if it is not specifically defined. (Some users have been defining the initial state with Action).

&nbsp;

The State property was added to get or set the present state.

&nbsp;

The Lock property was added to better control locking of the switch state. For example, you may not want the switch to change states when changing solution modes from snapshot to Daily. You have to unlock (Lock=NO) before an Action will take place.

&nbsp;

State and Reset force the switch position.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Save time and frustration with HelpNDoc's WinHelp HLP to CHM conversion feature](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
