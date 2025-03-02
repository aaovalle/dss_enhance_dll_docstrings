# Next

&nbsp;

(read only)

&nbsp;

Sets next element in active class to be the active DSS object. If object is a CktElement, ActiveCktElement also points to this element.&nbsp; Returns 0 if no more.

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

myidx = DSSActiveClass.Next;

***
_Created with the Standard Edition of HelpNDoc: [Easily create Help documents](<https://www.helpndoc.com/feature-tour>)_
