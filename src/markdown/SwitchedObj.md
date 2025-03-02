# SwitchedObj

&nbsp;

(read/write)

&nbsp;

This property sets/gets the full name of the circuit element switch that the fuse controls. Defaults to the MonitoredObj.

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

% Activates the first fuse on the list

myIdx = DSSFuses.First;

% gets the name of the switching object

myOldSWObj = DSSFuses.SwitchedObj;

% Then assigns the fuse to switch line.line1

DSSFuses.SwitchedObj = 'Line.Line1';

***
_Created with the Standard Edition of HelpNDoc: [Easily create iPhone documentation](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
