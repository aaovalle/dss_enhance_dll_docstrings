# FirstPDElement

&nbsp;

(read only)

&nbsp;

This property sets the first Power Delivery (PD) element to be the active element.

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

DSSElement = DSSCircuit.ActiveCktElement;

% Sets the first PCE on the list as the active element

i = DSSCircuit.FirstPDElement;

% Gets the name of the active PDElement

myElement = DSSElement.Name;

***
_Created with the Standard Edition of HelpNDoc: [Free Web Help generator](<https://www.helpndoc.com>)_
