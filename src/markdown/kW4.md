# kW

(read/write)

&nbsp;

This property get/set the Total base kW for the active WindGen obj.

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

***
_Created with the Standard Edition of HelpNDoc: [Produce online help for Qt applications](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
