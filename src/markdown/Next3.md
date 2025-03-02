# Next

&nbsp;

(read only)

&nbsp;

Advance the active Generator element pointer to the next Generator. Returns 0 if no more Generators.

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

DSSGen = DSSCircuit.Generators;

myGenNames = \[\];

% swipes all the generators to get their names (to make the example interesting)

i = DSSGen.First;

while&nbsp; i \> 0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myGenNames = \[myGenNames;DSSGen.Name\];

i = DSSGen.Next;

end;

***
_Created with the Standard Edition of HelpNDoc: [Upgrade your help files and your workflow with HelpNDoc's WinHelp HLP to CHM conversion](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
