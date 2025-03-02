# Bus Coordinates

\
\
If you define the bus coordinates, the OpenDSS can create circuit diagrams like the one below through the Plot Circuit command. See help on the Plot command in the program. Review the [Plot menu commands](<Plot.md>) section in the present current manual for further information.

&nbsp;

![Image](<lib/NewItem34.png>)

&nbsp;

Here is a snippet from the bus coordinate file used to generate this picture :

&nbsp;

N1281316,11894731.7357567,4197454.61149251

N803916,11889166.8368259,4191218.12266468

N803934,11889172.6049164,4191368.65538736

N803973,11889179.3419549,4191671.84618535

N803991,11888721.2904665,4191769.9645205

N804007,11889192.7223036,4191921.63084902

N804035,11888875.825641,4192170.328771

N804041,11888573.6037911,4192204.52313619

N804043,11889387.0172781,4192251.83059776

N804045,11888842.7015518,4192255.4100057

N804048,11889107.2864213,4192321.93050299

N1281316,11894731.7357567,4197454.61149251

N803916,11889166.8368259,4191218.12266468

N803934,11889172.6049164,4191368.65538736

N803973,11889179.3419549,4191671.84618535

N803991,11888721.2904665,4191769.9645205

N804007,11889192.7223036,4191921.63084902

N804035,11888875.825641,4192170.328771

N804041,11888573.6037911,4192204.52313619

N804043,11889387.0172781,4192251.83059776

N804045,11888842.7015518,4192255.4100057

N804048,11889107.2864213,4192321.93050299

&nbsp;

The format for the DSS is simply:

&nbsp;

\< Bus name\>, \<X\>, \<Y\> (one to a line)

&nbsp;

You can use white space instead of commas:

&nbsp;

\< Bus name\> \<X\> \<Y\>

&nbsp;

Then you can simply issue the command:

&nbsp;

Buscoords myfilename.csv

&nbsp;

The DSS does not need graphical bus coordinates to do its basic circuit calculations. You do not have to define bus coordinates. However, if you supply coordinates, it will draw circuit diagrams for you in a multitude of ways. (Some users bypass the DSS facilities and draw their own pictures with R , MATLAB, Excel, or Python using the COM interface in OpenDSSEngine.DLL).

&nbsp;

The only trick is to wait until the OpenDSS has established a bus list before you define the bus coordinates. The bus list does not exist until some action is taken that requires it. If the bus list does not exist, it ignores the definition. I recommend doing this after the first Solve command. You can also issue MakeBusList to force the building of the bus list, but Solve does it too.

&nbsp;

Here is the script that generated the above plot

&nbsp;

Compile (C:\\Projects\\EPRI\\GreenCircuits\\DOMPHEV\_ver2\\Master.dss)

vsource.source.pu=1.05

Solve

Buscoords Buscoords.txt

plot circuit Power max=5000 y n C1=$00FF0000

&nbsp;

You may add or change bus coordinate definitions any time after they are first created.


***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your Documentation Output with HelpNDoc's Stunning User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
