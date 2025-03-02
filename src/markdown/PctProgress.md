# PctProgress

&nbsp;

(write only)

&nbsp;

This property sets the percent progress to indicate \[0..100\].

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
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with HelpNDoc's Project Analyzer](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
