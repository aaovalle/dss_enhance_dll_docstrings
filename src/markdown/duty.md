# duty

&nbsp;

(read/write)

&nbsp;

This property sets/gets the name of the LoadShape for a duty cycle simulation. Must be previously defined as a LoadShape object.&nbsp; Typically would have time intervals less than 1 hr. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.Set to NONE to reset to no LoadShape. Set Status=Fixed to ignore LoadShape designation.&nbsp; Defaults to Daily curve If not specified.

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

% gets the the LoadShape(duty) name for the active load

myOldLoadShape = DSSLoads.duty;

% Defines a new LoadShape

DSSText.Command = 'New Loadshape.MyIrrad npts=24 interval=1 mult=\[0 0 0 0 0 0 .1 .2 .3&nbsp; .5&nbsp; .8&nbsp; .9&nbsp; 1.0&nbsp; 1.0&nbsp; .99&nbsp; .9&nbsp; .7&nbsp; .4&nbsp; .1 0&nbsp; 0&nbsp; 0&nbsp; 0&nbsp; 0\]';

% activates the first load on the list (again)

i = DSSLoads.First;

% Assigns the new LoadShape (duty) to the active load

DSSLoads.duty = 'MyIrrad';

***
_Created with the Standard Edition of HelpNDoc: [Make your documentation accessible on any device with HelpNDoc](<https://www.helpndoc.com/feature-tour/produce-html-websites/>)_
