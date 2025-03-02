# SeqPowers

***SeqPowers***

&nbsp;

&nbsp;

This property returns a double array of sequence powers into each 3-phase terminal of the active element.

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

&nbsp; &nbsp; % Gets the sequence powers

&nbsp; &nbsp; myPQ = DSSActiveElement.SeqPowers;

&nbsp; &nbsp; mySize = size(myPQ);

&nbsp; &nbsp; % organizes the array in complex pairs

&nbsp; &nbsp; myPQMat = \[\]

&nbsp; &nbsp; for a = 1:2:mySize(2),

&nbsp; &nbsp; &nbsp; &nbsp; myPQMat = \[myPQMat;\[myPQ(a), myPQ(a + 1)\]\];

&nbsp; &nbsp; end; &nbsp;

else&nbsp;

&nbsp; &nbsp; disp('It seems that you have no lines\!');

end


***
_Created with the Standard Edition of HelpNDoc: [What is a Help Authoring tool?](<https://www.helpauthoringsoftware.com>)_
