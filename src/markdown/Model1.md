# Model

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Integer code for the model to use for load variation with voltage. Valid values are:

&nbsp;

&#49; : Standard constant P+jQ load. (Default) (***dssLoadConstPQ***).

&#50; : Constant impedance load. (***dssLoadConstZ***).

&#51; : Const P, Quadratic Q (like a motor). (***dssLoadMotor***).

&#52; : Nominal Linear P, Quadratic Q (feeder mix). Use this with CVRfactor. (***dssLoadCVR***).

&#53; : Constant Current Magnitude. (***dssLoadConstI***).

&#54; : Const P, Fixed Q. (***dssLoadConstPFixedQ***).

&#55; : Const P, Fixed Impedance Q. (***dssLoadConstPFixedX***).

&#56; : ZIPV (7 values). (***dssLoadZIPV***).

&nbsp;

For Types 6 and 7, only the P is modified by load multipliers.

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

% gets the model for the active load

disp(DSSLoads.Model)


***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Output with HelpNDoc's Stunning User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
