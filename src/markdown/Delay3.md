# Delay

&nbsp;

(read/write)

&nbsp;

This property sets/gets the time delay \[s\] between arming and opening or closing the switch.&nbsp; Control may reset before actually operating the switch.

&nbsp;

*Example*

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Unable to start openDSS');

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

DSSText = DSSObject.Text;

DSSCircuit = DSSObject.ActiveCircuit;

% Compile a model &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSSwtCtrl = DSSCircuit.SwtControls;

% activates the first SW of the list

DSSSwtCtrl.First;

% gets the delay of the active SW

myDelay = DSSSwtCtrl.Delay;

***
_Created with the Standard Edition of HelpNDoc: [Write EPub books for the iPad](<https://www.helpndoc.com/create-epub-ebooks>)_
