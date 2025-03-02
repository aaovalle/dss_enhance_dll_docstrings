# OpenDSS C++

&nbsp;

OpenDSS-C is an electric power distribution system simulator (DSS) designed to support distributed energy resource (DER) grid integration and grid modernization. It enables engineers to perform complex analyses using a flexible, customization, and easy to use platform intended specifically to meet current and future distribution system challenges and provides a foundation for understanding and integrating new technologies and resources. This power system analysis software tool was translated from the Delphi computer language (Electric Power Research Institute, 2022) into C++ to make it accessible to a larger community of software developers and used as a core library upon which to build new capabilities. OpenDSS (the Delphi version) that runs on a Windows operating system is available at the [software repository](<https://sourceforge.net/p/electricdss/code/HEAD/tree/> "target=\"\_blank\"") along with the C++ version. The C++ mimics the Delphi version, which is the reference.&nbsp;

&nbsp;

This guide documents the process for building the OpenDSS – C++ version (henceforth referred to as OpenDSS-C) for the Microsoft Windows 10 and Red Hat Enterprise Linux 8 (RHEL 8) Operating System (OS). Build instructions are provided for the Integrated Development Environments (IDEs) listed in [Table 1](<OpenDSSDocumentation.md#\_Ref99826099>) and using Clang/CMake in a command line environment ([Table 2](<OpenDSSDocumentation.md#\_Ref110354497>)). Throughout this guide the IDEs will typically be referred to by their acronyms as listed in [Table 1](<OpenDSSDocumentation.md#\_Ref99826099>). Software developers are welcome to contribute instructions to this guide for building OpenDSS-X for other IDEs and OS.&nbsp;

&nbsp;

Table 1. IDEs supported by OpenDSS C++

| IDE | OS | Acronym |
| --- | --- | --- |
| Visual Studio Community 2019 | Windows 10 | VS Code 2019 |
| Visual Studio Community 2022 | Windows 10 | VS Code 2022 |
| Visual Studio Professional 2019 | Windows 10 | VS Pro 2019 |
| Visual Studio Professional 2022 | Windows 10 | VS Pro 2022 |


&nbsp;

Table 2. OpenDSS-C compiler requirements

| Item | Description |
| --- | --- |
| C++ | GCC 4.8.5 (Red Hat 4.8.5-4) Microsoft Visual Studio Community 2022 (64-bit) - Version 17.1.3 (Windows 10) |
| Build Engine | Clang 12.0.1 C++ compiler (Red Hat 12.0.1-4) CMake 3.20.2 for build process |


&nbsp;

![Image](<lib/NewItem 46.png>)

The Visual Studio IDEs were selected because of their compatibility with CMake. Information on CMake can be found on the distribution site for the software application (CMake, 2022). The OpenDSS-X project files do not include a [Visual Studio](<CompileusingMSVSWindows.md>) project because Visual Studio operates as an IDE around CMake. However, you do not need Visual Studio for compiling OpenDSS-C, the compilation process can also be done using [command line](<CompileusingCMDLinux.md>) commands. Both processes are described in this section.


***
_Created with the Standard Edition of HelpNDoc: [Effortlessly Create High-Quality Documentation with a Help Authoring Tool](<https://www.helpndoc.com/news-and-articles/2022-09-27-why-use-a-help-authoring-tool-instead-of-microsoft-word-to-produce-high-quality-documentation/>)_
