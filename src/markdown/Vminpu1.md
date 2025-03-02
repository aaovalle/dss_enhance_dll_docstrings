# Vminpu

&nbsp;

(read/write)

&nbsp;

This property sets/gets the minimum per unit voltage for which the MODEL is assumed to apply. Lower end of normal voltage range.Below this value, the load model reverts to a constant impedance model that matches the model at the transition voltage. See also "Vlowpu" which causes the model to match Model=2 below the transition voltage. Default = 0.95.&nbsp;

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

DSSLoads = DSSCircuit.Loads;

% activates the first load on the list

i = DSSLoads.First;

% sets the min voltage pu to 0.9 for the active load

DSSLoads.Vmaxpu = 0.9;

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create Professional Documentation with HelpNDoc's Clean UI](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
