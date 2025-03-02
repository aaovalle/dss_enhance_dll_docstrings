# LoadMult

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Default load multiplier applied to all non-fixed loads. Does not affect loads designated to be "fixed".&nbsp; All other base kW values are multiplied by this number. Defaults to 1.0 when the circuit is created. As with other values, it always stays at the last value to which it was set until changed again.

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

% Set load multiplier 1.1

DSSSolution.LoadMult = 1.1;&nbsp;

&nbsp;

% Solve the model

DSSSolution.Solve();&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Easily share your documentation with the world through a beautiful website](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
