# Yarray

&nbsp;

(read/write)

&nbsp;

This property sets/gets the Y values in curve; Set Npts to max number expected if setting.

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
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create Professional Documentation with HelpNDoc's Clean UI](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
