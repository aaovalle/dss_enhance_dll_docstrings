# CustInterrupts

&nbsp;

(read only)

&nbsp;

This property returns the total customer interruptions for this Meter zone based on reliability calcs.

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

% gets the total customer interruptions in the area of the active EM

myNInterrupts = DSSMeters.CustInterrupts;

***
_Created with the Standard Edition of HelpNDoc: [Easy EPub and documentation editor](<https://www.helpndoc.com>)_
