# Zmag

&nbsp;

(read/write)

&nbsp;

This property sets/gets the value of impedance value associated with the DoShortLines method. Lines with less impedance will be merged out of the circuit, eliminating one or more buses.

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

DSSReduceCkt = DSSCircuit.ReduceCkt;

DSSLines = DSSCircuit.Lines;

% activates the first line on the list

i = DSSLines.First;

myLine = DSSLines.Name

&nbsp;

% set the PDE name for the reduction

DSSReduceCkt.StartPDElement = myLine;

% breaks loops first

DSSReduceCkt.DoLoopBreak();

% merge parallel lines

DSSReduceCkt.DoParallelLines();

% get the Zmag

disp(\['Zmag: ', num2str(DSSReduceCkt.Zmag())\]);

% reduce short lines

DSSReduceCkt.DoShortLines();

&nbsp;

% get the OpenDSS command

myStr = DSSReduceCkt.EditString;

***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create Professional Documentation with HelpNDoc's Clean UI](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
