# Caption

&nbsp;

(write only)

&nbsp;

This property sets the caption to appear on the bottom of the DSS Progress form.

&nbsp;

*Example*

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Unable to start openDSS');

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

% Getting the DSSProgress interface

DSSProgress = DSSObject.DSSProgress;

% Sets the caption of the progress form

DSSProgress.Caption = 'My caption';

***
_Created with the Standard Edition of HelpNDoc: [Qt Help documentation made easy](<https://www.helpndoc.com/feature-tour/create-help-files-for-the-qt-help-framework>)_
