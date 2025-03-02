# Status

&nbsp;

(read/write)

&nbsp;

This property sets/gets the response to load multipliers={Variable \| Fixed \| Exempt}.&nbsp; Default is variable. If Fixed, no load multipliers apply;&nbsp; however, growth multipliers do apply.&nbsp; All multipliers apply to Variable loads.&nbsp; Exempt loads are not modified by the global load multiplier, such as in load duration curves, etc.&nbsp; Daily multipliers do apply, so setting this property to Exempt is a good way to represent industrial load that stays the same day-after-day for the period study.

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

DSSLoads = DSSCircuit.Loads;

% activates the first load on the list

i = DSSLoads.First;

% gets the status of the active load

myStat = DSSLoads.Status;


***
_Created with the Standard Edition of HelpNDoc: [Create HTML Help, DOC, PDF and print manuals from 1 single source](<https://www.helpndoc.com/help-authoring-tool>)_
