# cmul

&nbsp;

(read/write)

&nbsp;

This property multiplies two complex numbers: (a1, b1) \* (a2, b2). Returns result as a variant array of two doubles.

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

% Loads the complex math lib

DSSCmathLib = DSSObject.CmathLib;

% Multiplies 1 + 2i by 2 + 3i

myResult = DSSCmathLib.cmul(1,2,2,3);

% Converts the array into a complex number

myCmplx = myResult(1) + i\*myResult(2);

***
_Created with the Standard Edition of HelpNDoc: [Don't Let Unauthorized Users View Your PDFs: Learn How to Set Passwords](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
