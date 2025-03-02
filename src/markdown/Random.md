# Random

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Randomization mode for random variables "Gaussian" or "Uniform". It can be One of \[Uniform \| Gaussian \| Lognormal \| None \] for Monte Carlo Variables.

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

% Set max control iterations to 100

DSSSolution.LoadMult = 100;&nbsp;

% Set max solution iterations to 20

DSSSolution.MaxIterations = 20;&nbsp;

% set simulation mode daily

DSSSolution.Mode = 1;

% Set number to perform only 12 hours

DSSSolution.Number = 12;&nbsp;

&nbsp;

% Solve the model

DSSSolution.Solve();&nbsp;

% shows the name of the random mode

switch DSSSolution.Random

&nbsp; &nbsp; case 0\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('None')\
&nbsp; &nbsp; &nbsp; &nbsp; case 1\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Gaussian')

&nbsp; &nbsp; case 2\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Uniform')\
&nbsp; &nbsp; &nbsp; &nbsp; case 3\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('LogNormal')

&nbsp; &nbsp; otherwise\
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Control mode not identified')\
&nbsp; &nbsp; end

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly bring your documentation online with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
