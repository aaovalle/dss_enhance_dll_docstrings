# ActiveCktElement

&nbsp;

This interface can be used to gain access to the features of the active circuit element without having to use a specific element interface. This interface is embedded within the ActiveCircuit interface, requiring the definition of this interface before getting access the to ActiveCktElement interface.

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

DSSActiveElement = DSSCircuit.ActiveCktElement;

***
_Created with the Standard Edition of HelpNDoc: [Create HTML Help, DOC, PDF and print manuals from 1 single source](<https://www.helpndoc.com/help-authoring-tool>)_
