# Z

(read/write)

&nbsp;

This property gets/sets the R and X properties for the active reactor in the active circuit by delivering/inserting both values simultaneously.

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

% gets the Z of the active reactor

myZ = DSSRc.Z;

&nbsp;

% Sets the Z of the active reactor with junk values

feature('COM\_SafeArraySingleDim',1);

a = \[1 2\];

b = a';

DSSReactor.Z = b;

feature('COM\_SafeArraySingleDim',0);

&nbsp;

% Z is set, read again

myZ2 = DSSRc.Z;

***
_Created with the Standard Edition of HelpNDoc: [News and information about help authoring tools and software](<https://www.helpauthoringsoftware.com>)_
