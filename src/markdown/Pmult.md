# Pmult

&nbsp;

(read/write)

&nbsp;

This property sets/gets a variant array of Doubles for the P multiplier in the LoadShape.

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

DSSLoadShapes = DSSCircuit.LoadShapes;

% Activates the first LoadShape of the list

i = DSSLoadShapes.First;

myMult = DSSLoadShapes.Pmult;

% reduces the LoadShape to 80%

feature('COM\_SafeArraySingleDim',1);

DSSLoadShapes.Pmult = (myMult.\*0.8)';


***
_Created with the Standard Edition of HelpNDoc: [Full-featured multi-format Help generator](<https://www.helpndoc.com/help-authoring-tool>)_
