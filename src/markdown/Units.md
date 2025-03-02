# Units

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Length Units = {none \| mi\|kft\|km\|m\|Ft\|in\|cm } for the active line. Default is None - assumes length units match impedance units.

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

DSSLines = DSSCircuit.Lines;

% activates the first line on the list

DSSLines.First;

% Gets length units of the active line

myUnits = DSSLines.Units;

***
_Created with the Standard Edition of HelpNDoc: [Easy EBook and documentation generator](<https://www.helpndoc.com>)_
