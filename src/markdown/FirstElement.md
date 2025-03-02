# FirstElement

&nbsp;

(read only)

&nbsp;

This method sets the first element of active class to be the Active element in the active circuit. Returns 0 if none.

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

% Sets 'Load' as the active class

DSSCircuit.SetActiveClass('Load');

% Sets the first load on the list as the active element

i = DSSCircuit.FirstElement;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
