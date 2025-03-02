# Algorithm

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Base Solution algorithm: {dssNormalSolve \| dssNewtonSolve}.

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

% Check solution algorithm

if DSSSolution.Algorithm == 0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mySolver = 'Normal';

&nbsp; &nbsp; else

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; mySolver = 'Newton';

end;

disp(\['Active solver: ', mySolver\]);

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly create a professional-quality documentation website with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
