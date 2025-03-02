# Properties

&nbsp;

(read/write)

&nbsp;

This method returns the Collection of properties for Active DSS object (general element or circuit element). The property name has to be specified in the argument. use this method to get the value of a particular property of the active element in case this is not included in the specific interface.

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

DSSLines = DSSCircuit.Lines;

DSSElement = DSSCircuit.ActiveDSSElement;

% Sets The first line of the list as the active element

DSSLines.First;

myLinePhases = DSSElement.Properties('phases').Val;


***
_Created with the Standard Edition of HelpNDoc: [Transform Your Documentation Workflow with HelpNDoc's Intuitive UI](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
