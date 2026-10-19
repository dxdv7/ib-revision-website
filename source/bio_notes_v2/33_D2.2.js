{
  unified: true,
  subtitle: "Gene expression is the mechanism linking the genetic code to the phenotype &mdash; this chapter examines how transcription and translation are regulated, how one genome gives rise to a dynamic transcriptome and proteome, how epigenetic tags can switch genes on or off and even be inherited, and how bacteria use operons to switch gene expression on and off in response to their environment.",
  keyTerms: [
    {icon:"leaf", color:"green", term:"Gene expression", def:"The mechanism by which information in genes has effects on the phenotype: the genetic code is transcribed into mRNA, which is translated into proteins at ribosomes, and these proteins determine the phenotype."},
    {icon:"atom", color:"teal", term:"Phenotype", def:"The observable traits of an organism, resulting from its genotype and from environmental factors."},
    {icon:"bars", color:"gold", term:"Genotype", def:"The combination of alleles inherited by an organism &mdash; its genetic makeup."},
    {icon:"atom", color:"plum", term:"Transcription factor", def:"A protein that binds to specific DNA sequences to control the transcription of mRNA."},
    {icon:"leaf", color:"red", term:"Enhancer", def:"A regulatory DNA sequence, often thousands of base pairs upstream (or downstream) of a gene, which increases the rate of its transcription when bound by activator proteins."},
    {icon:"bars", color:"green", term:"Promoter", def:"A DNA sequence just before the start of a gene, where RNA polymerase and transcription factors assemble into a transcription complex before transcription can begin."},
    {icon:"atom", color:"teal", term:"Poly-A tail", def:"A string of adenine nucleotides added to the 3&prime; end of an mRNA molecule; its shortening is one of the key steps that initiates degradation of the mRNA once it is no longer needed for translation."},
    {icon:"leaf", color:"gold", term:"Epigenesis", def:"The development of patterns of differentiation in the cells of a multicellular organism, from an undifferentiated zygote."},
    {icon:"atom", color:"red", term:"Epigenetics", def:"The study of heritable changes in gene activity that are not caused by changes in the DNA base sequence (epi = outside), such as DNA methylation and histone modification."},
    {icon:"bars", color:"plum", term:"Genome", def:"The whole of the genetic information of an organism; it is the same in every cell of a multicellular organism, since all its cells derive from one zygote by cell division."},
    {icon:"leaf", color:"teal", term:"Transcriptome", def:"The range of mRNA transcripts produced in a specific cell or tissue type at a particular time, determined by differential gene expression."},
    {icon:"atom", color:"gold", term:"Proteome", def:"All the proteins expressed within a cell, tissue or organism at a given time; unlike the genome, it is dynamic, varying with a cell&rsquo;s function, location and environment."},
    {icon:"bars", color:"red", term:"Methylation", def:"The reversible addition of a methyl group (&ndash;CH<sub>3</sub>) within chromatin, usually to a cytosine base in DNA at a promoter (sometimes to histone tails); extensive methylation usually inactivates a gene."},
    {icon:"leaf", color:"plum", term:"Epigenetic tag", def:"A chemical tag, such as a methyl or acetyl group, added directly to DNA or to histone proteins to regulate gene expression by blocking or allowing access to a gene&rsquo;s &lsquo;on&rsquo; switch."},
    {icon:"atom", color:"green", term:"Epigenetic inheritance", def:"An inheritance pattern in which modification of chromatin by epigenetic tags alters gene expression; a parent&rsquo;s experiences can be passed to offspring without any change to the DNA base sequence."},
    {icon:"bars", color:"teal", term:"Imprinting", def:"A process in which only one copy of a gene (maternal or paternal) is expressed in an individual while the other copy is epigenetically silenced during gamete formation &mdash; one of the few epigenetic tags (~1% of genes) that survives reprogramming of the egg and sperm."},
    {icon:"leaf", color:"gold", term:"Monozygotic twins", def:"Identical twins, resulting from a single fertilized egg that splits into two early in development; they share the same genome and are always the same sex."},
    {icon:"atom", color:"red", term:"Dizygotic twins", def:"Non-identical twins, developing from two separately fertilized eggs, each with its own distinct combination of alleles."},
    {icon:"bars", color:"plum", term:"Operon", def:"A sequence of adjacent bacterial genes, found only in prokaryotes, all under the transcriptional control of the same operator."},
    {icon:"leaf", color:"green", term:"Operator", def:"A DNA region at one end of an operon that acts as the binding site for a repressor protein; when bound by the repressor, transcription of the operon is prevented."},
    {icon:"atom", color:"teal", term:"Repressor &amp; inducer", def:"Repressor: the protein product of a regulator gene that binds the operator and blocks transcription. Inducer: a small molecule (e.g. lactose) that inactivates a repressor by binding to it, switching transcription on."},
    {icon:"bars", color:"gold", term:"Lac operon &amp; trp operon", def:"Lac operon: an inducible operon that switches on only when lactose is present. Trp operon: a repressible operon, normally on, switched off once tryptophan (a co-repressor) accumulates."}
  ],
  theories: [
    {
      icon:"leaf", title:"Gene Expression and the Phenotype",
      blocks:[
        {type:"prose", text:"Gene expression is the mechanism linking the genetic code to the phenotype: the genetic code is transcribed into mRNA, which is translated into proteins at ribosomes, and the proteins an organism produces determine its phenotype. The most common stages in gene expression are therefore transcription, translation, and the function of the protein product, such as an enzyme."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Gene expression:</strong> the mechanism by which information in genes has effects on the phenotype &mdash; the genetic code is transcribed into mRNA, which is translated into proteins at ribosomes, and these proteins determine the phenotype."},
        {type:"prose", text:"Transcription is the first stage of gene expression and the key stage at which a gene&rsquo;s expression can be switched on or off. Non-coding sequences of DNA, which do not themselves code for polypeptides, include regulators of gene expression that act at this stage."},
        {type:"prose", text:"Different patterns of gene expression underlie cell differentiation, and are often triggered by changes in the environment. Biochemical gradients within an early-stage embryo also affect gene expression, helping to pattern the developing body plan."},
        {type:"prose", text:"Gene expression can also be switched on by cell signalling: an intracellular receptor, once activated by a signalling chemical binding to it, can itself bind specific DNA sequences to promote transcription of a gene."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"Plant hormones such as auxin regulate gene expression mechanisms in the nucleus that control growth and development."}
      ],
      notes:[
        {label:"Common mistake", text:"Do not confuse genotype and phenotype. Genotype is the genetic makeup of an individual (the genetic information in its cells); phenotype is the outward, observable effect of that genotype on the body, as shaped by environmental factors too."}
      ]
    },
    {
      icon:"atom", title:"Regulation of Transcription by DNA-Binding Proteins",
      blocks:[
        {type:"prose", text:"Transcription factors are proteins that bind to specific DNA sequences to switch genes on or off, giving each cell type and developmental stage its own unique pattern of gene expression. Each transcription factor has a DNA-binding site that lets it bind specific regulatory sequences called enhancers or promoters; regulatory sequences can be thousands of base pairs long and are generally upstream of (before) the gene being transcribed, though they can also lie downstream."},
        {type:"heading", text:"Promoters and enhancers"},
        {type:"prose", text:"A promoter occurs on the DNA strand just before the start of a gene&rsquo;s sequence of bases. Only once a transcription complex &mdash; RNA polymerase plus transcription factors &mdash; has assembled at the promoter can transcription of the gene&rsquo;s template strand begin. Enhancer sequences, when bound by transcription factors, instead increase the transcription of an associated gene: when activator proteins bind an enhancer site, a new complex forms and makes contact with the polymerase&ndash;transcription factor complex at the promoter, increasing the rate of gene expression."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Promoter:</strong> a DNA sequence just before the start of a gene, where RNA polymerase and transcription factors assemble into a transcription complex before transcription can begin.",
          "<strong>Enhancer:</strong> a regulatory DNA sequence, often thousands of base pairs upstream (or downstream) of a gene, which increases the rate of its transcription when bound by activator proteins."
        ]},
        {type:"prose", text:"Regulation of transcription is the most common form of gene control. Because different transcription factors are active in different cell types and at different developmental stages, the same genome can be expressed uniquely in each one."}
      ],
      notes:[
        {label:"Concept: Change", text:"Regulation by transcription factors determines which genes are encoded into proteins within a cell. In this way, the proteome of a cell can change according to the needs of the cell and its function."}
      ]
    },
    {
      icon:"book", title:"Control of mRNA Degradation",
      blocks:[
        {type:"prose", text:"Degrading mRNA once it is no longer needed is itself a form of gene regulation, ensuring that proteins are synthesized only when, and for as long as, they are actually required. After transcription, mRNA is examined, modified and transported to ribosomes, where it is eventually translated into protein; in human cells, an mRNA molecule may persist for anywhere from minutes to days before it is broken down (degraded) by nucleases."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Poly-A tail:</strong> a string of adenine nucleotides added to the 3&prime; end of an mRNA molecule; its shortening is one of the key steps that initiates degradation of the mRNA once it is no longer needed for translation."},
        {type:"prose", text:"The 3&prime; poly-A tail of an mRNA molecule must be degraded (shortened) before the rest of the molecule can be broken down. Controlling the rate of mRNA degradation is therefore a means of regulating translation: it ensures proteins are synthesized only when they are needed, and that mRNA transcripts are removed once their job is done, rather than being translated indefinitely."}
      ],
      notes:[
        {label:"Common mistake", text:"The link between gene expression and cell differentiation is sometimes under-appreciated: genes are selectively expressed to produce the specific proteins a particular cell type needs &mdash; differentiation is a consequence of which genes are switched on, not of different cells carrying different genes."}
      ]
    },
    {
      icon:"atom", title:"Epigenesis, and the Genome, Transcriptome and Proteome",
      blocks:[
        {type:"prose", text:"Epigenesis is the process by which a single, undifferentiated zygote develops into the many specialized cell types of a multicellular organism, determined by the genome and by gene expression; environmental factors can also change gene activity, and these changes can sometimes be passed on to offspring."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Epigenesis:</strong> the development of patterns of differentiation in the cells of a multicellular organism, from an undifferentiated zygote."},
        {type:"prose", text:"The genome &mdash; the whole of an organism&rsquo;s genetic information &mdash; is identical in every cell of a multicellular organism, because all its cells are ultimately derived from one original zygote by cell division. No cell expresses all of its genes at once: expressing a gene costs energy, so it is more efficient for a cell to switch on only the genes it actually needs for its specific structure and function (e.g. digestive enzymes in gut cells, collagen in bone cells)."},
        {type:"heading", text:"Genome, transcriptome and proteome"},
        {type:"prose", text:"The transcriptome is the range of mRNA transcripts produced in a specific cell or tissue type at a particular time, depending on which genes are differentially expressed there; it determines which proteins can be synthesized, which in turn depends on which parts of the genome have been activated. The proteome is all the proteins expressed within a cell, tissue or organism at a given time."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", text:"Because gene expression varies with a cell&rsquo;s function, location and environmental conditions (via differentiation), the proteome &mdash; unlike the stable genome &mdash; is dynamic: one genome (~22 000 genes) gives rise, via alternative promoters, alternative splicing and mRNA editing, to a much larger transcriptome (~200 000 transcripts), which in turn gives rise, via post-translational modification, to an even larger proteome (over one million proteins)."}
      ],
      notes:[
        {label:"Described figure &mdash; genome, transcriptome and proteome (Fig. D2.2.1)", text:"A single genome of around 22 000 genes is expanded, through alternative promoters, alternative splicing and mRNA editing, into a transcriptome of around 200 000 distinct mRNA transcripts; these are expanded further, through post-translational modification, into a proteome of over one million distinct proteins &mdash; illustrating how each successive stage of gene expression multiplies molecular diversity."},
        {label:"Top tip", text:"Every individual has a unique proteome (except monozygotic twins), because the genome &mdash; unique to each individual &mdash; determines which proteome is expressed. Proteomics is the study of the structure and function of an organism&rsquo;s entire set of proteins."}
      ],
      side:{
        title:"Scale of molecular diversity",
        table:{
          title:"Genome, transcriptome and proteome (Fig. D2.2.1)",
          head:["Level","Approx. size"],
          rows:[
            ["Genome","~22 000 genes"],
            ["Transcriptome","~200 000 transcripts"],
            ["Proteome",">1 000 000 proteins"]
          ]
        }
      }
    },
    {
      icon:"atom", title:"Methylation of the Promoter and Histones in Nucleosomes",
      blocks:[
        {type:"prose", text:"Methylation adds a reversible chemical tag directly onto DNA or histone proteins, and this &mdash; not any change to the DNA base sequence &mdash; can switch a gene off or on. Nucleosomes are stable, but not static, protein&ndash;DNA complexes: they can inhibit or facilitate transcription depending on their chemical state."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Methylation:</strong> the reversible addition of a methyl group (&ndash;CH<sub>3</sub>) within chromatin, usually to a cytosine base in DNA at a promoter (sometimes to histone tails); extensive methylation usually inactivates a gene.",
          "<strong>Epigenetic tag:</strong> a chemical tag, such as a methyl or acetyl group, added directly to DNA or to histone proteins to regulate gene expression by blocking or allowing access to a gene&rsquo;s &lsquo;on&rsquo; switch."
        ]},
        {type:"prose", text:"Extensive methylation usually inactivates a gene, repressing transcription and so expression of the gene downstream; removal of methyl groups can switch the gene back on. Methylation of amino acids in histones can either enable or disable the recruitment of regulatory proteins to the chromatin, so repressing or activating transcription."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", text:"Once a gene has been methylated, this state can persist from one cell division to the next, since the methyl groups remain in situ. External conditions adverse to a cell or organism can leave a lasting mark on DNA through extensive methylation, switching genes off."}
      ],
      notes:[
        {label:"Described figure &mdash; DNA methylation (Fig. D2.2.2)", text:"Shows a methyl group added to cytosine within the DNA double helix, converting it to 5-methylcytosine; the diagram marks several other sites along the helix where methylation has also occurred, illustrating that methylation marks accumulate at multiple positions across a stretch of chromatin, not just at a single base."}
      ]
    },
    {
      icon:"leaf", title:"Epigenetic Inheritance Across Generations",
      blocks:[
        {type:"prose", text:"Epigenetic changes acquired by a parent during their lifetime can be passed on to their offspring &mdash; sometimes for several generations &mdash; through modification of chromatin, rather than through any change to the DNA sequence itself."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Epigenetic inheritance:</strong> an inheritance pattern in which modification of chromatin by epigenetic tags alters gene expression; a parent&rsquo;s experiences can be passed to offspring without any change to the DNA base sequence."},
        {type:"prose", text:"This is the acquisition of characteristics gained by a parent during their lifetime and passed on to their offspring, via modification of chromatin through epigenetic tags such as DNA methylation or histone modification; because the DNA nucleotide sequence itself is unchanged, this differs fundamentally from a mutation. It can occur only if the epigenetic tags remain in place through mitosis or meiosis &mdash; if the tags are instead removed during cell division, epigenetic inheritance does not take place."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"In 1944, wartime conditions deprived communities in the western Netherlands of food for over six months (the Dutch famine). Babies born to pregnant mothers who survived the famine were underweight at birth, but despite being fed normally afterwards, grew up to be heavier than average as adults with higher rates of obesity &mdash; as though the parents&rsquo; starvation was imprinted onto the children&rsquo;s DNA, triggering development of greater body mass as a survival strategy."},
        {type:"prose", text:"This evidence challenges the older view, held from Mendel&rsquo;s time through to Watson and Crick&rsquo;s discovery of the chemical nature of the gene, that genes and alleles are unchangeable by external factors and that the environment&rsquo;s only influence is on which alleles survive selection (not on gene performance itself). It now appears that poor diet, for example, can interfere with the performance of genes in succeeding generations, presumably via epigenetic markers attached to the parents&rsquo; DNA."}
      ],
      notes:[
        {label:"Nature of science: Patterns and trends", text:"Methylation can last a lifetime and can be, and often is, transmitted to offspring and sometimes to further generations &mdash; meaning the environment experienced by one generation may have an impact on gene expression for generations to come."}
      ]
    },
    {
      icon:"book", title:"Environmental Effects on Gene Expression",
      blocks:[
        {type:"prose", text:"Gene expression is sensitive to a wide range of external, environmental factors. Many such factors can affect gene expression, including diet, oxygen levels, humidity, light cycles, drugs, temperature and exposure to mutagens."},
        {type:"heading", text:"Air pollution as an example"},
        {type:"prose", text:"Traffic-related air pollution &mdash; particulate matter from diesel vehicles, ozone (O<sub>3</sub>), carbon monoxide (CO) and nitrogen oxides (NO<sub>x</sub>) &mdash; contributes to cardiovascular disease and to lung conditions including asthma and chronic obstructive pulmonary disease (COPD). Recent research indicates that exposure to air pollution can modify DNA and histone methylation patterns, which may in turn affect inflammation and disease development."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"Air pollution exposure is correlated with negative long-term respiratory outcomes, including interstitial lung diseases (ILDs) &mdash; an overall term for diseases causing inflammation of lung tissues (bronchioles, alveoli and the capillaries surrounding the alveoli), leading to scarring and thickening of tissue. In the alveoli, this thickening reduces the rate of oxygen diffusion into the blood; in the bronchioles, inflammation causes asthma. Hypersensitivity pneumonitis (HP), one of the most common forms of ILD, is triggered by inhaling organic and inorganic substances, including air pollutants, and these pollutants influence HP development through epigenetic modification."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", text:"Exercise and B vitamins have been suggested as possible ways to reduce the impact of air pollution on methylation patterns and health."}
      ]
    },
    {
      icon:"leaf", title:"Removal of Epigenetic Tags from Gametes, and Genomic Imprinting",
      blocks:[
        {type:"prose", text:"Human egg and sperm cells erase nearly all epigenetic marks during gamete formation &mdash; though many organisms retain and pass on epigenetic marks acquired from environmental exposure via their gametes. In humans and other mammals, egg and sperm cells undergo extensive reprogramming during development that removes (&lsquo;silences&rsquo;) nearly all epigenetic marks, thought to have evolved to prevent environmentally caused methylation changes from being transmitted across generations. Any tag that is not removed may still affect the development and function of the next generation."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Imprinting:</strong> a process in which only one copy of a gene (maternal or paternal) is expressed in an individual while the other copy is epigenetically silenced during gamete formation &mdash; one of the few epigenetic tags (~1% of genes) that survives reprogramming of the egg and sperm."},
        {type:"prose", text:"For a small minority of genes (approximately 1%), epigenetic tags survive this reprogramming and pass unchanged from parent to offspring, through imprinting: epigenetic tags are added to DNA during gametogenesis (gamete formation by meiosis), switching &lsquo;on&rsquo; some parts of the DNA and &lsquo;off&rsquo; other parts. For most genes, two working copies are inherited, one from each parent; for imprinted genes, only one working copy is inherited, because differential silencing means that either the maternal copy or the paternal copy is epigenetically silenced, depending on the gene. In sperm development, maternal tags are silenced; in egg development, paternal tags are silenced."},
        {type:"heading", text:"Tigons and ligers"},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"Tigons and ligers, both lion&ndash;tiger hybrids, reveal imprinting&rsquo;s effects: a male tiger (160&ndash;230 kg) crossed with a female lion (120&ndash;180 kg) produces a tigon about the same size as, or smaller than, either parent, while a female tiger (140&ndash;180 kg) crossed with a male lion (170&ndash;230 kg) produces a liger exceeding 400 kg &mdash; much bigger than either parent species."},
        {type:"prose", text:"The difference is explained by different imprinting patterns, thought to reflect each species&rsquo; mating system. Because female lions may mate with multiple males, a male lion&rsquo;s genes benefit from encouraging extra growth in his own cubs relative to potential half-siblings in the same litter; in response, female lions have evolved anti-growth imprinted genes, since a lioness is equally related to all her cubs and gains from distributing resources equally to maximize the number that survive. Female tigers typically mate with only one male per litter, who is equally related to all the cubs, so male tigers have not evolved growth-promoting imprinted genes, and female tigers have not evolved anti-growth defences against them. Crossing a female tiger (lacking anti-growth imprinting) with a male lion (which does contribute growth-encouraging genes) therefore produces the oversized liger."}
      ],
      notes:[
        {label:"Common mistake", text:"Do not confuse genetic imprinting with a different type of imprinting, such as animal behavioural imprinting (e.g. young birds following their mother) &mdash; the two are unrelated phenomena that happen to share a name."}
      ],
      side:{
        title:"Tigons vs ligers: parent and offspring size",
        table:{
          title:"Approximate adult body mass",
          head:["Cross","Mother","Father","Offspring"],
          rows:[
            ["Tigon","Female lion (120&ndash;180 kg)","Male tiger (160&ndash;230 kg)","&asymp; same size as, or smaller than, parents"],
            ["Liger","Female tiger (140&ndash;180 kg)","Male lion (170&ndash;230 kg)","&gt;400 kg"]
          ]
        }
      }
    },
    {
      icon:"atom", title:"Monozygotic Twin Studies",
      blocks:[
        {type:"prose", text:"Monozygotic (identical) twin studies let biologists estimate how much of a phenotypic trait is due to genes (&lsquo;nature&rsquo;) versus environment (&lsquo;nurture&rsquo;), because identical twins share an identical genome. No two members of a family, other than identical twins, are genetically identical; differences between relatives can be due to genetic factors (e.g. blood group), environmental factors (e.g. a suntan), or a combination of both (e.g. height and body mass)."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Monozygotic twins:</strong> identical twins, resulting from a single fertilized egg that splits into two early in development; they share the same genome and are always the same sex.",
          "<strong>Dizygotic twins:</strong> non-identical twins, developing from two separately fertilized eggs, each with its own distinct combination of alleles."
        ]},
        {type:"prose", text:"Monozygotic twins develop from a single fertilized egg that splits into two early in development, so they cannot be distinguished by DNA fingerprinting; dizygotic twins, developing from two separately fertilized eggs, can be distinguished this way. Twin studies compare monozygotic and dizygotic twins raised together or apart. If separated monozygotic twins closely resemble each other for a trait, that trait is probably mainly genetic; if they differ significantly, environment is probably more important. Because monozygotic twins share all their genes, any difference between them must be due to non-shared environmental influences; if both monozygotic and dizygotic twins resemble each other closely, shared environment is probably responsible; and if monozygotic twins resemble each other more closely than dizygotic twins do, genetic factors likely play a role."},
        {type:"prose", text:"Although monozygotic twins share an identical genotype, most are not perfectly identical in physical features or disease predisposition &mdash; explained by epigenetic differences (DNA methylation and histone acetylation) that accumulate over each twin&rsquo;s lifetime; methylation levels tend to increase with age."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"In a 1990 study published in <em>The New England Journal of Medicine</em>, geneticist Claude Bouchard fed male monozygotic twins an extra 1000 calories a day for three months. Every participant gained weight, but weight gain within each pair of twins was much more similar than weight gain between different twin pairs, and twins in each pair tended to gain weight in the same body regions &mdash; suggesting that genetic factors strongly influence body-fat storage."}
      ]
    },
    {
      icon:"book", title:"External Factors: Hormones and the Lac Operon",
      blocks:[
        {type:"prose", text:"External signals &mdash; from steroid hormones in animals to the presence or absence of a nutrient in bacteria &mdash; can switch gene expression on or off from outside the cell. Steroid hormones such as oestradiol, progesterone and testosterone affect gene expression by binding to receptors in the cytoplasm; these receptor complexes act as ligand-gated transcription factors that, with the help of co-activators and co-repressors, bind to DNA to alter transcription."},
        {type:"heading", text:"The lac operon"},
        {type:"prose", text:"In bacteria, gene expression is most commonly controlled at the level of transcription (how much mRNA is made), though translational-level control (the rate of translation of mRNA into protein) also occurs. In prokaryotes, an operon is a region of DNA containing a group of closely related structural genes plus regulatory elements &mdash; a promoter, an operator and a terminator; structural genes encode the enzymes of a metabolic pathway, and the operator determines whether they are transcribed."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Operon:</strong> a sequence of adjacent bacterial genes, found only in prokaryotes, all under the transcriptional control of the same operator.",
          "<strong>Operator:</strong> a DNA region at one end of an operon that acts as the binding site for a repressor protein; when bound by the repressor, transcription of the operon is prevented.",
          "<strong>Repressor &amp; inducer:</strong> repressor &mdash; the protein product of a regulator gene that binds the operator and blocks transcription; inducer &mdash; a small molecule (e.g. lactose) that inactivates a repressor by binding to it, switching transcription on."
        ]},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"<em>E. coli</em>, found in the human gut, gains access to lactose when we drink milk. The lac operon ensures <em>E. coli</em> only produces lactose-metabolizing enzymes when lactose is actually present, avoiding wasted energy and resources. The mechanism involves a repressor (coded for by a regulator gene), an operator next to the structural gene it controls, and a promoter."},
        {type:"prose", text:"When lactose is absent, no lactose is available to bind the repressor, so the repressor binds the operator and physically blocks RNA polymerase from binding the promoter &mdash; the structural gene for the lactose-metabolizing enzyme (lactase) is not transcribed. When lactose is present, it binds to and changes the shape of the repressor, so the repressor can no longer bind the operator; RNA polymerase can then bind the promoter and transcribe the structural gene, and the resulting mRNA passes to ribosomes where lactase is synthesized. Once all the lactose has been metabolized, the repressor is free to bind the operator again, switching the gene back off."},
        {type:"prose", text:"The lac operon is therefore an inducible operon: transcription is normally switched off but is turned on by a small effector molecule called the inducer (here, lactose). The repressor&rsquo;s ability to bind the operator depends on its conformation, which is allosterically regulated by the inducer, so the inducer&rsquo;s concentration determines the operon&rsquo;s activity. Operons are found only in prokaryotes; the regulatory mechanisms of eukaryotes are more complex."}
      ],
      side:{
        title:"The lac operon: on or off",
        table:{
          title:"Lac operon state",
          head:["Condition","Repressor","Operon"],
          rows:[
            ["Lactose absent","Binds operator","Off (not transcribed)"],
            ["Lactose present","Inactivated, releases operator","On (transcribed)"]
          ]
        }
      }
    },
    {
      icon:"atom", title:"The trp Operon: A Repressible System",
      blocks:[
        {type:"prose", text:"The trp operon works by the opposite logic to the lac operon: it is normally switched on, and is only switched off once the amino acid it makes, tryptophan, has accumulated enough to repress it. <em>E. coli</em> synthesizes the amino acid tryptophan from a precursor molecule through a series of metabolic steps, each catalysed by a specific enzyme; the five coding regions for these tryptophan-synthesizing enzymes (starting with trpE) are arranged sequentially in the trp operon, and when <em>E. coli</em> needs to make its own tryptophan, all five enzymes in the pathway are synthesized together."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Trp operon:</strong> a repressible operon, normally on, switched off once tryptophan (a co-repressor) accumulates.",
          "<strong>Lac operon:</strong> an inducible operon that switches on only when lactose is present."
        ]},
        {type:"prose", text:"The trp repressor is the product of a regulatory gene, trpR, located some distance from the operon it controls and with its own promoter. It is synthesized in an inactive form with little affinity for the trp operator; only once tryptophan binds to the repressor does it change to an active form that can bind the operator and inhibit transcription of the structural genes."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", text:"Tryptophan therefore acts as a co-repressor &mdash; in contrast to lactose, which acts as an inducer in the lac operon &mdash; cooperating with the repressor protein to switch the operon off. As tryptophan accumulates, more tryptophan molecules bind the trp repressor, which can then bind the trp operator and inhibit synthesis of the tryptophan-biosynthesis enzymes."}
      ],
      notes:[
        {label:"Lac operon vs trp operon", text:"The lac operon is <strong>inducible</strong> (normally off, switched on by its small molecule, lactose, which inactivates the repressor); the trp operon is <strong>repressible</strong> (normally on, switched off by its small molecule, tryptophan, which activates the repressor). In both cases, the same metabolic economy is achieved: enzymes are made only when they are actually needed."}
      ],
      side:{
        title:"Comparing the two bacterial operons",
        table:{
          title:"Lac operon vs trp operon",
          head:["Feature","Lac operon","Trp operon"],
          rows:[
            ["Type","Inducible","Repressible"],
            ["Normal state","Off","On"],
            ["Small molecule","Lactose (inducer)","Tryptophan (co-repressor)"],
            ["Effect of binding repressor","Inactivates it","Activates it"]
          ]
        }
      }
    }
  ],
  workedExamples: [
    {
      title:"Reasoning about the lac operon",
      question:"<em>E. coli</em> cells are grown in a medium containing no lactose. (a) State whether the lac repressor is bound to the operator under these conditions, and explain the consequence for transcription of the structural gene for lactase. (b) Lactose is then added to the medium. Explain, in terms of the repressor and operator, how the lac operon responds.",
      answer:[
        "(a) With no lactose present, no inducer molecule is available to bind the repressor, so the repressor remains free to bind to the operator. This physically blocks RNA polymerase from binding to the promoter, so the structural gene for lactase is not transcribed &mdash; the operon is switched off.",
        "(b) Once lactose is added, it binds to the repressor protein and changes its conformation (shape), so that it can no longer bind the operator. RNA polymerase can now bind the promoter and transcribe the structural gene; the resulting mRNA is translated at ribosomes to produce lactase, which metabolizes the available lactose. The lac operon is an inducible operon, since lactose (the inducer) switches its transcription on."
      ]
    },
    {
      title:"Comparing the lac and trp operons",
      question:"Both the lac operon and the trp operon are controlled by repressor proteins, yet one is described as inducible and the other as repressible. Distinguish between these two operons, explaining the role of the small molecule involved in each case.",
      answer:[
        "The lac operon is inducible: it is normally switched off, and lactose acts as an inducer, binding to the repressor and inactivating it so that it can no longer bind the operator &mdash; this switches transcription on.",
        "The trp operon is repressible: it is normally switched on, and tryptophan acts as a co-repressor, binding to an otherwise-inactive repressor and activating it so that it can now bind the operator &mdash; this switches transcription off.",
        "Both systems achieve the same underlying metabolic economy by opposite means: genes are transcribed only when their expression is actually useful to the cell &mdash; the lac operon&rsquo;s enzymes only when lactose is available to metabolize, and the trp operon&rsquo;s enzymes only when tryptophan is not already abundant enough to make its own synthesis unnecessary."
      ]
    },
    {
      title:"Explaining tigon and liger body size from imprinting",
      question:"Using the concept of genomic imprinting, explain why a liger (the offspring of a male lion and a female tiger) grows much larger than a tigon (the offspring of a male tiger and a female lion), even though both crosses combine lion and tiger genes.",
      answer:[
        "Female lions typically mate with multiple males, so a male lion&rsquo;s genes benefit evolutionarily from promoting extra growth in his own cubs relative to any half-siblings in the same litter; in response, female lions have evolved anti-growth imprinted genes, since a lioness is equally related to all her cubs and gains from distributing resources equally among them.",
        "Female tigers, in contrast, typically mate with only one male per litter, who is equally related to all the cubs; male tigers have therefore not evolved growth-promoting imprinted genes, and female tigers have not evolved any anti-growth imprinting defence against them.",
        "In a liger (father = lion, mother = tiger), the father&rsquo;s growth-promoting imprinted genes are inherited, and the tiger mother has no anti-growth imprinting defence to oppose them &mdash; so growth proceeds unchecked, producing an unusually large hybrid.",
        "In a tigon (father = tiger, mother = lion), the father (tiger) does not contribute growth-promoting imprinted genes, while the mother (lion) does contribute her anti-growth imprinted genes &mdash; so the tigon grows to about the same size as, or smaller than, its parents."
      ]
    },
    {
      title:"Distinguishing genome, transcriptome and proteome",
      question:"A liver cell and a skin cell from the same person both contain the full human genome of about 22 000 genes. Explain why the two cell types nevertheless have different proteomes, using the terms transcriptome and gene expression in your answer.",
      answer:[
        "The genome in the liver cell and the skin cell is identical, since both cells are ultimately derived from the same original zygote by cell division.",
        "However, each cell type expresses (switches on) only the subset of genes required for its own specific structure and function &mdash; this differential gene expression produces a different transcriptome (range of mRNA transcripts) in each cell type.",
        "Because the proteome is built from whichever mRNA transcripts are present, and is further diversified by alternative splicing, mRNA editing and post-translational modification, the two cell types end up producing different sets of proteins (e.g. digestive and metabolic enzymes in the liver, versus keratin in the skin), even though their underlying genome is the same."
      ]
    },
    {
      title:"Interpreting a monozygotic twin study",
      question:"A pair of monozygotic twins raised in different households is found to have very similar IQ scores, while a pair of dizygotic twins raised in the same household has quite different IQ scores. Explain what these two observations together suggest about the relative importance of genetic and environmental factors in determining IQ.",
      answer:[
        "Monozygotic twins share an identical genome; if they were raised apart (in different environments) but still show similar IQ scores, this similarity is unlikely to be due to a shared environment, pointing instead towards genetic factors being important in determining IQ.",
        "Dizygotic twins do not share an identical genome (they are no more genetically similar than ordinary siblings); if they were raised together (the same environment) but still show quite different IQ scores, this suggests that a shared environment alone does not account for IQ, reinforcing that genetic differences matter.",
        "Taken together, both observations are consistent with IQ being substantially influenced by genetic factors (&lsquo;nature&rsquo;) rather than being determined mainly by shared environment (&lsquo;nurture&rsquo;) &mdash; though a full twin study would need many such twin pairs to draw a reliable general conclusion, since environmental factors can still contribute to variation within genetically identical individuals (e.g. via epigenetic differences accumulating over a lifetime)."
      ]
    }
  ],
  summary: [
    "Gene expression is the mechanism by which the genetic code (via transcription into mRNA and translation into protein) determines the phenotype; it operates throughout the course, from switching genes on and off in transcription to hormone and auxin signalling.",
    "Transcription factors bind specific regulatory DNA sequences (enhancers, promoters) to switch genes on or off; a transcription complex of RNA polymerase and transcription factors must assemble at the promoter before transcription can begin.",
    "mRNA degradation, initiated by shortening of the 3&prime; poly-A tail, regulates translation by ensuring proteins are made only when needed and by removing transcripts once their job is done.",
    "Epigenesis is the development of differentiated cell types from one zygote; although every cell in a multicellular organism shares an identical genome, differential gene expression produces a distinct transcriptome and proteome in each cell type or tissue.",
    "The genome (~22 000 genes) is stable and amplified via alternative promoters, alternative splicing and mRNA editing into a much larger transcriptome (~200 000 transcripts), which is further amplified via post-translational modification into an even larger, highly dynamic proteome (over 1 million proteins).",
    "Methylation &mdash; the reversible addition of a methyl group to cytosine in DNA (or to histone tails) &mdash; is an epigenetic tag that usually represses transcription of the gene downstream, without altering the DNA base sequence itself, and can persist across cell divisions.",
    "Epigenetic inheritance lets a parent&rsquo;s environmentally acquired epigenetic changes affect their offspring&rsquo;s gene expression, as shown by the Dutch famine (1944) studies; many external factors (diet, oxygen, drugs, temperature, mutagens, air pollution) can alter gene expression via such epigenetic tags.",
    "During gamete formation, human egg and sperm cells erase almost all epigenetic tags, but roughly 1% of genes escape this reprogramming through imprinting, in which only the maternal or only the paternal copy of a gene is expressed &mdash; as dramatically illustrated by the very different sizes of tigons and ligers.",
    "Monozygotic (identical) twins share an identical genome, letting twin studies estimate the relative contribution of genetic (&lsquo;nature&rsquo;) versus environmental (&lsquo;nurture&rsquo;) factors to a trait; differences between monozygotic twins are attributed to epigenetic changes accumulated over their separate lifetimes.",
    "External signals regulate gene expression from outside the cell: steroid hormones act as ligand-gated transcription factors, while in bacteria, operons (found only in prokaryotes) couple structural genes to regulatory promoter, operator and terminator sequences.",
    "The lac operon is inducible (normally off, switched on when lactose inactivates its repressor); the trp operon is repressible (normally on, switched off when tryptophan activates its repressor as a co-repressor) &mdash; opposite strategies achieving the same metabolic economy."
  ]
}
