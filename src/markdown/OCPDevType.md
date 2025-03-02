# OCPDevType

&nbsp;

(read only)

&nbsp;

This property returns an integer representing the type of OCP: 0=None; 1=Fuse; 2=Recloser; 3=Relay.

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

DSSLines = DSSCircuit.Capacitors;

% Compile a model &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSActiveElement = DSSCircuit.ActiveCktElement;

% Sets the first line of the list as the active element

if DSSLines.First \> 0,

&nbsp; &nbsp; % Check if there is an OCP tied to it

&nbsp; &nbsp; HasOCP = DSSActiveElement.HasOCPDevice;

&nbsp; &nbsp; if HasOCP,

&nbsp; &nbsp; &nbsp; &nbsp; % Gets the OCP type tied to the active element

&nbsp; &nbsp; &nbsp; &nbsp; myOCPType = DSSActiveElement.OCPDevType;

&nbsp; &nbsp; end;

else&nbsp;

&nbsp; &nbsp; disp('It seems that you have no lines\!');

end;

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Convert Your Word Doc to an eBook: A Step-by-Step Guide](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
