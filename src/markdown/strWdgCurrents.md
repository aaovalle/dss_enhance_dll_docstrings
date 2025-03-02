# strWdgCurrents

&nbsp;

(read only)

&nbsp;

This property returns all winding currents in a CSV string corresponding to the floating-point (double) values returned by the WdgCurrents property.

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

DSSXfmr = DSSCircuit.Transformers;

% Activates the first transformer on the list

i = DSSXfmr.First;

% Activates the first winding of the active transformer

DSSXfmr.Wdg = 1;

% gets the Rneut for the active transformer

for j = 1:DSSXfmr.NumWindings,

&nbsp; &nbsp; DSSXfmr.Wdg = j;

&nbsp; &nbsp; disp(\['Winding ', num2str(j),' currents = ', DSSXfmr.strWdgCurrents\]);

end;

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create High-Quality Documentation with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
