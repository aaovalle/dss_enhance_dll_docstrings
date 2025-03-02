# Generators

&nbsp;

This interface can be used to gain access to the features of the generators deployed across the circuit model in OpenDSS. This interface is embedded within the ActiveCircuit interface, requiring the definition of this interface before getting access the to Generators interface.

&nbsp;

*Example*

&nbsp;

% Create DSS object

DSSObject = actxserver('OpenDSSEngine.DSS')

if ~DSSObject.Start(0),

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; disp("Unable to start openDSS");

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; return

end;

DSSCircuit = DSSObject.ActiveCircuit;

DSSGen = DSSCircuit.Generators;

***
_Created with the Standard Edition of HelpNDoc: [Converting Word Documents to eBooks: A Step-by-Step Guide with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
