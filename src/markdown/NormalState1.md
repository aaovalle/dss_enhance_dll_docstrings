# NormalState

&nbsp;

(read/write)

&nbsp;

This property sets/gets the normal state (the state for which the active recloser will be forced into at the beginning of the simulation) for the active recloser.

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

% gets the normal state of the recloser

myNState = DSSReclosers.NormalState;


***
_Created with the Standard Edition of HelpNDoc: [Streamline Your CHM Help File Creation with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
