# VSources

&nbsp;

This interface can be used to gain access to the features of the voltage sources (VSources) installed across the model. Voltage sources are the equivalent to a substation or reference for the model. This interface is embedded within the ActiveCircuit interface, requiring the definition of this interface before getting access the to the VSources interface.

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

DSSVSources = DSSCircuit.VSources;

***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with HelpNDoc's Intuitive Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
