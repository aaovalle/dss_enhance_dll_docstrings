# EndOfTimeStepUpdate

&nbsp;

(method)

&nbsp;

This method calls EndOfTimeStepCleanup in SolutionAlgs (Do Cleanup, sample monitors, and increment time).

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

% Solves direct, with no control actions

DSSText.Command = '\_SolveNoControl';

% Finishes the time step

DSSCircuit.EndOfTimeStepUpdate;

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Productivity with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
