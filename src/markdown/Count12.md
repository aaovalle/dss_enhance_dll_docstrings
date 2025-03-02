# Count

&nbsp;

(read only)

&nbsp;

This property returns the number of Power Delivery Elements (PDE) in the Active Circuit.

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

% gets the total number of PDEs in the model

myNPDEs = DSSPDE.Count;


***
_Created with the Standard Edition of HelpNDoc: [Free EBook and documentation generator](<https://www.helpndoc.com>)_
