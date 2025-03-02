# Counting Tap Operations using the OpenDSS

\
Given today’s interests in conservation voltage reduction (CVR) voltvar optimization (VVO), changes in control strategies will likely end up affecting the number of tap operations of regulators (and/or load tap changers), as well as switching operations of capacitor banks. Assuming that you have correctly implemented the controls in the OpenDSS with their correct delays, setpoints, bands, and so forth, the OpenDSS can provide data for determining the operation counts of those controlled devices.

&nbsp;

Typically, we would use MONITOR objects in the OpenDSS to keep track of tap positions at each solution point. Monitor objects record the final tap positions at the end of a time step. For accurate counting of the tap operations of regulators, switching operations of capacitors, or other control elements, one must delve into the event log. For those unfamiliar with the event log, it is a list of actions that are performed by the control elements (capacitor controls, regulator controls, storage element controls, etc) based on circuit conditions and (possibly) time step in the simulation. Although it is beyond the scope of this article to go into the control queue and its interaction with the various solution modes, one can read up on the different solution modes using the help file, user manual, and examples that ship with the OpenDSS.

&nbsp;

A parameter in the regulator control that is available to the user is called ‘maxtapchange’ (it defaults to a value of 16). This value indicates the maximum number of tap movements that can be made for each control iteration. When it is desired to count the number of tap operations directly, we need to set the value of this parameter to 1. This tells the regulator control (regcontrol) to only move the tap position by one tap per control iteration (when conditions arise in the circuit that tell the regcontrol to perform an action). Then the other controls that are part of the circuit under study have the opportunity to change their state, if needed, in the next control iteration in response to this single tap position movement.

&nbsp;

You can set the maxtapchange property when you define the regcontrol, or you can use a statement similar to the following, after the regcontrol has been defined:

&nbsp;

MyRegulatorControl.maxtapchange=1

&nbsp;

Once the OpenDSS has completed the solution(s) that it has been instructed to do via the script commands, the user can review the event log to see the actual number of tap operations, based on the settings of all of the control elements in the circuit. There are two ways to get the event log contents out of the OpenDSS and into a text editor or spreadsheet/file:

&nbsp;

&#49;. From the OpenDSS main menu, click on Show, and then click on Event Log. This will bring up a dialog box that contains the contents of the event log up to and including the last solution performed. You can then copy/paste out of this dialog box. Please note that depending on the number of entries in the event log, this dialog box may take a couple of seconds to appear.

&nbsp;

&#50;. Using the script command “export EventLog”. This will save the event log contents into a CSV file whose default name is: EXP\_EVTLOG.CSV

&nbsp;

The event log will contain a record of all control action events, by default, and so may include regcontrol tap movements, capacitor status changes (switching), energy storage element actions, and so forth. With recent builds of the OpenDSS, the ability to selectively turn off the logging of events from the various control elements in your circuit has been added. If you don’t want to collect the event log entries associated with a given control element’s action(s), just use the EventLog property of that control element, and set it to ‘No’ or “False”, as follows:

&nbsp;

MyEnergyStorageControl.EventLog=no

&nbsp;

The event log will be reset when the solution mode is changed or you can force it to reset using the ‘reset’ command.


***
_Created with the Standard Edition of HelpNDoc: [Easily share your documentation with the world through a beautiful website](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
