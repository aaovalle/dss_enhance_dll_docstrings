# Solution

&nbsp;

(read only)

&nbsp;

This property returns a handler for the Solution interface.

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

% Returns the handler to the Solution interface

DSSSolution = DSSCircuit.Solution;

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your PDF Protection with These Simple Steps](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
