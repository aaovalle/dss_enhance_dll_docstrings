# Using Timers in OpenDSS 

&nbsp;

**Time measurement in OpenDSS**

&nbsp;

*Introduction*

&nbsp;

To improve the performance of OpenDSS for Quasi‐Static Time Series (QSTS) simulations project, it has become necessary to add a timer functionality to OpenDSS in order to record the time required for the different segments of the power flow solution. The power flow solution involves three main stages as follows:

&nbsp;

![Image](<lib/NewItem251.png>)

Figure 1. General diagram describing the Power Flow solution in sequential‐time simulations (OpenDSS)

&nbsp;

• The Solution stage: In this stage the program will solve the circuit power flow for one time step. This stage is an iterative stage that will update the injected currents from loads and generators until the circuit solution converges. This stage also includes the control actions performed by the controls such as Inverter controls, capacitor controls, regulators, among others.

&nbsp;

• The Sampling stage: the Solution stage is followed by a routine for sampling the meters and monitors distributed by the user on the circuit. This action involves dynamic memory allocations and disk file I/O. If there are no monitors/meters defined on the circuit this stage should not add much time to the Solution stage.

&nbsp;

• The Simulation stage: This stage contains the both stages described above and includes an iteration counter defined by the parameter number in OpenDSS, which causes OpenDSS to perform the power flow solution and sampling number times as specified by the user. This is how sequential‐time simulations and dynamic simulations are executed.

&nbsp;

These 3 stages report different times since each one incorporates part of the process of the simulation routine. This suggests that it is necessary to have a different timer for each part as shown in Figure 1.

&nbsp;

As can be seen in Figure 1, the sequential‐time solution process has the 3 stages clearly identified. However, the way these are integrated in the algorithm is not the same since stage 3 contains stages 1 and 2. This feature makes it necessary to create 3 different timers for measuring the entire solution process in its different stages.

&nbsp;

The 3 timers created for measuring the time of each stage rely on the windows API to measure the elapsed time based on processor ticks. The tick count is later processed using the processor’s frequency to translate ticks into time units (nanoseconds, microseconds, milliseconds) as needed. The expression used for this translation is as follows:

&nbsp;

![Image](<lib/eq113.png>) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; (1)

&nbsp;

In expression (1) the Initial Time is taken when the process starts and the current time is the time at the moment the calculation is completed. Since the time is in terms of processor ticks these values are absolute and the current time will be always greater that the initial time. After dividing this value by the processors frequency (CPU Freq) the time obtained will be in the lowest time units possible with the processor. Considering that nowadays processor CPU frequencies are expressed in GHz, this unit will be in tenths of a nanosecond.

&nbsp;

To convert this to a more practical time, the results are multiplied by a compensation factor, Mult. The value of this factor can be changed depending on the time units required for this project. For timing QSTS simulations, the most accurate unit for expressing the time required for each stage will be in

microseconds, a time unit that requires mult=1e6.

&nbsp;

The features of each of the 3 timers are described in TABLE I.

&nbsp;

| **Timer Name** | **Stage** | **Access** **privileges** | **Operation** |
| --- | --- | --- | --- |
| ProcessTime | Measures the duration of the Solution Stage | Read only | When the routine for solving the power flow of the circuit in memory is called the initial time is stored in memory, and the current time is the time captured once the power flow solution is found including control actions for the time step. |
| TimeStep | Measures the time after the Sampling Stage | Read only | This is the total time for the time step including solving the power flow and then sampling all the meters and monitors placed on the circuit. |
| TotalTime | Measures the duration of the Simulation Stage | Read/Write | This is the time for solving a QSTS simulation. The initial time is stored in memory, and the current time is captured once the entire simulation is done. This timer includes both stages 1 and 2 (Solution and Sampling). It is also cumulative for multiple simulations until reset to zero in the OpenDSS script. |


&nbsp;

&nbsp;

