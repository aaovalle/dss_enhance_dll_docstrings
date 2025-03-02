# Rho

&nbsp;

(read/write)

&nbsp;

This property sets/gets the earth resistivity used to compute earth correction factor. Overrides Line geometry definition if specified. Default=100 meter ohms. &nbsp;

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

DSSLines = DSSCircuit.Lines;

% activates the first line on the list

DSSLines.First;

% Gets earth resistivity for the active line

myRho = DSSLines.Rho;

***
_Created with the Standard Edition of HelpNDoc: [Transform your help documentation into a stunning website](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
