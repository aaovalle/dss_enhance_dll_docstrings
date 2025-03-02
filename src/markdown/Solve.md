# Solve

&nbsp;

(method)

&nbsp;

This method executes solution for present solution mode.

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

% set simulation mode daily

DSSSolution.Mode = 1;

% set simulation step size 1 h

DSSSolution.StepSize = 1;

&nbsp;

% Solve the model

DSSSolution.Solve();&nbsp;

&nbsp;

% gets the new hour we are located

myHour = DSSSolution.Hour;
***
_Created with the Standard Edition of HelpNDoc: [Full-featured Kindle eBooks generator](<https://www.helpndoc.com/feature-tour/create-ebooks-for-amazon-kindle>)_
