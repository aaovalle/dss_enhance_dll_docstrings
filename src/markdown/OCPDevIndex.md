# OCPDevIndex

&nbsp;

(read only)

&nbsp;

This property returns the Index into Controller list of OCP Device controlling the active circuit element.

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

&nbsp; &nbsp; &nbsp; &nbsp; % Gets the OCP device index tied to the active element

&nbsp; &nbsp; &nbsp; &nbsp; myOCPIdx = DSSActiveElement.OCPDevIndex;

&nbsp; &nbsp; end;

else&nbsp;

&nbsp; &nbsp; disp('It seems that you have no lines\!');

end;


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly optimize your documentation website for search engines](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
