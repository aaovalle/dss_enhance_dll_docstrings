# NextParam

&nbsp;

(read only)

&nbsp;

This property gets the next token and return tag name (before = sign) if any. See AutoIncrement.

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

&nbsp;

&nbsp;

DSSText.Command = 'compile "C:\\Program Files\\OpenDSS\\EPRITestCircuits\\ckt5\\Master\_ckt5.DSS"';

DSSText.Command = 'set maxiterations=1000 maxcontroliter=1000'; &nbsp; % Just in case

DSSCircuit.Solution.Solve(); % Solves Actor 1

&nbsp;

% sets the string to be parsed

DSSParser.CmdString = set maxcontroliter=100';

% Gets the next token

myToken = DSSParser.NextParam;

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Documentation Workflow with HelpNDoc's Intuitive UI](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
