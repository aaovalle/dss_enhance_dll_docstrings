# First

&nbsp;

(read only)

&nbsp;

Sets first element in the active class to be the active DSS object. If object is a CktElement, ActiveCktELment also points to this element. Returns 0 if none.

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

DSSActiveClass = DSSCircuit.ActiveClass;

% Sets class "load" as the active class

DSSCircuit.SetActiveClass("load")

myidx = DSSActiveClass.First;

***
_Created with the Standard Edition of HelpNDoc: [Free EBook and documentation generator](<https://www.helpndoc.com>)_
