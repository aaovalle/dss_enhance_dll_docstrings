# QFlag

(read/write)

&nbsp;

This property get/set the reactive power and voltage control for the active WindGen obj. Set 1 to activate, otherwise, 0.

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

% Gets the kvar output/input

mykvar = DSSWG.kvar;

% Gets the kW output

mykW = DSSWG.kW;

&nbsp;

% Gets the QFlag

myQFlg = DSSWG.QFlag;

***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Ease of Use of HelpNDoc for CHM Help File Generation](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
