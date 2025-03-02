# Next

&nbsp;

(read only)

&nbsp;

Invoking this property advances to the next Line code element active.&nbsp; Returns 0 if no more line codes.&nbsp; Otherwise, index of the line code element.

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

DSSLineCodes = DSSCircuit.LinesCodes;

% activates the first line code on the list

i = DSSLineCodes.First;

% Gets the line code names using First/next commands

myNames = \[\];

while&nbsp; i \> 0,

&nbsp; &nbsp; myNames = \[myNames, DSSLineCodes.Name\];

i = DSSLineCodes.Next;

end;

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Documentation Workflow with HelpNDoc's Intuitive UI](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
