# LineCodes

&nbsp;

This interface can be used to gain access to the features of the Line codes (LineCodes) used for defining circuit elements in the model in OpenDSS. Line codes can be used to define the features of multiple lines across the model without having to redefine them for each line when creating the model.&nbsp;

Also, if the properties of a line code change, those changes will automatically be inherited by the lines pointing to the line code modified. This interface is embedded within the ActiveCircuit interface, requiring the definition of this interface before getting access the to LineCodes interface.

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

DSSLineCodes = DSSCircuit.LineCodes;

***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Ease of Use of HelpNDoc for CHM Help File Generation](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
