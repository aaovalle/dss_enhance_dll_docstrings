# ByteStream

&nbsp;

(read only)

&nbsp;

This property returns a Byte Array containing monitor stream values. Make sure a "save" is done first (standard solution modes do this automatically).

&nbsp;

Example

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp('Unable to start openDSS');

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

DSSText = DSSObject.Text;

DSSCircuit = DSSObject.ActiveCircuit;

% Compile a model &nbsp; &nbsp; &nbsp; &nbsp;

DSSText.Command = 'Compile C:\\myPath\\myModel.dss';

DSSMonitors = DSSCircuit.Monitors;

% saves all monitors registers

DSSMonitors.SaveAll();

% select the first monitor on the list

DSSMonitors.First;&nbsp;

%Request the Bytestream

Freqs = DSSMonitors.ByteStream;&nbsp;

% To adjust the matrix

iMonitorDataSize = typecast(Freqs(9:12),'int32');&nbsp;

%Adjusts the content

VIMonitor = typecast(Freqs(273:end),'single');&nbsp;

VIMonitor\_reg = reshape(VIMonitor, iMonitorDataSize+2, \[\])';

% reset all monitors

DSSMonitors.ResetAll();&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Eliminate the Struggles of Documentation with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
