# Spectrum

&nbsp;

(read/write)

&nbsp;

This property sets/gets the name of harmonic current spectrum shape (to be used for Harmonic-Harmonic-T simulations). Must be previously defined. Default is "defaultload", which is defined when the DSS starts.

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

% gets the spectrum name for the active load

myOldSpec = DSSLoads.Spectrum;

% Defines a new spectrum

DSSText.Command = 'New "Spectrum.Spectrum\_1" NumHarm=8 CSVFile=Spectrum\_Load\_1.csv' ;

% activates the first load on the list (again)

i = DSSLoads.First;

% Assigns the new spectrum to the active load

DSSLoads.Spectrum = 'Spectrum\_1';

***
_Created with the Standard Edition of HelpNDoc: [Streamline your documentation process with HelpNDoc's HTML5 template](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
