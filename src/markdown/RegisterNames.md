# RegisterNames

&nbsp;

(read only)

&nbsp;

This property returns a variant array of Names of all generator energy meter registers.

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

% gets the generator energy meter registers

myGens = DSSGen.RegisterNames;

***
_Created with the Standard Edition of HelpNDoc: [iPhone web sites made easy](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
