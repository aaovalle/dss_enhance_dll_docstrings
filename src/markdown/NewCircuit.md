# NewCircuit

&nbsp;

(method)

&nbsp;

This method makes a new circuit and return interface to active circuit.

&nbsp;

*Example*

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Unable to start openDSS');

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

% Clears the existing model from memory

DSSObject.ClearAll();

% Creates a new one and gets the handler

DSSCircuit = DSSObject.NewCircuit(My\_Circuit');

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Documentation Process with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
