# Count

&nbsp;

(read only)

&nbsp;

This property returns the number of CapControls defined in the model.

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

DSSCapCtrls = DSSCircuit.CapControls;

% Gets the number of CapControls deployed across the model

myNumCapCtrls &nbsp; &nbsp; =&nbsp; &nbsp; DSSCapCtrls.Count;

***
_Created with the Standard Edition of HelpNDoc: [Create iPhone web-based documentation](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
