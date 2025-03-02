# SolutionI (Int) Interface

&nbsp;

This interface can be used to read/write certain properties of the active DSS object. The structure of the interface is as follows:

&nbsp;

int32\_t SolutionI(int32\_t Parameter, int32\_t Argument);

&nbsp;

This interface returns an integer according to the number sent in the variable “parameter”. The parameter can be one of the following:

&nbsp;

### Parameter 0: Solution.Solve

Executes the solution for the present solution mode. Returns 0.

&nbsp;

### Parameter 1: Solution.Mode - Read

This parameter returns the present solution mode (See DSS help).

&nbsp;

### Parameter 2: Solution.Mode - Write

This parameter modifies the present solution mode (See DSS help).

&nbsp;

### Parameter 3: Solution.hour - Read

This parameter returns the present hour (See DSS help).

&nbsp;

### Parameter 4: Solution.hour - Write

This parameter modifies the present hour (See DSS help).

&nbsp;

### Parameter 5: Solution.Year - Read

This parameter returns the present Year (See DSS help).

&nbsp;

### Parameter 6: Solution.Year - Write

This parameter modifies the present Year (See DSS help).

&nbsp;

### Parameter 7: Solution.Iterations

This parameter returns the number of iterations taken for the last solution.

&nbsp;

### Parameter 8: Solution.MaxIterations - Read

This parameter returns the Maximum number of iterations used to solve the circuit.

&nbsp;

### Parameter 9: Solution.MaxIterations - Write

This parameter modifies the Maximum number of iterations used to solve the circuit.

&nbsp;

### Parameter 10: Solution.Number - Read

This parameter returns the number of solutions to perform for MonteCarlo and time series simulations.

&nbsp;

### Parameter 11: Solution.Number - Write

This parameter modifies the number of solutions to perform for MonteCarlo and time series simulations.

&nbsp;

### Parameter 12: Solution.Random - Read

This parameter returns the randomization mode for random variables "Gaussian" o "Uniform".

&nbsp;

### Parameter 13: Solution.Random - Write

This parameter modifies the randomization mode for random variables "Gaussian" o "Uniform".

&nbsp;

### Parameter 14: Solution.LoadModel - Read

This parameter returns the Load Model: {dssPowerFlow (default)\|dssAdmittance}.

&nbsp;

### Parameter 15: Solution.LoadModel - Write

This parameter modifies the Load Model: {dssPowerFlow (default)\|dssAdmittance}.

&nbsp;

### Parameter 16: Solution.AddType - Read

This parameter returns the type of device to add in AutoAdd Mode: {dssGen (default)\|dssCap}.

&nbsp;

### Parameter 17: Solution.AddType - Write

This parameter modifies the type of device to add in AutoAdd Mode: {dssGen (default)\|dssCap}.

&nbsp;

### Parameter 18: Solution.Algorithm - Read

This parameter returns the base solution algorithm: {dssNormalSolve \| dssNewtonSolve}.

&nbsp;

### Parameter 19: Solution.Algorithm - Write

This parameter modifies the base solution algorithm: {dssNormalSolve \| dssNewtonSolve}.

&nbsp;

### Parameter 20: Solution.ControlMode - Read

This parameter returns the mode for control devices: {dssStatic (default) \| dssEvent \| dssTime}.

&nbsp;

### Parameter 21: Solution.ControlMode - Write

This parameter modifies the mode for control devices: {dssStatic (default) \| dssEvent \| dssTime}.

&nbsp;

### Parameter 22: Solution.ControlIterations - Read

This parameter returns the current value of the control iteration counter.

&nbsp;

### Parameter 23: Solution.ControlIterations - Write

This parameter modifies the current value of the control iteration counter.

&nbsp;

### Parameter 24: Solution.MaxControlIterations - Read

This parameter returns the maximum allowable control iterations.

&nbsp;

### Parameter 25: Solution.MaxControlIterations - Write

This parameter modifies the maximum allowable control iterations.

&nbsp;

### Parameter 26: Solution.Sample\_DoControlActions

This parameter sample controls and then process the control queue for present control mode and dispatch control actions. Returns 0.

