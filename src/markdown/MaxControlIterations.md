# MaxControlIterations

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Max control iterations per solution.&nbsp; Default is 10.

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

DSSSolution.MaxControlIterations = 1000;&nbsp;

&nbsp;

% solves the circuit without control actions

DSSSolution.SolveNoControl();&nbsp;

% samples and executes control actions

DSSSolution.CheckControls();

% Executes status check in all fault objects

DSSSolution.CheckFaultStatus();

% Executes status check in all fault objects

DSSSolution.Cleanup();

&nbsp;

% displays the number of control iterations obtained

myNumCtrlIter = DSSSolution.ControlIterations;
***
_Created with the Standard Edition of HelpNDoc: [Create iPhone web-based documentation](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
