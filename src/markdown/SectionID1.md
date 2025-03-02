# SectionID

&nbsp;

(read only)

&nbsp;

This property returns an Integer ID of the feeder section that this PDElement branch is part of.

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

% Handler for PDelements interface

DSSPDE = DSSObject.PDElements;

% Activates the first PDE on the list

i = DSSPDE.First;

% gets the section ID of the active PDE

mySID = DSSPDE.SectionID;

***
_Created with the Standard Edition of HelpNDoc: [Free HTML Help documentation generator](<https://www.helpndoc.com>)_
