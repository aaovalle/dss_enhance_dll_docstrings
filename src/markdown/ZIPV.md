# ZIPV

&nbsp;

(read/write)

&nbsp;

This property sets/gets an array of 7&nbsp; doubles with values for ZIPV property of the active load object:

&nbsp;

&nbsp;First 3 are ZIP weighting factors for real power (should sum to 1).

&nbsp;Next 3 are ZIP weighting factors for reactive power (should sum to 1).

&nbsp;Last 1 is cut-off voltage in p.u. of base kV; load is 0 below this cut-off.

&nbsp;No defaults; all coefficients must be specified if using model=8.&nbsp;

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

DSSLoads = DSSCircuit.Loads;

% activates the first load on the list

i = DSSLoads.First;

% gets the ZIPV coefficients for the active load

myZIPV = DSSLoads.ZIPV;

***
_Created with the Standard Edition of HelpNDoc: [Say Goodbye to Documentation Headaches with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
