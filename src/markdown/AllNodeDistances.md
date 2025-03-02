# AllNodeDistances

&nbsp;

(read only)

&nbsp;

This property returns an array of distances from parent EnergyMeter for each Node. Corresponds to AllBusVMag sequence.

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
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Simplicity of HelpNDoc's User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
