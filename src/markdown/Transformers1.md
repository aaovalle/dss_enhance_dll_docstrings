# Transformers

&nbsp;

This interface can be used to gain access to the features of the transformers defined in the active model. This interface is embedded within the ActiveCircuit interface, requiring the definition of this interface before getting access to the Transformers interface.

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

DSSXfmr = DSSCircuit.Transformers;

***
_Created with the Standard Edition of HelpNDoc: [Streamline Your CHM Help File Creation with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
