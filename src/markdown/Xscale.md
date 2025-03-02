# Xscale

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Factor to scale X values from original curve.

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

DSSXY = DSSCircuit.XYCurves;

% activate the first XY curve of the list

i = DSSXY.First;

% define new XYCurve

DSSText.Command = 'New XYCurve.SmartInv0 npts=7 xarray=\[0.4 0.86 1 1 1 1.14 1.6\] yarray=\[1 1 0 0 0 -1 -1\]';

% get the X values

myXValues = DSSXY.Xarray;

% get the factor to scale X

myXScaleF = DSSXY.Xscale;

***
_Created with the Standard Edition of HelpNDoc: [HelpNDoc's Project Analyzer: Incredible documentation assistant](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
