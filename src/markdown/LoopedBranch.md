# LoopedBranch

&nbsp;

(read only)

&nbsp;

This property activates the first looped branch, return index or 0 if none.

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

% moves to the first looped branch&nbsp;

if DSSTopology.LoopedBranch == 0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('no looped branches here');

else

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp(\['first looped branch',DSSTopology.BranchName\]);

end;


***
_Created with the Standard Edition of HelpNDoc: [News and information about help authoring tools and software](<https://www.helpauthoringsoftware.com>)_
