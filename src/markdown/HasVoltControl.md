# HasVoltControl

&nbsp;

(read only)

&nbsp;

This property returns true if the active element has a CapControl or RegControl attached.

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

DSSCaps = DSSCircuit.Capacitors;

% Compile a model &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSActiveElement = DSSCircuit.ActiveCktElement;

% Sets the first line of the list as the active element

if DSSCaps.First \> 0,

&nbsp; &nbsp; % Check if there is a VoltControl tied to it

&nbsp; &nbsp; if DSSActiveElement.HasVoltControl,

&nbsp; &nbsp; &nbsp; &nbsp; disp('It has VoltControl\!');

&nbsp; &nbsp; else

&nbsp; &nbsp; &nbsp; &nbsp; disp('No VoltControl linked to this element');

&nbsp; &nbsp; end;

else&nbsp;

&nbsp; &nbsp; disp('It seems that you have no capacitors\!');

end;

***
_Created with the Standard Edition of HelpNDoc: [Easy Qt Help documentation editor](<https://www.helpndoc.com>)_
