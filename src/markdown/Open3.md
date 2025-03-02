# Open

&nbsp;

(method)

&nbsp;

This method opens recloser's controlled element and lock out the recloser.

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

DSSReclosers = DSSCircuit.Reclosers;

% Activates the first recloser on the list

i = DSSReclosers.First;

% opens the active recloser manually

DSSReclosers.Open();

***
_Created with the Standard Edition of HelpNDoc: [Easily create CHM Help documents](<https://www.helpndoc.com/feature-tour>)_
