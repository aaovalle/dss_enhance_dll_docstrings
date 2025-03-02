# Why Delphi ?

&nbsp;

The top structure of the OpenDSS that maintains the data definitions of the circuit elements is written in Object Pascal using the Delphi environment (originally from Borland, now from [Embarcadero.com](<https://www.embarcadero.com/> "target=\"\_blank\"")). The various sparse matrix solvers employed by the DSS over the years have been written in C and C++.

&nbsp;

Since Pascal is seldom taught in engineering and computer science education in the US anymore, we are often asked why we used Delphi. At the time the DSS was started, the main developer, Roger Dugan, had been tinkering with the relatively new 32-bit versions of Delphi for a couple of years and wanted to try it on a large, hard-working engineering program that would not have the usual fixed problem size limitations of typical engineering programs of the time. A rapid development environment was needed because he was also doing engineering work and the DSS was mainly developed in spare time.&nbsp;

&nbsp;

Another reason was the desire to have a [COM interface](<COMInterface.md>) to allow easy access from other programs. Delphi provided an easy way to build these interfaces early on. The main alternative at the time would have been Visual Basic, but the performance of VB was not acceptable. Fortunately, when Tom McDermott joined Electrotek a few months later, he also knew Pascal as well as many other languages and was able to contribute immediately to the development. Thus, the die was cast, and the main part of the standard program has remained in Delphi as it has evolved to the 64-bit environment.

&nbsp;

While the choice of programming languages is largely one of personal preference, here are a few things that might be considered advantages with Delphi:

&nbsp;

**&#49;**. The compiler is fast. A typical full build of the entire program takes only 3 seconds on a Dell Precision 5510 running Delphi 10.2 Tokyo compiler. This allows fast debug-and-test cycles.

&nbsp;

**&#50;.** By default, the program is completely linked into one relatively compact EXE file and can be installed simply by copying the program to a desired disk location. This has made it convenient to distribute new versions to users. No complicated installs.

&nbsp;

**&#51;.** The text processing speed for reading circuit scripts has exceeded expectations and has proven more than adequate for the task. Our previous experience with other engineering programs had led us to believe this was going to be a problem, but we were pleasantly surprised that it was not. You should find that the OpenDSS processes large circuit description scripts with relative ease. The math processing speed appears to be comparable to any natively-compiled programming language. This has improved over the years as the Delphi environment has introduced function in-lining, which has been exploited in the program for several years now.

&nbsp;

**&#52;**. Writing [COM interfaces](<COMInterface.md>) and [DLLs](<OpenDSSSharedlibrary-DirectDLL1.md>) are relatively easy tasks for a programmer. Accessing the COM interface using the popular Python language is quite easy and other Python interfaces have been developed by users. MATLAB and Excel are also good choices.&nbsp;

&nbsp;

**&#53;**. The structure of the Pascal language enforces a discipline that helps avoid the introduction of bugs. Most of the time, once you can get it to compile it will work. You should also find the code readable. So, if you are only interested in seeing how we did something, it should be easy to understand.

&nbsp;

While we develop using the professional Delphi version, there are open-source Pascal compilers available on the Web, such as the [Free Pascal Compiler (FPC)](<https://gitlab.com/freepascal.org/fpc/>) ([Lazarus IDE](<https://www.lazarus-ide.org/>)), for which we strive to maintain as much compatibility with as possible. There are many conditional compiles in the code to permit compatible compilation with Delphi and FPC.several years now. Embarcadero also provides a Community version of Delphi for little or no cost, which is a good option for students.

&nbsp;

**The C++ version**

&nbsp;

In 2022 there was a project sponsored by an EPRI member that later was co-sponsored by EPRI for translating the source code of OpenDSS from pascal to C++. This to provide access to other compilers to the solution core and structure of DSS, as well as to facilitate the interaction of other developers with the simulator source code. This version is available to the public starting in summer 2024 and will be maintained following the development route of Delphi (pascal). The Delphi version is and will be the reference for OpenDSS developments, the C++ will follow Delphi's development route.

&nbsp;

The C++ version is compatible with CMake and g++ compilers, avoiding properties provided by other vendors that extend the C++ commands. It can be edited with MS Visual Studio ([https://visualstudio.microsoft.com/vs/community/](<https://visualstudio.microsoft.com/vs/community/> "target=\"\_blank\"")) or any other preferred IDE available around.


***
_Created with the Standard Edition of HelpNDoc: [From Word to ePub or Kindle eBook: A Comprehensive Guide](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
