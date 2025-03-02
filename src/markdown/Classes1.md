# Classes

&nbsp;

(read only)

&nbsp;

This property returns the list of DSS intrinsic classes (names of the classes).

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

% Gets the names of all the classes included in OpenDSS

myClasses = DSSObject.Classes;

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly optimize your documentation website for search engines](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
