# IsDelta

&nbsp;

(read/write)

&nbsp;

This property sets/gets a flag for indicating if the measured voltages are line-line (true). Currents are always line currents.

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

DSSSensors = DSSCircuit.Sensors;

% activates the first sensor on the list

i = DSSSensors.First;

% Check if the voltages are measured LL, if not, force it

if ~DSSSensors.IsDelta,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; DSSSensors.IsDelta = true;

end;

***
_Created with the Standard Edition of HelpNDoc: [Create help files for the Qt Help Framework](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
