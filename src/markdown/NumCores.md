# NumCores

&nbsp;

(read only)

&nbsp;

This property returns the number of physical Cores at the local PC.

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

% Handler for Parallel processing functions

DSSParallel = DSSCircuit.Parallel; &nbsp; &nbsp;

% Gets the number of physical cores this PC has

myCores = DSSParallel.NumCores; &nbsp; &nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Experience the power of a responsive website for your documentation](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
