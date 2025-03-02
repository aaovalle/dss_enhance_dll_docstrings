# Reset

&nbsp;

(method)

&nbsp;

This method resets the relay to its normal state. If open, it locks out the relay. If closed, the relay is reset to its first operation.

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

% Activates the first relay of the list

i = DSSRelays.First;

% resets the active relay

DSSRelays.Reset();

***
_Created with the Standard Edition of HelpNDoc: [Full-featured multi-format Help generator](<https://www.helpndoc.com/help-authoring-tool>)_
