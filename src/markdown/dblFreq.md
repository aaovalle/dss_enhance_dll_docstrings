# dblFreq

&nbsp;

(read only)

&nbsp;

This property returns a variant array of doubles containing frequency values for harmonics mode solutions; Empty for time mode solutions (use dblHour).

&nbsp;

Example

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Unable to start openDSS');

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

DSSText = DSSObject.Text;

DSSCircuit = DSSObject.ActiveCircuit;

% Compile a model &nbsp; &nbsp; &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSText.Command = 'solve mode=Harmonic';

DSSMonitors = DSSCircuit.Monitors;

% saves all monitors registers

DSSMonitors.SaveAll();

% select the first monitor on the list

DSSMonitors.First

% gets the frequencies recorded from the last harmonic solve

myFreq = DSSMonitors.dblFreq;&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Free Qt Help documentation generator](<https://www.helpndoc.com>)_
