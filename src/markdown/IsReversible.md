# IsReversible

&nbsp;

(read/write)

&nbsp;

This property sets/gets if the regulator can use different settings in the reverse direction.&nbsp; Usually not applicable to substation transformers.

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

% Checks if the active RegControl is reversible, if not, makes it reversible

myIsRev = DSSRegCtrls.IsReversible;

if ~DSSRegCtrls.IsReversible,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; DSSRegCtrls.IsReversible = true;

end;

***
_Created with the Standard Edition of HelpNDoc: [Upgrade Your Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
