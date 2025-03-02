# GenMult

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Default Multiplier applied to generators (like LoadMult).

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

% set simulation mode yearly

DSSSolution.Mode = 2;

% set simulation step size 1 h

DSSSolution.StepSize = 1;

&nbsp;

% get the generator kW for AutoAdd mode

myGenkW = DSSSolution.GenkW;

% get the generator multiplier

myGenMult = DSSSolution.GenMult;

***
_Created with the Standard Edition of HelpNDoc: [Produce online help for Qt applications](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
