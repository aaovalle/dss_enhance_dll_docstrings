# NumLoops

&nbsp;

(read only)

&nbsp;

This property returns the number of loops in the active circuit.

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

DSSTopology = DSSCircuit.Topology;

% Activate first branch on the list (closer to the substation)

i = DSSTopology.Fist;

% gets the index of the first load in the active branch&nbsp;

j = DSSTopology.FirstLoad;

% gets the number of loops in the circuit

myNumLoops = DSSTopology.NumLoops;

***
_Created with the Standard Edition of HelpNDoc: [How to Protect Your PDFs with Encryption and Passwords](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
