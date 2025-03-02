# Tolerance

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Solution convergence tolerance.

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

% Solve the model

DSSSolution.Solve();&nbsp;

% gets the name of the solution mode used

disp(\['Solution mode used: ', DSSSolution.ModeID\])

% gets the tolerance value

disp(\['Solution convergence tolerance: ', num2str(DSSSolution.Tolerance)\])

***
_Created with the Standard Edition of HelpNDoc: [Enhance Your Documentation with HelpNDoc's Advanced Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
