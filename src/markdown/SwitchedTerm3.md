# SwitchedTerm

&nbsp;

(read/write)

&nbsp;

This property sets/gets the terminal number of the switched object that will be opened when the SwtControl operates.

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

i = DSSSwtCtrl.First;

% gets the SWObj operating terminal for the active SW

mySWTrm = DSSSwtCtrl.SwitchedTerm;

***
_Created with the Standard Edition of HelpNDoc: [What is a Help Authoring tool?](<https://www.helpauthoringsoftware.com>)_
