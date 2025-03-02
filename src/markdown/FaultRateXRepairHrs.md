# FaultRateXRepairHrs

&nbsp;

(read only)

&nbsp;

This property returns the sum of Fault Rate time Repair Hrs in this section of the active meter zone.

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

% gets the sum of fault rate time repair in the active area

myRHours = DSSMeters.FaultRateXRepairHrs;

***
_Created with the Standard Edition of HelpNDoc: [Produce electronic books easily](<https://www.helpndoc.com/create-epub-ebooks>)_
