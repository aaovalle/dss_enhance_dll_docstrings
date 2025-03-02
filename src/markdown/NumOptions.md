# NumOptions

&nbsp;

(read only)

&nbsp;

This property returns the Number of DSS Executive Options (preceded by&nbsp; 'set').

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

DSSExecutive = DSSObject.Executive;

% Returns the number of options

NumCmd = DSSExecutive.NumOptions;

***
_Created with the Standard Edition of HelpNDoc: [Easily share your documentation with the world through a beautiful website](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
