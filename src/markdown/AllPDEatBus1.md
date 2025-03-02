# AllPDEatBus

&nbsp;

(read only)

&nbsp;

This property returns the names of all power delivery elements (PDE) connected to the active bus. The names are returned as an array of string.

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

% Sets bus "myBus" as the active Bus

DSSCircuit.SetActiveBus('myBus')

myPDE = DSSActiveBus.AllPDEatBus;

***
_Created with the Standard Edition of HelpNDoc: [Free EPub producer](<https://www.helpndoc.com/create-epub-ebooks>)_
