# SwitchedObj

&nbsp;

(read/write)

&nbsp;

This property sets/gets the full name of object that will be switched when the active relay trips. (class.name -\> e.g. Load.myloadName).

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

% gets the name of the object to be switched by the active relay

mySwObj = DSSRelays.SwitchedObj;

***
_Created with the Standard Edition of HelpNDoc: [Easily create Help documents](<https://www.helpndoc.com/feature-tour>)_
