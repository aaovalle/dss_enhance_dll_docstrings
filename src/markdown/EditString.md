# EditString

&nbsp;

(read/write)

&nbsp;

This property sets/gets the string containing the OpenDSS command appended to the BranchRemove option when a new load is defined to represent the load on the removed branch.

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

&nbsp;

% breaks loops first

DSSReduceCkt.DoLoopBreak();

% merge parallel lines

DSSReduceCkt.DoParallelLines();

% reduce the short lines algorithm

DSSReduceCkt.DoSwitches();

&nbsp;

% get the OpenDSS command

myStr = DSSReduceCkt.EditString;

***
_Created with the Standard Edition of HelpNDoc: [Say Goodbye to Documentation Headaches with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
