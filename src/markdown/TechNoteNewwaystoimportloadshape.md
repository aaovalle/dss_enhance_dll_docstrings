# TechNote New ways to import loadshapes

&nbsp;

***Importing Packed Binary Files into Array Properties***

&nbsp;

Capabilities for importing packed files of doubles or singles into floating point array properties have been added.

For example, you can use the following syntax for array properties:

&nbsp;

Mult=\[file=myfile.txt\]

Mult=\[dblfile=myfile.dbl\]

Mult=\[sngfile=mufile.sng\]

&nbsp;

This should speed up the importing of AMI data into Loadshape objects. You can create the .dbl and .sng files with any language that can create packed binary files.

&nbsp;

If you are working with VBA, look at help on the Put \& Get statements. Also, you can use Action property in the Loadshape Object to use OpenDSS to create the dbl and sng files.

&nbsp;

First, you read the loadshape data into the program from text files or just putting the data into a long text array. Then you would issue this command, for example:

&nbsp;

Loadshape.myloadshape.action=sngsave

&nbsp;

This will save the presently defined myloadshape values into

&nbsp;

Myloadshape\_P.sng

&nbsp;

If you defined Qmult, you will also get

&nbsp;

Myloadshape\_Q.sng

&nbsp;

In the Result window, you will get an example script you can use for importing this data in its new format.

&nbsp;

So you can read in your loadshapes one time from text files and save them to files of singles, for example. (Singles are usually sufficent for loadshapes.) Then subsequent simulations should go faster. (Be sure to edit your scripts after the first time.) This should be a big help if loading 8760hr curves for every meter.

&nbsp;

See also TechNote CvrtLoadShapes Command. This command has been added to supplement this capability.

***
_Created with the Standard Edition of HelpNDoc: [Keep Your Sensitive PDFs Safe with These Easy Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
