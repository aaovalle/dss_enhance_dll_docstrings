# AllowDuplicates

&nbsp;

(read/write)

&nbsp;

This property sets/gets {True \| False\*}&nbsp; whether to allow duplicate names of objects.

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

&nbsp;

% Checks if the system allows duplicates

if DSSSettings.AllowDuplicates,

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('We accept duplicate names for objects');

else

disp('Sorry, We don't accept duplicate names for objects');

end;

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Word Document into a Professional eBook with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
