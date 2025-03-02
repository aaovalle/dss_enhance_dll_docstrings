# NumTaps

&nbsp;

(read/write)

&nbsp;

This property sets/gets the active winding number of tap steps between MinTap and MaxTap.&nbsp; Default is 32 (16 raise and 16 lower taps about the neutral position). The neutral position is not counted.

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

% Activates the first winding of the active transformer

DSSXfmr.Wdg = 1;

% gets the number of taps for the active transformer

for j = 1:2,

&nbsp; &nbsp; DSSXfmr.Wdg = j;

&nbsp; &nbsp; disp(\['Winding ', num2str(j),' has ', num2str(DSSXfmr.NumTap), ' taps'\]);

end;

***
_Created with the Standard Edition of HelpNDoc: [Make Help Documentation a Breeze with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
