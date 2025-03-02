# LDCurve

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Load-Duration (LD) Curve name for LD modes. Global load multiplier is defined by this curve for LD1 and LD2 solution modes. Default is Nil.

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

% Solve the model

DSSSolution.Solve();&nbsp;

% gets the LD curve name

myLDCurve = DSSSolution.LDCurve;
***
_Created with the Standard Edition of HelpNDoc: [Transform your help documentation into a stunning website](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
