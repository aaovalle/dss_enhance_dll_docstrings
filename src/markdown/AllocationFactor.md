# AllocationFactor

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Allocation factor for allocating loads based on connected kVA at a bus. Side effect:&nbsp; kW, PF, and kvar are modified by multiplying this factor times the XFKVA (if \> 0). Default = 0.5.

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

% gets the allocation factor for the active load

myAllocFactor = DSSLoads.AllocationFactor;

***
_Created with the Standard Edition of HelpNDoc: [Produce electronic books easily](<https://www.helpndoc.com/create-epub-ebooks>)_
