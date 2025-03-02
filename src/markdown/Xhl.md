# Xhl

&nbsp;

(read/write)

&nbsp;

This property sets/gets the percent reactance, H-L (winding 1 to winding 2).&nbsp; Use for 2- or 3-winding transformers. On the kVA base of winding 1.&nbsp;

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

&nbsp;

% gets the name of the XfmrCode for the active transformer (if any)

myXfmrCode = DSSXfmr.XfmrCode;

% gets the % reactance for the active transformer

myXHL = DSSXfmr.xhl;

***
_Created with the Standard Edition of HelpNDoc: [Experience the Power and Ease of Use of HelpNDoc for CHM Help File Generation](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
