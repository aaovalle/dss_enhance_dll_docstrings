# AllPropertyNames

&nbsp;

(read only)

&nbsp;

This property returns a variant array (strings) containing all property names of the active DSS object.

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

DSSElement = DSSCircuit.ActiveDSSElement;

% Sets load as the active class

DSSCircuit.SetActiveClass('Load')

myLoadProp = DSSElement.AllPropertyNames;

% Sets line as the active class

DSSCircuit.SetActiveClass('Line')

myLineProp = DSSElement.AllPropertyNames;

***
_Created with the Standard Edition of HelpNDoc: [Free help authoring tool](<https://www.helpndoc.com/help-authoring-tool>)_
