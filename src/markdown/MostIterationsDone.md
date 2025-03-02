# MostIterationsDone

&nbsp;

(read only)

&nbsp;

This property returns the Max number of iterations required to converge at any control iteration of the most recent solution.

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

% Set min solution iterations to 1

DSSSolution.MinIterations = 1;&nbsp;

&nbsp;

% Solve the model

DSSSolution.Solve();&nbsp;

% gets the name of the solution mode used

disp(\['Solution mode used: ', DSSSolution.ModeID\])

% gets the max number of iterations done

disp(\['Max iterations performed: ', num2str(DSSSolution.MostIterationsDone)\])

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create Encrypted, Password-Protected PDFs](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
