# Reset

&nbsp;

(method)

&nbsp;

This method resets DSS Initialization for restarts, etc from applets.

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

% Reset OpenDSS

DSSObject.Reset();

***
_Created with the Standard Edition of HelpNDoc: [Free EBook and documentation generator](<https://www.helpndoc.com>)_
