# SAIFIKW

&nbsp;

(read only)

&nbsp;

This property returns the SAIFI based on kW rather than number of customers for the active meter's zone. Execute DoReliabilityCalc first.

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

DSSMeters = DSSCircuit.Meters;

% performs the reliability calculations for the model

% assuming automatic restoration

DSSMeters.DoreliabilityCalc(true);

% activates the first EM on the list

i = DSSMeters.First;

% gets the SAIFI based on kW for the active EnergyMeter's zone

mySAIFIkW = DSSMeters.SAIFIKW;

***
_Created with the Standard Edition of HelpNDoc: [Ensure High-Quality Documentation with HelpNDoc's Hyperlink and Library Item Reports](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
