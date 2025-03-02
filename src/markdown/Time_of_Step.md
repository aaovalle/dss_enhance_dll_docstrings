# Time_of_Step

&nbsp;

(read only)

&nbsp;

This property returns the solution process time + sample time for time step (in microseconds).

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

% gets the percent default of load growth

disp(\['Total time required for performing the last step (us): ', num2str(DSSSolution.Time\_of\_Step)\])

***
_Created with the Standard Edition of HelpNDoc: [Eliminate the Struggles of Documentation with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
