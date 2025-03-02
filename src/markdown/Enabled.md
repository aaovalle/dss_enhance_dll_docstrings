# Enabled

&nbsp;

(read/write)

&nbsp;

This property can be used to get/set the enabled flag of the active element, which will be reflected on the circuit model. An disabled element (enabled = False) is removed from the circuit solution, but not removed from memory, which allows to bring it back by changing the status of the element to enabled (enabled = True).

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

&nbsp; &nbsp; % Checks if it's enabled

&nbsp; &nbsp; if DSSActiveElement.Enabled ~= 0,

&nbsp; &nbsp; &nbsp; &nbsp; % If so, disables the line

&nbsp; &nbsp; &nbsp; &nbsp; DSSActiveElement.Enabled = 0;

&nbsp; &nbsp; end;

else&nbsp;

&nbsp; &nbsp; disp('It seems that you have no lines\!');

end;


***
_Created with the Standard Edition of HelpNDoc: [Elevate your documentation to new heights with HelpNDoc's built-in SEO](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
