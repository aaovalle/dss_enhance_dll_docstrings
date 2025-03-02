# ConcatenateReports

&nbsp;

(read/write)

&nbsp;

This property activates/deactivates the concatenate reports option. With this option, the user can put together all the individual reports for the actors automatically.

&nbsp;

*Example*

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Unable to start openDSS');

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

DSSText = DSSObject.Text;

DSSCircuit = DSSObject.ActiveCircuit;

% Handler for Parallel processing functions

DSSParallel = DSSCircuit.Parallel; &nbsp; &nbsp;

% Gets the number of CPUs this PC has

CPUs = DSSParallel.NumCPUs; &nbsp; &nbsp;

% Checks if concatenate reports is enabled, if not, enables it

if ~DSSParallel.ConcatenateReports,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; DSSParallel.ConcatenateReports = 1;

end;

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create High-Quality Help Documentation with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
