# Converged

&nbsp;

(read/write)

&nbsp;

This property sets/gets a Flag to indicate whether the circuit solution converged.

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

&nbsp;

% Solve the model

DSSSolution.Solve();&nbsp;

&nbsp;

% Check if the latest solution converged

if DSSSolution.Converged,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Solution converged');

else

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Solution did not converge');

end;
***
_Created with the Standard Edition of HelpNDoc: [Transform Your Documentation Process with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
