# Reset

&nbsp;

(Method)

&nbsp;

This method resets the fuse to its normal state.

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

DSSFuses = DSSCircuit.Fuses;

% Selects the first fuse from the list

DSSFuses.First;

% Resets the active fuse

DSSFuses.Reset();

***
_Created with the Standard Edition of HelpNDoc: [Easily create iPhone documentation](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
