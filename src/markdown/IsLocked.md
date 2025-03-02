# IsLocked

&nbsp;

(read/write)

&nbsp;

This property sets/gets the SwtControl flag for indicating if it is locked. The lock prevents both manual and automatic switch operation.

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

DSSSwtCtrl = DSSCircuit.SwtControls;

% activates the first SW of the list

i = DSSSwtCtrl.First;

% Check if the SW is locked

if DSSSwtCtrl.IsLocked,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('The SW is Locked');

end;

***
_Created with the Standard Edition of HelpNDoc: [Experience a User-Friendly Interface with HelpNDoc's Documentation Tool](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
