# Amps

&nbsp;

(read/write)

&nbsp;

This property sets/gets the magnitude of the active ISOURCE in amps.

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

DSSIsources = DSSCircuit.Isources;

% Selects the first Isource from the list

DSSIsources.First;

% Sets the amps level for the ISource (10 amps)

DSSIsources.Amps = 10;

***
_Created with the Standard Edition of HelpNDoc: [Full-featured EBook editor](<https://www.helpndoc.com/create-epub-ebooks>)_
