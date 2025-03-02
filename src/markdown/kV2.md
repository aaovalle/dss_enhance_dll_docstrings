# kV

&nbsp;

(read/write)

&nbsp;

This property sets/gets the kV rating for active Load. For 2 or more phases set Line-Line kV. Else actual kV across terminals.

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

DSSLoads = DSSCircuit.Loads;

% activates the first load on the list

i = DSSLoads.First;

% gets the kV rating for the active load

mykV = DSSLoads.kV;

***
_Created with the Standard Edition of HelpNDoc: [Single source CHM, PDF, DOC and HTML Help creation](<https://www.helpndoc.com/help-authoring-tool>)_
