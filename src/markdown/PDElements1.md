# PDElements

&nbsp;

This interface can be used to gain access to the features of the Power Delivery Elements (PDE) included in OpenDSS. With the PDElements interface it is possible to navigate through combined PDE classes (Line, transformer, etc.) without having to use a specific interface for the class. This interface is embedded within the ActiveCircuit interface, requiring the definition of this interface before getting access the to PDElements interface.

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

DSSPDElements = DSSCircuit.PDElements;

***
_Created with the Standard Edition of HelpNDoc: [Easily share your documentation with the world through a beautiful website](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
