# AddType

&nbsp;

(read/write)

&nbsp;

This property sets/gets the type of device to add in AutoAdd Mode: {dssGen (Default) \| dssCap}.

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

DSSSolution = DSSCircuit.Solution;

&nbsp;

% gets the type of device to add in AutoAdd mode

if DSSSolution.AddType == 1,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('AutoAdd device is dssGen');

&nbsp; &nbsp; else

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('AutoAdd device is dssCap');

end;

***
_Created with the Standard Edition of HelpNDoc: [What is a Help Authoring tool?](<https://www.helpauthoringsoftware.com>)_
