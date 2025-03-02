# idx

&nbsp;

(read/write)

&nbsp;

This property sets/gets active a PVSystem by index;&nbsp; 1..Count.

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

% Activates the next PV on the list

DSSPVSystems.idx = i + 1;

% Gets the name of the active PV

myPV = DSSPVSystems.Name;

***
_Created with the Standard Edition of HelpNDoc: [Free Web Help generator](<https://www.helpndoc.com>)_
