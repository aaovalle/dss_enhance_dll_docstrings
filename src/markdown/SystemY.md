# SystemY

&nbsp;

(read only)

&nbsp;

This property returns the system Y matrix as an array of doubles representing complex number pairs (dense format- includes 0s - after a solution has been performed)

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

DSSSolution = DSSCircuit.Solution;

DSSSolution.Solve();

% Gets the System Y

mySysY = DSSCircuit.SystemY;

myNodeList = DSSCircuit.AllNodeNames;

YSysSize = size(myNodeList);

% Formats Y matrix data as a complex dense matrix

myYMat = \[\];

myIdx = 1;

for a = 1:YSysSize(1),

&nbsp; &nbsp; myRow = \[\];

&nbsp; &nbsp; for b = 1:YSysSize(1),

&nbsp; &nbsp; &nbsp; &nbsp; myRow = \[myRow,(mySysY(myIdx) + i\*mySysY(myIdx + 1))\];

&nbsp; &nbsp; &nbsp; &nbsp; myIdx = myIdx + 2;

&nbsp; &nbsp; end;

&nbsp; &nbsp; myYMat = \[myYMat;myRow\];

end;


***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Documentation with HelpNDoc's Project Analyzer Features](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
