# YNodeOrder

&nbsp;

(read only)

&nbsp;

This property returns a variant array of strings containing the names of the nodes in the same order as the Y matrix.

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

% Gets the names of the nodes as assigned in the Y bus matrix

myYNodes = DSSCircuit.YNodeOrder;

***
_Created with the Standard Edition of HelpNDoc: [Easily create EBooks](<https://www.helpndoc.com/feature-tour>)_
