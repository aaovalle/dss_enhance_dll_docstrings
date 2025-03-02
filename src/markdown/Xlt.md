# Xlt

&nbsp;

(read/write)

&nbsp;

This property sets/gets the percent reactance, L-T (winding 2 to winding 3).&nbsp; Use for 3-winding transformers only. On the kVA base of winding 1. &nbsp;

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

% gets the % reactance 1-2 for the active transformer

myXHL = DSSXfmr.xhl;

% gets the % reactance 1-3 for the active transformer

myXHT = DSSXfmr.xht;

% gets the % reactance 2-3 for the active transformer

myXLT = DSSXfmr.xlt;

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Capabilities with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