These timers are available through the multiple interfaces available in OpenDSS (Executable, COM and Direct DLL). Additionally, two of these timers can be captured at each time step using monitors in mode 5. The values of the timers Process Time and Step Time are saved in Monitor channels 12 and 13

(SolveSnap\_uSecs and TimeStep\_uSecs respectively). It is not important where the mode‐5 monitor is placed in the circuit; it is common to put in on the main Vsource. It simply needs to exist when the monitors are sampled. An explanation of how to access the timers in the various forms of OpenDSS

follows:

&nbsp;

**Accessing the timers using the standalone (Executable) interface**

&nbsp;

In the Executable version the user will have access to the timers by using the options ProcessTime, TotalTime and StepTime as follows:

&nbsp;

| Get ProcessTime | \! Returns the value of the time required to solve the most recent circuit solution |
| --- | --- |
| Get StepTime | \! Returns the value of the time required to solve the latest time step + the time \! required for sampling monitors/meters |
| Get TotalTime | \! Returns the value of the Totaltime accumulator, usually for the entire simulation |
| Set TotalTime=0 | \! Sets (initializes) the value of the total simulation time accumulator |


&nbsp;

The return values are display in the Result window, as with all Get commands.

&nbsp;

The following example shows how to query the timers using an OpenDSS script (the file master.dss is the master script of the IEEE 8500 node feeder \[1\]).

&nbsp;

**Example 1**

&nbsp;

Compile (master.dss)

&nbsp;

New Energymeter.m1 Line.ln5815900-1 1

New monitor.SysVars element=Line.ln5815900-1 terminal=1 mode=5 \! This monitor records the timers using a CSV file

Set Maxiterations=20 \! Sometimes the solution takes more than the default 15 iterations

&nbsp;

Set TotalTime=0 \! The total timer is set to 0

&nbsp;

Solve mode=time \!--- this mode automatically samples Monitors and Meters after the 1 snapshot solution

&nbsp;

get ProcessTime \! Request the time required to perform the latest solution without sampling meters

get StepTime \! Request the time required to perform the latest solution including sampling meters

&nbsp;

solve \!--- do another time step

&nbsp;

Export Monitor SysVars

&nbsp;

get TotalTime \! At this point The TotalTime timer will report the time required to perform 2 time steps

&nbsp;

After running this script the user will find a file in the projects folder called IEEE8500\_Mon\_sysvars.csv,bthis file will report the values presented in TABLE II (Columns 7 to 13).

&nbsp;

| **IntervalHrs** | **SolutionCount** | **Mode** | **Frequency** | **Year** | **SolveSnap\_uSecs** | **TimeStep\_uSecs** |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| &#49; | &#55; | &#49;6 | &#54;0 | &#48; | &#51;79324 | &#51;79326 |
| &#49; | &#56; | &#49;6 | &#54;0 | &#48; | &#54;260.87 | &#54;262.73 |


&nbsp;

As can be seen in TABLE II the last two columns of the report show the time required for solving the circuit power flow for the time step in column 12, and then the total time for the time step including the time required for sampling meters in column 13. Using the information provided by these registers it can be inferred that the time required for sampling the existing meters is 2 microseconds, or to be more exact, 1.86 microseconds.

&nbsp;

Additionally, in the results window of OpenDSS will appear the value 385592.9139, which is the value stored in the TotalTime timer and can be calculated by adding the time registered for the TimeStep timer at each simulation step. These values depend on the CPU frequency and can change from one PC

to another according to their characteristics. In this particular case, the computer used was an Intel(R) Core(TM) i5‐5200U CPU @ 2.20GHz.

&nbsp;

**Accessing the update from the COM interface**

&nbsp;

In the COM interface 3 new properties have been included in the Solution Interface: Process\_Time, Time\_of\_Step and Total\_Time. To illustrate the use of these properties using the COM interface the following example is proposed (MATLAB):

&nbsp;

Example 2

&nbsp;

clc;

clear;

\[DSSStartOK, DSSObj, DSSText\] = DSSStartup;

myDir = cd;

if DSSStartOK

