# CktModel

&nbsp;

(read/write)

&nbsp;

This property sets/gets an integer for indicating if the circuit model is positive sequence {dssMultiphase \* \| dssPositiveSeq}.

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

DSSSettings = DSSCircuit.Settings;

% Check if the active circuit is positive sequence

if DSSSettings.CktModel == 0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('The circuit model is multiphase');

&nbsp; &nbsp; else

disp('The circuit model is positive sequence');

end;

***
_Created with the Standard Edition of HelpNDoc: [Elevate your documentation to new heights with HelpNDoc's built-in SEO](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
