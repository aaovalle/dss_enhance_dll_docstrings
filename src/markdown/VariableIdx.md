# VariableIdx

&nbsp;

(read/write)

&nbsp;

For PCElements only, gets/sets the index of a state variable turning it into the active state variable for the active circuit element. If the index exceeds the number of state variables or the active circuit element is not a PCelement this will trigger an error message.&nbsp;

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

DSSLines = DSSCircuit.Lines;

% Compile a model &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSActiveElement = DSSCircuit.ActiveCktElement;

% Activates the generator located in this model

DSSCircuit.SetActiveElement('Generator.G1');

% gets the names of all the state variables of the active element

mySVNames = DSSActiveElement.AllVariableNames;

% requests for state variable Pshaft

Value = 1.23;

&nbsp;

%Activates variable PShaft(4) by index

DSSActiveElement.VariableIdx = 4;

DSSActiveElement.VariableValue = Value;

mynewVal = DSSActiveElement.VariableValue;

myVarName = DSSActiveElement.VariableName;


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Capabilities with HelpNDoc's User-Friendly UI](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
