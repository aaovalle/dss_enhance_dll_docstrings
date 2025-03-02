# MeteredTerminal

&nbsp;

(read/write)

&nbsp;

This property sets/gets the number of the metered terminal of the metered element at the active EnergyMeter.

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

DSSMeters = DSSCircuit.Meters;

% activates the first EM on the list

i = DSSMeters.First;

% If the metered terminal is 1 it will change it to 2

if DSSMeters.MeteredTerminal == 1,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; DSSMeters.MeteredTerminal = 2;

end;

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly optimize your documentation website for search engines](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
