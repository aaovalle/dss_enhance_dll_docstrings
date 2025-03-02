# PF

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Power factor (pos. = producing vars). Updates kvar based on present kW value.

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

% gets the pf for the active Generator

myPF = DSSGen.pf;

***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Creation with a Help Authoring Tool](<https://www.helpndoc.com>)_
