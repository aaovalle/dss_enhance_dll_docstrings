# Iterations

&nbsp;

(read only)

&nbsp;

This property returns the number of iterations taken for last solution. (Same as TotalIterations).

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

% Initialize snap solution

DSSSolution.InitSnap();&nbsp;

% solves the circuit without control actions

DSSSolution.SolveNoControl();&nbsp;

% Do control actions

DSSSolution.DoControlActions();

&nbsp;

% get the number of iterations required for the latest solution

myNumIter = DSSSolution.Iterations;
***
_Created with the Standard Edition of HelpNDoc: [Keep Your Sensitive PDFs Safe with These Easy Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
