# Sensor

&nbsp;

(read only)

&nbsp;

This property returns the name of the sensor monitoring the active PV System.

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

% My sensor name

mySensor = DSSPVSystems.Sensor;

if mySensor == '',

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('There is no sensor connected to this PV');

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;
***
_Created with the Standard Edition of HelpNDoc: [Produce online help for Qt applications](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
