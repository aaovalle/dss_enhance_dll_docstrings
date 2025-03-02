# DoSwitches

&nbsp;

(method)

&nbsp;

This method merges Line objects in which the IsSwitch property is true with the down-line Line object.

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

DSSPDE = DSSObject.PDElements;

% Activates the first PDE on the list

i = DSSPDE.First;

% breaks loops first

DSSReduceCkt.DoLoopBreak();

% merge parallel lines

DSSReduceCkt.DoParallelLines();

% merge switches

DSSReduceCkt.DoSwitches();

***
_Created with the Standard Edition of HelpNDoc: [Create cross-platform Qt Help files](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
