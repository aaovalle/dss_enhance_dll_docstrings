# CtrlQueue

&nbsp;

This interface can be used to gain access to the features and properties of the simulation control queue (CtrlQueue). Because it is embedded within the ActiveCircuit interface, requires the definition of this interface before getting access the to CtrlQueue interface.

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

DSSCtrlQueue = DSSCircuit.CtrlQueue;

***
_Created with the Standard Edition of HelpNDoc: [Free EPub and documentation generator](<https://www.helpndoc.com>)_
