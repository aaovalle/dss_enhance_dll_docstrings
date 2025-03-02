# LossWeight

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Weighting factor applied to Loss register values.

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

% Gets the array for getting EM registers (Losses)

myEMIdx = DSSSettings.LossRegs;

% Gets the weighting factor for the EM registers (Losses)

myEMW = DSSSettings.LossWeight;

***
_Created with the Standard Edition of HelpNDoc: [Enhance Your Documentation with HelpNDoc's Advanced Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
