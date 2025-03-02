# EmergVminpu

&nbsp;

(read/write)

&nbsp;

This property sets/gets the per unit (pu) minimum voltage for Emergency conditions.

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

DSSSettings = DSSCircuit.Settings;

% Gets the max voltage pu for emergency conditions

myEmergVmax = DSSSettings.EmergVmaxpu;

% Gets the min voltage pu for emergency conditions

myEmergVmin = DSSSettings.EmergVminpu;

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly bring your documentation online with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
