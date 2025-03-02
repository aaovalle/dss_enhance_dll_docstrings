# Yshift

&nbsp;

(read/write)

&nbsp;

This property sets/gets the amount to shift Y value from original curve.

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

% set value X in 1.13

DSSXY.x = 1.13;

% get the Y value corresponding to X

myY = DSSXY.y;

% get the Y values

myYValues = DSSXY.Yarray;

% get the factor to scale y

myYScaleF = DSSXY.Yscale;

% get Y shift

myYShift = DSSXY.Yshift;

***
_Created with the Standard Edition of HelpNDoc: [Produce Kindle eBooks easily](<https://www.helpndoc.com/feature-tour/create-ebooks-for-amazon-kindle>)_
