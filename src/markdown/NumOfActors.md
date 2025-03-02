# NumOfActors

&nbsp;

(read only)

&nbsp;

This property returns the number of Actors created so far.

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

% Handler for Parallel processing functions

DSSParallel = DSSCircuit.Parallel; &nbsp; &nbsp;

% Gets the number of CPUs this PC has

CPUs = DSSParallel.NumCPUs; &nbsp; &nbsp;

% By default one actor is created, if you want more than one

% parallel instance you will have to create them. Try to leave at least

% One CPU available to handle the rest of windows, otherwise will block everything

disp('Creating Actors');

DSSText.Command = 'compile "C:\\Program Files\\OpenDSS\\EPRITestCircuits\\ckt5\\Master\_ckt5.DSS"';

DSSText.Command = 'set maxiterations=1000 maxcontroliter=1000'; &nbsp; % Just in case

DSSCircuit.Solution.Solve(); % Solves Actor 1

&nbsp;

DSSText.Command = \['Clone ',int2str(CPUs-2)\]; %Creates the other actors

DSSText.Command = 'set ActiveActor=\*';&nbsp; &nbsp; &nbsp; &nbsp; %activates all actors to send commands concurrently

DSSText.Command = 'set mode=Time stepsize=1h number=16000';

&nbsp;

%Gets the number of actors created so far

myNActors = DSSParallel.NumActors;

***
_Created with the Standard Edition of HelpNDoc: [Make Your PDFs More Secure with Encryption and Password Protection](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
