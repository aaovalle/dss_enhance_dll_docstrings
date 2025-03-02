# N_interrupts

&nbsp;

(read only)

&nbsp;

This property returns the Number of interruptions per year for the active bus.

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

myNInterrupt = DSSActiveBus.N\_Interrupts;

***
_Created with the Standard Edition of HelpNDoc: [Produce online help for Qt applications](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
