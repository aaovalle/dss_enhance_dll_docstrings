# UseActual

&nbsp;

(read/write)

&nbsp;

This property sets/gets the True/False flag to let Loads know to use the actual value in the curve rather than use the value as a multiplier.

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

DSSLoadShapes = DSSCircuit.LoadShapes;

% Activates the first LoadShape of the list

i = DSSLoadShapes.First;

% Activates the first LoadShape of the list

if DSSLoadShapes.UseActual,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Uses actual values');

else

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Uses values in pu');

end;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Full-featured Help generator](<https://www.helpndoc.com/feature-tour>)_
