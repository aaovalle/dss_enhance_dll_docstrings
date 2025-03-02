# PriceCurve

&nbsp;

(read/write)

&nbsp;

This property sets/gets the name of LoadShape object that serves as the source of price signal data for yearly simulations, etc.

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

% get the name of the price curve

myPriceShp = DSSSettings.PriceCurve;

***
_Created with the Standard Edition of HelpNDoc: [Easily Add Encryption and Password Protection to Your PDFs](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
