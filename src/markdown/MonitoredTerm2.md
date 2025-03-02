# MonitoredTerm

&nbsp;

(read/write)

&nbsp;

This property sets/gets the terminal number of the Monitored object for the active recloser .

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

% gets the name of the element monitored by the active recloser

myMonObj = DSSReclosers.MonitoredObj;

% gets the monitored terminal, if 2 force it to 1 (for the example)

if DSSReclosers.MonitoredTerm == 2,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; DSSReclosers.MonitoredTerm = 1;

end

***
_Created with the Standard Edition of HelpNDoc: [Add an Extra Layer of Security to Your PDFs with Encryption](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
