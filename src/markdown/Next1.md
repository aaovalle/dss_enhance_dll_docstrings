# Next

&nbsp;

(read only)

&nbsp;

Sets the next element in the capacitors class to be the active DSS object. Returns 0 if none.

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

DSSCapacitors = DSSCircuit.Capacitors;

myCapSteps = \[\];

% swipes all the caps to get the number of available steps for each

i = DSSCapacitors.First;

while&nbsp; i \> 0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myCapSteps = \[myCapSteps;DSSCapacitors.AvailableSteps\];

i = DSSCapacitors.Next;

end;

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Capabilities with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
