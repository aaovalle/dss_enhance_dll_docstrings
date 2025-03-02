# OpenDSS LOADSHAPE

&nbsp;

New Ways to Enter Array Data

&nbsp;

To better accommodate large amounts of AMI data, the capability has been added to import packed files of doubles or singles into floating point array properties. For example, you can use the syntax:

&nbsp;

Mult=\[file=myfile.txt\]

Mult=\[dblfile=myfile.dbl\]

Mult=\[sngfile=myfile.sng\]

&nbsp;

This syntax will work on just about any property of any class of element in the OpenDSS where an array of numbers is expected.

&nbsp;

The addition of the capability to handle the two packed binary file types should significantly speed up the importing of AMI data into Loadshape objects. Also, the way the Mean and Std Deviation calculation is done has been changed to delay calculation until these values are actually needed. This should minimize the computing overhead on reading loadshapes back in.

&nbsp;

You can create the .DBL and .SNG files with any language that can create packed binary files. If you are working in VBA, look at Put \& Get. For an example, look for the WriteToSingleFile macro in the SampleDSSDriver.xls file on the SourceForge website.

&nbsp;

However, I also added options to the Action property in the Loadshape Object to allow you to use OpenDSS to create the dbl and sng files. (see the next section)

&nbsp;

To go along with changes allowing LoadShapes to be read from files of Singles and files of Doubles, the CvrtLoadshapes command has been added to write all presently-loaded LoadShape elements to either SNG or DBL files (see description of the command below). And the command will also produce a script for reading them back in. So you can load the LoadShapes once from text scripts or files and save them.

&nbsp;

Note: this won't save you anything if you are changing the LoadShape objects every time you run. You would be better off creating them initially using either SNG or DBL files. In Matlab, use the fwrite statement with the precision for the array:

&nbsp;

fwrite(obj,A,'precision')

&nbsp;

where precision=single or double, etc.

&nbsp;

In Excel VBA, for example:

&nbsp;

Dim sngTemp as Single

Dim X8760(1 to 8760) as Double ‘ Array of multipliers

… (do stuff)

Open MyFileName.sng For Binary Access Write As #1

&nbsp;

For i = 1 To 8760

sngTemp = X8760(i) ' convert double to single

Put #1, , sngTemp ' put it to the binary file

Next i

&nbsp;

Close #

&nbsp;

**Saving Sng or Dbl Files from the Loadshape Element**

&nbsp;

First, you read the LoadShape data into the program from text files or just putting the data into a long array in the OpenDSS script.

&nbsp;

Then you would issue this command, for example, to save a file of singles:

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

Thus, you can read in your loadshapes one time from text files and save them to a file of singles, for example. (Singles are usually sufficient for LoadShape objects). Then subsequent simulations should go faster. (be sure to edit your scripts after the first time). This should be a big help if loading 8760's for every Load.

&nbsp;

**Computing Mean and Std Deviation**

&nbsp;

In previous versions of OpenDSS, the Mean and StdDev properties of any loadshape was computed upon reading the loadshape out of the array definition. In the interest of faster processing, this has been changed so that these values are only computed when the Mean or StdDev property values are requested by some process within OpenDSS. Only a few solution modes, such as Monte Carlo load studies, actually use these so they will be only

rarely computed.

&nbsp;

This should be transparent to the user. If you show the Properties for a LoadShape object, the values are computed.

&nbsp;

**The CvrtLoadshapes Command**

&nbsp;

Issuing this command will cause the OpenDSS two write out all presently-loaded LoadShape Objects to either files of Single or files of doubles as specified.

&nbsp;

cvrtloadshapes type=sng (this is the default)

cvrtloadshapes type=dbl

&nbsp;

A separate file is created for each P and each Q loadshape. The naming should be obvious. The command also creates a script file named ReloadLoadshapes.DSS for reading the loadshapes back in.

&nbsp;

This can create a lot of files. Be sure the present folder is really where you want the files. Of course, you can always move the files later and change the reload script accordingly.

***
_Created with the Standard Edition of HelpNDoc: [Free help authoring tool](<https://www.helpndoc.com/help-authoring-tool>)_
