# Powers

&nbsp;

(read only)

&nbsp;

This property returns the a complex array of powers into each conductor of each terminal for the active element.

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

DSSLines = DSSCircuit.Capacitors;

% Compile a model &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSActiveElement = DSSCircuit.ActiveCktElement;

% Sets the first line of the list as the active element

if DSSLines.First \> 0,

&nbsp; &nbsp; % Gets the powers (P,Q) for all phases of the active element

&nbsp; &nbsp; myPowers = DSSActiveElement.Powers;

&nbsp; &nbsp; mySize = size(myPowers);

&nbsp; &nbsp; % organizes the array in complex pairs

&nbsp; &nbsp; myPQMat = \[\]

&nbsp; &nbsp; for a = 1:2:mySize(2),

&nbsp; &nbsp; &nbsp; &nbsp; myPQMat = \[myPQMat;\[myPowers(a), myPowers(a + 1)\]\];

&nbsp; &nbsp; end;

else&nbsp;

&nbsp; &nbsp; disp('It seems that you have no lines\!');

end;


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Output with HelpNDoc's Advanced Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
