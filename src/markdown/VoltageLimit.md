# VoltageLimit

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Voltage Limit for bus to which the regulated winding is connected (e.g. first customer). Default is 0.0. Set to a value greater then zero to activate this function.

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

DSSRegCtrls = DSSCircuit.RegControls;

% Activates the first RegControl of the list

i = DSSRegCtrls.First;

% verifies if the voltage limit functionality is ON for the active RegControl

myXfmr = DSSRegCtrls.VoltageLimit;

if DSSRegCtrls.VoltageLimit \> 0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Voltage limit functionality ON');

end;

***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Ease of Use of a Help Authoring Tool](<https://www.helpndoc.com>)_
