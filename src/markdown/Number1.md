# Number

&nbsp;

(read only)

&nbsp;

This property returns the Number of solutions to perform for Monte Carlo and time series simulations.

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

% gets the max number of iterations done

disp(\['Max iterations performed: ', num2str(DSSSolution.MostIterationsDone)\])

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create High-Quality Help Documentation with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
