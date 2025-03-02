# RatedCurrent

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Multiplier or actual amps for the TCCcurve object. Defaults to 1.0.&nbsp; Multiply current values of TCC curve by this to get actual amps.

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

% Selects the first fuse from the list

DSSFuses.First;

% gets the current rated current,

% if 0, sets RatedCurrent to 1&nbsp;

if DSSFuses.RatedCurrent == 0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; DSSFuses.RatedCurrent = 1.0;

end;

***
_Created with the Standard Edition of HelpNDoc: [Free PDF documentation generator](<https://www.helpndoc.com>)_
