# SetActiveClass

&nbsp;

(write only)

&nbsp;

This method sets the Active DSS Class for use with ActiveClass interface. Same as SetActiveClass in Circuit interface.

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

% Sets class 'Load' as the active class

i = DSSObject.SetActiveClass('Load');

% verify if the class exists

if i \< 0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('The class does not exist');

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

***
_Created with the Standard Edition of HelpNDoc: [How to Protect Your PDFs with Encryption and Passwords](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
