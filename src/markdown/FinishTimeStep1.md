# FinishTimeStep

&nbsp;

(method)

&nbsp;

This method Call Cleanup, sample monitors, and increment time at end of time step.

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

% set the control iterations to 1000

DSSSolution.ControlIterations = 1000;&nbsp;

% set simulation mode yearly

DSSSolution.Mode = 2;

% set simulation step size 1 h

DSSSolution.StepSize = 1;

&nbsp;

% gets the name of the default load shape (yearly)

myDefLS = DSSSolution.DefaultYearly;

&nbsp;

% set simulation hour 1.5

DSSSolution.dblHour = 1.5;&nbsp;

% solves the circuit without control actions

DSSSolution.SolveNoControl();&nbsp;

% Do control actions

DSSSolution.DoControlActions(); &nbsp;

% finish time step

DSSSolution.FinishTimeStep(); &nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Elevate your documentation to new heights with HelpNDoc's built-in SEO](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
