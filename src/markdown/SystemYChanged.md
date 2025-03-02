# SystemYChanged

&nbsp;

(read only)

&nbsp;

This property returns Flag that indicates if elements of the System Y have been changed by recent activity.

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

% Set load multiplier 1.1

DSSSolution.LoadMult = 1.1;&nbsp;

% Set max control iterations to 100

DSSSolution.LoadMult = 100;&nbsp;

% Set max solution iterations to 20

DSSSolution.MaxIterations = 20;&nbsp;

% Set simulation step size (sec)

DSSSolution.StepSize = 1;

&nbsp;

% solves the circuit including

DSSSolution.SolveSnap();

&nbsp;

% check if the SystemY has changed

if DSSSolution.SystemYChanged,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('The Y bus matrix has changed');

end;

***
_Created with the Standard Edition of HelpNDoc: [Free help authoring environment](<https://www.helpndoc.com/help-authoring-tool>)_
