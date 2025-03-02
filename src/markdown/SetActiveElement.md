# SetActiveElement

&nbsp;

(write only)

&nbsp;

This method sets the Active Circuit Element using the full object name (e.g. "generator.g1"). Returns -1 if not found. Else index to be used in CktElements collection or AllElementNames.

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

% Sets load 'load1' as the active circuit element

if (DSSCircuit.SetActiveElement('Load.Load1')) \< 0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('The element does not exist');

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Output with HelpNDoc's Advanced Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
