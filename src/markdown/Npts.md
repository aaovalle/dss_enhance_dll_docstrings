# Npts

&nbsp;

(read/write)

&nbsp;

This property sets/gets the max number of points to expect in load shape vectors. This gets reset to the number of multiplier values found (in files only) if less than specified.

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

% gets the number of points in the active LoadShape

myNpts = DSSLoadShapes.Npts;

***
_Created with the Standard Edition of HelpNDoc: [What is a Help Authoring tool?](<https://www.helpauthoringsoftware.com>)_
