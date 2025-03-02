# YNodeVarray

&nbsp;

(read only)

&nbsp;

This property returns a complex array of actual node voltages in same order as SystemY matrix.

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

% Gets the Y voltages obtained after solving

myYV = DSSCircuit.YNodeVarray;

mySize = size(myYV);

% Formats the voltages vector as a complex and polar vectors

myVCmplx = \[\];

myVPolar = \[\];

for a = 1:2:mySize(2),

&nbsp; &nbsp; cmplxNum = myYV(a)+ i\*myYV(a + 1);

&nbsp; &nbsp; myVCmplx = \[myVCmplx;cmplxNum\];

&nbsp; &nbsp; myVPolar = \[myVPolar;\[abs(cmplxNum),angle(cmplxNum)\*180/pi\]\];

end;


***
_Created with the Standard Edition of HelpNDoc: [Free help authoring tool](<https://www.helpndoc.com/help-authoring-tool>)_
