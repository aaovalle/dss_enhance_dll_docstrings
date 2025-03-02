# kVArated

&nbsp;

(read/write)

&nbsp;

This property sets/gets the rated kVA value for the active PVSystem.

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

% Gets the nominal kVA value for the active PV

mykVA = DSSPVSystems.kVArated;

***
_Created with the Standard Edition of HelpNDoc: [Free help authoring tool](<https://www.helpndoc.com/help-authoring-tool>)_
