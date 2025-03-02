# AddInAuxCurrents Interface

&nbsp;

This interface executes the procedure AddInAuxCurrents, which is used in the DoNormalSolution routine to rebuild the Y Matrix. The structure of this interface is as follows:

&nbsp;

void AddInAuxCurrents (int32 SType);

&nbsp;

The value of SType (NEWTONSOLVE=1, NORMALSOLVE=0) will have the same effects and interpretation of the function implemented within the OpenDSS code.


***
_Created with the Standard Edition of HelpNDoc: [Free PDF documentation generator](<https://www.helpndoc.com>)_
