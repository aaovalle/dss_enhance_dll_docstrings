# Mode

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Monitor mode (bitmask integer). It can be one of the following:

&nbsp;

&#48; = Voltages and currents at designated terminal

&#49; = Powers at designated terminal

&#50; = Tap Position (Transformer Device only)

&#51; = State Variables (PCElements only)

&#52; = Flicker level and severity index (Pst) for voltages. No adders apply. Flicker level at simulation time step, Pst at 10-minute time step.

&#53; = Solution variables (Iterations, etc). Normally, these would be actual phasor quantities from solution.

&#54; = Capacitor Switching (Capacitors only)

&#55; = Storage state vars (Storage device only)

&#56; = All winding currents (Transformer device only)

&#57; = Losses, watts and var (of monitored device)

&#49;0 = All Winding voltages (Transformer device only) Normally, these would be actual phasor quantities from solution.

&#49;1 = All terminal node voltages and line currents of monitored device

&nbsp;

Combine mode with adders below to achieve other results for terminal quantities:

\+16 = Sequence quantities

\+32 = Magnitude only

\+64 = Positive sequence only or avg of all phases

&nbsp;

Mix adder to obtain desired results. For example:

Mode=112 will save positive sequence voltage and current magnitudes only

Mode=48 will save all sequence voltages and currents, but magnitude only.

&nbsp;

Example

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Unable to start openDSS');

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

DSSText = DSSObject.Text;

DSSCircuit = DSSObject.ActiveCircuit;

% Compile a model &nbsp; &nbsp; &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSText.Command = 'solve mode=daily';

DSSMonitors = DSSCircuit.Monitors;

% select the first monitor on the list

i = DSSMonitors.First;

% gets the active monitor's mode

myMode = DSSMonitors.Mode;


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your CHM Help File Capabilities with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
