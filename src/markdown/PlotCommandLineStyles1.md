# Plot Command Line Styles

&nbsp;

&nbsp;

***Setting Line Styles for Circuit Plots***

&nbsp;

As of this writing (see date below) two properties have been added to the Plot command. This applies to version 7.3.3 build 67 and later. The two

properties are

&nbsp;

&#49;phLineStyle

&#51;phLineStyle

&nbsp;

These can be abbreviated 1ph and 3ph if desired.

&nbsp;

Values of these properties can be an integer from 1 to 7 as follows

&nbsp;

&#49; = solid (default for both properties each time the Plot command is issued)

&#50; = dashed

&#51; = dotted (this often looks better than dashed)

&#52; = dashdot

&#53; = dashdotdot

&#54; = clear

&#55; = inside frame

&nbsp;

***Example***

&nbsp;

This example produces the typical power plot with the 1phase lines drawn as dotted lines.

&nbsp;

Plot Circuit Power Max=2000 dots=n labels=n subs=y C1=$00FF0000 1ph=3

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Full-featured Help generator](<https://www.helpndoc.com/feature-tour>)_
