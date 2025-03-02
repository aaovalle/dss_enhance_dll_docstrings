# ParentPDElement

&nbsp;

(read only)

&nbsp;

This property sets the parent PD element of the active PDE element to be the active circuit element.&nbsp; Returns 0 if no more elements up-line.

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

% Handler for PDelements interface

DSSPDE = DSSObject.PDElements;

% Activates the first PDE on the list

i = DSSPDE.First;

% gets the name of the active PDE

myName = DSSPDE.Name;

% Activates the parent PDE of the active PDE as the active element

myIdx = DSSPDE.ParentPDElement;

if DSSPDE.ParentPDElement == 0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp(\['No Parent PDE for ', myName\]);

end;

***
_Created with the Standard Edition of HelpNDoc: [Make Documentation a Breeze with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
