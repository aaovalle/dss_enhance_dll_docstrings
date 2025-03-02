# ParentPDElement

&nbsp;

(read only)

&nbsp;

This property sets Parent PD element, if any, to be the active circuit element and returns index\>0; Returns 0 if it fails or not applicable..

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

DSSElement = DSSCircuit.ActiveCktElement;

% Sets the first PDE on the list as the active element

i = DSSCircuit.FirstPDElement;

% Sets the next PDE on the list as the active element

i = DSSCircuit.NextPDElement;

% Activates the parentPDE

i = DSSCircuit.ParentPDElement;

if i ~= 0,

&nbsp; &nbsp; myParent = DSSElement.Name;

end;

&nbsp;

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Import and export Markdown documents](<https://www.helpndoc.com/feature-tour/markdown-import-export-using-helpndoc-help-authoring-tool/>)_
