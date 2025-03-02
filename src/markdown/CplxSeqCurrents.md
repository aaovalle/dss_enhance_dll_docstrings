# CplxSeqCurrents

&nbsp;

(read only)

&nbsp;

This property returns a complex double array of Sequence Currents for all conductors of all terminals of active circuit element.

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

DSSLines = DSSCircuit.Lines;

% Compile a model &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSActiveElement = DSSCircuit.ActiveCktElement;

% Sets the first line of the list as the active element

if DSSLines.First \> 0,

&nbsp; &nbsp; % Gets the complex sequence currents

&nbsp; &nbsp; mySeqCurr = DSSActiveElement.CplxSeqCurrents;

&nbsp; &nbsp; % Formats the array as complex and polar arrays

&nbsp; &nbsp; mySize = size(mySeqCurr);

&nbsp; &nbsp; myCurrCmplx = \[\]

&nbsp; &nbsp; myCurrPolar = \[\]

&nbsp; &nbsp; for a = 1:2:mySize(2),

&nbsp; &nbsp; &nbsp; &nbsp; CNum = mySeqCurr(a) + i\*mySeqCurr(a + 1);

&nbsp; &nbsp; &nbsp; &nbsp; myCurrCmplx = \[myCurrCmplx;CNum\];

&nbsp; &nbsp; &nbsp; &nbsp; myCurrPolar = \[myCurrPolar;\[abs(CNum),angle(CNum)\*180/pi\]\];

&nbsp; &nbsp; end;

else&nbsp;

&nbsp; &nbsp; disp('It seems that you have no lines\!');

end;


***
_Created with the Standard Edition of HelpNDoc: [5 Reasons Why a Help Authoring Tool is Better than Microsoft Word for Documentation](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
