# SaveSample

&nbsp;

(method)

&nbsp;

This method forces all meters and monitors to save their current buffers.

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

% Solves the circuit in snap mode (meters and monitors don't sample automatically)

DSSText.Command = 'Solve mode=snap';

% Forces meters and monitor to take a sample

DSSCircuit.Sample();

% Forces meters and monitor to save their current buffers

DSSCircuit.SaveSample();

***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Output with HelpNDoc's Stunning User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
