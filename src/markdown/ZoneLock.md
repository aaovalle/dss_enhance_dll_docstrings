# ZoneLock

&nbsp;

(read/write)

&nbsp;

This property sets/gets {True \| False\*} for Locking Zones on energy meters to prevent rebuilding if a circuit change occurs.

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

DSSSettings = DSSCircuit.Settings;

% Check if zone lock is active

if DSSSettings.ZoneLock,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('ZoneLock is active');

end;

***
_Created with the Standard Edition of HelpNDoc: [Write eBooks for the Kindle](<https://www.helpndoc.com/feature-tour/create-ebooks-for-amazon-kindle>)_
