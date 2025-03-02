# EndQuote

&nbsp;

(read/write)

&nbsp;

This property sets/gets the String containing characters, in order, that match the beginning quote characters in BeginQuote. Default is "')\]}.

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

% Gets the end quote chars

myEQ = DSSParser.EndQuote;

&nbsp;

DSSText.Command = 'compile "C:\\Program Files\\OpenDSS\\EPRITestCircuits\\ckt5\\Master\_ckt5.DSS"';

DSSText.Command = 'set maxiterations=1000 maxcontroliter=1000'; &nbsp; % Just in case

DSSCircuit.Solution.Solve(); % Solves Actor 1

&nbsp;

% sets the string to be parsed

DSSParser.CmdString = set maxcontroliter=100';

% Gets the next value as double

myCtrlIter = DSSParser.DblValue;

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Capabilities with HelpNDoc's User-Friendly UI](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
