# Mode

&nbsp;

(read/write)

&nbsp;

This property sets/gets an integer representing the solution mode. One of the following:

&nbsp;

&nbsp; 0 - Snapshot,

&nbsp; 1 - Daily,

&nbsp; 2 - Yearly (follow Yearly curve),

&nbsp; 3 - DIrect ,

&nbsp; 4 - DUtycycle,

&nbsp; 5 - Time, ( see LoadShapeClass option)

&nbsp; 6 - DYnamic,&nbsp; ( see LoadShapeClass option)

&nbsp; 7 - Harmonic,

&nbsp; 8 - HarmonicT,&nbsp; (sequential Harmonic Mode)

&nbsp; 9 - M1 (Monte Carlo 1),

&nbsp; 10 - M2 (Monte Carlo 2),

&nbsp; 11 - M3 (Monte Carlo 3),

&nbsp; 12 - Faultstudy,

&nbsp; 13 - MF (monte carlo fault study)

&nbsp; 14 - Peakday,

&nbsp; 15 - LD1 (load-duration 1)

&nbsp; 16 - LD2 (load-duration 2)

&nbsp; 17 - AutoAdd (see AddType)

&nbsp; 18 - YearlyVQ (Yearly Vector Quantiaztion)

&nbsp; 19 - DutyVQ (Duty Vector Quantiaztion)

&nbsp;

Side effect: setting the Mode property resets all monitors and energy meters. It also resets the time step, etc. to defaults for each mode.&nbsp; After the initial reset, the user must explicitly reset the monitors and/or meters until another Set Mode= command.

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

% set the control iterations to 1000

DSSSolution.ControlIterations = 1000;&nbsp;

% set simulation mode daily

DSSSolution.Mode = 1;

% set simulation step size 1 h

DSSSolution.StepSize = 1;

&nbsp;

% gets the name of the default load shape (daily)

myDefLS = DSSSolution.DefaultDaily;

&nbsp;

% set simulation hour 1.5

DSSSolution.dblHour = 1.5;&nbsp;

% Solve the model

DSSSolution.Solve();&nbsp;

&nbsp;

% gets the new hour we are located

myHour = DSSSolution.dblHour;
***
_Created with the Standard Edition of HelpNDoc: [Bring your WinHelp HLP help files into the present with HelpNDoc's easy CHM conversion](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
