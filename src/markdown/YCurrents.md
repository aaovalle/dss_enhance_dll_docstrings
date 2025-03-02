# YCurrents

&nbsp;

(read only)

&nbsp;

This property returns a variant array of doubles containing complex injection currents for the present solution. It is the "I" vector of I=YV.

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

% Gets the Y currents

myYCurr = DSSCircuit.YCurrents;

mySize = size(myYCurr);

% Formats the injection currents vector as a complex and polar vectors

myInjCurrCmplx = \[\];

myInjCurrPolar = \[\];

for a = 1:2:mySize(2),

&nbsp; &nbsp; cmplxNum = myYCurr(a)+ i\*myYCurr(a + 1);

&nbsp; &nbsp; myInjCurrCmplx = \[myInjCurrCmplx;cmplxNum\];

&nbsp; &nbsp; myInjCurrPolar = \[myInjCurrPolar;\[abs(cmplxNum),angle(cmplxNum)\*180/pi\]\];

end;


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Productivity with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
