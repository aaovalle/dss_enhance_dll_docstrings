# DeviceHandle

&nbsp;

(read only)

&nbsp;

This property returns a handle to the user’s control device from the Active Action. The user-written code driving the COM interface may support more than one control element as necessary to perform the simulation. This handle is an index returned to the user program that lets the program know which control is to perform the active action.

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

...

% Gets the handle code for the active device

myHandle = DSSCtrlQueue.DeviceHandle;

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Productivity with HelpNDoc's CHM Help File Creation Features](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
