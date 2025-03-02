# DSSim_Coms

&nbsp;

(read only)

DEPRECATED

&nbsp;

This property returns a handler for the DSSim\_Coms interface. This interface is deprecated and has no useful purpose in OpenDSS.

&nbsp;

*Example*

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Unable to start openDSS');

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

% Returns the handler to the DSSim\_Coms interface

DSSComs = DSSObject.DSSim\_Coms;

***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
