# Xarray

&nbsp;

(read/write)

&nbsp;

This property sets/gets the X values as a Variant array of doubles. Set Npts to max number expected if setting.

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

% define new XYCurve

DSSText.Command = 'New XYCurve.SmartInv0 npts=7 xarray=\[0.4 0.86 1 1 1 1.14 1.6\] yarray=\[1 1 0 0 0 -1 -1\]';

% activate the first XY curve of the list

i = DSSXY.First;

% get the X values

myXValues = DSSXY.Xarray;

% Set the X values

B = \[0.5 0.86 1 1 1 1.14 1.6\];

B = B';&nbsp; &nbsp; % transpose

feature('COM\_SafeArraySingleDim',1);&nbsp; % enable this setting for allow MATLAB to export the array properly

DSSXY.Xarray=B;

feature('COM\_SafeArraySingleDim',0);&nbsp; % Goes back to normal

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Free iPhone documentation generator](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
