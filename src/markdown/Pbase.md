# Pbase

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Base P value for normalization. Default is zero, meaning the peak will be used.

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

DSSLoadShapes = DSSCircuit.LoadShapes;

% Activates the first LoadShape of the list

i = DSSLoadShapes.First;

% gets the base P of the active LoadShape

myPBase = DSSLoadShapes.Pbase;

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Help Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com>)_
