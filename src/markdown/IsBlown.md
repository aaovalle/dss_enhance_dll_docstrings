# IsBlown

&nbsp;

(Method)

&nbsp;

This method returns the current state of the fuses. TRUE if any fuse on any phase is blown. Else FALSE..

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

% Checks if the fuse is blown

if DSSFuses.IsBlown(),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('The fuse is blown');

end;

***
_Created with the Standard Edition of HelpNDoc: [Free iPhone documentation generator](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
