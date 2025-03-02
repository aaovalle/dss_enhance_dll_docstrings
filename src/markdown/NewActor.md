# NewActor

&nbsp;

&nbsp;

This command creates a new actor (OpenDSS Instance) and sets the new actor as the active actor. There can be only 1 circuit per actor. The NewActor Instruction will increment the variable NumOfActors; however, if the number of actors is the same as the number of available CPUs the new actor will not be created, generating an error message. This instruction will return the ID of the active actor. This command does not require a precedent command.

***
_Created with the Standard Edition of HelpNDoc: [Revolutionize Your CHM Help File Output with HelpNDoc](<https://www.helpndoc.com/feature-tour/create-chm-help-files/>)_
