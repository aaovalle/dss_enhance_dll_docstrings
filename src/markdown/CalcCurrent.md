# CalcCurrent

&nbsp;

(read/write)

&nbsp;

This property sets/gets the magnitude of the real part of the Calculated Current (normally determined by solution) for the Meter to force some behavior on Load Allocation.

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

% gets the real part of the calculated current for the active EM

myCurrentR = DSSMeters.CalcCurrent;

***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Output with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
