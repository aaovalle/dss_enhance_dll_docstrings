# SwtControls

&nbsp;

This interface can be used to gain access to the features of the switch controls (SwtControls) installed across the model. This interface is embedded within the ActiveCircuit interface, requiring the definition of this interface before getting access the to SwtControls interface.

&nbsp;

*Example*

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp("Unable to start openDSS");

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

DSSCircuit = DSSObject.ActiveCircuit;

DSSSwtCtrl = DSSCircuit.SwtControls;


***
_Created with the Standard Edition of HelpNDoc: [Write eBooks for the Kindle](<https://www.helpndoc.com/feature-tour/create-ebooks-for-amazon-kindle>)_
