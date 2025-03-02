# Capacity

&nbsp;

(method)

&nbsp;

This method computes the maximum load the active circuit can serve in the PRESENT YEAR. Uses the EnergyMeter objects with the registers set with the SET UEREGS= (..) command for the AutoAdd functions.&nbsp;

Returns the metered kW (load + losses - generation) and per unit load multiplier for the loading level at which something in the system reports an overload or undervoltage. If no violations, then it returns the metered kW for peak load for the year (1.0 multiplier). Aborts and returns 0 if no energymeters.

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

DSSText.Command = 'Solve';

DSSCircuit = DSSObject.ActiveCircuit;

% Calculates the circuit's capacity for the current year,

% requires the initial value for the load and the increment&nbsp;

% as arguments (0.9 and 0.005 respectively)

DSSCapacity = DSSCircuit.Capacity(0.9,0.005);

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create Professional Documentation with HelpNDoc's Clean UI](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
