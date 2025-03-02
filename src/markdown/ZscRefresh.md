# ZscRefresh

&nbsp;

(method)

&nbsp;

This method recomputes Zsc for active bus for present circuit configuration.

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

% Refreshes the Zsc for the model using the last solution

DSSActiveBus.ZscRefresh();

***
_Created with the Standard Edition of HelpNDoc: [Write EPub books for the iPad](<https://www.helpndoc.com/create-epub-ebooks>)_
