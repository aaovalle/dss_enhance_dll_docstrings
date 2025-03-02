# IntervalHrs

&nbsp;

(read/write)

&nbsp;

This property Get/Set the Solution.IntervalHrs variable used for devices that integrate.

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

DSSSolution = DSSCircuit.Solution;

&nbsp;

% Check whats the interval Hrs for devices that integrate

myIntHrs = DSSSolution.IntervalHrs;&nbsp;

&nbsp;

% Initialize snap solution

DSSSolution.InitSnap();&nbsp;

% solves the circuit without control actions

DSSSolution.SolveNoControl();&nbsp;

% Do control actions

DSSSolution.DoControlActions();
***
_Created with the Standard Edition of HelpNDoc: [What is a Help Authoring tool?](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
