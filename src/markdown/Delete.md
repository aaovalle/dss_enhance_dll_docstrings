# Delete

&nbsp;

(method)

&nbsp;

This method deletes an Action from the DSS Control Queue by the handle that is returned when the action is added. (The Push function returns the handle.)&nbsp; The return value is always zero.

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

% Deletes the added action (for the example)

DSSSolution.Delete(myHandle);

% Apply control action

DSSSolution.DoControlActions();


***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Documentation with HelpNDoc's Project Analyzer Features](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
