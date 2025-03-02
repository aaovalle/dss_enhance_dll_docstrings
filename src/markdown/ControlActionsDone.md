# ControlActionsDone

&nbsp;

(read/write)

&nbsp;

This property sets/gets a flag for indicating that the control actions are done.

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

% Executes status check in all fault objects

DSSSolution.CheckFaultStatus();

% Executes status check in all fault objects

DSSSolution.Cleanup();

% Checks if the control actions are done

if DSSSolution.ControlActionsDone,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mySolver = 'Control actions are done';

&nbsp; &nbsp; else

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mySolver = 'No control actions executed';

end;

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Word Doc into a Professional-Quality eBook with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
