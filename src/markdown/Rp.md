# Rp

(read/write)

&nbsp;

This property gets/sets the resistance in parallel with R and X (the entire branch) for the active reactor in the active circuit.

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

% gets the Rp of the active reactor

myRp = DSSRc.Rp;

***
_Created with the Standard Edition of HelpNDoc: [Revolutionize your documentation process with HelpNDoc's online capabilities](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
