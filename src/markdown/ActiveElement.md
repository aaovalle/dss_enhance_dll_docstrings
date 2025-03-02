# ActiveElement

&nbsp;

(read only)

&nbsp;

This property returns a handler to the active circuit element interface, same as ActiveCktElement.

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

% Returns the handler to the active element interface

DSSCktElement = DSSCircuit.ActiveElement;

***
_Created with the Standard Edition of HelpNDoc: [Create Professional CHM Help Files with HelpNDoc's Easy-to-Use Tool](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
