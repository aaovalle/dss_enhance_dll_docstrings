# IsZ1Z0

&nbsp;

(read only)

&nbsp;

Invoking this property returns a flag denoting whether impedance data were entered in symmetrical components.

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

i = DSSLineCodes.First;

% Checks if the impedance data was entered in symm components

if DSSLineCodes.IsZ1Z0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('The impedance data was entered in symmetrical components');

else

&nbsp; &nbsp; disp('The impedance data was not entered in symmetrical components');

end;

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly create a professional-quality documentation website with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
