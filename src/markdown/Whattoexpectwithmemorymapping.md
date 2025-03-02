# What to expect with memory mapping ?

&nbsp;

When using memory mapping, the time required for uploading a model containing a significant amount of load shapes will be drastically reduced without compromising the simulation performance (depending on the source format). In a model with 2768 buses (3952 nodes) with 724 load shapes in SNG format, loading the model into memory without memory mapping takes about 157 seconds. Otherwise, by using memory mapping the loading time gets reduced to 760 ms as shown in Figure 15.

&nbsp;

![Image](<lib/NewItem47.png>)

&nbsp;

Figure 15. Time required to compile a model

&nbsp;

In terms of performance, depending on the format of the source the simulation overhead will be more noticeable. If the source file is in ASCII format (string) the simulation performance will be mostly affected due to the parsing process taking place during the simulation. On the other hand, DBL and SNG files will add little or none overhead to the simulation.

&nbsp;

To demonstrate this concept, consider the example proposed [here](<https://sourceforge.net/p/electricdss/code/HEAD/tree/trunk/Version8/Distrib/Examples/MemoryMappingLoadShapes/>). In this example we are proposing different multiple ways for declaring the same load shape, one of the lines declares the model as an ASCII file, others as DBL and SNG, and other formats.

&nbsp;

\! These are different waynpts=8760 interval=1 MemoryMapping=Yes mult=(file=LS\_Phase\_AOK.txt)

\!New Loadshape.LS\_PhaseA npts=8760 interval=1 MemoryMapping=Yes mult=(dblfile=myDBL.dbl)

\!New Loadshape.LS\_PhaseA npts=8760 interval=1 MemoryMapping=Yes mult=(sngfile=mySGL.sng)s for defining the same load shape using memory mapped files

New Loadshape.LS\_PhaseA&nbsp;

&nbsp;

Once the model is loaded into memory a yearly simulation is performed for each case and compared to the original simulation (with no memory mapping). The results are shown below.

&nbsp;

![Image](<lib/NewItem48.png>)

Figure 16. Yearly QSTS simulation performance with different load shapes format when using memory mapping

&nbsp;

The performance is also tied to the hard drive technology in the host computer. SSD are the best choice in this case, while classic electro-mechanic devices may add more overhead to the simulation.

&nbsp;


***
_Created with the Standard Edition of HelpNDoc: [Maximize Your Reach: Convert Your Word Document to an ePub or Kindle eBook](<https://www.helpndoc.com/step-by-step-guides/how-to-convert-a-word-docx-file-to-an-epub-or-kindle-ebook/>)_
