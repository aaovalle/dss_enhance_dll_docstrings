# NextLoad

&nbsp;

(read only)

&nbsp;

This property activates the next load at the active branch, return index or 0 if none (no load at the active branch).

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

if DSSTopology.NextLoad == 0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp(\['no more loads at branch ',DSSTopology.BranchName\]);

end;

***
_Created with the Standard Edition of HelpNDoc: [What is a Help Authoring tool?](<https://www.helpauthoringsoftware.com>)_
