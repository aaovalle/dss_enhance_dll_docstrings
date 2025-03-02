# Phases

&nbsp;

(read/write)

&nbsp;

This property sets/gets the number of phases of the active Line code.

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

DSSLineCodes = DSSCircuit.LinesCodes;

% activates the first line code on the list

DSSLineCodes.First;

% Gets number of phases of the active line code

myNPhases = DSSLineCodes.Phases;

***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Help Documentation with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
