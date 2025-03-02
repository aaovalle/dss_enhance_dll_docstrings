# Name

&nbsp;

(read/write)

&nbsp;

This property sets/gets the active Relay by name.

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

DSSRelays = DSSCircuit.Relays;

% Activates the first relays on the list

i = DSSRelays.First;

% gets the name of the object monitored by the active relay

myMonObj = DSSRelays.MonitoredObj;

% gets the terminal monitored by the active relay

myMonTrm = DSSRelays.MonitoredTerm;

% gets the name of the active relay

myRelay = DSSRelays.Name;

***
_Created with the Standard Edition of HelpNDoc: [Full-featured EBook editor](<https://www.helpndoc.com/create-epub-ebooks>)_
