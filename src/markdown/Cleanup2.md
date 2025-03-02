# Cleanup

&nbsp;

(method)

&nbsp;

This method Update storage, invcontrol, etc at the end of time step.

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

% solves the circuit without control actions

DSSSolution.SolveNoControl();&nbsp;

% samples and executes control actions

DSSSolution.CheckControls();

% Executes status check in all fault objects

DSSSolution.CheckFaultStatus();

% Executes status check in all fault objects

DSSSolution.Cleanup();

***
_Created with the Standard Edition of HelpNDoc: [Keep Your PDFs Safe from Unauthorized Access with These Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
