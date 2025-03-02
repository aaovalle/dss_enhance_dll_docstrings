# BeginQuote

&nbsp;

(read/write)

&nbsp;

This property sets/gets a string containing the the characters for Quoting in OpenDSS scripts. Matching pairs defined in EndQuote. Default is "'(\[{.

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

% Handler for Parser functions

DSSParser = DSSObject.Parser;

% gets the string containing the quoting chars in DSS

myQStr = DSSParser.BeginQuote;

&nbsp;

DSSText.Command = 'compile "C:\\Program Files\\OpenDSS\\EPRITestCircuits\\ckt5\\Master\_ckt5.DSS"';

DSSText.Command = 'set maxiterations=1000 maxcontroliter=1000'; &nbsp; % Just in case

DSSCircuit.Solution.Solve(); % Solves Actor 1

***
_Created with the Standard Edition of HelpNDoc: [Write eBooks for the Kindle](<https://www.helpndoc.com/feature-tour/create-ebooks-for-amazon-kindle>)_
