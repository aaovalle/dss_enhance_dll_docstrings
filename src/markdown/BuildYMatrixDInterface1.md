# BuildYMatrixD Interface

&nbsp;

This interface executes the procedure BuildYMatrix, which is used in the DoNormalSolution routine to rebuild the Y Matrix. The structure of this interface is as follows:

&nbsp;

void BuildYMatrixD (int32 BuildOps, int32 AllocateVI);

&nbsp;

The values of BuildOps (SERIESONLY=1, WHOLEMATRIX=2) and AllocateVI (TRUE=1, FALSE=0) will have the same effects and interpretation of the function implemented within the OpenDSS code.


***
_Created with the Standard Edition of HelpNDoc: [Say Goodbye to Documentation Headaches with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
