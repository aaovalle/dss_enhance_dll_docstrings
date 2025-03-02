# UEregs

&nbsp;

(read/write)

&nbsp;

This property sets/gets an array of Integers defining energy meter registers to use for computing UE in AutoAdd Mode. May be one or more registers.&nbsp; if more than one, register values are summed together. Array of integer values \> 0.&nbsp; Defaults to 11 (for Load EEN).

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

DSSSettings = DSSCircuit.Settings;

% gets the energy meter registers to use for UE

myUERegs = DSSSettings.UEregs;

***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Ease of Use of a Help Authoring Tool](<https://www.helpndoc.com>)_
