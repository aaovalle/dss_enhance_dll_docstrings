# DSSProgressI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t DSSProgressI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: DSSProgress.PctProgress

This parameter sets the percent progress to indicate \[0..100\].

&nbsp;

### Parameter 1: DSSProgress.Show

This parameter shows progress form with null caption and progress set to zero.

&nbsp;

### Parameter 2: DSSProgress.Close

This parameter closes (hides) DSS Progress form.


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your PDF Protection with These Simple Steps](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
