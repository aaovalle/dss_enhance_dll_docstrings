# CapControls

&nbsp;

This interface can be used to gain access to the features and properties of all the capacitor controls (CapControls) deployed across the model. Because it is embedded within the ActiveCircuit interface, requires the definition of this interface before getting access the to CapControls interface.

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

DSSCapCtrls = DSSCircuit.CapControls;

***
_Created with the Standard Edition of HelpNDoc: [Easily share your documentation with the world through a beautiful website](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
