# KeepLoad

&nbsp;

(read/write)

&nbsp;

This property sets/gets a flag for indicating to keep the load for Reduction options that remove branches.

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

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Productivity with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
