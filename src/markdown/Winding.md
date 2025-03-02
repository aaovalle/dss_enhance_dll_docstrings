# Winding

&nbsp;

(read/write)

&nbsp;

This property sets/gets the number of the winding of the transformer element that the RegControl is monitoring. 1 or 2, typically.&nbsp; Side Effect: Sets TAPWINDING property to the same winding.

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

% Gets the name of the transformer controlled by the active RegControl

myXfmr = DSSRegCtrls.Transformer;

% gets the number of winding monitoring for the transformer controlled by the active RegControl

myWdg = DSSRegCtrls.Winding;


***
_Created with the Standard Edition of HelpNDoc: [Upgrade Your Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
