# Delay

&nbsp;

(read/write)

&nbsp;

This property sets/gets the fixed delay time in seconds added to the fuse blowing time determined by the TCC curve. Default is 0.

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

DSSFuses = DSSCircuit.Fuses;

% Selects the first fuse from the list

DSSFuses.First;

% gets the current delay for the active Fuse,

% if 0, sets delay to 1 sec

if DSSFuses.Delay == 0,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; DSSFuses.Delay = 1;

end;

***
_Created with the Standard Edition of HelpNDoc: [5 Reasons Why a Help Authoring Tool is Better than Microsoft Word for Documentation](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
