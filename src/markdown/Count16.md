# Count

&nbsp;

(read only)

&nbsp;

This property returns the number of relays deployed across the model.

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

DSSRelays = DSSCircuit.Relays;

% Gets the number of relays across the model

myNRelays = DSSRelays.Count

***
_Created with the Standard Edition of HelpNDoc: [Generate Kindle eBooks with ease](<https://www.helpndoc.com/feature-tour/create-ebooks-for-amazon-kindle>)_
