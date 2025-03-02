# dblHour

&nbsp;

(read only)

&nbsp;

This property returns a Variant array of doubles containing time value in hours for time-sampled monitor values; Empty if frequency-sampled values for harmonics solution (see dblFreq).

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

DSSText.Command = 'solve mode=daily';

DSSMonitors = DSSCircuit.Monitors;

% saves all monitors registers

DSSMonitors.SaveAll();

% select the first monitor on the list

DSSMonitors.First

% gets the hours recorded in the last solve

myHour = DSSMonitors.dblHour;&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Step-by-Step Guide: How to Turn Your Word Document into an eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
