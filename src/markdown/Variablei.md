# Variablei

&nbsp;

(read/write)

&nbsp;

For PCElement, get the value of a state variable by index. If Code \> 0 Then no variable by this name or the active circuit element is not a PCelement.

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

% requests for state variable Vd (3)

myStVIdx = 3;

myCode = 0;

myVd = DSSActiveElement.Variablei(myStVIdx, myCode);

if myCode == 0

&nbsp; &nbsp; disp(\[mySVNames{myStVIdx},' value: ', num2str(myVd)\]);

else

&nbsp; &nbsp; disp('The variable does not exist');

end;


***
_Created with the Standard Edition of HelpNDoc: [Free iPhone documentation generator](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
