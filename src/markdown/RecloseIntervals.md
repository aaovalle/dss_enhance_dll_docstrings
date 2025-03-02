# RecloseIntervals

&nbsp;

(read only)

&nbsp;

This property returns a variant Array of Doubles: reclose intervals, s, between shots.

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

% gets the name of the active recloser

myName = DSSReclosers.Name;

% gets the name of the element monitored by the active recloser

myMonObj = DSSReclosers.MonitoredObj;

% gets the reclosing intervals for the active recloser

myRInter = DSSReclosers.RecloseIntervals;

***
_Created with the Standard Edition of HelpNDoc: [Create iPhone web-based documentation](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