DSSText.command = \['Compile (',myDir,'\\master.dss)'\];

DSSText.Command = 'New monitor.SysVars element=Line.ln5815900-1

terminal=1 mode=5';

% Set up the interface variables

DSSCircuit = DSSObj.ActiveCircuit;

DSSSolution = DSSCircuit.Solution;

% Starts simulation

DSSSolution.Total\_Time= 0;

DSSText.Command = 'Set Maxiterations=20';

DSSText.Command = 'Set mode=time';

DSSSolution.Solve;

Time0 = DSSSolution.Process\_Time

Time1 = DSSSolution.Time\_of\_Step

DSSSolution.Solve;

DSSText.command = 'Export Monitors SysVars';

Total\_Time = DSSSolution.Total\_Time

else

a='DSS Did Not Start'

disp(a)

end

&nbsp;

After running the latest script, the results should be very nearly the same as the ones described in section (a). In this case, the time required to solve the first iteration of the simulation are stored at variables Time0 and Time1 for the Process Time and Time Step timers respectively, and the total time for the simulation (Total Time timer) is stored at Total\_Time.

&nbsp;

**Accessing the update from the DIRECT DLL interface**

&nbsp;

In the Direct DLL interface, 4 new parameters have been included in the SolutionF Interface: 24 (Process\_Time), 25 (Total\_Time read), 26 (Total\_Time Write) and 27 (Time\_Step). As in the cases above, the use of these parameters will be illustrated using an example (MATLAB).

&nbsp;

Example 3

&nbsp;

Process\_Time = 24;

Total\_Time\_Read = 25;

Total\_Time\_Write = 26;

Time\_of\_Step = 27;

Start = 3;

Solve = 0;

% Connect to the DLL

%addpath(fullfile(pwd))

myDir = cd;

loadlibrary('OpenDSSDirect.dll',@DEngineProto);

calllib('OpenDSSDirect','DSSI',Start,0);

calllib('OpenDSSDirect','DSSPut\_Command',\['compile (',myDir,'\\master.dss)'\]);

calllib('OpenDSSDirect','DSSPut\_Command','New monitor.SysVars

element=Line.ln5815900-1 terminal=1 mode=5');

calllib('OpenDSSDirect','DSSPut\_Command','set mode=time maxiterations=20');

calllib('OpenDSSDirect','SolutionF',Total\_Time\_Write,0);

calllib('OpenDSSDirect','SolutionI',Solve,0);

Time0 = calllib('OpenDSSDirect','SolutionF',Process\_Time,0)

Time1 = calllib('OpenDSSDirect','SolutionF',Time\_of\_Step,0)

&nbsp;

calllib('OpenDSSDirect','SolutionI',Solve,0);

&nbsp;

calllib('OpenDSSDirect','DSSPut\_Command','Export monitor SysVars');

Total\_Time = calllib('OpenDSSDirect','SolutionF',Total\_Time\_Read,0)

% Disconenct the DLL

unloadlibrary 'OpenDSSDirect'

&nbsp;

The file DEngineProto.m is a prototype file created manually to identify the interfaces of the DLL in MATLAB, this file is provided with the MATLAB example at the OpenDSS website and can be updated manually by the user. The components and interfaces of this DLL are described at the DLL’s user manual.

&nbsp;

**References**

&nbsp;

\[1\] R. F. Arritt and R. C. Dugan, "The IEEE 8500‐node test feeder," in 2010 IEEE PES Transmission and Distribution Conference and Exposition, 2010, pp. 1‐6.&nbsp;

&nbsp;

*Acknowledgement*

&nbsp;

This feature in OpenDSS was requested and funded by the US DOE SuNLaMP project through Sandia National Laboratory and the National Renewable Energy Laboratory to allow comparisons of various techniques to speed up Quasi‐static Time Series (QSTS) simulations in OpenDSS.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Elevate Your Documentation with HelpNDoc's Project Analyzer Features](<https://www.helpndoc.com/feature-tour/advanced-project-analyzer/>)_
