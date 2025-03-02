# AllowForms

&nbsp;

(read/write)

&nbsp;

Default is TRUE. Use this property to set/get the status of the flag to allow forms and dialogs such as progress bars and/or warnings to be displayed during while using OpenDSS.

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

% Checks if form are allowed, if so, disable them

if DSSObject.AllowForms,

&nbsp; &nbsp; DSSObject.AllowForms = false;

end;


***
_Created with the Standard Edition of HelpNDoc: [Bring your WinHelp HLP help files into the present with HelpNDoc's easy CHM conversion](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
