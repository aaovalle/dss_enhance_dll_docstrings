# WdgCurrents

&nbsp;

(read only)

&nbsp;

This property returns all Winding currents (ph1, wdg1, wdg2,... ph2, wdg1, wdg2 ...) in an array of floating point (doubles) values.

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

j = DSSXfmr.First;

% Get the currents on each winding (complex)

myCurrents = DSSXfmr.WdgCurrents;

myCols = size(myCurrents)/DSSXfmr.NumWindings;

% Format complex data into mag - angle

myAmpsMagAng = \[\];

for k = 1:DSSXfmr.NumWindings,

&nbsp; &nbsp; myRow = \[\];

&nbsp; &nbsp; myShift = myCols(2) \* (k - 1);

&nbsp; &nbsp; for a = 1:2:myCols(2),

&nbsp; &nbsp; &nbsp; &nbsp; myMag = abs(myCurrents(1,a + myShift) + i\*myCurrents(1,a + myShift + 1));

&nbsp; &nbsp; &nbsp; &nbsp; myAng = angle(myCurrents(1,a + myShift) + i\*myCurrents(1,a + myShift + 1)) \* 180/pi;

&nbsp; &nbsp; &nbsp; &nbsp; myRow = \[myRow, \[myMag, myAng\]\];

&nbsp; &nbsp; end;

&nbsp; &nbsp; myAmpsMagAng = \[myAmpsMagAng; myRow\];

end;

&nbsp;

&nbsp;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Review with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
