# NextElement

&nbsp;

(read only)

&nbsp;

This method sets the next element of the active class to be the active element in the active circuit. Returns 0 if no more elements..

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

% Sets 'Load' as the active class

DSSCktElement = DSSCircuit.ActiveCktElement;

DSSCircuit.SetActiveClass('Load');

myLoadList = \[\];

% Sets the first load on the list as the active element

i = DSSCircuit.FirstElement;

% Creates an array with the names of all the elements of the active class

while i \> 0,

&nbsp; &nbsp; myLoadList = \[myLoadList;{DSSCktElement.Name}\];

&nbsp; &nbsp; i = DSSCircuit.NextElement;

end;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Create Professional CHM Help Files with HelpNDoc's Easy-to-Use Tool](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
