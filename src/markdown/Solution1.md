# Solution

&nbsp;

This interface can be used to gain access to the simulation options and execution interface. This interface is embedded within the ActiveCircuit interface, requiring the exposure of this interface before getting access to it.

&nbsp;

*Example*

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp("Unable to start openDSS");

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

DSSCircuit = DSSObject.ActiveCircuit;

DSSSolution = DSSCircuit.Solution;

***
_Created with the Standard Edition of HelpNDoc: [Make Documentation a Breeze with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
