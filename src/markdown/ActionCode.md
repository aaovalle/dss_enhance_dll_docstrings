# ActionCode

&nbsp;

(read only)

&nbsp;

This property returns the code for the active action. Long integer code to tell the control device what to do. Use this to determine what the user-defined controls are supposed to do. Can be any long (32-bit) integer of the programmer’s choosing and is the same value that the control pushed onto the control queue earlier.

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

DSSCtrlQueue = DSSCircuit.CtrlQueue;

% Gets the code for the active action

myAction = DSSCtrlQueue.ActionCode;

***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Ease of Use of a Help Authoring Tool](<https://www.helpndoc.com>)_
