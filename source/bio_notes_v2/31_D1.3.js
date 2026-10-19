{
  unified: true,
  subtitle: "A gene mutation is a change in the base sequence of a gene &mdash; the ultimate source of all genetic variation. This chapter covers how mutations arise, what their molecular and phenotypic consequences can be, and how scientists have learned to deliberately engineer them, from knocking out single genes to editing genomes with CRISPR-Cas9.",
  keyTerms: [
    {icon:"atom", color:"green", term:"Gene mutation", def:"A change in the sequence of bases of a particular gene."},
    {icon:"bars", color:"teal", term:"Point mutation", def:"A change in a single base of a gene sequence, resulting from the substitution, insertion or deletion of a base or bases."},
    {icon:"atom", color:"gold", term:"Substitution", def:"A type of mutation in which one nucleotide is replaced by a different nucleotide."},
    {icon:"leaf", color:"plum", term:"Insertion", def:"A type of mutation that involves the addition of one or more nucleotides into a segment of DNA."},
    {icon:"bars", color:"red", term:"Deletion", def:"A type of mutation that involves the loss of one or more nucleotides from a segment of DNA."},
    {icon:"atom", color:"teal", term:"Frameshift", def:"A mutation that occurs when the number of nucleotides inserted or deleted is not a multiple of three, so that every codon beyond the point of mutation is read incorrectly during translation."},
    {icon:"leaf", color:"gold", term:"Nonsense &amp; missense mutation", def:"Nonsense: a mutation that produces a codon with no meaning, so the genetic code cannot be read. Missense: a mutation that causes a different amino acid to be coded for."},
    {icon:"bars", color:"green", term:"Mutagen", def:"An agent that causes gene mutations; anything that causes a mutation may also cause cancer, e.g. chemicals in tobacco smoke, X-rays, short-wave UV light and some viruses."},
    {icon:"atom", color:"plum", term:"Transition", def:"A substitution between bases of similar shape: purine&harr;purine (adenine&harr;guanine) or pyrimidine&harr;pyrimidine (cytosine&harr;thymine)."},
    {icon:"leaf", color:"red", term:"Transversion", def:"A substitution between a purine base and a pyrimidine base."},
    {icon:"bars", color:"gold", term:"SNP", def:"Single-nucleotide polymorphism: a difference of a single base pair at one position in the genome, resulting from a base substitution mutation."},
    {icon:"atom", color:"green", term:"Germ cell &amp; germ line mutation", def:"Germ cell: a reproductive cell of the body (in the ovaries, testes, or the anthers/embryo sacs of flowering plants). Germ line mutation: a mutation arising in a germ cell, which may therefore be passed to offspring."},
    {icon:"leaf", color:"teal", term:"Somatic mutation", def:"A mutation arising in a body cell, passed only to that cell&rsquo;s descendants within the same organism; never inherited by offspring, though it can still contribute to cancer."},
    {icon:"bars", color:"plum", term:"Trinucleotide repeat disorder", def:"A disorder caused by an abnormal number of repeats of a three-base sequence within a gene, e.g. the CAG repeat of the <em>HTT</em> gene in Huntington&rsquo;s disease."},
    {icon:"atom", color:"red", term:"Allele", def:"An alternative form of a gene, created by random mutation, occupying a specific locus on a chromosome."},
    {icon:"leaf", color:"gold", term:"Gene knockout (KO)", def:"<strong>HL</strong> &mdash; A technique that produces a genetically engineered organism with one non-functional gene, allowing researchers to investigate the function of that gene."},
    {icon:"bars", color:"green", term:"Model organism", def:"<strong>HL</strong> &mdash; A non-human organism, such as the mouse (<em>Mus musculus</em>) or <em>Drosophila melanogaster</em>, used to understand simple and complex biological functions."},
    {icon:"atom", color:"teal", term:"Mutant", def:"<strong>HL</strong> &mdash; An organism with altered genetic material, abruptly altered by a mutation."},
    {icon:"leaf", color:"plum", term:"CRISPR sequences", def:"<strong>HL</strong> &mdash; Sequences in the genomes of some prokaryotes that act as a genomic record of previous viral attack."},
    {icon:"bars", color:"red", term:"Cas9 enzyme", def:"<strong>HL</strong> &mdash; A bacterial endonuclease that forms a double-strand break in DNA at a specific target site within a larger recognition sequence."},
    {icon:"atom", color:"gold", term:"Genome editing", def:"<strong>HL</strong> &mdash; The manipulation of DNA by deleting, replacing or inserting a DNA sequence, for example to correct a genetic disorder."},
    {icon:"leaf", color:"green", term:"Conserved sequences", def:"<strong>HL</strong> &mdash; Identical or similar sequences in nucleic acids (DNA and RNA), across species or a group of species, that have remained essentially unchanged throughout evolution."}
  ],
  theories: [
    {
      icon:"atom", title:"Gene Mutations as Structural Changes to DNA",
      blocks:[
        {type:"prose", text:"A gene mutation is a change in the base sequence of a gene, arising from uncorrected errors during DNA replication or from exposure to environmental mutagens. DNA polymerase &lsquo;proofreads&rsquo; and corrects most errors as it builds a complementary DNA strand during replication, but this proofreading, although highly efficient, does not correct every error, so gene mutations can and do arise spontaneously during replication. Environmental factors &mdash; including ionising radiation, UV light and various chemicals &mdash; can also alter the DNA base sequence directly."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Point mutation:</strong> a change in a single base of a gene sequence, resulting from the substitution, insertion or deletion of a base or bases.",
          "<strong>Substitution:</strong> a type of mutation in which one nucleotide is replaced by a different nucleotide.",
          "<strong>Insertion:</strong> a type of mutation that involves the addition of one or more nucleotides into a segment of DNA.",
          "<strong>Deletion:</strong> a type of mutation that involves the loss of one or more nucleotides from a segment of DNA."
        ]},
        {type:"prose", text:"Because bases are read in triplets (codons) during translation, an insertion or deletion whose length is not a multiple of three produces a frameshift: every codon beyond the point of mutation is shifted out of register and read incorrectly. Some substitutions produce a &lsquo;nonsense&rsquo; mutation, where the changed codon cannot be read and has no meaning; if a substitution instead causes a different amino acid to be coded for, it is called a &lsquo;missense&rsquo; mutation."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Frameshift:</strong> a mutation that occurs when the number of nucleotides inserted or deleted is not a multiple of three, so that every codon beyond the point of mutation is read incorrectly during translation.",
          "<strong>Nonsense mutation:</strong> a mutation that produces a codon with no meaning, so the genetic code cannot be read. <strong>Missense mutation:</strong> a mutation that causes a different amino acid to be coded for."
        ]}
      ],
      notes:[{label:"Common mistake", text:"Mutations are not automatically harmful. Because of the degeneracy of the genetic code, and because much of the genome is non-coding, many mutations have a neutral effect; others can be beneficial, giving an adaptive advantage, while some are harmful, leading to deleterious effects on the organism."}]
    },
    {
      icon:"book", title:"Consequences of Base Substitutions",
      blocks:[
        {type:"prose", text:"Whether a base substitution actually changes the proteome depends on exactly where it falls, and on whether the degeneracy of the genetic code buffers its effect."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"Sickle-cell anaemia is caused by a single base change in the codon for glutamic acid, causing the amino acid valine to be incorporated into the polypeptide instead."},
        {type:"prose", text:"However, because the genetic code is degenerate &mdash; most amino acids have several possible codons &mdash; a base substitution may still match an alternative codon for the same amino acid, leaving the polypeptide, and so the cell&rsquo;s proteome, completely unaffected. A substitution in a non-coding region of DNA may likewise have a neutral effect on the proteome. But a substitution within a regulatory region that directs a gene&rsquo;s expression can prevent that gene from being expressed at all, significantly affecting the proteins found in the cell."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>SNP (single-nucleotide polymorphism):</strong> a difference of a single base pair at one position in the genome, resulting from a base substitution mutation."}
      ]
    },
    {
      icon:"leaf", title:"Consequences of Insertions and Deletions: Two Case Studies",
      blocks:[
        {type:"prose", text:"Major insertions and deletions, including the frameshifts they can cause, increase the likelihood that a polypeptide fails to function &mdash; illustrated by an insertion that causes Huntington&rsquo;s disease and a deletion that confers partial resistance to HIV."},
        {type:"heading", text:"Insertion: Huntington&rsquo;s disease"},
        {type:"prose", text:"The <em>HTT</em> gene normally contains a CAG trinucleotide repeat segment 10 to 35 copies long; repeats within this normal range are even associated with higher cognitive function. An insertion mutation that expands the repeat beyond 39 copies causes Huntington&rsquo;s disease, a neurodegenerative disorder involving progressive mental deterioration accompanied by involuntary muscle movements."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", items:[
          "Huntington&rsquo;s disease is extremely rare &mdash; about 1 case per 20 000 live births.",
          "It is caused by a mutated dominant allele, so it tends to appear in one or more members of every generation in a family pedigree chart.",
          "Symptoms usually do not appear until the affected person is 40&ndash;50 years old, by which time they may unknowingly have already passed the allele on to their children."
        ]},
        {type:"heading", text:"Deletion: HIV resistance"},
        {type:"prose", text:"The delta 32 mutation removes a section of the <em>CCR5</em> gene, preventing functional expression of the CCR5 protein co-receptor that most HIV-1 strains need to enter CD4<sup>+</sup> T-cells (the lymphocytes responsible for cell-mediated immunity). Without a functional receptor, HIV can no longer efficiently bind to and enter the cell &mdash; though resistance is not complete, since the virus can use alternative, less-efficient co-receptors."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"People who inherit two copies of the delta 32 allele are significantly less susceptible to HIV-1 infection. The mutation is thought to have arisen as long as 2500 years ago, when it was rare (about 1 in 20 000 Europeans); it is now found in around 1 in 10 people, suggesting a past viral disease provided the selection pressure that increased its frequency over time."}
      ],
      notes:[{label:"Described figure &mdash; Huntington&rsquo;s disease (Fig. D1.3.1)", text:"Illustrates how successive insertions progressively lengthen the CAG trinucleotide repeat within the <em>HTT</em> gene, moving it from the normal range (10&ndash;35 repeats) into the disease-causing range (beyond 39 repeats)."}]
    },
    {
      icon:"atom", title:"Causes of Gene Mutation",
      blocks:[
        {type:"prose", text:"A mutagen is any factor that increases the mutation rate; beyond mutagens, mutation also arises from the small fraction of DNA replication and repair errors that escape correction."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Mutagen:</strong> an agent that causes gene mutations; anything that causes a mutation may also cause cancer, e.g. chemicals in tobacco smoke, X-rays, short-wave UV light and some viruses. A factor&rsquo;s effects are described as &lsquo;mutagenic&rsquo;, and many mutagens are also carcinogens, since a mutation can trigger the uncontrolled cell division of cancer."},
        {type:"prose", text:"As well as by mutagens, mutation can be caused by errors in DNA replication or repair. DNA polymerase proofreads during replication to ensure the base code is copied correctly, removing most mistakes."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", text:"It is estimated that, in eukaryotes, DNA polymerase makes an error approximately once every 10<sup>4</sup>&ndash;10<sup>5</sup> nucleotides copied &mdash; meaning that each time a diploid mammalian cell replicates its genome, between 100 000 and 1 000 000 polymerase errors occur. Most are corrected, but when the correction mechanism fails, a mutation results; if the error lies within a coding sequence, the protein synthesized may be changed."}
      ],
      side:{
        title:"Principal mutagenic factors",
        table:{
          title:"Factors that increase mutation rate and cancer risk",
          head:["Factor","Effect"],
          rows:[
            ["Ionising radiation","X-rays and radiation (&gamma; rays, &alpha; and &beta; particles) from radioactive sources trigger damaging ions/radicals in the nucleus, breaking up DNA"],
            ["Non-ionising radiation (UV)","Less penetrating than ionising radiation, but absorbed by nitrogenous bases, causing adjacent bases on one strand to bind to each other instead of their partner (thymine dimers)"],
            ["Bacterial infection","Some infections trigger cancer directly, e.g. <em>Helicobacter pylori</em> and stomach cancer"],
            ["Chemicals","Carcinogens in tobacco smoke; prolonged asbestos exposure can trigger pleural cancer, often only apparent years later"],
            ["Virus infection","e.g. hepatitis B/C, HPV and HIV; HPV inserts part of its genome into the host, producing proteins that disrupt cell cycle control"]
          ]
        }
      }
    },
    {
      icon:"book", title:"Randomness in Mutation: Transitions, Transversions and Hotspots",
      blocks:[
        {type:"prose", text:"Mutation is random in the sense that no natural mechanism deliberately alters a particular base to produce a desired trait &mdash; mutations are more likely at certain points in the cell cycle (e.g. during DNA replication) than at others, but evolution by natural selection selects among alleles that random mutation has already generated, rather than creating new alleles deliberately; there is no known natural way to target a specific base for change."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Transition:</strong> a substitution between bases of similar shape &mdash; purine&harr;purine (adenine&harr;guanine) or pyrimidine&harr;pyrimidine (cytosine&harr;thymine).",
          "<strong>Transversion:</strong> a substitution between a purine base and a pyrimidine base."
        ]},
        {type:"prose", text:"Transitions are more common than transversions because they preserve the overall ring-shape structure of the base pair, and &mdash; thanks to the degeneracy of the genetic code &mdash; are less likely to change the amino acid encoded. They therefore more often persist as &lsquo;silent substitutions&rsquo; (SNPs with no phenotypic effect), though not every SNP is a transition."},
        {type:"heading", text:"Mutational hot spots"},
        {type:"prose", text:"The most commonly mutated sequence is CG (&lsquo;CpG&rsquo;). Proofreading is &lsquo;blind&rsquo; to the location of the bases it corrects, yet CpG sites mutate particularly often: both C and G form three hydrogen bonds with their partner base, holding this stretch of DNA more tightly together, and CpG-rich regions are often heavily methylated &mdash; both factors make proofreading more difficult. Mutation &lsquo;hot spots&rsquo; also arise from variation in the large-scale organisation (&lsquo;superstructure&rsquo;) of DNA within chromosomes, and from regions where accessory proteins are scarcer, raising the local error rate above the correction rate. Environmentally induced mutations are similarly biased, since exposure to different mutagenic stimuli is not equally likely for every individual."}
      ],
      side:{
        table:{
          title:"Transition vs transversion",
          head:["Type","Base change","Relative frequency"],
          rows:[
            ["Transition","Purine&harr;purine or pyrimidine&harr;pyrimidine","More common; often silent"],
            ["Transversion","Purine&harr;pyrimidine","Less common"]
          ]
        }
      }
    },
    {
      icon:"leaf", title:"Germ Line and Somatic Mutations; Mutation as the Source of Variation",
      blocks:[
        {type:"prose", text:"Whether a mutation can be inherited depends entirely on which cells it occurs in &mdash; yet whichever cells it arises in, mutation remains the ultimate original source of all genetic variation."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Germ line mutation:</strong> a mutation arising in a germ cell &mdash; a reproductive cell of the body, in the ovaries, testes, or the anthers/embryo sacs of flowering plants &mdash; which may therefore be passed to offspring and can cause inherited diseases such as Huntington&rsquo;s disease.",
          "<strong>Somatic mutation:</strong> a mutation arising in a body cell, passed only to that cell&rsquo;s descendants within the same organism; never inherited by offspring, though it can still contribute to cancer &mdash; somatic mutations disappear when the organism dies."
        ]},
        {type:"prose", text:"Alleles &mdash; different versions of the same gene &mdash; are created by random mutation; this makes gene mutation the original source of all genetic variation between individuals, with no two individuals identical in all their traits."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", text:"Many mutations affecting non-coding DNA are neutral, with no phenotypic effect; others are harmful (e.g. sickle-cell anaemia). But because all individuals in a population differ slightly, a change in the environment can give some individuals a selective advantage, altering the gene pool of the population over time &mdash; and if reproductive isolation then occurs, speciation can take place."}
      ],
      notes:[{label:"Described figure &mdash; variation in ladybird beetles (Fig. D1.3.4)", text:"Shows the wide range of colour and patterning found among ladybird beetles, illustrating how this kind of diversity within a species accumulates from mutations occurring over many generations."}]
    },
    {
      icon:"atom", hl:true, title:"Gene Knockout and Model Organisms",
      blocks:[
        {type:"prose", text:"Deliberately disabling (&lsquo;knocking out&rsquo;) a single gene in a model organism and observing the resulting phenotype is a powerful way to discover that gene&rsquo;s normal function."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Gene knockout (KO):</strong> a technique that produces a genetically engineered organism with one non-functional gene &mdash; usually by introducing a deletion &mdash; allowing researchers to investigate the function of that gene by comparing the knockout&rsquo;s phenotype with a normal individual&rsquo;s.",
          "<strong>Model organism:</strong> a non-human organism used to understand simple and complex biological functions more generally."
        ]},
        {type:"callout", style:"example", icon:"leaf", title:"Example", items:[
          "The <strong>p53 KO mouse</strong> carries a disabled version of the <em>p53</em> gene, which normally directs synthesis of a protein that regulates the cell cycle; without this protein, tumour cells form, raising the risk of bone and other cancers.",
          "The <strong>Methuselah KO mouse</strong> shows increased longevity, letting researchers study the biology of ageing.",
          "The <strong>obese KO mouse</strong> shows increased body fat and metabolic disorders, giving insight into the genetics of human obesity."
        ]},
        {type:"prose", text:"Model organisms work because the genetic code is universal and basic biological processes &mdash; such as oxidative phosphorylation during aerobic respiration &mdash; are shared by almost all living organisms, so in vivo findings using model organisms can often predict similar effects in closely related species, including humans."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", text:"Following the development of the gene knockout technique, the 2007 Nobel Prize in Physiology or Medicine was awarded to Mario Capecchi, Martin Evans and Oliver Smithies; a library of knockout organisms now exists for several species, supporting ongoing research."}
      ],
      side:{
        title:"Common model organisms",
        table:{
          title:"Model organisms and their uses",
          head:["Organism","Example use"],
          rows:[
            ["<em>Caenorhabditis elegans</em> (roundworm)","Organ development and programmed cell death (apoptosis)"],
            ["<em>Drosophila melanogaster</em> (fruit fly)","High homology with human cells; studying Parkinson&rsquo;s and Alzheimer&rsquo;s disease"],
            ["<em>Danio rerio</em> (zebrafish)","Transparent embryos allow in vivo imaging of the circulatory system and metastasis"],
            ["<em>Arabidopsis thaliana</em> (flowering plant)","First plant genome sequenced; floral production and stress responses"]
          ]
        }
      }
    },
    {
      icon:"atom", hl:true, title:"CRISPR-Cas9: From Bacterial Immunity to Gene Editing",
      blocks:[
        {type:"prose", text:"CRISPR-Cas9 is a natural bacterial defence against viruses that scientists have repurposed into a precise tool for editing any genome, including the human genome."},
        {type:"heading", text:"Natural bacterial immunity"},
        {type:"prose", text:"When infected by a bacteriophage, bacteria cut up the invading viral DNA and insert fragments (&lsquo;spacers&rsquo;) into their own genome as CRISPR sequences &mdash; a genomic memory of the infection. Bacteria transcribe these spacers into RNA, which forms a complex with the Cas9 enzyme; this complex monitors the cell for any DNA sequence complementary to the spacer RNA. When matching (viral) DNA is found, Cas9 is activated and cuts it, halting the infection."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>CRISPR sequences:</strong> sequences in the genomes of some prokaryotes that act as a genomic record of previous viral attack.",
          "<strong>Cas9 enzyme:</strong> a bacterial endonuclease that forms a double-strand break in DNA at a specific target site within a larger recognition sequence."
        ]},
        {type:"heading", text:"Laboratory gene editing"},
        {type:"prose", text:"Cas9 is directed to a specific target sequence by a complementary guide RNA. The Cas9&ndash;guide RNA complex binds the target and cuts the DNA there, removing the unwanted sequence; a desired sequence, supplied via a DNA template, can then be inserted in its place, producing a customised DNA sequence &mdash; this manipulation of DNA by deleting, replacing or inserting a sequence is called genome editing."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", text:"Emmanuelle Charpentier and Jennifer Doudna were awarded the 2020 Nobel Prize in Chemistry for developing CRISPR-Cas9 as precise &lsquo;genetic scissors&rsquo; &mdash; the first time this prize was won by two women alone."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"Researchers are investigating CRISPR to correct the genetic defects behind cystic fibrosis, sickle-cell disease, haemophilia and muscular dystrophy, and to develop more targeted cancer treatments. In one experimental treatment, scientists edited a sickle-cell patient&rsquo;s own bone-marrow cells with CRISPR so they would produce foetal haemoglobin &mdash; a form normally made only before birth &mdash; to compensate for the sickle-shaped haemoglobin."}
      ],
      notes:[{label:"Nature of science &mdash; ethical and global concerns", text:"Possible off-target (unintended) mutations, the very high cost of germ line-editing technology (which could restrict access to wealthy countries), unpredictable effects of editing human embryos, and the risk of non-therapeutic use leading to loss of human diversity and eugenics, mean that CRISPR&rsquo;s use is the subject of an international effort to harmonise regulation."}],
      side:{
        title:"CRISPR treatment of sickle-cell disease",
        charts:[
          {title:"One patient&rsquo;s blood test results", caption:"After CRISPR-edited bone-marrow cells were returned to the patient", axis:"Percentage (%)", svg: bv2BarChartSvg([
            {label:"Foetal Hb", v:46, color:"var(--teal)"},
            {label:"Modified RBCs", v:99.7, color:"var(--hv-green)"},
            {label:"Marrow cells", v:81, color:"var(--gold)"}
          ], "Bar chart of CRISPR sickle-cell treatment outcomes in one patient: 46% of haemoglobin was foetal haemoglobin, present in 99.7% of red blood cells, and over 81% of bone marrow cells carried the genetic change")}
        ]
      }
    },
    {
      icon:"book", hl:true, title:"Conserved and Highly Conserved Sequences",
      blocks:[
        {type:"prose", text:"Some DNA sequences remain almost unchanged across species and over immense evolutionary timescales, most likely because they are essential to basic cellular function, because they mutate more slowly, or both."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Conserved sequences:</strong> identical or similar sequences in nucleic acids (DNA and RNA), across species or a group of species, that have remained essentially unchanged throughout evolution. <strong>Highly conserved sequences</strong> remain essentially unchanged over long periods of evolution &mdash; for example, genes for ribosomal proteins, found in every domain of life."},
        {type:"heading", text:"Hypothesis 1: functional requirement"},
        {type:"prose", text:"Highly conserved sequences are usually required for basic cellular stability, function and reproduction, so they must be maintained largely unchanged from one generation to the next throughout evolutionary history."},
        {type:"heading", text:"Hypothesis 2: slower mutation rate"},
        {type:"prose", text:"Research shows that highly transcribed genes generally have lower mutation rates than less-expressed genes, and that the transcribed strand of a gene mutates less than the non-transcribed strand &mdash; possibly because actively transcribed DNA receives enhanced proofreading and repair."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"Highly conserved sequences are not confined to protein-coding genes: the genome also contains a large amount of regulatory DNA, and in vertebrates, highly conserved non-coding sequences occur in and around genes that act as developmental regulators &mdash; further evidence for a shared evolutionary origin of all vertebrates."}
      ]
    }
  ],
  workedExamples: [
    {
      title:"Classifying point mutations and predicting frameshifts",
      question:"A particular gene&rsquo;s DNA sequence suffers three separate, independent accidents: (a) one base is replaced by a different base; (b) two extra bases are inserted; (c) three bases are deleted. For each, name the type of mutation and state, with reasoning, whether it will cause a frameshift.",
      answer:[
        "(a) A <strong>substitution</strong>. The total number of bases is unchanged, so no frameshift occurs &mdash; though the substituted codon may still be silent, missense or nonsense, depending on which amino acid (if any) it now specifies.",
        "(b) An <strong>insertion</strong> of 2 bases. Two is not a multiple of three, so a <strong>frameshift</strong> results: every codon beyond the insertion point is shifted out of register and read incorrectly during translation.",
        "(c) A <strong>deletion</strong> of 3 bases. Three is a multiple of three, so no frameshift occurs &mdash; but one whole codon (amino acid) is simply removed from the resulting polypeptide."
      ]
    },
    {
      title:"Degeneracy of the code and the sickle-cell mutation",
      question:"Explain, using the concept of degeneracy of the genetic code, why one particular base substitution in the gene for &beta;-globin causes sickle-cell anaemia, while many other base substitutions elsewhere in the genome have no effect on the proteome at all.",
      answer:[
        "In sickle-cell anaemia, the substitution changes the codon for glutamic acid into a codon for valine, so a different amino acid is actually incorporated into the &beta;-globin polypeptide, altering the protein&rsquo;s structure and function.",
        "Because the genetic code is degenerate, most amino acids are specified by more than one codon. If a substitution elsewhere happens to produce an alternative codon for the <em>same</em> amino acid, the polypeptide sequence is unchanged and the cell&rsquo;s proteome is unaffected.",
        "A substitution that falls in a non-coding region, or in a regulatory region that still permits normal gene expression, can likewise leave the proteome unaffected.",
        "The sickle-cell substitution is harmful specifically because valine&rsquo;s chemical properties differ enough from glutamic acid&rsquo;s to change the protein&rsquo;s folding and behaviour &mdash; unlike a synonymous (same amino acid) substitution, which has no such consequence."
      ]
    },
    {
      title:"Interpreting a CAG repeat count for Huntington&rsquo;s disease",
      question:"A patient&rsquo;s <em>HTT</em> gene is found, by genetic testing, to carry 42 CAG repeats, present in every cell sampled from the body. (a) State whether this patient is likely to develop Huntington&rsquo;s disease, with reasoning. (b) Suggest why the patient&rsquo;s parent, who also carried this mutation, may not have known this when deciding whether to have children. (c) State whether this is a germ line or a somatic mutation, with reasoning.",
      answer:[
        "(a) Yes. The normal range is 10&ndash;35 CAG repeats; disease results once the repeat expands beyond 39 copies, and 42 exceeds this threshold.",
        "(b) Huntington&rsquo;s disease is caused by a dominant allele, but symptoms usually do not appear until the affected person is 40&ndash;50 years old &mdash; by which time a carrier may already have had children without any sign of the condition.",
        "(c) It must be a <strong>germ line mutation</strong>. Because the mutant allele is present in every cell sampled from the body, it must have been present from the earliest stages of development (i.e. it arose in a gamete, or very early in the embryo) &mdash; a mutation arising later, in a single somatic cell line, would be confined to the descendants of that one cell, not found throughout the whole body."
      ]
    },
    {
      title:"Transitions versus transversions",
      question:"Classify each of the following base substitutions as a transition or a transversion: (a) adenine &rarr; guanine, (b) cytosine &rarr; adenine, (c) thymine &rarr; cytosine. Then state which type of substitution is statistically more common overall, and explain why.",
      answer:[
        "(a) <strong>Transition</strong> (purine &rarr; purine).",
        "(b) <strong>Transversion</strong> (pyrimidine &rarr; purine).",
        "(c) <strong>Transition</strong> (pyrimidine &rarr; pyrimidine).",
        "Transitions are statistically more common than transversions overall. They preserve the overall ring-shape structure of the base pair, making them less structurally disruptive, and &mdash; owing to the degeneracy of the genetic code &mdash; are less likely to change the amino acid encoded, so they more often persist unnoticed as silent SNPs rather than being eliminated by natural selection."
      ]
    },
    {
      title:"Designing a gene knockout investigation",
      question:"A research team suspects a newly identified mouse gene is involved in regulating bone density. Outline how gene knockout technology could be used to investigate this, and suggest one reason CRISPR-Cas9 might be favoured over older knockout methods for this project.",
      answer:[
        "The team would use CRISPR-Cas9 (or another knockout method) to disable or delete the suspected gene in mice, producing a knockout strain with one non-functional copy of that gene.",
        "They would then compare the phenotype of knockout mice &mdash; e.g. bone density and skeletal structure &mdash; against normal (wild-type) mice of the same strain, kept under the same conditions; any consistent difference reveals something about the gene&rsquo;s normal function.",
        "Mice are a suitable model organism because, as mammals, they share substantial genetic and physiological similarity with humans, so findings can often be extrapolated.",
        "CRISPR-Cas9 might be favoured over older knockout methods because of its precision: a guide RNA directs Cas9 to cut at the exact target sequence, significantly reducing the risk of accidentally disrupting other, unrelated genes."
      ]
    }
  ],
  summary: [
    "A gene mutation is a change in the base sequence of a gene, arising spontaneously from uncorrected replication errors or from exposure to mutagens such as ionising/non-ionising radiation, certain chemicals, and some bacterial or viral infections.",
    "Point mutations take the form of substitution, insertion or deletion; insertions/deletions whose length is not a multiple of three cause a frameshift, altering every downstream codon, while substitutions may be silent, missense or nonsense.",
    "Because the genetic code is degenerate, many base substitutions have no effect on the proteome; substitutions in non-coding DNA, or in a regulatory region that still permits normal expression, can also be neutral &mdash; while a regulatory mutation that blocks expression entirely can have a major effect.",
    "Insertions can expand trinucleotide repeats (e.g. the CAG repeat in the <em>HTT</em> gene, causing Huntington&rsquo;s disease once it exceeds about 39 copies); deletions can also be beneficial, as in the CCR5 delta 32 mutation that reduces susceptibility to HIV.",
    "Mutagens &mdash; including ionising and non-ionising radiation, certain chemicals, and bacterial or viral infections &mdash; increase mutation rate; mutation also arises from the small fraction of DNA polymerase replication errors (roughly 1 in 10<sup>4</sup>&ndash;10<sup>5</sup> nucleotides) that escape proofreading.",
    "Mutation is a random process with no known natural mechanism for deliberately altering a specific base; mutations are nonetheless unevenly distributed &mdash; transitions are more common and more often silent than transversions, and CpG sequences and other regions form mutational &lsquo;hot spots&rsquo;.",
    "Germ line mutations (in cells that give rise to gametes) can be inherited and may cause genetic disease; somatic mutations occur in body cells, are never inherited, and disappear with the organism, though they can cause cancer.",
    "Mutation is the ultimate original source of all genetic variation (and so of all alleles); this variation is the raw material acted on by natural selection and can, with reproductive isolation, lead to speciation.",
    "<strong>HL:</strong> gene knockout disables a specific gene in a model organism (e.g. the mouse) to reveal its normal function by observing the resulting phenotype, relying on the universality of the genetic code and shared basic biology across species.",
    "<strong>HL:</strong> CRISPR-Cas9, originally a bacterial defence against viruses, has been adapted as a precise gene-editing tool guided by a complementary guide RNA &mdash; used experimentally to treat genetic diseases such as sickle-cell anaemia, but raising serious ethical and regulatory concerns.",
    "<strong>HL:</strong> highly conserved sequences (e.g. ribosomal protein genes) change little across species and evolutionary time, likely because they are functionally essential and/or mutate more slowly, possibly due to enhanced proofreading of actively transcribed DNA."
  ]
}
