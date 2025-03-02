# NormalState

&nbsp;

(read/write)

&nbsp;

This property sets/gets the normal state of the active fuse (the state forced for the element at the beginning of the simulation).

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

% gets the normal state of the fuse

myNState = DSSFuses.NormalState

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Capabilities with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
