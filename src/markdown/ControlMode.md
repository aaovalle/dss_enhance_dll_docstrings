# ControlMode

&nbsp;

(read/write)

&nbsp;

This property sets/gets an integer representing the value of the {dssStatic\* (0)\| dssEvent (1) \| dssTime (2)}&nbsp; Modes for control devices. Default is "STATIC".&nbsp; Control mode for the solution. Set to OFF to prevent controls from changing.

STATIC = Time does not advance.&nbsp; Control actions are executed in order of shortest time to act until all actions are cleared from the control queue.&nbsp; Use this mode for power flow solutions which may require several regulator tap changes per solution.

&nbsp;

EVENT = solution is event driven.&nbsp; Only the control actions nearest in time are executed and the time is advanced automatically to the time of the event.&nbsp;

&nbsp;

TIME = solution is time driven.&nbsp; Control actions are executed when the time for the pending action is reached or surpassed.

&nbsp;

Controls may reset and may choose not to act when it comes their time.&nbsp;

Use TIME mode when modeling a control externally to the DSS and a solution mode such as DAILY or DUTYCYCLE that advances time, or set the time (hour and sec) explicitly from the external program.&nbsp;

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

DSSSolution = DSSCircuit.Solution;

&nbsp;

% set the control iterations to 1000

DSSSolution.ControlIterations = 1000;&nbsp;

&nbsp;

% shows the name of the active control mode

switch DSSSolution.ControlMode\
&nbsp; &nbsp; &nbsp; &nbsp; case 0\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Static')\
&nbsp; &nbsp; &nbsp; &nbsp; case 1\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Event')\
&nbsp; &nbsp; &nbsp; &nbsp; case 2\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Time')\
&nbsp; &nbsp; &nbsp; &nbsp; otherwise\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Control mode not identified')\
&nbsp; &nbsp; end

***
_Created with the Standard Edition of HelpNDoc: [Streamline your documentation process with HelpNDoc's HTML5 template](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
