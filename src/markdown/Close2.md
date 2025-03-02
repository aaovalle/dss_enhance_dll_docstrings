# Close

&nbsp;

(method)

&nbsp;

This method closes (hides) DSS Progress form.

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

% Shows the progress form

DSSProgress.Show();

% Sets the caption of the progress form

DSSProgress.Caption = 'My caption';

% Sets the progress pct

DSSProgress.PctProgress = 50;

% Closes the progress form

DSSProgress.Close();


***
_Created with the Standard Edition of HelpNDoc: [Achieve Professional Documentation Results with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
