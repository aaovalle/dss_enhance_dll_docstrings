# BusNames

&nbsp;

(read/write)

&nbsp;

This property set/get a variant array of strings. Get&nbsp; Bus definitions to which each terminal is connected. 0-based array.

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

DSSLoads = DSSCircuit.Loads;

% Compile a model &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSActiveElement = DSSCircuit.ActiveCktElement;

% Sets the first load of the list as the active element

if DSSLoads.First \> 0,

myBuses = DSSActiveElement.BusNames;

else&nbsp;

disp('It seems that you have no loads\!');

end;


***
_Created with the Standard Edition of HelpNDoc: [News and information about help authoring tools and software](<https://www.helpauthoringsoftware.com>)_
