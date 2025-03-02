# Class

&nbsp;

(read/write)

&nbsp;

This property sets/gets a code number used to separate loads by class or group. No effect on the solution.

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

DSSLoads = DSSCircuit.Loads;

% activates the first load on the list

i = DSSLoads.First;

% gets the class for the active load

myClass = DSSLoads.Class;

***
_Created with the Standard Edition of HelpNDoc: [Write eBooks for the Kindle](<https://www.helpndoc.com/feature-tour/create-ebooks-for-amazon-kindle>)_
