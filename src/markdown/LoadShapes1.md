# LoadShapes

&nbsp;

This interface can be used to gain access to the features of the Load shapes (LoadShapes) used for describing the behavior in time of Power Conversion Elements (PCE) and controllers in the model. LoadShapes can be used to define the features of multiple PCE across the model.&nbsp;

This interface is embedded within the ActiveCircuit interface, requiring the definition of this interface before getting access the to LoadShapes interface.

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

DSSLoadShapes = DSSCircuit.LoadShapes;

***
_Created with the Standard Edition of HelpNDoc: [Eliminate the Struggles of Documentation with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
