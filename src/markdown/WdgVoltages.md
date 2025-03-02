# WdgVoltages

&nbsp;

(read only)

&nbsp;

This property returns a complex array of voltages for the active winding in the active transformer.

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

&nbsp;

% Format complex data into mag - angle

myAmpsMagAng = \[\];

for k = 1:DSSXfmr.NumWindings,

&nbsp; &nbsp; % get the voltages for the winding (complex)

&nbsp; &nbsp; myVolts = DSSXfmr.WdgVoltages;

&nbsp; &nbsp; myCols = size(myVolts);

&nbsp; &nbsp; myRow = \[\];

&nbsp; &nbsp; &nbsp; &nbsp; for a = 1:2:myCols(2),

&nbsp; &nbsp; &nbsp; &nbsp; myMag = abs(myVolts(1,a) + i\*myVolts(1,a + 1));

&nbsp; &nbsp; &nbsp; &nbsp; myAng = angle(myVolts(1,a) + i\*myVolts(1,a + 1)) \* 180/pi;

&nbsp; &nbsp; &nbsp; &nbsp; myRow = \[myRow, \[myMag, myAng\]\];

&nbsp; &nbsp; end;

&nbsp; &nbsp; myAmpsMagAng = \[myAmpsMagAng; myRow\];

end;


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Efficiency with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
