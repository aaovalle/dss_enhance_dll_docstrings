# SetActiveBusi

&nbsp;

(write only)

&nbsp;

This method sets ActiveBus by Integer value.&nbsp; 0-based index compatible with SetActiveBus return value and AllBusNames indexing. Returns 0 if OK.

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

% Sets the first bus of the list as the active bus

DSSCircuit.SetActiveBusi(1);

***
_Created with the Standard Edition of HelpNDoc: [Revolutionize your documentation process with HelpNDoc's online capabilities](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
