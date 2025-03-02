# DataPath

&nbsp;

(read/write)

&nbsp;

This property can be used to set/get the DSS Data File Path.&nbsp; This is the default path for reports, etc. from DSS.

&nbsp;

*Example*

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp("Unable to start openDSS");

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

myDataPath = DSSObject.DataPath;

***
_Created with the Standard Edition of HelpNDoc: [Easily create Qt Help files](<https://www.helpndoc.com/feature-tour>)_
