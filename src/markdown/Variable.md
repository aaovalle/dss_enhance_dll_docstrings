# Variable

&nbsp;

(read/write)

&nbsp;

For PCElement, get the value of a state variable by name. If Code \> 0 Then no variable by this name or the active circuit element is not a PCelement.

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

% requests for state variable Vd

myStVar = 'Vd';

myCode = 0;

myVd = DSSActiveElement.Variable(myStVar, myCode);

if myCode == 0

&nbsp; &nbsp; disp(\[myStVar,' value: ', num2str(myVd)\]);

else

&nbsp; &nbsp; disp('The variable does not exist');

end;


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Reach: Convert Your Word Document to an ePub or Kindle eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
