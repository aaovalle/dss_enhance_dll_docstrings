# AllElementLosses

&nbsp;

(read only)

&nbsp;

This property returns an array of total losses (complex) in each circuit element.

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

% Gets the losses for all the elements in the model

myElementNames = DSSCircuit.AllElementNames;

myELosses = DSSCircuit.AllElementLosses;

mySize = size(myELosses);

myPairs = \[\];

% Sorts the losses in pairs (P,Q)

for i = 1:2:(mySize(2) - 1),

myPairs = \[myPairs;\[myELosses(i),myELosses(i + 1)\]\];

end; &nbsp;

% Links the element's name to the losses

myLosses = \[\];

for i = 1:size(myElementNames),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; myLosses = \[myLosses;\[myElementNames(i),num2str(myPairs(i,1)),num2str(myPairs(i,2))\]\];

end;


***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
