# AngleDeg

&nbsp;

(read/write)

&nbsp;

This property sets/gets the phase angle of the active ISOURCE in degrees.

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

% Sets the phase angle for the ISource (30 deg)

DSSIsources.AngleDeg = 30;

***
_Created with the Standard Edition of HelpNDoc: [Full-featured Kindle eBooks generator](<https://www.helpndoc.com/feature-tour/create-ebooks-for-amazon-kindle>)_
