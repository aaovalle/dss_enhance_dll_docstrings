# MonitoredObj

&nbsp;

(read/write)

&nbsp;

This property sets/gets the full name of the circuit element to which the fuse is connected.

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

DSSFuses = DSSCircuit.Fuses;

% gets the name of the monitored object

myOldMonObj = DSSFuses.MonitoredObj;

% Then assigns the fuse to monitor line.line1

DSSFuses.MonitoredObj = 'Line.Line1';

***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your CHM Help File Output with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
