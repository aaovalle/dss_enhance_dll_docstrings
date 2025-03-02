# RdcOhms

&nbsp;

(read/write)

&nbsp;

This property sets/gets the active Winding dc resistance in OHMS. Useful for GIC analysis. From transformer test report. Defaults to 85% of %R property.

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

% gets the RdcOhms for the active transformer

for j = 1:DSSXfmr.NumWindings,

&nbsp; &nbsp; DSSXfmr.Wdg = j;

&nbsp; &nbsp; disp(\['Winding ', num2str(j),' has RdcOhms = ', num2str(DSSXfmr.RdcOhms)\]);

end;

***
_Created with the Standard Edition of HelpNDoc: [Upgrade your help files and your workflow with HelpNDoc's WinHelp HLP to CHM conversion](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
