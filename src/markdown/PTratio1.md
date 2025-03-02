# PTratio

&nbsp;

(read/write)

&nbsp;

This property sets/gets the ratio of the PT that converts the controlled winding voltage to the regulator control voltage. Default is 60.&nbsp; If the winding is Wye, the line-to-neutral voltage is used.&nbsp; Else, the line-to-line voltage is used. SIDE EFFECT: Also sets RemotePTRatio property.

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

% Gets the PTRatio of the active RegControl

myPTRatio = DSSRegCtrls.PTratio;

***
_Created with the Standard Edition of HelpNDoc: [Full-featured multi-format Help generator](<https://www.helpndoc.com/help-authoring-tool>)_
