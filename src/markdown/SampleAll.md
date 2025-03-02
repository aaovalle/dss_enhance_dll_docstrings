# SampleAll

&nbsp;

(method)

&nbsp;

This method forces all EnergyMeter objects to take a sample at the present time. Use it when no automatic sampling routines take place, like for example, when using snapshot solution mode.

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

DSSMeters = DSSCircuit.Meters;

% forces all EMs to take a sample

DSSMeters.SampleAll();

***
_Created with the Standard Edition of HelpNDoc: [Powerful and User-Friendly Help Authoring Tool for Markdown Documents](<https://www.helpndoc.com/feature-tour/markdown-import-export-using-helpndoc-help-authoring-tool/>)_
