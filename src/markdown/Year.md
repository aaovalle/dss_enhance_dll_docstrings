# Year

&nbsp;

(read only)

&nbsp;

This property sets/gets the year for planning studies as an integer. Does not include decimal part.

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

% Set year = 2

DSSSolution.Year = 2;&nbsp;

&nbsp;

% Solve the model

DSSSolution.Solve();&nbsp;

% gets the name of the solution mode used

disp(\['Solution mode used: ', DSSSolution.ModeID\])


***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Review with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
