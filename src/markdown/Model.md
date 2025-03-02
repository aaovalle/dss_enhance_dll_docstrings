# Model

&nbsp;

(read/write)

&nbsp;

This property sets/gets the generator model using an integer. It can be one of the following:

&nbsp;

&#49; : Generator injects a constant kW at specified power factor.

&#50; : Generator is modeled as a constant admittance.

&#51; : Const kW, constant kV.&nbsp; Somewhat like a conventional transmission power flow P-V generator.

&#52; : Const kW, Fixed Q (Q never varies)

&#53; : Const kW, Fixed Q(as a constant reactance)

&#54; : Compute load injection from User-written Model.(see usage of Xd, Xdp)

&#55; : Constant kW, kvar, but current-limited below Vminpu. Approximates a simple inverter. See also Balanced.

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

DSSGen = DSSCircuit.Generators;

% Selects the first Generator from the list

DSSGen.First;

% Gets the generator model, if it's model 1, change it to model 4

% (For the example)

if DSSGen.model == 1,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; DSSGen.model = 4;

end;

***
_Created with the Standard Edition of HelpNDoc: [Easily create Qt Help files](<https://www.helpndoc.com/feature-tour>)_
