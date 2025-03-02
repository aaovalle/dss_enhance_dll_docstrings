# TotalPower

&nbsp;

(read only)

&nbsp;

This property returns the total power, watts and vars delivered to the circuit. The negative magnitudes (-) indicate that the power is coming out of the substations.

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

% Returns the total power (P,Q) delivered to the circuit

myTotalPower = DSSCircuit.TotalPower;

***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
