# LoadModel

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Load Model: {dssPowerFlow (default) \| dssAdmittance}.

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

DSSSolution = DSSCircuit.Solution;

&nbsp;

% Solve the model

DSSSolution.Solve();&nbsp;

% gets the load model

if DSSSolution.LoadModel == 1,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Power flow model');

else

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Admittance model');

end; 
***
_Created with the Standard Edition of HelpNDoc: [Produce online help for Qt applications](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
