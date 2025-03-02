# Save

&nbsp;

(method)

&nbsp;

This method causes active monitor to save its current sample buffer to its monitor stream. Then you can access the ByteStream or channel data. Most standard solution modes do this automatically.

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

% samples the active monitor

DSSMonitors.Sample();

% saves the active monitor's registers

DSSMonitors.Save();

% select the first monitor on the list

DSSMonitors.First;&nbsp;

%Request the Bytestream

Freqs = DSSMonitors.ByteStream;&nbsp;

% To adjust the matrix

iMonitorDataSize = typecast(Freqs(9:12),'int32');&nbsp;

%Adjusts the content

VIMonitor = typecast(Freqs(273:end),'single');&nbsp;

VIMonitor\_reg = reshape(VIMonitor, iMonitorDataSize+2, \[\])';

% reset the active monitor

DSSMonitors.Reset();&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Documentation with HelpNDoc's Project Analyzer Features](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
