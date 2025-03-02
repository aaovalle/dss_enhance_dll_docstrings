# SaveCircuit

&nbsp;

(method)

&nbsp;

This method executes the Save Circuit command from the COM interface. Saves the reduced circuit in a directory with the specified name. The full path name of the Master.DSS file is return in the DSSText.Result property.

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

DSSReduceCkt = DSSCircuit.ReduceCkt;

DSSMeters = DSSCircuit.Meters;

% gets the names of the first EM on the list

i = DSSMeters.First;

myEM = DSSMeters.Name;

&nbsp;

% set the EM name for the reduction

DSSReduceCkt.EnergyMeter = myEM;

% command to keep load&nbsp;

DSSReduceCkt.KeppLoad = true;

% breaks loops first

DSSReduceCkt.DoLoopBreak();

% merge parallel lines

DSSReduceCkt.DoParallelLines();

% reduce&nbsp;

DSSReduceCkt.DoDefault();

&nbsp;

% get the OpenDSS command

myStr = DSSReduceCkt.EditString;

&nbsp;

% Saves the circuit after reduction

DSSReduceCkt.SaveCircuit('myNewCircuit');

***
_Created with the Standard Edition of HelpNDoc: [News and information about help authoring tools and software](<https://www.helpauthoringsoftware.com>)_
