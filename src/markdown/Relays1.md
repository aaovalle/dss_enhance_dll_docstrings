# Relays

&nbsp;

This interface can be used to gain access to the features of the relays installed across the model. This interface is embedded within the ActiveCircuit interface, requiring the definition of this interface before getting access the to Relays interface.

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

DSSRelays = DSSCircuit.Relays;

***
_Created with the Standard Edition of HelpNDoc: [Full-featured EBook editor](<https://www.helpndoc.com/create-epub-ebooks>)_
