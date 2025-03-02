# YscMatrix

&nbsp;

(read only)

&nbsp;

This property returns a complex array of Ysc matrix column by column for the active bus.

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

DSSActiveBus = DSSCircuit.ActiveBus;

&nbsp;

DSSText.Command = 'Solve mode=fault';

% Sets bus "myBus" as the active Bus

DSSCircuit.SetActiveBus('myBus')

myYscM = DSSActiveBus.YscMatrix;

mySize = DSSActiveBus.NumNodes;

myCMatrix = \[\];

%Recreate the matrix

for i=1:mySize,

myRow = \[\];

&nbsp; &nbsp; &nbsp; &nbsp; %Creates the row

&nbsp; &nbsp; &nbsp; &nbsp; for k=1:2:(mySize \* 2),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myRow = \[myRow, complex(myYscM(k),myYscM(k + 1))\];

&nbsp;&nbsp; &nbsp; &nbsp; end;

myCMatrix = \[myCMatrix; myRow\];

end;


***
_Created with the Standard Edition of HelpNDoc: [Easily create Web Help sites](<https://www.helpndoc.com/feature-tour>)_
