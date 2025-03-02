# IsDelta

&nbsp;

(read/write)

&nbsp;

This boolean property sets/gets the connection of the active winding. If (true) then the winding is connected in delta. If (false), it is connected in Wye (false).

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

DSSXfmr = DSSCircuit.Transformers;

% Activates the first transformer on the list

i = DSSXfmr.First;

% Checks each winding for their connection type

for j = 1:2,

&nbsp; &nbsp; DSSXfmr.Wdg = j;

&nbsp; &nbsp; if DSSXfmr.IsDelta,

&nbsp; &nbsp; &nbsp; &nbsp; connType = 'delta';

&nbsp; &nbsp; else

&nbsp; &nbsp; &nbsp; &nbsp; connType = 'Wye';&nbsp; &nbsp; &nbsp;

&nbsp; &nbsp; end;

&nbsp; &nbsp; disp(\['Winding ', num2str(j),' is ', connType, ' connected'\]);

end;


***
_Created with the Standard Edition of HelpNDoc: [Make Help Documentation a Breeze with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
