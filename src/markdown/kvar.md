# kvar

&nbsp;

(read/write)

&nbsp;

This property sets/gets the kvar output rating for the active generator. Updates power factor based on present kW value.

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

DSSGen = DSSCircuit.Generators;

% Selects the first Generator from the list

DSSGen.First;

% gets the kvar output for the active Generator

mykvar = DSSGen.kvar;

***
_Created with the Standard Edition of HelpNDoc: [Easily Add Encryption and Password Protection to Your PDFs](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
