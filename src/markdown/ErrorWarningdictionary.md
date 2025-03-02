# Error/Warning dictionary

&nbsp;

In OpenDSS there are errors and warnings like in any other software application for informing users about inconsistencies when compiling a circuit model. There is a subtle difference between warning and error messages related to the effect they have on the compilation process.&nbsp;

&nbsp;

On one side there are the [error messages](<Errordictionary.md>), these messages highlight critical mistakes that can affect the program stability. Error messages will stop the program's execution and return the error code and explanation back to the user. The user can choose to ignore or abort the script's compilation, however, be thoughtful when doing this since the option for ignoring exceptions must be used only when the user knows what's going on. Otherwise, it is possible to break the application. OpenDSS has a total of 90 error messages across the application.

&nbsp;

On the other side there are the [warning messages](<Warningdictionary.md>). These messages inform about non-standard practices that may not affect the simulation environment (not too bad at lest), but the simulation results and the way an element and/or the whole circuit model. If your mode is not reporting the correct data or something does not look right, think on the last warning message delivered by OpenDSS, that can be the clue. OpenDSS has 719 warning messages across the application.

&nbsp;

Figure 1 illustrates the differences between these 2 types of messages.

&nbsp;

![Image](<lib/NewItem 45.png>)

Figure 1

Features of warning and error messages in OpenDSS


***
_Created with the Standard Edition of HelpNDoc: [Add an Extra Layer of Security to Your PDFs with Encryption](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
