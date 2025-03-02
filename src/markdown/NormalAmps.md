# NormalAmps

&nbsp;

(read/write)

&nbsp;

This property can be used to get/set the Normal Ampere Rating for the active element (if it is a PD element).

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

DSSLines = DSSCircuit.Lines;

% Compile a model &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSActiveElement = DSSCircuit.ActiveCktElement;

% Sets the first line of the list as the active element

if DSSLines.First \> 0,

&nbsp; &nbsp; % gets the normal amp rating of the active line

&nbsp; &nbsp; disp(num2str(DSSActiveElement.NormAmps));

else&nbsp;

&nbsp; &nbsp; disp('It seems that you have no lines\!');

end;

***
_Created with the Standard Edition of HelpNDoc: [Experience the power of a responsive website for your documentation](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