&nbsp;

### Parameter 27: Solution.CheckFaultStatus

This parameter executes status check on all fault objects defined in the circuit. Returns 0.

&nbsp;

### Parameter 28: Solution.SolveDirect

This parameter executes a direct solution from the system Y matrix, ignoring compensation currents of loads, generators (includes Yprim only).

&nbsp;

### Parameter 29: Solution.SolvePflow

This parameter solves using present power flow method. Iterative solution rather than direct solution.

&nbsp;

### Parameter 30: Solution.SolveNoControl

This parameter is similar to SolveSnap except no control actions are checked or executed.

&nbsp;

### Parameter 31: Solution.SolvePlusControl

This parameter executes a power flow solution (SolveNoControl) plus executes a CheckControlActions that executes any pending control actions.

&nbsp;

### Parameter 32: Solution.InitSnap

This parameter initializes some variables for snap shot power flow. SolveSnap does this automatically.

&nbsp;

### Parameter 33: Solution.CheckControls

This parameter performs the normal process for sampling and executing Control Actions and Fault Status and rebuilds Y if necessary.

&nbsp;

### Parameter 34: Solution.SampleControlDevices

This parameter executes a sampling of all intrinsic control devices, which push control actions into the control queue.

&nbsp;

### Parameter 35: Solution.DoControlActions

This parameter pops control actions off the control queue and dispatches to the proper control element.

&nbsp;

### Parameter 36: Solution.BuildYMatrix

This parameter forces building of the System Y matrix according to the argument: {1= series elements only \| 2= Whole Y matrix}.

&nbsp;

### Parameter 37: Solution.SystemYChanged

This parameter indicates if elements of the System Y have been changed by recent activity. If changed returns 1; otherwise 0.

&nbsp;

### Parameter 38: Solution.Converged - Read

This parameter indicates whether the circuit solution converged (1 converged \| 0 not converged).

&nbsp;

### Parameter 39: Solution.Converged - Write

This parameter modifies the converged flag (1 converged \| 0 not converged).

&nbsp;

### Parameter 40: Solution.TotalIterations

This parameter returns the total iterations including control iterations for most recent solution.

&nbsp;

### Parameter 41: Solution.MostIterationsDone

This parameter returns the max number of iterations required to converge at any control iteration of the most recent solution.

&nbsp;

### Parameter 42: Solution.ControlActionsDone - Read

This parameter indicates that the control actions are done: {1 done, 0 not done}.

&nbsp;

### Parameter 43: Solution.ControlActionsDone - Write

This parameter modifies the flag to indicate that the control actions are done: {1 done, 0 not done}.

&nbsp;

### Parameter 44: Solution.FinishTimeStep

This parameter calls cleanup, sample monitors, and increment time at end of time step.

&nbsp;

### Parameter 45: Solution.Cleanup

This parameter update storage, invcontrol, etc., at end of time step.

&nbsp;

### Parameter 46: Solution.SolveAll

This parameter starts the solution process for all the actors created in memory. Please be sure that the circuits of each actor have been compiled and ready to be solved before using this command.

&nbsp;

### Parameter 47: Solution.CalcIncMatrix

This parameter starts the calculation of the incidence matrix for the active actor. Please be sure that the circuits of each actor have been compiled and ready to be solved before using this command.

&nbsp;

### Parameter 48: Solution.CalcIncMatrix\_O

This parameter starts the calculation of the Branch to Node incidence matrix for the active actor. Please be sure that the circuits of each actor have been compiled and ready to be solved before using this command. The difference between this command and the CalcIncMatrix is that the calculated matrix will be ordered hierarchically from the substation to the feeder end, which can be helpful for many operations. Additionally, the Bus Levels vector is calculated and the rows (PDElements) and columns (Buses) are permuted so it is easy to identify their position in the circuit.


***
_Created with the Standard Edition of HelpNDoc: [Protect Your Confidential PDFs with These Simple Security Measures](<https://www.helpndoc.com/step-by-step-guides/how-to-generate-an-encrypted-password-protected-pdf-document/>)_
