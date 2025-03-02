# OCPDeviceType

&nbsp;

(read only)

&nbsp;

This property gets the type of OCP device. 1=Fuse; 2=Recloser; 3=Relay,located in the active meter's zone (if any).

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

DSSMeters = DSSCircuit.Meters;

% activates the first EM on the list

i = DSSMeters.First;

% gets the OCP device type within the area of the active EM

switch DSSMeters.OCPDeviceType

&nbsp; &nbsp; case 1

&nbsp; &nbsp; &nbsp; &nbsp; disp('Fuse')

&nbsp; &nbsp; case 2

&nbsp; &nbsp; &nbsp; &nbsp; disp('Recloser')

&nbsp; &nbsp; case 3

&nbsp; &nbsp; &nbsp; &nbsp; disp('Relay')

&nbsp; &nbsp; otherwise

&nbsp; &nbsp; &nbsp; &nbsp; disp('OCP not recognized')

end


***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Output with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
