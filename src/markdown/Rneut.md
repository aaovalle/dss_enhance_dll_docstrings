# Rneut

&nbsp;

(read/write)

&nbsp;

This property sets/gets the neutral resistance if the active load is wye-connected. Default = 1. Used to designate high priority loads such as hospitals, etc. Is multiplied by number of customers and load kW during reliability calculations. If entered as a negative value, the neutral can be open, or floating, or it can be connected to node 0 (ground), which is the usual default. If \>=0 be sure to explicitly specify the node connection for the neutral, or last, conductor. Otherwise, the neutral impedance will be shorted to ground.

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

% gets the neutral resistance for the active load

myRN = DSSLoads.Rneut;

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Documentation Capabilities with a Help Authoring Tool](<https://www.helpauthoringsoftware.com>)_
