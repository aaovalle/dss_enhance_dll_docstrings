# SwitchedTerm

&nbsp;

(read/write)

&nbsp;

This property sets/gets the terminal number of the switched object for the active recloser .

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

DSSReclosers = DSSCircuit.Reclosers;

% Activates the first recloser on the list

i = DSSReclosers.First;

% gets the name of the element switched by the active recloser

mySWObj = DSSReclosers.SwitchedObj;

% gets the switched terminal, if 2 force it to 1 (for the example)

if DSSReclosers.SwitchedTerm == 2,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; DSSReclosers.SwitchedTerm = 1;

end

***
_Created with the Standard Edition of HelpNDoc: [What is a Help Authoring tool?](<https://www.helpauthoringsoftware.com>)_
