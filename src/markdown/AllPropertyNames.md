# AllPropertyNames

&nbsp;

(read only)

&nbsp;

This property returns a variant array (strings) containing all property names of the active device.

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

DSSActiveElement = DSSCircuit.ActiveCktElement;

% Sets load 'Load1' as the active element

DSSCircuit.SetActiveElement('Load.Load1')

myLoadProp = DSSActiveElement.AllPropertyNames;

% Sets line 'Line1' as the active element

DSSCircuit.SetActiveElement('Line.Line1')

myLineProp = DSSActiveElement.AllPropertyNames;

***
_Created with the Standard Edition of HelpNDoc: [Create cross-platform Qt Help files](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
