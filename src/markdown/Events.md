# Events

&nbsp;

(read only)

&nbsp;

This property returns an interface to the DSS events interface.

&nbsp;

*Example*

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Unable to start openDSS');

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

% Returns the handler to the Events interface

DSSEvents = DSSObject.Events;

***
_Created with the Standard Edition of HelpNDoc: [Make Your PDFs More Secure with Encryption and Password Protection](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
