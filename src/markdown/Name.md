# Name

&nbsp;

(read/write)

&nbsp;

This property is a read/write property that returns the name of the active object within the active class. if assigned, it sets the object specified in the given string as the active object.

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

myElement = DSSActiveClass.Name;&nbsp; %Returns the name of the active object

***
_Created with the Standard Edition of HelpNDoc: [Easily create EBooks](<https://www.helpndoc.com/feature-tour>)_
