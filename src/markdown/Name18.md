# Name

&nbsp;

(read/write)

&nbsp;

This property sets/gets the name of active Recloser by name.

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

% gets the monitored terminal, if 2 force it to 1

if DSSReclosers.MonitoredTerm == 2,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; DSSReclosers.MonitoredTerm = 1;

end;

% gets the name of the active recloser

myName = DSSReclosers.Name;

&nbsp;&nbsp; &nbsp; &nbsp; 
***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Productivity with HelpNDoc's Efficient User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
