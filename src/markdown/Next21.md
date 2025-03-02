# Next

&nbsp;

(read/write)

&nbsp;

This property advances to next XYCurve object; returns 0 if no more objects of this class

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

DSSXY = DSSCircuit.XYCurves;

% activate the first XY curve of the list

i = DSSXY.First;

% Enumerates XYCurves by name

myNames = \[\];

while&nbsp; i \> 0,

&nbsp; &nbsp; myNames = \[myNames; DSSXY.Name\];

&nbsp; &nbsp; i = DSSXY.Next;

end;


***
_Created with the Standard Edition of HelpNDoc: [Transform Your CHM Help File Creation Process with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
