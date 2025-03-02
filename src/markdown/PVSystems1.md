# PVSystems

&nbsp;

This interface can be used to gain access to the features of the photo voltaic systems (PVSystems) installed across the model. This interface is embedded within the ActiveCircuit interface, requiring the definition of this interface before getting access the to PVSystems interface.

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

DSSPVSystems = DSSCircuit.PVSystems;

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create Professional Documentation with HelpNDoc's Clean UI](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
