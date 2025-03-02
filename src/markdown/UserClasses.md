# UserClasses

&nbsp;

(read only)

&nbsp;

This property returns the list of DSS user defined classes (names of the classes).

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

% Gets the names of all the user defined classes

myUClasses = DSSObject.UserClasses;

***
_Created with the Standard Edition of HelpNDoc: [Free Qt Help documentation generator](<https://www.helpndoc.com>)_
