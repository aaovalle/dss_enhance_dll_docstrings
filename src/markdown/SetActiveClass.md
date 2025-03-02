# SetActiveClass

&nbsp;

(write only)

&nbsp;

This method sets the active class by name.&nbsp; Use FirstElement, NextElement to iterate through the class. Returns -1 if fails.

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

% Sets class 'Load' as the active class

i = DSSCircuit.SetActiveClass('Load');

% verify if the class exists

if i \< 0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('The class does not exist');

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

***
_Created with the Standard Edition of HelpNDoc: [Make your documentation accessible on any device with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
