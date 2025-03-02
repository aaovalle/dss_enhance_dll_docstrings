# Editing Property Values

&nbsp;

There are two "official" (safe) ways to change a property of an existing DSS object:

&nbsp;

Edit Load.36082264c yearly=Load12\_Phasec .... \[continue setting properties\]

&nbsp;

Or Just give the fully qualified name of the property and its new value

&nbsp;

Load.36082264c.yearly=Load12\_Phasec .... \[continue setting properties\]

&nbsp;

If you were to execute this script statement

&nbsp;

New Load.36082264c yearly=Load12\_Phasec

&nbsp;

And you did not allow duplicates, you will get a warning message and it will replace the presently defined object.

&nbsp;

If you set allowduplicates=Yes, the New command will create another Load object with the same name (and not all essential properties set). This is probably not what you will want.

&nbsp;

The OpenDSS is essentially always in Edit mode. Thus, if Load.36082264c were the active device, you could simply say

&nbsp;

\~ yearly=Load12\_Phasec

&nbsp;

(~ is an alternate for the More command}

Or simply

&nbsp;

\~ yearly=Load12\_Phasec

&nbsp;

However, this is discouraged because

&nbsp;

&#49;. You don't really saving any time and

&#50;. Something might happen and another object becomes active and you end up setting the property of another object.

&nbsp;

Alternatively, you could say

&nbsp;

Edit Load.36082264c

\~ yearly=Load12\_Phasec

&nbsp;

Or

&nbsp;

Select Load.36082264c

\~ yearly=Load12\_Phasec


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly upgrade your WinHelp HLP help files to CHM with HelpNDoc](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-hlp-winhelp-help-file-to-a-chm-html-help-help-file/>)_
