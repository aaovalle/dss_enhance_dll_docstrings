# Rmatrix

(read/write)

&nbsp;

This property gets/sets resistance matrix, lower triangle, ohms at base frequency for the active reactor in the active circuit.

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

% gets the Rmatrix of the active reactor

myRmat = DSSRc.Rmatrix;

&nbsp;

% Sets the Rmatrix of the active reactor with junk values

feature('COM\_SafeArraySingleDim',1);

a = \[1 2 3 4 5 6\];

b = a';

DSSReactor.Rmatrix = b;

feature('COM\_SafeArraySingleDim',0);

&nbsp;

% The Rmatrix is set, read again

myRmat2 = DSSRc.Rmatrix;

***
_Created with the Standard Edition of HelpNDoc: [Free iPhone documentation generator](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
