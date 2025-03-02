# RegisterValues

&nbsp;

(read only)

&nbsp;

This property returns a variant Array of PVSYSTEM energy meter register values.

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

% Handler for PVSystems interface

DSSPVSystems = DSSObject.PVSystems;

% Sets the first PV in the list active

i = DSSPVSystems.First;

% My EM register values

myRVals = DSSPVSystems.RegisterValues;

***
_Created with the Standard Edition of HelpNDoc: [From Word to ePub or Kindle eBook: A Comprehensive Guide](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
