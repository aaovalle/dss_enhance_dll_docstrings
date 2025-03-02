# CmathLib

&nbsp;

This interface is a collection of libraries for complex math using the OpenDSS core. The CmathLib is exposed directly by the DSS object (OpenDSSEngine).

&nbsp;

*Example*

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp("Unable to start openDSS");

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

DSSCmathlib = DSSObject.CmathLib;

***
_Created with the Standard Edition of HelpNDoc: [Produce Kindle eBooks easily](<https://www.helpndoc.com/feature-tour/create-ebooks-for-amazon-kindle>)_
