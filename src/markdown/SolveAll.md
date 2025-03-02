# SolveAll

&nbsp;

(method)

&nbsp;

This method Solves all the circuits (Actors) loaded into memory by the user.

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

% to send commands to each actor separately you need to select each actor independently

% Go back to actor 1

DSSParallel.ActiveActor = 1;&nbsp;

% Assigns CPU 0 to actor 1

DSSParallel.ActorCPU = 0;&nbsp; &nbsp;

% Activates the parallel features

DSSParallel.ActiveParallel = 1;&nbsp;

&nbsp;

% Now the actors are solved

DSSCircuit.Solution.SolveAll();

&nbsp;

pause(0.1);&nbsp;

BoolStatus&nbsp; &nbsp; &nbsp; = &nbsp; 0;

while BoolStatus == 0,

&nbsp; &nbsp; ActorStatus &nbsp; &nbsp; = &nbsp; DSSParallel.ActorStatus;

&nbsp; &nbsp; BoolStatus&nbsp; &nbsp; &nbsp; = &nbsp; all(ActorStatus \& 1); %Checks if everybody has ended

&nbsp; &nbsp; ActorProgress &nbsp; = &nbsp; DSSParallel.ActorProgress;

&nbsp; &nbsp; clc;

&nbsp; &nbsp; for i=1:CPUs-1,

&nbsp; &nbsp; &nbsp; &nbsp; fprintf('Actor %i Progress(%%) @ CPU %i : %i\\n',i,i-1,ActorProgress(i));

&nbsp; &nbsp; end;

&nbsp; &nbsp; pause(0.5);&nbsp; %&nbsp; A little wait to not saturate the Processor &nbsp;

end;

disp('Simulation finished by all the actors');

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create High-Quality Help Documentation with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
