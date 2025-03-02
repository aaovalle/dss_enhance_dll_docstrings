# ParallelI (Integer) Interface

&nbsp;

This interface allows to control parameters of the parallel computing suite of OpenDSS-PM where its value can be specified as an integer number. The structure of the interface is as follows:

&nbsp;

int32\_t ParalleI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer number with the result of the query according to the value of the variable Parameter, which can be one of the following:

&nbsp;

### Parameter 0: Parallel.NumCPUs 

This parameter returns the number of CPUs available in the local computer.

&nbsp;

### Parameter 1: Parallel.NumCores

This parameter returns the number of physical cores available in the local computer. If your computer has less than 64 Cores, this number should be the number of CPUs/2. For more information, please check: https://www.howtogeek.com/194756/cpu-basics-multiple-cpus-cores-and-hyper-threading-explained/.

&nbsp;

### Parameter 2: Parallel.ActiveActor read

This parameter returns the ID of the active actor.

&nbsp;

### Parameter 3: Parallel.ActiveActor write

This parameter sets the ID of the active actor; this number cannot be higher than the number of existing actors.

&nbsp;

### Parameter 4: Parallel.CreateActor

This parameter creates a new actor and sets the active actor ID as the ID for the recently created actor. If there are no more CPUs available, the system will not allow the creation of the new actor

&nbsp;

### Parameter 5: Parallel.ActorCPU read

This parameter gets the ID of the CPU assigned for the execution of the active actor.

&nbsp;

### Parameter 6: Parallel.ActorCPU write

This parameter sets the CPU for the execution of the active actor.

&nbsp;

### Parameter 7: Parallel.NumActors

This parameter gets the number of actors created in the actual session.

&nbsp;

### Parameter 8: Parallel.Wait

This parameter waits until all the actors are free and ready to receive a new command. 

&nbsp;

### Parameter 9: Parallel.ActiveParallel read

This parameter gets if the parallel features of OpenDSS are active. If active, this parameter will return 1, otherwise, will return 0 and OpenDSS-PM will behave sequentially.

&nbsp;

### Parameter 10: Parallel.ActiveParallel write

This parameter enables/disables the parallel features of OpenDSS. To enable set the argument in 1, otherwise, the argument should be 0 and OpenDSS-PM will behave sequentially.

&nbsp;

### Parameter 11: Parallel.ConcatenateReports Read

This parameter gets the state of the ConcatenateReports property of OpenDSS-PM. If 1, means that every time the user executes a Show/Export monitor operation, the data stored on the monitors with the same name for each actor will be concatenated one after the other. Otherwise (0), to get access of each monitor the user will have to activate the actor of interest and then perform the Show/Export command on the desired monitor.

&nbsp;

### Parameter 12: Parallel.ConcatenateReports Write

This parameter sets the state of the ConcatenateReports property of OpenDSS-PM. If 1, means that every time the user executes a Show/Export monitor operation, the data stored on the monitors with the same name for each actor will be concatenated one after the other. Otherwise (0), to get access of each monitor the user will have to activate the actor of interest and then perform the Show/Export command on the desired monitor.

***
_Created with the Standard Edition of HelpNDoc: [Make CHM Help File Creation a Breeze with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
