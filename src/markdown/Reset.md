# Reset

&nbsp;

(method)

&nbsp;

This method forces a Reset of this CapControl.

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

DSSCapCtrls = DSSCircuit.CapControls;

% Resets the active CapControl

DSSCapCtrls.Reset();

***
_Created with the Standard Edition of HelpNDoc: [Easy Qt Help documentation editor](<https://www.helpndoc.com>)_
