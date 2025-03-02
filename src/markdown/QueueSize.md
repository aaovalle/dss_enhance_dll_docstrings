# QueueSize

&nbsp;

(read only)

&nbsp;

This property returns the number of items on the OpenDSS control Queue.&nbsp;

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

% Gets the number of actions pending at the queue

myNActions = DSSCtrlQueue.QueueSize;

***
_Created with the Standard Edition of HelpNDoc: [Easily create Qt Help files](<https://www.helpndoc.com/feature-tour>)_
