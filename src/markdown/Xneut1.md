# Xneut

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Neutral reactance of wye (star)-connected winding in actual ohms.&nbsp; May be + or -. See the help for the Rneut property.&nbsp; If Rneut=-1, the neutral is assumed to be open (floating) unless it is connected to a node by the Bus definition.

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

% gets the neutral reactance for the active transformer

myXNeut = DSSXfmr.Xneut;

***
_Created with the Standard Edition of HelpNDoc: [Upgrade Your Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
