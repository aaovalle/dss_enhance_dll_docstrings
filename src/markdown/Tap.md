# Tap

&nbsp;

(read/write)

&nbsp;

This property sets/gets the active Winding tap in per-unit of the active transformer.

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

DSSXfmr = DSSCircuit.Transformers;

% Activates the first transformer on the list

i = DSSXfmr.First;

% Activates the first winding of the active transformer

DSSXfmr.Wdg = 1;

% gets the Rneut for the active transformer

for j = 1:DSSXfmr.NumWindings,

&nbsp; &nbsp; DSSXfmr.Wdg = j;

&nbsp; &nbsp; disp(\['Winding ', num2str(j),' Tap = ', num2str(DSSXfmr.Tap)\]);

end;


***
_Created with the Standard Edition of HelpNDoc: [Full-featured Kindle eBooks generator](<https://www.helpndoc.com/feature-tour/create-ebooks-for-amazon-kindle>)_
