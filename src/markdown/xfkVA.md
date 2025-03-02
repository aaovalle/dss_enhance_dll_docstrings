# xfkVA

&nbsp;

(read/write)

&nbsp;

This property sets/gets the rated kVA of service transformer for allocating loads based on connected kVA at a bus. Side effect:&nbsp; kW, PF, and kvar are modified. See help on kVA. Default = 0.0.&nbsp;

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

% gets the rated kVA of service xfmr for the active load

myXkrmkVA = DSSLoads.xfkVA;

***
_Created with the Standard Edition of HelpNDoc: [Quickly and Easily Convert Your Word Document to an ePub or Kindle eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
