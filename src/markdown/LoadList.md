# LoadList

&nbsp;

(read only)

&nbsp;

This property returns a Variant Array of Strings containing the list of LOAD elements connected to the active bus.&nbsp;

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

myLoads = DSSActiveBus.LoadList;

***
_Created with the Standard Edition of HelpNDoc: [iPhone web sites made easy](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
