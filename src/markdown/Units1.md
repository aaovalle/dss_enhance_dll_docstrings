# Units

&nbsp;

(read/write)

&nbsp;

This property sets/gets the units of the active Line code, it can be one of (ohms per ...) {none\|mi\|km\|kft\|m\|me\|ft\|in\|cm}.&nbsp; Default is none; assumes units agree with length units given in Line object.

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

DSSLineCodes = DSSCircuit.LinesCodes;

% activates the first line code on the list

DSSLineCodes.First;

% Gets the units for the active line code

myUnits = DSSLineCodes.Units;

***
_Created with the Standard Edition of HelpNDoc: [Easily create CHM Help documents](<https://www.helpndoc.com/feature-tour>)_
