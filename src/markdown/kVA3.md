# kVA

(read/write)

&nbsp;

This property get/set the kVA rating of electrical machine, for the active WindGen obj. Defaults to 1.2\* kW if not specified.

&nbsp;

Example

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

disp('Unable to start openDSS');

&nbsp; &nbsp; &nbsp; return

end;

DSSText = DSSObject.Text;

DSSCircuit = DSSObject.ActiveCircuit;

DSSWG = DSSCircuit.WingGens;

% Compile a model &nbsp; &nbsp; &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSSolution.Solve;

&nbsp;

% gets the names of all wind generators in the model

myWGs = DSSWG.AllNames;

&nbsp;

% Activates the first WG of the list

NumWG = DSSWG.First;

&nbsp;

% Gets the rated kV

mykV = DSSWG.kV;

% Gets the rated kVA

mykVA = DSSWG.kVA;

***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Simplicity of HelpNDoc's User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
