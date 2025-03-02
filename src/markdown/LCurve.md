# LCurve

(read/write)

&nbsp;

This property gets/sets the name of the XY curve object describing per-unit variation of phase inductance, L=X/w, vs. frequency for the active reactor in the active circuit.

&nbsp;

Example

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

disp('Unable to start openDSS');

&nbsp; &nbsp; &nbsp; return

end;

DSSText = DSSObject.Text;

DSSCircuit = DSSObject.ActiveCircuit;

DSSSolution = DSSCircuit.Solution;

DSSRc = DSSCircuit.Reactors;

% Compile a model &nbsp; &nbsp; &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSSolution.Solve;

&nbsp;

% gets the number of reactors within the active circuit

NumRX = DSSRc.Count;

&nbsp;

% gets the name of the first reactor in the model (if any)

Idx = DSSRc.First;

myName = DSSRc.Name

&nbsp;

% gets the LCurve of the active reactor

myLCurve = DSSRc.LCurve;

***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
