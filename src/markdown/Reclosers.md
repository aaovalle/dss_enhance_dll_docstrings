# Reclosers

&nbsp;

(read only)

&nbsp;

This property returns a handler for the Reclosers interface.

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

% Returns the handler to the Reclosers interface

DSSReclosers = DSSCircuit.Reclosers;

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly bring your documentation online with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
