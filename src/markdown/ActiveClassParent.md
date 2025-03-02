# ActiveClassParent

&nbsp;

(read only)

&nbsp;

Returns the name of the parent class for the active class. For example, the Load class is a child of power conversion elements (PCE), on the other hand, the Line class is a child of power delivery elements (PDE).

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

myParent = DSSActiveClass.ActiveClassParent; % returns TPCClas indicating that the parent class is PCE

DSSCircuit.SetActiveClass("line")

myParent = DSSActiveClass.ActiveClassParent; % returns TPDClass indicating that the parent class is PCE


***
_Created with the Standard Edition of HelpNDoc: [Create iPhone web-based documentation](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
