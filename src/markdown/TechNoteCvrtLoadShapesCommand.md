# TechNote CvrtLoadShapes Command

&nbsp;

To go along with changes allowing LoadShape objects to be read from binary files of Singles or Doubles, which are approximately 6X faster, this command will write all presently-loaded LoadShape objects to packed binary files of either Singles or Doubles. And the command will produce a script for reading them back in.

&nbsp;

So you can load the LoadShapes once from text scripts or files and save them to binary form for any future use.

&nbsp;

Usually files of singles are adequate precision for loadshapes.

&nbsp;

***Syntax:***

&nbsp;

cvrtloadshapes type=sng (this is the default)

cvrtloadshapes type=dbl

&nbsp;

A DSS script for reloading the loadshapes from the created files is produced and displayed in the default editor. You can insert this script into your original script in place of the script for reading from the text files.

&nbsp;

Note: this won't save you anything if you are changing the LoadShape objects often. You would be better off creating them initially using either SNG or DBL files.

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Productivity with HelpNDoc's CHM Help File Creation Features](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
