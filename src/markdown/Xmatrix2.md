# Xmatrix

(read/write)

&nbsp;

This property gets/sets reactance matrix, lower triangle, ohms at base frequency for the active reactor in the active circuit.

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

% gets the Xmatrix of the active reactor

myXmat = DSSRc.Xmatrix;

&nbsp;

% Sets the Xmatrix of the active reactor with junk values

feature('COM\_SafeArraySingleDim',1);

a = \[1 2 3 4 5 6\];

b = a';

DSSReactor.Xmatrix = b;

feature('COM\_SafeArraySingleDim',0);

&nbsp;

% The Xmatrix is set, read again

myXmat2 = DSSRc.Xmatrix;

***
_Created with the Standard Edition of HelpNDoc: [Simplify Your Help Documentation Process with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
