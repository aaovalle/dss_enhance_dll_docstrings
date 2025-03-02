# OpenDSS Time-based Simulations in Matlab

&nbsp;

**Driving a Time-based Simulation from MATLAB for Custom Calculations and Control**

&nbsp;

The OpenDSS allows other programs to ‘drive’ the simulations and perform custom calculations and control via the program’s COM interface. This documentation is provided to give the reader with a basic understanding for how to drive the OpenDSS using the familiar Matlab program.

&nbsp;

Note that the OpenDSS program is provided in two forms:

&nbsp;

&#49;. OpenDSS.EXE: A stand-alone executable that does not have a COM interface. This is for running the program through text scripts, and for developing and testing scripts.

&nbsp;

&#50;. OpenDSSEngine.DLL: An in-process COM server designed to provide easy access to program features via the COM interface. This module must be registered with the Windows operating system.

&nbsp;

These two forms are functionally equivalent for distribution system analysis. The DLL version lacks some of the features available through the menus of the EXE version. More documentation on the COM interface is available in the ‘doc’ folder that is provided on the Sourceforge.Net website. A direct link to the folder is:

&nbsp;

These two forms are functionally equivalent for distribution system analysis. The DLL version lacks some of the features available through the menus of the EXE version.

&nbsp;

More documentation on the COM interface is available in the ‘doc’ folder that is provided on the Sourceforge.Net website. A direct link to the folder is:

&nbsp;

