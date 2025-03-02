# TCCcurve

&nbsp;

(read/write)

&nbsp;

This property sets/gets the name of the TCCcurve object that determines fuse blowing.

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

% Compile a model &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSFuses = DSSCircuit.Fuses;

% Then assigns the TCC for the active fuse

DSSFuses.TCCcurve = 'tlink';

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create High-Quality Help Documentation with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
