# ActiveBus

&nbsp;

This interface can be used to gain access to the features of the active Bus. Since buses are not objects, this interface provides access to the bus properties and values. The active bus needs to be specified by using the Active Circuit interface. The ActiveBus interface is embedded within the ActiveCircuit interface, requiring the definition of this interface before getting access the to ActiveBus interface.

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

DSSActiveBus = DSSCircuit.ActiveBus;

***
_Created with the Standard Edition of HelpNDoc: [Converting Word Documents to eBooks: A Step-by-Step Guide with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
