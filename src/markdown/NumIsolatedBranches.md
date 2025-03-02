# NumIsolatedBranches

&nbsp;

(read only)

&nbsp;

This property returns the number of isolated branches (PD elements and capacitors).

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

DSSTopology = DSSCircuit.Topology;

% Activate first branch on the list (closer to the substation)

i = DSSTopology.Fist;

% gets the index of the first load in the active branch&nbsp;

j = DSSTopology.FirstLoad;

% gets the number of isolated branches

myNumIsolatedBr = DSSTopology.NumIsolatedBranches;

***
_Created with the Standard Edition of HelpNDoc: [Write EPub books for the iPad](<https://www.helpndoc.com/create-epub-ebooks>)_
