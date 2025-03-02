# ShowPanel

&nbsp;

(write only)

&nbsp;

This method shows non-MDI child form of the Main DSS Edit Form.

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

% Shows the non-MDI form

DSSObject.ShowPanel();


***
_Created with the Standard Edition of HelpNDoc: [Easy EBook and documentation generator](<https://www.helpndoc.com>)_
