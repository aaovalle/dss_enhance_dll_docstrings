# ForwardX

&nbsp;

(read/write)

&nbsp;

This property sets/gets the line drop compensator X setting in Volts.

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

DSSRegCtrls = DSSCircuit.RegControls;

% Activates the first RegControl of the list

i = DSSRegCtrls.First;

% Gets the LCD X setting for the active RegControl

myFwX = DSSRegCtrls.ForwardX;

***
_Created with the Standard Edition of HelpNDoc: [Transform your help documentation into a stunning website](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
