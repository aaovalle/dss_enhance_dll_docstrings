# Seconds

&nbsp;

(read/write)

&nbsp;

This property sets/gets the simulation seconds as an integer. Does not include decimal part.

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

% set simulation hour 1

DSSSolution.Hour = 1;&nbsp;

% set simulation secs = 60 (1 min)

DSSSolution.Seconds = 60;&nbsp;

% Solve the model

DSSSolution.Solve();&nbsp;

&nbsp;

% gets the new hour we are located

myHour = DSSSolution.Hour;
***
_Created with the Standard Edition of HelpNDoc: [Make your documentation accessible on any device with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
