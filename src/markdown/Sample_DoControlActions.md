# Sample_DoControlActions

&nbsp;

(method)

&nbsp;

This method samples controls and then process the control queue for present control mode and dispatch control actions.

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

% set simulation mode daily

DSSSolution.Mode = 1;

% Set number to perform only 12 hours

DSSSolution.Number = 12;&nbsp;

&nbsp;

% solves the circuit without control actions

DSSSolution.SolveNoControl();&nbsp;

% sample, do control actions

DSSSolution.Sample\_DoControlActions();&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Creation with a Help Authoring Tool](<https://www.helpndoc.com>)_
