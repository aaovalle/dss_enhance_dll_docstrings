# Cmatrix

&nbsp;

(read/write)

&nbsp;

This property sets/gets the nodal Capacitance matrix, lower triangle, nf per unit length for the active line code. Order of the matrix is the number of phases. May be used to specify the shunt capacitance of any line configuration. Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition.&nbsp; For balanced line models, you may use the standard symmetrical component data definition instead.

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

DSSLineCodes = DSSCircuit.LinesCodes;

% activates the first line code on the list

DSSLineCodes.First;

% Gets Cmatrix for the active line code

myCmatrix = DSSLineCodes.Cmatrix;

myCmatrix = reshape(myCmatrix,\[DSSLineCodes.phases,DSSLineCodes.phases\]);

***
_Created with the Standard Edition of HelpNDoc: [Protect Your Confidential PDFs with These Simple Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
