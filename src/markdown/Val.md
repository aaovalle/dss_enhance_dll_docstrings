# Val

&nbsp;

(read/write)

&nbsp;

This property set/get the value of the property. The value must be specified as string.

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

DSSElement = DSSCircuit.ActiveDSSElement;

% Sets The first load of the list as the active element

DSSLoads.First;

% Gets the kW value

mykW = str2num(DSSElement.Properties('kW').Val);

%&nbsp; and increases it 10%

DSSElement.Properties('kW').Val = num2str(mykW \* 1.1);


***
_Created with the Standard Edition of HelpNDoc: [Full-featured EPub generator](<https://www.helpndoc.com/create-epub-ebooks>)_
