# Next

&nbsp;

(read only)

&nbsp;

Advance the active Fuse element pointer to the next fuse. Returns 0 if no more fuses.

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

DSSFuses = DSSCircuit.Fuses;

myFuseNames = \[\];

% swipes all the fuses to get their names (to make the example interesting)

i = DSSFuses.First;

while&nbsp; i \> 0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myFuseNames = \[myFuseNames;DSSFuses.Name\];

i = DSSFuses.Next;

end;

***
_Created with the Standard Edition of HelpNDoc: [Simplify Your Help Documentation Process with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
