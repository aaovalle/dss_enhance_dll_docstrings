# Name

&nbsp;

(read/write)

&nbsp;

This property sets/gets the active generator by name.

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

% Gets the name of the active generator

myGenName = DSSGen.Name;

% Activates generator 'myGen01'

DSSGen.Name = 'myGen01';

***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Output with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
