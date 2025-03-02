# Xneut

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Neutral reactance of wye(star)-connected loads in actual ohms.&nbsp; May be + or -.&nbsp;

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

% gets the neutral reactance for the active load (only if wye)

if ~DSSLoads.IsDelta,

&nbsp; &nbsp; &nbsp; &nbsp; myXN = DSSLoads.Xneut;

else

&nbsp; &nbsp; &nbsp; &nbsp; myXN = 0;

disp(\['Error, load ', DSSLoads.Name, ' is delta connected'\]);

end;


***
_Created with the Standard Edition of HelpNDoc: [Benefits of a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
