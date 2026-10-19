{
  unified: true,
  subtitle: "Viruses are non-cellular, obligate parasites that depend entirely on a host cell&rsquo;s own ribosomes and enzymes to reproduce. Despite carrying almost no genes of their own, they show enormous structural and genomic diversity, can switch between two very different reproductive strategies, and evolve faster than almost any cellular organism.",
  keyTerms: [
    {icon:"leaf", color:"green", term:"Virus", def:"A non-cellular parasite of animals, plants and bacteria consisting of nucleic acid (DNA or RNA, never both) surrounded by a protein coat (a capsid)."},
    {icon:"atom", color:"teal", term:"Obligate parasite", def:"An organism that can only reproduce inside a living host cell; viruses are obligate parasites because they lack the ribosomes and metabolic enzymes needed for protein synthesis."},
    {icon:"bars", color:"gold", term:"Capsid &amp; capsomere", def:"Capsid: the protein coat enclosing a virus&rsquo;s genome, built from protein subunits called capsomeres. Capsid shapes include helical (e.g. TMV), conical (e.g. HIV) and polyhedral/icosahedral (e.g. adenovirus, bacteriophages)."},
    {icon:"atom", color:"plum", term:"Envelope &amp; nucleocapsid", def:"Envelope: a membrane, usually from the host plasma membrane, studded with viral glycoproteins (e.g. HIV, influenza, coronaviruses). Nucleocapsid: the capsid of an enveloped virus. Non-enveloped viruses (e.g. bacteriophages, poliovirus) rely on the capsid alone."},
    {icon:"leaf", color:"red", term:"Virion", def:"An isolated, infectious virus particle found outside a host cell."},
    {icon:"bars", color:"teal", term:"Positive-sense / negative-sense RNA", def:"Positive-sense RNA has the same sequence as viral mRNA and can be translated immediately (e.g. SARS-CoV-2). Negative-sense RNA is complementary to viral mRNA and must first be converted by RNA polymerase before translation (e.g. influenza)."},
    {icon:"atom", color:"green", term:"Reverse transcriptase", def:"A viral enzyme, found in HIV and other retroviruses, that converts viral RNA into DNA (reverse transcription); it lacks a proofreading mechanism, giving these viruses a high mutation rate."},
    {icon:"leaf", color:"gold", term:"Retrovirus &amp; provirus", def:"Retrovirus: a virus with an RNA genome that uses reverse transcriptase to copy itself into host DNA, e.g. HIV. Provirus: the resulting viral DNA once integrated into the host cell&rsquo;s genome, replicated whenever the host cell divides."},
    {icon:"bars", color:"plum", term:"Lytic cycle", def:"A phage life cycle in which the phage injects its DNA, which replicates separately from host DNA and directs production of new virions that lyse (burst) and kill the host cell."},
    {icon:"atom", color:"red", term:"Lysogenic cycle", def:"A phage life cycle in which injected viral DNA integrates into the host chromosome as a prophage and is replicated passively with the host, without killing the cell, until induction triggers the lytic cycle."},
    {icon:"leaf", color:"teal", term:"Prophage &amp; lysogen", def:"Prophage: a bacteriophage genome integrated into, and replicated with, the bacterial host chromosome. Lysogen: a bacterial host cell carrying a prophage."},
    {icon:"bars", color:"green", term:"Bacteriophage (phage)", def:"A virus that infects bacteria; phages are highly specific to the bacterial species (and often strain) they infect, e.g. bacteriophage lambda only infects <em>E. coli</em>."},
    {icon:"atom", color:"gold", term:"Temperate phage &amp; virulent phage", def:"Temperate phage: one that can adopt either the lytic or the lysogenic cycle, e.g. lambda. Virulent phage: one that can only follow the lytic cycle, always killing its host."},
    {icon:"leaf", color:"plum", term:"Multiplicity of infection (MOI)", def:"The ratio of infectious virus particles to target host cells present in a sample; MOI is one factor that determines whether an infecting phage enters the lytic cycle or the lysogenic (dormant) phase."},
    {icon:"bars", color:"red", term:"Plaque &amp; phage titre", def:"Plaque: a localized clear patch in a bacterial lawn on an agar plate, caused by phages released from one infected cell killing neighbouring bacteria. Phage titre: the concentration of phage particles in a suspension, estimated by counting plaques."},
    {icon:"atom", color:"teal", term:"Antigenic drift", def:"Small, continual mutations in influenza genes that gradually change the surface antigens haemagglutinin (HA) and neuraminidase (NA), eventually letting the virus escape recognition by the host immune system."},
    {icon:"leaf", color:"green", term:"Antigenic shift &amp; recombination", def:"Antigenic shift: a sudden, major change in an influenza A virus producing new HA and/or NA proteins and potentially a new subtype. It results from recombination &mdash; genetic material from two co-infecting strains combining within one host cell."},
    {icon:"atom", color:"plum", term:"Polyphyletic", def:"Having arisen from more than one independent evolutionary origin; viruses are considered polyphyletic, since no single gene is shared by all of them and they probably arose repeatedly by different mechanisms."},
    {icon:"bars", color:"gold", term:"NCLDV", def:"Nucleocytoplasmic large DNA viruses: a group of viruses with unusually large genomes carrying genes for DNA repair, replication, transcription and translation, hypothesised to have played a role in the evolutionary origin of the eukaryotic nucleus."},
    {icon:"leaf", color:"red", term:"Baltimore classification &amp; ICTV", def:"Baltimore classification (1971): groups viruses into seven classes by nucleic acid type, strandedness and replication method. ICTV: the International Committee on Taxonomy of Viruses (formed 1966), which maintains a universal, modified-Linnaean taxonomic scheme for viruses from order down to species."},
    {icon:"atom", color:"teal", term:"Convergent evolution &amp; analogous structures", def:"Convergent evolution: unrelated species independently evolving similar features in response to similar selective pressures. The shared structural features of all viruses may themselves be a product of convergent evolution towards obligate parasitism, producing analogous structures."},
    {icon:"bars", color:"plum", term:"Basic reproduction number (R&#8320;)", def:"The expected number of secondary infections produced by a single infected individual in a population that is completely susceptible; used in SIR epidemiological models to predict the course of an epidemic."}
  ],
  theories: [
    {
      icon:"leaf", title:"Viruses as Non-Cellular Obligate Parasites",
      blocks:[
        {type:"prose", text:"All living organisms &mdash; eukaryotes and prokaryotes &mdash; have nucleic acids that make up their genomes. Viruses also contain nucleic acid, but lack the ribosomes and metabolic enzymes needed for protein synthesis, so they depend entirely on a host cell&rsquo;s own ribosomes and enzymes to reproduce &mdash; a fundamentally different strategy of existence from any cellular organism. This total dependence makes a virus an <strong>obligate parasite</strong>. A virus itself is <strong>non-cellular</strong> &mdash; no part of it is cellular &mdash; so it has no nucleus, no nucleoid, no cytoplasm and few or no enzymes of its own; it should never be described as a &lsquo;cell&rsquo;."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Virus:</strong> a non-cellular parasite of animals, plants and bacteria consisting of nucleic acid (DNA or RNA, never both) surrounded by a protein coat (a capsid).",
          "<strong>Obligate parasite:</strong> an organism that can only reproduce inside a living host cell; viruses are obligate parasites because they lack the ribosomes and metabolic enzymes needed for protein synthesis."
        ]},
        {type:"heading", text:"Discovered before they could be seen"},
        {type:"prose", text:"Viruses were first directly observed only in 1931, once electron microscopes were developed, but their existence had already been inferred from indirect evidence. Fine filters could remove bacteria from infected tissue, yet the filtered fluid remained infective &mdash; proving an infectious agent smaller than bacteria was responsible. In 1915, English bacteriologist Frederick Twort discovered bacteriophages after noticing tiny clear spots within bacterial colonies, and hypothesised that an organism was killing the bacteria."},
        {type:"heading", text:"Vaccination before virology"},
        {type:"prose", text:"Vaccination itself predates knowledge of viruses by over a century. Edward Jenner developed the first vaccine, against smallpox, in 1798, after noticing that people who had previously caught cowpox from cattle never later died of smallpox; he named the technique after the Latin <em>vacca</em> (cow). Louis Pasteur developed the first rabies vaccine roughly 90 years later, suspecting a pathogen too small to see with contemporary microscopes. Neither understood what caused the diseases they were preventing &mdash; the chemical nature of viruses was not established until 1935."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", items:[
          "Viruses were observed directly only in <strong>1931</strong> (after electron microscopes were developed), though their existence was inferred decades earlier from filterable, bacteria-free infectious fluid.",
          "Vaccination (Jenner, 1798) predates virology by over a century &mdash; early vaccines worked without anyone knowing what a virus was."
        ]},
        {type:"heading", text:"Classifying viruses"},
        {type:"prose", text:"Since 1966, the International Committee on Taxonomy of Viruses (ICTV) has coordinated a universal taxonomic scheme for viruses, using a modified version of the Linnaean system that runs from order down to species (e.g. HIV sits in family Retroviridae because it is a retrovirus containing RNA and reverse transcriptase). A separate scheme, the <strong>Baltimore classification</strong> (1971), instead groups viruses into seven classes according to their nucleic acid, strandedness and method of replication. Because viruses are non-cellular, they are not classified within the Linnaean system or the three-domain system used for cellular life."}
      ],
      notes:[{label:"Common mistake", text:"A virus is not a cell. &lsquo;Non-cellular&rsquo; means no part of a virus is cellular &mdash; and the terms &lsquo;nucleus&rsquo; and &lsquo;nucleoid&rsquo; apply only to eukaryotes and prokaryotes respectively, never to the genetic material of a virus."}],
      side:{
        title:"Viruses vs bacteria",
        table:{
          title:"Table A2.3.1 Viruses compared with bacteria",
          head:["Characteristic","Viruses","Bacteria"],
          rows:[
            ["Cellular","No","Yes"],
            ["Approximate diameter","0.02&ndash;0.2 &micro;m","1&ndash;5 &micro;m"],
            ["Nucleic acid","Either DNA or RNA, never both","Both DNA and RNA"],
            ["Ribosomes","Rarely present","70S"],
            ["Outer surface","Protein capsid (&plusmn; lipoprotein envelope)","Cell wall containing peptidoglycan"],
            ["Motility","None","Some (rotating flagella)"],
            ["Replication","Protein synthesis then self-assembly, inside cells","Binary fission, generally outside cells"]
          ]
        }
      }
    },
    {
      icon:"atom", title:"Structural Features Common to All Viruses",
      blocks:[
        {type:"prose", text:"Despite their huge diversity, every virus shares the same minimal structural toolkit, built as economically as possible since the virus itself carries out no independent life processes. All viruses share five common features: an extremely small, fixed size range of 20&ndash;400 nm in diameter; nucleic acid (DNA or RNA) as their genetic material; a protein capsid surrounding that nucleic acid; no cytoplasm; and few or even no enzymes of their own."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Capsid &amp; capsomere:</strong> the capsid is the protein coat enclosing a virus&rsquo;s genome, built from protein subunits called capsomeres. Capsid shapes include helical (e.g. TMV), conical (e.g. HIV) and polyhedral/icosahedral (e.g. adenovirus, bacteriophages)."},
        {type:"heading", text:"Capsid shapes"},
        {type:"prose", text:"A capsid is built from many identical protein subunits called <strong>capsomeres</strong>, which self-assemble into one of several characteristic shapes: <strong>helical</strong> (e.g. tobacco mosaic virus, TMV, where a spiral of capsomeres winds around a central canal holding a single strand of RNA), <strong>conical</strong> (e.g. HIV) or <strong>polyhedral</strong> (e.g. adenovirus). The most complex capsids are found in bacteriophages: an elongated <strong>icosahedral</strong> head, built from 20 fused equilateral triangles &mdash; the optimal way to form a closed shell from identical protein subunits &mdash; encloses the genome, joined to a tail shaft with fibres used to attach to the host bacterial cell wall. Capsids protect the viral genome, but are often the main target recognised by a host&rsquo;s immune system."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"Tobacco mosaic virus demonstrates helical capsid structure particularly clearly: electron micrographs show both a hollow tube in side view and a rosette-like pattern end-on, matching the mottled, mosaic-patterned leaf damage it causes in infected tobacco plants."},
        {type:"heading", text:"Genome size and replication speed"},
        {type:"prose", text:"Genome size varies hugely between viruses and reflects this minimalism: the bacteriophage Q&beta; genome is only a few thousand nucleotides long and carries just four genes, while the structurally far more complex bacteriophage T4 carries 289 genes, most involved in building its elaborate capsid. There is a roughly inverse relationship between a virus&rsquo;s genome size and how much it depends on its host cell&rsquo;s own machinery for replication &mdash; and because a smaller genome replicates faster, rapid replication is favoured by a small genome size. Viruses with prokaryotic hosts tend to replicate especially fast, reflected in the unusually compact, overlapping-gene genomes of many bacteriophages."}
      ],
      notes:[
        {label:"Described figure &mdash; the icosahedron (Fig. A2.3.5)", text:"An icosahedron is shown unfolded as a flat net of 20 identical equilateral triangles, and folded into a closed, roughly spherical 20-sided solid &mdash; the shape adopted by many complex viral capsids, including bacteriophage heads."},
        {label:"Described figure &mdash; tobacco mosaic virus (Fig. A2.3.4)", text:"TMV&rsquo;s helical capsid is drawn as polypeptide capsomeres arranged in a spiral around a central canal holding its single RNA strand; electron micrographs show both the hollow tube in side view and the rosette-like end view, alongside the mottled, mosaic-patterned leaf damage the virus causes in infected tobacco plants."}
      ]
    },
    {
      icon:"book", title:"Diversity of Viral Genomes and Envelopes",
      blocks:[
        {type:"prose", text:"Viruses are classified largely by the type of genome they carry &mdash; DNA or RNA, single- or double-stranded, positive- or negative-sense, linear or circular &mdash; and by whether or not that genome is wrapped in a host-derived envelope. The viral genome is either DNA (e.g. adenoviruses, most bacteriophages) or RNA (e.g. HIV, coronaviruses), but never both; because the genetic code is shared between viruses and living organisms, host cells can transcribe viral DNA into mRNA and translate it into protein using their own machinery."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Positive-sense RNA:</strong> has the same sequence as viral mRNA and can be translated immediately (e.g. SARS-CoV-2).",
          "<strong>Negative-sense RNA:</strong> is complementary to viral mRNA and must first be converted by RNA polymerase before translation (e.g. influenza)."
        ]},
        {type:"prose", text:"Nucleic acid replication location also differs: SARS-CoV-2 replicates entirely in the host cytoplasm, while influenza replicates its RNA in the host nucleus. In HIV, viral RNA instead acts as a template for synthesising viral DNA in the cytoplasm using the enzyme reverse transcriptase. A viral genome may be linear (e.g. coronaviruses) or circular (e.g. hepatitis B), single-stranded (e.g. hepatitis E virus, coronaviruses) or double-stranded (e.g. HIV, SV-40); some viruses even carry more than one copy of their genome (e.g. HIV, influenza)."},
        {type:"heading", text:"Enveloped vs non-enveloped viruses"},
        {type:"prose", text:"Viruses are also classified as <strong>enveloped</strong> (e.g. HIV, influenza, coronaviruses) or <strong>non-enveloped</strong> (e.g. bacteriophages, poliovirus). An envelope is usually derived from the host plasma membrane and studded with virally encoded spike glycoproteins (coronaviruses are an exception, taking their envelope from internal host membranes instead). The envelope protects the virion from enzymes and other chemicals, giving enveloped viruses an advantage over non-enveloped virions, and its glycoproteins bind host-cell surface receptors, enabling recognition and uptake of the virion into the cell."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", items:[
          "DNA viruses: adenoviruses, most bacteriophages. RNA viruses: HIV, coronaviruses.",
          "Enveloped viruses (HIV, influenza, coronaviruses) gain protection from host enzymes; non-enveloped viruses (bacteriophages, poliovirus) rely on the capsid alone."
        ]}
      ],
      notes:[{label:"Nature of science &mdash; patterns and trends", text:"Before modern molecular techniques existed, viruses could only be studied by observing the effects of virus-infected extracts on living animals; an approximate measure of infectivity was obtained simply by diluting an extract and testing how far it could still be diluted while remaining able to cause infection."}],
      side:{
        title:"Classifying a viral genome",
        table:{
          title:"Genome property and examples",
          head:["Property","Examples"],
          rows:[
            ["Nucleic acid: DNA","Adenovirus, most bacteriophages"],
            ["Nucleic acid: RNA","HIV, coronaviruses"],
            ["Single-stranded","Hepatitis E virus, coronaviruses"],
            ["Double-stranded","HIV, SV-40"],
            ["Linear genome","Coronaviruses"],
            ["Circular genome","Hepatitis B"],
            ["Positive-sense RNA","SARS-CoV-2"],
            ["Negative-sense RNA","Influenza viruses"]
          ]
        }
      }
    },
    {
      icon:"atom", title:"The Lytic Cycle of a Virus",
      blocks:[
        {type:"prose", text:"In the lytic cycle, a phage hijacks a bacterium purely to mass-produce copies of itself, destroying the host cell completely once new virions are ready for release."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Lytic cycle:</strong> a phage life cycle in which the phage injects its DNA, which replicates separately from host DNA and directs production of new virions that lyse (burst) and kill the host cell."},
        {type:"prose", text:"<strong>Attachment:</strong> the tail fibre of bacteriophage lambda binds to specific receptors on the surface of its host, <em>E. coli</em>. <strong>Penetration:</strong> the phage injects its double-stranded DNA genome into the host cell; the protein capsid itself is left outside."},
        {type:"prose", text:"The viral DNA remains a separate molecule within the bacterium, rather than becoming incorporated into the host genome, and replicates independently of the host&rsquo;s own DNA. <strong>Biosynthesis:</strong> the bacterial DNA is broken down by hydrolysis, while phage DNA is replicated; viral genes are then expressed using host enzymes and ribosomes to produce viral proteins."},
        {type:"prose", text:"<strong>Maturation:</strong> the newly made viral proteins self-assemble around copies of the replicated viral DNA to form mature virions. <strong>Release:</strong> lysis of the bacterial cell wall destroys the host cell, releasing the new phage particles. Bacteriophages that can only follow this pathway are called <strong>virulent phages</strong>."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", items:[
          "The five lytic stages always run in the same order: <strong>Attachment &rarr; Penetration &rarr; Biosynthesis &rarr; Maturation &rarr; Release</strong>.",
          "Only <strong>virulent phages</strong> are restricted to this pathway alone &mdash; they can never enter a dormant lysogenic phase."
        ]}
      ],
      notes:[{label:"Common mistake", text:"Viruses cannot move under their own power. They move passively &mdash; carried in phloem, blood, other body fluids or air &mdash; until they happen to encounter and bind to a receptor on a host cell surface, which then draws the virus particle into the cell."}]
    },
    {
      icon:"leaf", title:"The Lysogenic Cycle and the Prophage State",
      blocks:[
        {type:"prose", text:"Many phages, including bacteriophage lambda, can instead enter a dormant lysogenic cycle &mdash; hiding inside the host genome as a harmless passenger for many generations before stress conditions trigger a switch into the lytic cycle. The phage still infects the host cell by injecting its DNA, but this time the viral DNA becomes incorporated into the host cell&rsquo;s own chromosome, forming a <strong>prophage</strong>; a bacterial host carrying a prophage is called a <strong>lysogen</strong>."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Lysogenic cycle:</strong> a phage life cycle in which injected viral DNA integrates into the host chromosome as a prophage and is replicated passively with the host, without killing the cell, until induction triggers the lytic cycle.",
          "<strong>Prophage &amp; lysogen:</strong> prophage &mdash; a bacteriophage genome integrated into, and replicated with, the bacterial host chromosome; lysogen &mdash; a bacterial host cell carrying a prophage."
        ]},
        {type:"prose", text:"Because the prophage replicates passively together with the host chromosome every time the bacterium divides by binary fission, it is passed on to all daughter cells &mdash; and because a prophage still contains genes, it can confer entirely new properties on its bacterial host. Under stressful conditions, the phage DNA is excised from the bacterial chromosome and switches into the lytic cycle: phage DNA replicates, phage proteins are made and assembled into new virions, and the cell finally lyses, releasing the phage."},
        {type:"heading", text:"What determines lytic vs lysogenic fate"},
        {type:"prose", text:"Whether an infection favours the lytic or lysogenic outcome partly depends on the host&rsquo;s physiological state: bacteria grown in rich medium contain high levels of proteases (protein-degrading enzymes essential for completing the lytic cycle) and more readily support lytic replication, while poorly growing bacteria have lower protease levels and more readily establish lysogeny instead. The <strong>multiplicity of infection (MOI)</strong> &mdash; the number of infectious virus particles divided by the number of target host cells present &mdash; is another factor governing whether a phage enters the lytic cycle or the dormant lysogenic phase. Phages able to adopt either pathway, such as lambda, are called <strong>temperate phages</strong>."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", items:[
          "Rich growth medium (high protease levels) favours the lytic cycle; poorly growing bacteria more often enter lysogeny instead.",
          "A prophage still carries functional genes, so it can give its bacterial host entirely new properties."
        ]}
      ],
      notes:[{label:"Nature of science &mdash; experiments", text:"If a bacteriophage infects bacteria spread on an agar plate, phages released from one infected cell can only infect their immediate neighbours, producing a localized clearing in the bacterial lawn called a plaque. Counting plaques lets a biologist estimate the concentration of phage particles in a suspension &mdash; its phage titre &mdash; on the assumption that each plaque corresponds to one original phage particle."}],
      side:{
        title:"Bacteriophage lambda summary",
        table:{
          title:"Table A2.3.2 Summary of bacteriophage lambda",
          head:["Feature","Description"],
          rows:[
            ["Viral genome","Linear DNA, with sticky ends"],
            ["Capsid","Icosahedral head, tail sheath, one tail fibre"],
            ["Envelope","None (naked virus)"],
            ["Host","<em>E. coli</em> (Gram-negative)"],
            ["Cycle","Both lytic and lysogenic"],
            ["Attachment","Tail fibre binds receptor on host surface"],
            ["Degradation of host DNA","Only during the lytic stage"],
            ["Release","Osmotic lysis kills the host, releasing phage"]
          ]
        }
      }
    },
    {
      icon:"book", title:"Evidence for Several Origins of Viruses",
      blocks:[
        {type:"prose", text:"Because no single gene is shared by every known virus, biologists think viruses are polyphyletic &mdash; arising independently, more than once, by at least three different proposed mechanisms, rather than descending from one common ancestor. It seems unlikely that the enormous diversity of known viruses &mdash; infecting every kind of cellular organism &mdash; shares one single common ancestor."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Polyphyletic:</strong> having arisen from more than one independent evolutionary origin; viruses are considered polyphyletic, since no single gene is shared by all of them and they probably arose repeatedly by different mechanisms."},
        {type:"heading", text:"Three hypotheses for viral origin"},
        {type:"prose", text:"The <strong>virus-first hypothesis</strong> proposes that viruses evolved before, or alongside, their current host cells: short, self-complementary pieces of RNA may have folded like a protein, gradually growing more complex until they could self-replicate and then began infecting cells. The <strong>escaped genes (progressive) hypothesis</strong> proposes that viruses arose from genetic elements, such as transposons (mobile, repetitive DNA sequences already able to move between chromosomes in eukaryotes), that gained the further ability to move between cells entirely. The <strong>regressive (reduction) hypothesis</strong> proposes that viruses are the remnants of once-independent cellular organisms that, through a long-term mutualistic or parasitic relationship, progressively lost their own protein-building structures while retaining the ability to replicate and infect new hosts."},
        {type:"prose", text:"Both the escaped-genes and regressive hypotheses assume cells existed before viruses, but some researchers propose that viruses may instead have been among the very first replicating entities, appearing even before LUCA (the last universal common ancestor of cellular life)."},
        {type:"heading", text:"NCLDVs and convergent evolution"},
        {type:"prose", text:"A newly discovered group, the <strong>nucleocytoplasmic large DNA viruses (NCLDV)</strong>, have unusually large genomes carrying genes for DNA repair, replication, transcription and translation, and replicate in both the host nucleus and cytoplasm. It has been hypothesised that the eukaryotic nucleus itself arose through endosymbiosis of a complex, enveloped DNA virus into an ancestral eukaryotic cell &mdash; and that NCLDV viruses themselves evolved regressively, their ancestral cells losing key genes as they adopted an obligate parasitic lifestyle."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"NCLDV viruses illustrate how blurred the line between &lsquo;virus&rsquo; and &lsquo;cell&rsquo; can get: their genomes are large enough to carry their own DNA-repair and transcription genes, and one hypothesis proposes that the eukaryotic nucleus itself originated from an engulfed NCLDV ancestor."},
        {type:"prose", text:"Because every virus shares an extreme form of obligate parasitism on host cells, their shared structural features could themselves be a product of <strong>convergent evolution</strong> &mdash; unrelated species independently evolving similar &lsquo;analogous&rsquo; traits in response to similar selective pressures &mdash; rather than common descent. Retroviruses probably arose through a progressive route, while large DNA viruses probably arose through a regressive one; it remains possible that no single hypothesis explains every virus."}
      ],
      notes:[
        {label:"Described figure &mdash; escaped genes hypothesis (Fig. A2.3.9)", text:"A single-celled organism (containing RNA, a protein-building structure and a protein coat) undergoes unequal cell division into two mini-cells. The mini-cell lacking the protein-building structure cannot survive alone, but the one retaining the protein coat does survive &mdash; and, now able to replicate itself and infect other organisms, has become a virus."},
        {label:"Described figure &mdash; regressive hypothesis (Fig. A2.3.10)", text:"A single-celled organism with RNA and a protein-building structure enters a mutualistic relationship with another cell. Over time the smaller partner loses its own protein-building structures, but &mdash; still able to replicate and infect new organisms &mdash; has become a virus, now dependent entirely on its host."}
      ]
    },
    {
      icon:"atom", title:"Rapid Evolution in Viruses: Mutation, Influenza and HIV",
      blocks:[
        {type:"prose", text:"Mutation, recombination, large population sizes and rapid life cycles let viruses evolve far faster than their host cells &mdash; a fact made starkly visible in the ongoing evolution of influenza and HIV. A virus&rsquo;s evolution rate can be defined as the number of nucleotide substitutions per nucleotide site, per year. Mutations are a natural by-product of viral replication, occurring at a frequency set by the error rate of the replicating enzymes (adjusted by any proofreading that occurs); whether a mutant succeeds then depends on whether it has a selective advantage &mdash; mutations improving replication, transmission or immune evasion increase in frequency, while those reducing viral fitness are removed."},
        {type:"prose", text:"RNA viruses generally mutate far faster than DNA viruses because errors made copying their RNA genomes are not corrected by proofreading. Coronaviruses are an exception among RNA viruses, mutating more slowly because they produce an RNA polymerase that corrects some replication errors &mdash; but viruses overall still evolve faster than their host cells, giving them an advantage in staying ahead of the host immune response."},
        {type:"heading", text:"Influenza: antigenic drift and shift"},
        {type:"prose", text:"<strong>Influenza</strong> (types A, B and C) is an enveloped virus with a negative-sense, single-stranded, segmented RNA genome, infecting respiratory (and, in birds, intestinal) epithelial cells via binding between its haemagglutinin (HA) spike protein and host sialic acid receptors."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Antigenic drift:</strong> small, continual mutations in influenza genes that gradually change the surface antigens haemagglutinin (HA) and neuraminidase (NA), eventually letting the virus escape recognition by the host immune system.",
          "<strong>Antigenic shift &amp; recombination:</strong> antigenic shift is a sudden, major change in an influenza A virus producing new HA and/or NA proteins and potentially a new subtype, resulting from recombination &mdash; genetic material from two co-infecting strains combining within one host cell."
        ]},
        {type:"prose", text:"Antigenic drift causes seasonal flu, while antigenic shift &mdash; in which an influenza virus from an animal population swaps genome segments with a human strain co-infecting the same cell &mdash; produces a novel virus that most people have no existing immunity to."},
        {type:"heading", text:"HIV&rsquo;s high mutation rate"},
        {type:"prose", text:"<strong>HIV</strong>, the retrovirus that causes AIDS, converts its RNA genome into DNA inside the host cytoplasm using reverse transcriptase, then integrates that DNA into the host nucleus&rsquo;s genome as a provirus. Because reverse transcriptase lacks a proofreading mechanism, HIV has an unusually high mutation rate, and AIDS patients typically carry many genetically distinct HIV variants descended from their original infection; single-drug treatments fail quickly as drug-resistant strains arise by mutation, so effective therapy instead uses combinations of (typically three) drugs that each target a different viral protein. HIV&rsquo;s population size &mdash; the total number of infectious proviruses integrated across an individual&rsquo;s cells &mdash; combined with its short generation time and high mutation rate, lets it evolve and adapt to its host unusually quickly."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", items:[
          "RNA viruses mutate faster than DNA viruses because RNA replication is not proofread &mdash; coronaviruses are the exception.",
          "HIV&rsquo;s combination (typically triple-drug) therapy exists precisely because its error-prone reverse transcriptase lets drug-resistant strains arise quickly under single-drug treatment."
        ]}
      ],
      notes:[{label:"Nature of science &mdash; falsification", text:"The central dogma of molecular biology held that genetic information flows only one way: DNA &rarr; RNA &rarr; protein. In 1970, David Baltimore discovered reverse transcriptase in retroviruses, falsifying this strict one-directional flow by showing RNA could be copied back into DNA. The discovery underpinned the identification of HIV in 1984 and the development of effective HIV therapies, and RNA-to-DNA information transfer is now recognised as a general evolutionary principle across biology, not just in viruses."}],
      side:{
        title:"Comparing influenza and HIV",
        table:{
          title:"Two rapidly evolving viruses",
          head:["Feature","Influenza","HIV"],
          rows:[
            ["Genome","Negative-sense, single-stranded, segmented RNA","Single-stranded RNA (retrovirus)"],
            ["Key enzyme","&mdash;","Reverse transcriptase (no proofreading)"],
            ["Source of major change","Antigenic shift (recombination between co-infecting strains)","High mutation rate within one host"],
            ["Consequence","New subtypes can start pandemics","Many co-existing variants in one patient"]
          ]
        }
      }
    },
    {
      icon:"book", title:"Modelling Viral Spread: The SIR Model",
      blocks:[
        {type:"prose", text:"Simple compartmental models like the SIR model simplify the mathematics of an epidemic into just a few interacting categories of people, letting epidemiologists predict how an outbreak &mdash; and interventions against it &mdash; might unfold. Compartmental models classify a population into labelled groups to model the spread of infectious disease, including COVID-19. In the <strong>SIR model</strong>, people move one-way from <strong>S</strong>usceptible (able to catch the infection) to <strong>I</strong>nfectious (have the infection and can spread it) to <strong>R</strong>ecovered (had the disease, now better); it is most accurate for diseases spread only human-to-human, where recovery gives long-lasting resistance."},
        {type:"prose", text:"Plotted against time, the susceptible curve (S) starts high and falls as people become infected; the infectious curve (I) rises to a peak then falls as people recover; and the recovered curve (R) starts at zero and rises steadily as the epidemic runs its course."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Basic reproduction number (R&#8320;):</strong> the expected number of secondary infections produced by a single infected individual in a population that is completely susceptible; used in SIR epidemiological models to predict the course of an epidemic."},
        {type:"prose", text:"Such models try to predict how a disease will spread, the total number who will be infected, and how long an epidemic will last, and to estimate epidemiological parameters such as the basic reproduction number. Models can also test how interventions, such as a lockdown or a vaccination campaign, might change the outcome of an epidemic."},
        {type:"heading", text:"Viral evolution undermines vaccines"},
        {type:"prose", text:"The rapid evolution of viruses has direct consequences for controlling the diseases they cause. Flu vaccines must be redeveloped every year to maintain their efficacy (the percentage reduction in disease seen among a vaccinated group in a clinical trial) against antigenic drift. During the COVID-19 pandemic, successive variants reduced the efficacy of vaccines developed against earlier strains, sometimes also changing the symptoms of the disease."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"During the COVID-19 pandemic, SIR-style compartmental models were used to estimate how emerging variants and interventions such as lockdowns might change the course of the epidemic, while successive variants progressively eroded the efficacy of vaccines developed against earlier strains."}
      ],
      notes:[
        {label:"Described figure &mdash; the SIR model (Figs A2.3.13&ndash;14)", text:"Figure A2.3.13 shows three boxes &mdash; Susceptible, Infectious, Recovered &mdash; linked by one-way arrows showing the order people move through during an epidemic. Figure A2.3.14 plots number of people (y-axis) against time in days (x-axis): the S curve falls, the I curve rises then falls back down, and the R curve rises steadily, together tracing the typical course of an outbreak."},
        {label:"Top tip", text:"Emerging diseases such as HIV and COVID-19 are often especially virulent simply because they are not yet well adapted to their new host species."}
      ]
    }
  ],
  workedExamples: [
    {
      title:"Structural differences between a virus and a bacterium",
      question:"Using Table A2.3.1, state three structural differences between a virus and a bacterium, and explain how one of these differences relates to a virus being an obligate parasite.",
      answer:[
        "Viruses are non-cellular (0.02&ndash;0.2 &micro;m in diameter), while bacteria are single cells (1&ndash;5 &micro;m); viruses carry either DNA or RNA, never both, while bacteria carry both; and viruses rarely have ribosomes, while bacteria have 70S ribosomes.",
        "The absence of ribosomes (and of the metabolic enzymes needed for protein synthesis) directly explains why a virus is an obligate parasite: without its own protein-synthesising machinery, a virus cannot make the capsid proteins or enzymes it needs to reproduce, and so must take over a living host cell&rsquo;s ribosomes and enzymes instead."
      ]
    },
    {
      title:"Calculating the volume of virus suspension needed for a given MOI",
      question:"A scientist needs an MOI of 0.5 for an investigation. The virus particles are at a concentration of 2 &times; 10<sup>9</sup> cm<sup>&minus;3</sup> and the bacteria are at a concentration of 8 &times; 10<sup>8</sup> cm<sup>&minus;3</sup>. Calculate the volume of virus suspension that should be added to 0.25 cm<sup>3</sup> of bacteria.",
      answer:[
        "Number of target bacterial cells present = 8 &times; 10<sup>8</sup> cm<sup>&minus;3</sup> &times; 0.25 cm<sup>3</sup> = 2 &times; 10<sup>8</sup> cells.",
        "MOI = number of virus particles &divide; number of target cells, so the number of virus particles needed = MOI &times; number of target cells = 0.5 &times; 2 &times; 10<sup>8</sup> = 1 &times; 10<sup>8</sup> particles.",
        "Volume of virus suspension required = number of particles needed &divide; virus concentration = (1 &times; 10<sup>8</sup>) &divide; (2 &times; 10<sup>9</sup> cm<sup>&minus;3</sup>) = 0.05 cm<sup>3</sup>."
      ]
    },
    {
      title:"Distinguishing the lytic and lysogenic life cycles",
      question:"Distinguish between the lytic and lysogenic life cycles of a virus.",
      answer:[
        "In the lytic cycle, injected viral DNA remains separate from the host chromosome, replicates independently, and directs production of new virions; the host cell is always destroyed by lysis, releasing the new phage particles.",
        "In the lysogenic cycle, injected viral DNA instead integrates into the host chromosome as a prophage, is replicated passively alongside host DNA at every cell division, and does not kill the host cell &mdash; until a stress signal triggers excision of the prophage and a switch into the lytic cycle."
      ]
    },
    {
      title:"Why viruses are considered non-living, obligate parasites",
      question:"Discuss why viruses are considered non-living, and why they are classified as obligate parasites.",
      answer:[
        "Viruses lack cytoplasm, ribosomes and the metabolic enzymes needed to carry out independent life processes such as protein synthesis, respiration or growth &mdash; the criteria normally used to judge whether something is &lsquo;alive&rsquo; &mdash; so most biologists classify them as non-living.",
        "Because a virus cannot synthesise its own proteins or replicate its genome without borrowing a host cell&rsquo;s ribosomes, enzymes and energy supply, it can only reproduce inside a living host cell: this total dependence on a host for reproduction is exactly what defines an obligate parasite."
      ]
    },
    {
      title:"Interpreting an SIR epidemic graph",
      question:"Figure A2.3.14 plots the number of susceptible (S), infectious (I) and recovered (R) individuals in a population against time (days) during an outbreak. Describe the shape of each curve and deduce how S, I and R interact.",
      answer:[
        "The susceptible curve (S) starts high, at close to the whole population, and falls over time as more individuals are infected and move out of the susceptible group.",
        "The infectious curve (I) starts low, rises to a peak as the disease spreads rapidly through the still-large susceptible population, then falls again as susceptible individuals become scarcer and infected individuals recover.",
        "The recovered curve (R) starts at zero and rises steadily throughout the outbreak, as individuals move out of the infectious group once they recover and gain long-lasting resistance.",
        "The three curves are linked by one-way flow: the rate at which S falls equals the rate at which new individuals join I, and the rate at which I falls (once past its peak) equals the rate at which individuals join R &mdash; so the epidemic naturally burns out once the susceptible pool shrinks too far to sustain the infection rate."
      ]
    }
  ],
  summary: [
    "Viruses are non-cellular obligate parasites: nucleic acid (DNA or RNA, never both) enclosed in a protein capsid, with no cytoplasm and few or no enzymes of their own, so they can only reproduce by hijacking a host cell&rsquo;s ribosomes and enzymes.",
    "Viruses differ sharply from bacteria in size, nucleic acid content, ribosomes, outer surface, motility and method of replication (Table A2.3.1); the ICTV and the Baltimore classification each provide a system for naming and grouping them.",
    "All viruses share a fixed small size (20&ndash;400 nm), a capsid built from capsomeres in a helical, conical or polyhedral shape, and &mdash; in bacteriophages especially &mdash; a complex icosahedral head joined to a tail; genome size varies hugely (4 genes in bacteriophage Q&beta; vs 289 in T4) and tends to trade off against dependence on the host.",
    "Viral genomes are classified by nucleic acid (DNA or RNA), strandedness (single or double), polarity for RNA viruses (positive-sense, translatable immediately, vs negative-sense, needing conversion first), and shape (linear or circular); viruses may also be enveloped (host-membrane-derived, glycoprotein-studded) or non-enveloped.",
    "In the lytic cycle, a phage such as bacteriophage lambda attaches, injects its DNA, replicates it separately from the degraded host DNA, assembles new virions, and lyses the host cell to release them &mdash; phages that only do this are virulent phages.",
    "In the lysogenic cycle, injected phage DNA integrates into the host chromosome as a prophage (making the host a lysogen), replicates passively with the host, and can later be induced &mdash; often by stress &mdash; to excise and enter the lytic cycle; temperate phages such as lambda can follow either pathway, and the outcome depends partly on host protease levels and on the multiplicity of infection (MOI).",
    "Phage concentration (titre) can be estimated by counting plaques &mdash; localized clearings in a bacterial lawn caused by phages released from one infected cell.",
    "Because no single gene is shared by every virus, viruses are considered polyphyletic: three hypotheses &mdash; virus-first, escaped genes (progressive) and regressive (reduction) &mdash; propose different routes by which viruses may have arisen from or alongside cellular organisms, and NCLDV viruses may even have contributed to the origin of the eukaryotic nucleus.",
    "Viral evolution rate depends on mutation, recombination, population size and life cycle speed; RNA viruses typically mutate faster than DNA viruses (lacking proofreading), though coronaviruses are a slower-mutating exception, and viruses overall evolve faster than their hosts.",
    "Influenza evolves through antigenic drift (gradual mutation of HA/NA, driving seasonal flu) and antigenic shift (sudden recombination between co-infecting strains, potentially creating a pandemic subtype); HIV evolves rapidly because its reverse transcriptase lacks proofreading, generating many co-existing variants and requiring combination drug therapy.",
    "The 1970 discovery of reverse transcriptase by David Baltimore falsified the strict one-directional central dogma of molecular biology (DNA &rarr; RNA &rarr; protein), underpinning the later discovery of HIV and the development of effective antiretroviral therapy.",
    "Compartmental models such as the SIR model (Susceptible &rarr; Infectious &rarr; Recovered) simplify epidemic dynamics to predict disease spread, total cases and the basic reproduction number R&#8320;, and to test interventions &mdash; though rapidly evolving viruses constantly erode vaccine efficacy, requiring vaccines to be regularly redeveloped."
  ]
}
