# Push

&nbsp;

(write only)

&nbsp;

This method pushes an Action onto the DSS Control Queue. The return value is the handle to the action on the queue. Specify the time of the requested action in Hour, Seconds. Push an ActionCode that is meaningful to the user-written control object. DeviceHandle is a user-defined handle (a 32-bit Integer) to the control object that will be used to dispatch the control action to the proper control device managed by the user-written code when the Action is popped off the Control Queue. The DSS will automatically return this handle to the control proxy in the COM interface when the action is popped.&nbsp;

&nbsp;

The actual internal DSS Control Queue Push function passes one more argument not shown in this COM interface method. For internal control objects, it is the Self variable; for any control model coming through the COM interface, it is the address of the COMControlProxyObj variable. When an action destined for the user-written code is popped off the DSS Control Queue, the COMControlProxyObj.DoPendingAction function is called. This dispatches the action message to the Action List in the user-written code. Then the user-written code must decipher it.

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

% Defines some variables for the control

PTratio = 125.09; % for 26 kV system

ONsetting = 118.8;

OFFsetting = 121.2;

ActionCodeAdd = 201; % just an arbitrary action code

ActionCodeSub = 202; % just another arbitrary action code

DeviceHandle = 123; % arbitrary handle that signifies this control

Hour= 0; % the time when we want the action to take place

secDelay = 5;&nbsp; % delay

&nbsp;

DSSSolution.LoadMult = 1 \* 1.1&nbsp; %10% more each time

DSSSolution.InitSnap();

DSSSolution.SolveNoControl();

DSSSolution.SampleControlDevices(); %sample all other controls

&nbsp;

DSSCircuit.SetActiveBus('myBus'); % Where the device is connected to

V = DSSBus.VMagAngle;

% check the first phase magnitude

Vreg = V(0) / PTratio;

disp(\['Step ', num2str(i), ' Voltage=', num2str(Vreg), ' LoadMult=', num2str(DSSSolution.LoadMult)\]);&nbsp;

if Vreg \> OFFsetting, % push a message to bump down the number of steps

&nbsp; &nbsp; myHandle = DSSCtrlQueue.Push(hour, secDelay, ActionCodeSub, DeviceHandle);

end;

% Apply control action

DSSSolution.DoControlActions();


***
_Created with the Standard Edition of HelpNDoc: [Easily create Web Help sites](<https://www.helpndoc.com/feature-tour>)_
