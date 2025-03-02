# daily

&nbsp;

(read/write)

&nbsp;

This property sets/gets the name of the loadShape for a daily load profile (to be used in daily simulations). Must be previously defined as a LoadShape object of 24 hrs, typically. Set Status=Fixed to ignore LoadShape designation. Set to NONE to reset to no loadShape. Default is no variation (constant) if not defined. Side effect: Sets Yearly load shape if not already defined.

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

% gets the LoadShape name for the active load

myOldLoadShape = DSSLoads.daily;

% Defines a new LoadShape

DSSText.Command = 'New Loadshape.MyIrrad npts=24 interval=1 mult=\[0 0 0 0 0 0 .1 .2 .3&nbsp; .5&nbsp; .8&nbsp; .9&nbsp; 1.0&nbsp; 1.0&nbsp; .99&nbsp; .9&nbsp; .7&nbsp; .4&nbsp; .1 0&nbsp; 0&nbsp; 0&nbsp; 0&nbsp; 0\]';

% activates the first load on the list (again)

i = DSSLoads.First;

% Assigns the new LoadShape to the active load

DSSLoads.daily = 'MyIrrad';

***
_Created with the Standard Edition of HelpNDoc: [Transform Your Documentation Workflow with HelpNDoc's Intuitive UI](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
