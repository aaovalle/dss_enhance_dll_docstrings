# HasOCPDevice

&nbsp;

(read only)

&nbsp;

This property returns true if a recloser, relay, or fuse controlling this ckt element. OCP = Over current Protection.

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

DSSLines = DSSCircuit.Lines;

% Compile a model &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSActiveElement = DSSCircuit.ActiveCktElement;

% Sets the first line of the list as the active element

if DSSLines.First \> 0,

&nbsp; &nbsp; % Check if there is an OCP tied to it

&nbsp; &nbsp; HasOCP = DSSActiveElement.HasOCPDevice;

&nbsp; &nbsp; if HasOCP,

&nbsp; &nbsp; &nbsp; &nbsp; disp('Has OCP\!');

&nbsp; &nbsp; else

&nbsp; &nbsp; &nbsp; &nbsp; disp('No OCP linked to this element');

&nbsp; &nbsp; end;

else&nbsp;

&nbsp; &nbsp; disp('It seems that you have no lines\!');

end;


***
_Created with the Standard Edition of HelpNDoc: [Easily create EPub books](<https://www.helpndoc.com/feature-tour>)_