[http://electricdss.svn.sourceforge.net/viewvc/electricdss/Doc/](<http://electricdss.svn.sourceforge.net/viewvc/electricdss/Doc/>)

&nbsp;

Another document at this site relevant to writing custom control algorithms and interfacing with the OpenDSS through the CtrlQueue interface is

&nbsp;

‘OpenDSS CtrlQueue Interface.doc’.

&nbsp;

This document will outline the steps for running a time-based simulation that performs custom calculations for running a control algorithm. The examples here are for MATLAB. They can be implemented in other programming languages that support connecting to COM interfaces on the Windows platform. Similar algorithms have been developed using VBA in Microsoft Excel and Access and such languages as Python, C#, and Delphi.

&nbsp;

**Step 1: Get a connection to the OpenDSS COM interface and start the OpenDSS**

&nbsp;

First, define some variables and call the DSSStartup function with a directory path name. The DSSStartup function will make this directory the home directory and then start up the OpenDSS.

&nbsp;

%Start up the DSS

global DSSStartOK;

global DSSObj;

global DSSText;

\[DSSStartOK, DSSObj, DSSText\] = DSSStartup(myDir);

&nbsp;

The Matlab function DSSStartUp (below) starts the OpenDSS and provides a handle to the DSS via the Obj variable, which subsequently assigned to the DSSObj variable when the function returns. The function definition for the DSSStartup is shown here:

&nbsp;

function \[Start,Obj,Text\] = DSSStartup(mydir)

% Function for starting up the DSS

% make sure we are in the proper directory

cd(mydir);

%

%instantiate the DSS Object

Obj = actxserver('OpenDSSengine.DSS');

%

%Start the DSS. Without this statement, DSS will not run (gives

%max\_circuit=0 error). Only needs to be executed the first time

w/in a

%Matlab session

% Define the text interface

Start = Obj.Start(0);

Text = Obj.Text;

end

&nbsp;

Note that we’re instantiating the OpenDSSengine.DSS COM server via the Matlab actxvserver function, and then starting the OpenDSS by passing in the value ‘0’ to the Start method. Then we assign the local variable Text, which is returned in the function argument list to the DSSText variable, to the Text Interface of the OpenDSS for passing in text commands.

&nbsp;

**Step 2: Setting up the Time-based Simulation**

&nbsp;

Now that the OpenDSS COM server is running and ready for some circuit definitions or other initial steps, we need to do some ‘setup’ work before getting into the simulation loop itself.

&nbsp;

We have an OpenDSS script that includes all of the objects/classes that we need to define for the circuit on which we’re interested in performing simulations. This is usually a file named ‘master.dss’ that contains such things as a source definition, transformer definitions, line definitions, capacitor definitions, loadshape definitions and load definitions.

&nbsp;

An approach that we took in setting up the master.dss file was to not include any solve statements as we wanted to let the MATLAB code control any solutions as needed. This is not absolutely necessary, but it did allow us more flexibility. The master.dss file does contain a calcvoltagebases statement to set the base voltages. This causes a solution without any Load object or other shunt elements.

&nbsp;

To the code:

&nbsp;

% compile the base circuit which does NOT have a solve in it

DSSCircuit = DSSObj.ActiveCircuit;

result = dss\_Command('compile master.dss');

&nbsp;

First we set the DSSCircuit variable to the ActiveCircuit interface of the DSSObj. At this point, ActiveCircuit is empty because there is no circuit defined. The DSSCircuit variable gives us a handle into the Circuit interface of the OpenDSS COM server for convenience.

&nbsp;

Next, the text statement to compile the master.dss file is passed into the DSSText.Command interface using the dss\_Command function written in the Matlab code. Notice that the result code from the command is retrieved. Generally speaking, if the result code from dss\_Command is anything except 1, we want to exit the MATLAB script. We use the following general code to provide the text of the result to the user and then exit the script:

&nbsp;

% if an error returned from the DSS - return text from the DSS %

%and exit this function with a failure return value

if(result~= 1)

disp(\['Error:' result\])

k = 0;

return

end

&nbsp;

Some commands send a sizeable string back from the DSSText.Result interface, even when the text command is successfully parsed and executed. For example, you can retrieve voltages and currents, etc. through this interface if they are the result of the command. Check the Error interface to distinguish whether an actual error occurred.

&nbsp;

We perform a “snapshot” solve and then assign a variable that will allow us easy access to all of the EnergyMeter objects in the circuit:

&nbsp;

%solve the circuit in snap shot mode

result = dss\_Command('solve mode=snap');

DSSEnergyMeters = DSSCircuit.Meters;

&nbsp;

For a yearly simulation, we set the mode to ‘yearly’ via the text interface, and then, in this example we set the number of solutions per invocation of the Solve command and the interval (or step-size) between solutions using directly using numerical values in the Solution interface. We are telling the OpenDSS that we want only 1 solution for each time that it performs a Solve so that we can interact with the solution before advancing to

the next time step. Note that the stepsize is specified in seconds when using the Solution interface directly:

&nbsp;

result = dss\_Command('set mode = yearly');

DSSCircuit.Solution.Number = 1;

DSSCircuit.Solution.Stepsize = 3600;

&nbsp;

If we were using the Text interface to specify the stepsize, we could have defined it in minutes or hours as well using text strings. The following are equivalent;

&nbsp;

result = dss\_Command('set stepsize=3600');

result = dss\_Command('set stepsize=3600s');

result = dss\_Command('set stepsize=60m');

result = dss\_Command('set stepsize=1.0h');

&nbsp;

For our purposes, we want to get a variety of reports for each time step from the energymeters in the circuit. The following code sets this up:

&nbsp;

%set the case name

result = dss\_Command('set casename=pv\_var\_testing9');

&nbsp;

%set trace control to true

result = dss\_Command('set tracecontrol = yes');

&nbsp;

%we want an overload report

result = dss\_Command('set overloadreport=true');

&nbsp;

%we want a voltage exception report

result = dss\_Command('set voltexceptionreport=true');

&nbsp;

%we want verbose demand interval data

result = dss\_Command('set DIVerbose=true');

&nbsp;

%demand is true

result = dss\_Command('set demand=true');

&nbsp;

The last step before getting into the external solution and control loop, is to set the hour for the first simulation to zero. We can do that by setting the ‘dblHour’ property in the Solutions interface through the following statement:

&nbsp;

DSSCircuit.Solution.dblHour = 0.0;

&nbsp;

The dblHour property is expecting a double-precision floating-point number.

&nbsp;

**Step 3: Time-based Simulation Loop**

&nbsp;

For the time-based simulation that we’re performing we first want to get a solution of the circuit. Since the simulation is in Yearly mode, the loads will follow the yearly Loadshape objects that were defined when the master.dss file was loaded along with definitions of the Load objects and all other circuit elements.

&nbsp;

In our particular loop, we want to run for a certain number of steps. At each step we want to solve the circuit, perform some calculations that are specific to our problem, update some loads or other objects in the circuit definition based on a control algorithm, and repeat the process. The Matlab code for this is shown below:

&nbsp;

while(present\_step \<= num\_pts)

DSSCircuit.Solution.Solve;

&nbsp;

t = sample\_dss\_values(present\_step);

t = do\_custom\_control\_loop();

if (t == 0)

disp('Error running the pv control loop')

k = 0;

return

end

%increment the present step

present\_step = present\_step + 1;

end

result = dss\_Command('CloseDI');

&nbsp;

In more detail, at the top of the loop we first perform a Solve. Recall that we set the mode to ‘Yearly’, so the loads will follow their loadshapes. Had we been in Snapshot mode the loads would not follow their respective loadshapes – they would have been at the defined kW output level at each solve.

&nbsp;

Next, we call a function to sample some values from the OpenDSS solution that are pertinent to our control loop. Based on those values we go into our custom control loop that, in this example, updates reactive power output of some of the loads.

&nbsp;

The custom control loop function does some solutions of its own to iterate on the reactive power output, to set it to a correct value based on the conditions of the circuit. The solutions that the custom control loop performs are “NoControl” solutions. These perform solutions of the circuit, but do not allow any the other OpenDSS control objects to change the state of their controlled object

&nbsp;

We increment the internal (i.e., MATLAB) step counter variable, present\_step. Since we are in Yearly mode, the OpenDSS solution time variable is automatically incremented and the energy meters and monitors sampled each time Solve is executed. Since demand interval metering was turned on, the demand interval files have to be closed by the CloseDI command.


***
_Created with the Standard Edition of HelpNDoc: [Simplify Your Help Documentation Process with a Help Authoring Tool](<https://www.helpauthoringsoftware.com/articles/what-is-a-help-authoring-tool/>)_
