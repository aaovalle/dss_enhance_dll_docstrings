# PopAction

&nbsp;

(read only)

&nbsp;

This property sets the Active Action by popping the next action off the COM Control Proxy action list. Returns zero when there are no more actions to pop.&nbsp;

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

% Gets the number of actions pending

myIdx = DSSCtrlQueue.PopAction;

if myIdx == 0,

&nbsp; &nbsp; disp('No more actions in the queue');

end;


***
_Created with the Standard Edition of HelpNDoc: [Experience a User-Friendly Interface with HelpNDoc's Documentation Tool](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
