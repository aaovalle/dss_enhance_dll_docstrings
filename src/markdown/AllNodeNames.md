# AllNodeNames

&nbsp;

(read only)

&nbsp;

This property returns an array of strings containing full name of each node in system in same order as returned by AllBusVolts, etc.

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

% Gets the distances for all buses in the model to the parent Energy meter

myNodeDistances = DSSCircuit.AllNodeDistances;

myNodeNames = DSSCircuit.AllNodeNames;

myTable = \[\];

% Creates a table with node names and distances next to each other

for i = 1:size(myNodeNames),

myTable = \[myTable;\[myNodeNames(i),myNodeDistances(1,i)\]\];

end;

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Word Doc into a Professional-Quality eBook with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
