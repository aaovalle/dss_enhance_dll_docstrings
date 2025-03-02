# BuildYMatrix

&nbsp;

(method)

&nbsp;

This method sets/gets Forces building of the System Y matrix. This function requires 2 arguments: The first argument is an integer used to specify what elements of the matrix need to be built {1= series elements only \| 2= Whole Y matrix}. The second argument is another integer as well (1 or 0) that indicates DSS to rebuild the V and I vectors used for solving the circuit (1 = Reallocate VI vectors, 0 = Do not Reallocate VI; leave as is).

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

% Rebuild the whole Y matrix

DSSSolution.BuildYMatrix(2,0);

***
_Created with the Standard Edition of HelpNDoc: [Step-by-Step Guide: How to Turn Your Word Document into an eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
