# Fuses

&nbsp;

This interface can be used to gain access to the features of the fuses deployed across the circuit model in OpenDSS. This interface is embedded within the ActiveCircuit interface, requiring the definition of this interface before getting access the to Fuses interface.

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

DSSFuses = DSSCircuit.Fuses;

***
_Created with the Standard Edition of HelpNDoc: [Easily create EBooks](<https://www.helpndoc.com/feature-tour>)_
