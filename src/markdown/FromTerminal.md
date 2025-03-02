# FromTerminal

&nbsp;

(read only)

&nbsp;

This property returns the number of the terminal of the active PD element that is on the "from" side. This is set after the meter zone is determined (requires to have at least one energy meter in the model).

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

% Handler for PDelements interface

DSSPDE = DSSObject.PDElements;

% Activates the first PDE on the list

i = DSSPDE.First;

% Checks what terminal is in the "from" side (upstream)

myTerm = DSSPDE.FromTerminal;

***
_Created with the Standard Edition of HelpNDoc: [Add an Extra Layer of Security to Your PDFs with Encryption](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
