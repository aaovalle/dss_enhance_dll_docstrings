# Frequency

&nbsp;

(read/write)

&nbsp;

This property sets/gets the active VSource Frequency in Hz.

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

% get the freq of the active VSource

myFreq = DSSVSources.Frequency;

***
_Created with the Standard Edition of HelpNDoc: [Free help authoring tool](<https://www.helpndoc.com/help-authoring-tool>)_
