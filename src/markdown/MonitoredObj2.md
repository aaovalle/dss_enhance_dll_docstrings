# MonitoredObj

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Full name of the object monitored by the active recloser.

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

DSSReclosers = DSSCircuit.Reclosers;

% Activates the first recloser on the list

i = DSSReclosers.First;

% gets the name of the element monitored by the active recloser

myMonObj = DSSReclosers.MonitoredObj;

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Support Your Windows Applications with HelpNDoc's CHM Generation](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
