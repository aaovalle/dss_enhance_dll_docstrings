# kV

&nbsp;

(read/write)

&nbsp;

Returns the kV rating for the active capacitor.

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

myCapkVs = \[\];

% swipes all the caps to get the kV rating for each

i = DSSCapacitors.First;

while&nbsp; i \> 0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myCapkVs = \[myCapkVs;DSSCapacitors.kV\];

i = DSSCapacitors.Next;

end;

***
_Created with the Standard Edition of HelpNDoc: [Revolutionize your documentation process with HelpNDoc's online capabilities](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
