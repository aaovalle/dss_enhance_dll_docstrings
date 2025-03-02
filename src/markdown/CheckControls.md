# CheckControls

&nbsp;

(method)

&nbsp;

This method executes the normal process for sampling and executing Control Actions and Fault Status and rebuilds Y if necessary.

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

DSSSolution = DSSCircuit.Solution;

&nbsp;

% solves the circuit without control actions

DSSSolution.SolveNoControl();&nbsp;

% samples and executes control actions

DSSSolution.CheckControls();

***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with HelpNDoc's Intuitive Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
