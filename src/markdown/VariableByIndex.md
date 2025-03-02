# VariableByIndex

&nbsp;

(method - read/write)

&nbsp;

For PCElements only, gets/sets the value of a state variable by index. If Code \> 0 Then no variable by this name or the active circuit element is not a PCelement.&nbsp;

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

myVd = DSSActiveElement.VariableByIndex(myStVIdx, myCode);

if myCode == 0

&nbsp; &nbsp; disp(\[mySVNames{myStVIdx},' value: ', num2str(myVd)\]);

else

&nbsp; &nbsp; disp('The variable does not exist');

end;

&nbsp;

For writing operations, this method cannot be implemented using the basic late binding interpretation provided by some non-Windows native applications. Programs such MATLAB tend to have issues with it. If you are using MATLAB we recommend to use VariableName and VariableValue properties instead. The following example in VBA shows the method usage for writing operations:

&nbsp;

Public Sub TestVariables()

&nbsp;

Dim V As Variant, V2 As Variant

Dim N As Long

&nbsp;

Dim Code As Long, AValue As Double, i As Long

&nbsp;

DSSText.Command = "select generator.windgen1"

&nbsp;

V = DSSCktElement.AllVariableNames  ' returns a variant array of strings

V2 = DSSCktElement.AllVariableValues

&nbsp;

Debug.Print "All Variables"

For i = LBound(V) To UBound(V)

       Debug.Print i; " - "; V(i); " = "; V2(i)

Next i

&nbsp;

AValue = DSSCktElement.VariableByIndex(2, Code)  'Returns a single variable at Index 3

Debug.Print "Avalue="; AValue; " number of Variables="; UBound(V) + 1

&nbsp;

DSSCktElement.VariableByName("Slip", Code) = 0.01  ' Sets the Variable Torque to 100

AValue = DSSCktElement.VariableByName("Slip", Code)

Debug.Print "Slip="; AValue; " Code="; Code

&nbsp;

DSSCktElement.VariableByIndex(4, Code) = 120#   ' sets the 4th variable to 100

AValue = DSSCktElement.VariableByIndex(4, Code)

Debug.Print "4th var="; AValue; " Code="; Code

&nbsp;

End Sub

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Efficiency with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
