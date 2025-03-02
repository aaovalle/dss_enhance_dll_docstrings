# Pmpp

&nbsp;

(read/write)

&nbsp;

This property sets/gets the rated max power of the PV array for 1.0 kW/sq-m irradiance and a user-selected array temperature of the active PVSystem.

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

% Handler for PVSystems interface

DSSPVSystems = DSSObject.PVSystems;

% Sets the first PV in the list active

i = DSSPVSystems.First;

% Gets the nominal pmpp value for the active PV

myPmpp = DSSPVSystems.pmpp;

***
_Created with the Standard Edition of HelpNDoc: [Streamline Your Documentation Process with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
