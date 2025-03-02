# VariableValue

&nbsp;

(read/write)

&nbsp;

For PCElements only, gets/sets the value for the active state variable for the active circuit element. If there is no state variable active this will trigger an error message.&nbsp;

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

myStVar = 'PShaft';

Value = 1.23;

&nbsp;

DSSActiveElement.VariableName = myStVar;

DSSActiveElement.VariableValue = Value;

mynewVal = DSSActiveElement.VariableValue;

***
_Created with the Standard Edition of HelpNDoc: [Free EPub and documentation generator](<https://www.helpndoc.com>)_
