# pu

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Per unit of the base voltage that the source is actually operating at.

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

DSSVSources = DSSCircuit.VSources;

% Activates the first VSource on the list

k = DSSVSources.First;

% get the number of phases of the active VSource

myNPhases = DSSVSources.Phases;

% get the pu output of the active VSource

myPU = DSSVSources.pu;

***
_Created with the Standard Edition of HelpNDoc: [Elevate Your CHM Help Files with HelpNDoc's Advanced Customization Options](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
