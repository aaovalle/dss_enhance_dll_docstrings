# AllNames

&nbsp;

(read only)

&nbsp;

This property returns a variant array of strings containing names of all LoadShape objects currently defined.

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

% gets the names of all LoadShapes in the model

myLShapes = DSSLoadShapes.AllNames;

***
_Created with the Standard Edition of HelpNDoc: [Streamline your documentation process with HelpNDoc's HTML5 template](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
