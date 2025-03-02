# Count

(read only)

&nbsp;

This property returns the number of reactor elements available in the active circuit.

&nbsp;

Example

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

disp('Unable to start openDSS');

&nbsp; &nbsp; &nbsp; return

end;

DSSText = DSSObject.Text;

DSSCircuit = DSSObject.ActiveCircuit;

DSSSolution = DSSCircuit.Solution;

DSSRc = DSSCircuit.Reactors;

% Compile a model &nbsp; &nbsp; &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSSolution.Solve;

&nbsp;

% gets the number of reactors within the active circuit

NumRX = DSSRc.Count;

&nbsp;

% gets the name of the first reactor in the model (if any)

Idx = DSSRc.First;

myName = DSSRc.Name

&nbsp;

% gets the name of the next reactor in the model (if any)

Idx = DSSRc.Next;

myName2 = DSSRc.Name

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Capabilities with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
