# ForcedON

&nbsp;

(read/write)

&nbsp;

This property sets/gets whether the generator is forced ON regardless of other dispatch criteria.

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

DSSGen = DSSCircuit.Generators;

% Selects the first Generator from the list

DSSGen.First;

% gets the current state for the active generator,

% if not active, forces it to start generating

if DSSGen.ForcedON == 0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; DSSGen.ForcedON = true;

end;

***
_Created with the Standard Edition of HelpNDoc: [Full-featured Help generator](<https://www.helpndoc.com/feature-tour>)_
