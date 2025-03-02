# BackwardBranch

&nbsp;

(read only)

&nbsp;

This property moves back toward the source, return index of new active branch, or 0 if no more.

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

% moves backwards&nbsp;

j = DSSTopology.BackwardBranch;

% gets the name of the active branch

myBranch = DSSTopology.BranchName;


***
_Created with the Standard Edition of HelpNDoc: [What is a Help Authoring tool?](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
