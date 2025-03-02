# Option

&nbsp;

(read only)

&nbsp;

This property returns the Get i-th option. The index must be entered in the argument.

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

% Returns the option specified by index

myOp = DSSExecutive.Option(1);

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly bring your documentation online with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
