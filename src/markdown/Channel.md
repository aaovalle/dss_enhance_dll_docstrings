# Channel

&nbsp;

(read only)

&nbsp;

This property returns a Variant array of doubles for the specified channel (usage: MyArray = DSSMonitor.Channel(i)) A Save or SaveAll should be executed first. Done automatically by most standard solution modes.

&nbsp;

Example

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Unable to start openDSS');

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

DSSText = DSSObject.Text;

DSSCircuit = DSSObject.ActiveCircuit;

% Compile a model &nbsp; &nbsp; &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSText.Command = 'solve mode=daily';

DSSMonitors = DSSCircuit.Monitors;

% saves all monitors registers

DSSMonitors.SaveAll();

% select the first monitor on the list

DSSMonitors.First

% gets the content of channel 1

myReading = DSSMonitors.Channel(1);&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
