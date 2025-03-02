# CPU

&nbsp;

&nbsp;

This option can be used to get or set the CPU assigned to the active actor. CPU numbers are indexed from 0..n. That is, the CPU number is 0-based and cannot be greater than (NumCPUs – 1). Actors are indexed from 1..n. When a new actor is created it will have affininity to all the CPUs in the local machine. If negative (-1) means that the actor’s affinity is to all the CPUs and will be executed in the first available CPU and will be realocated into another CPU dynamically if the operating system requires it. By setting a CPU number for an actor will force the actor to be executed only on the specific CPU. Use the command Get or Set commands to operating on this value. The actor’s affinity can be returned to all CPUs by setting this parameter (CPU) with any negative value.

***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Productivity with HelpNDoc's Efficient User Interface](<https://www.helpndoc.com/feature-tour/stunning-user-interface/>)_
