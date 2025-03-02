# Examples

&nbsp;

**Examples**

&nbsp;

The following example will create three actors using a DSS script with the EXE version of OpenDSS. Then, the simulation mode, start time and number of steps is set for each actor. Finally, all the compiled systems are solved concurrently. The system being solved is EPRI’s Ckt5 test circuit.

&nbsp;

clearAll

set parallel=No

&nbsp;

compile "C:\\Program Files\\OpenDSS\\EPRITestCircuits\\ckt5\\Master\_ckt5.dss"

set CPU=0

Solve

&nbsp;

Clone 2

&nbsp;

set parallel=Yes

set activeActor=\*

&nbsp;

set mode=yearly number=2000 totaltime=0

&nbsp;

Set ActiveActor=1

Set hour=0

&nbsp;

set activeActor=2

set hour = 2000

&nbsp;

set activeActor=3

set hour = 4000

&nbsp;

SolveAll

Wait

&nbsp;

set ConcatenateReports=Yes

show monitor MS2

&nbsp;

You need to be careful when organizing OpenDSS parallel scripts – remember that now everything is happening at the same time. If the user wants to see the voltages, export monitors or execute any other “report” command, it is necessary to wait until all the processes are executed. Otherwise, OpenDSS will execute the processes immediately.&nbsp; To have control of the operations that you are performing in the script, you can select the part of the script that you want to execute, and then, by right-clicking with the mouse, select “Do selected” from the pop-up menu as shown in Figure 20.

&nbsp;

![Image](<lib/NewItem138.png>)

Figure 20. Selecting the parts of the script that the user wants to be executed

&nbsp;

&nbsp;

If you want to verify the execution of the solution in terms of CPU allocation after executing the script presented above, execute the windows Resource Monitor ([http://www.digitalcitizen.life/how-use-resource-monitor-windows-7](<https://www.digitalcitizen.life/how-use-resource-monitor-windows-7/> "target=\"\_blank\"")) or the Task Manager. You will be able to check how each system is being solved on a separate CPU. In the case of the example script, the first actor will be executed on CPU 0, the second on CPU 2 and the third on CPU 3. In the performance tab of the Task Manager you will see the utilization of the processors by the different actors when executing the solve command as shown in Figure 21.

&nbsp;

![Image](<lib/NewItem139.png>)\
Figure 21. Processor usage when performing parallel processing with OpenDSS

&nbsp;

As a general recommendation, do not to use all the available CPUs for an OpenDSS simulation Your system can freeze and will not let you to perform other activities in parallel to the simulation.


***
_Created with the Standard Edition of HelpNDoc: [Free iPhone documentation generator](<https://www.helpndoc.com/feature-tour/iphone-website-generation>)_
