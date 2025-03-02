# AllVariableValues

&nbsp;

(read only)

&nbsp;

This property returns a variant array of doubles. Values of state variables of active element if PC element.

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

myVarsVals = DSSActiveElement.AllVariableValues;

***
_Created with the Standard Edition of HelpNDoc: [Easy CHM and documentation editor](<https://www.helpndoc.com>)_
