# PhaseInst

&nbsp;

(read/write)

&nbsp;

This property sets/gets the phase instantaneous curve multipler or actual amps.

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

% gets the phase instantaneous curve multiplier for the active recloser

myPhaseInst = DSSReclosers.PhaseInst;

***
_Created with the Standard Edition of HelpNDoc: [Easy EPub and documentation editor](<https://www.helpndoc.com>)_
