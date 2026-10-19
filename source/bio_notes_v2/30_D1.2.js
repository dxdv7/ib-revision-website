{
  unified: true,
  subtitle: "A gene&rsquo;s sequence of DNA bases is first transcribed into a mobile messenger RNA copy, then translated at ribosomes &mdash; with tRNA acting as the interpreter between the three-base codons of mRNA and the amino acid sequence of a growing polypeptide. The reliability of this two-step process rests on complementary base pairing, a redundant (degenerate) genetic code, and &mdash; in eukaryotes &mdash; extensive processing of RNA and protein both before and after the ribosome does its work.",
  keyTerms: [
    {icon:"leaf", color:"green", term:"Gene", def:"A relatively short length of DNA within a chromosome that codes for a single protein; genes vary greatly in length, from as few as 75&ndash;100 nucleotides to well over 1000."},
    {icon:"atom", color:"teal", term:"Transcription", def:"The synthesis of messenger RNA using a DNA template."},
    {icon:"bars", color:"gold", term:"RNA polymerase", def:"The enzyme that catalyses the synthesis of RNA molecules from a DNA template."},
    {icon:"leaf", color:"plum", term:"Coding strand &amp; template strand", def:"Coding strand: the DNA strand not used as a template, whose sequence matches the mRNA produced (with U replacing T). Template strand: the complementary DNA strand actually read by RNA polymerase to synthesize mRNA."},
    {icon:"atom", color:"red", term:"Gene expression", def:"The process by which the information encoded in a gene is used to direct the synthesis of a protein molecule; typically fewer than 25% of a human cell&rsquo;s protein-coding genes are expressed at any one time."},
    {icon:"bars", color:"green", term:"Translation", def:"The process by which the information of mRNA is decoded into protein, as a sequence of amino acids."},
    {icon:"leaf", color:"teal", term:"Codon", def:"A sequence of three consecutive bases in mRNA (or, equivalently, in the DNA coding strand) that specifies one amino acid or a start/stop signal."},
    {icon:"atom", color:"gold", term:"Anticodon", def:"A sequence of three consecutive bases in a tRNA molecule, complementary to the codon it recognises on mRNA by base pairing."},
    {icon:"bars", color:"plum", term:"Degenerate code", def:"The genetic code contains more codons (64) than amino acids (20) to be coded for, so most amino acids are specified by more than one codon &mdash; e.g. any codon beginning UC codes for serine, regardless of the third base."},
    {icon:"leaf", color:"red", term:"Universality of the genetic code", def:"All organisms, prokaryote and eukaryote alike, use the same codons to specify the same amino acids &mdash; strong evidence for a single common origin of life."},
    {icon:"atom", color:"green", term:"Point mutation", def:"A change in DNA in which a single base pair is added, deleted or substituted for a different base pair."},
    {icon:"bars", color:"teal", term:"Polysome", def:"A structure of one mRNA molecule with several ribosomes attached to it simultaneously, each translating the same message and each carrying its own growing polypeptide chain."},
    {icon:"leaf", color:"gold", term:"Amino acid activation", def:"The ATP-requiring process, catalysed by a tRNA-activating enzyme, that covalently attaches a specific amino acid to its corresponding tRNA before it can be used in translation."},
    {icon:"atom", color:"plum", term:"A, P &amp; E ribosomal sites", def:"A site: where an incoming tRNA&ndash;amino acid complex first binds to the codon being read. P site: where the amino acid is added to the growing polypeptide chain by a peptide bond. E site: where the discharged, empty tRNA exits the ribosome."},
    {icon:"bars", color:"red", term:"Promoter", def:"<strong>HL</strong> &mdash; A DNA sequence, just before the start of a gene, that general transcription factors and RNA polymerase must assemble on before transcription of that gene can begin."},
    {icon:"leaf", color:"green", term:"Intron &amp; exon", def:"<strong>HL</strong> &mdash; Intron: a non-coding sequence within a eukaryotic gene that interrupts its coding sequence. Exon: a coding sequence of a eukaryotic gene, retained in mature mRNA after introns are spliced out."},
    {icon:"atom", color:"teal", term:"Telomere", def:"<strong>HL</strong> &mdash; A repetitive, non-coding DNA sequence at the end of a chromosome that protects it from degradation during repeated rounds of DNA replication."},
    {icon:"bars", color:"gold", term:"Post-transcriptional modification", def:"<strong>HL</strong> &mdash; Changes made to a newly transcribed pre-mRNA, before translation, including intron splicing, 5&rsquo; capping and addition of a poly-A tail."},
    {icon:"leaf", color:"plum", term:"Alternative splicing", def:"<strong>HL</strong> &mdash; Splicing of exons in different combinations, so that a single gene can give rise to more than one type of polypeptide (isoform)."},
    {icon:"atom", color:"red", term:"Post-translational modification", def:"<strong>HL</strong> &mdash; A biochemical modification made to one or more amino acids of a protein after it has already been translated by a ribosome, often converting an inactive precursor into its active form."},
    {icon:"bars", color:"green", term:"Proteolysis &amp; proteasome", def:"<strong>HL</strong> &mdash; Proteolysis: hydrolysis of peptide bonds, breaking a protein down into smaller peptides or amino acids. Proteasome: a protein complex that carries out proteolysis of damaged, misfolded or unneeded proteins, after they are tagged with ubiquitin."},
    {icon:"leaf", color:"teal", term:"Directionality (5&rsquo; &rarr; 3&rsquo;)", def:"<strong>HL</strong> &mdash; RNA polymerase reads the DNA template strand 3&rsquo; to 5&rsquo; while synthesizing mRNA 5&rsquo; to 3&rsquo;; ribosomes likewise read mRNA codons 5&rsquo; to 3&rsquo;, building the polypeptide from its N-terminus to its C-terminus."}
  ],
  theories: [
    {
      icon:"atom", title:"Transcription: Synthesizing mRNA from a DNA Template",
      blocks:[
        {type:"prose", text:"A chromosome&rsquo;s DNA is very long and codes for many proteins; the much shorter stretches that each code for a single protein are called genes. Because all proteins are assembled in the cytoplasm (at free ribosomes or those on the rough endoplasmic reticulum), a mobile copy of a gene&rsquo;s code must first be made and exported there; this copy, made of RNA, is called messenger RNA (mRNA), and the process that makes it is transcription, catalysed by the enzyme RNA polymerase."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Gene:</strong> a relatively short length of DNA within a chromosome that codes for a single protein; genes vary greatly in length, from as few as 75&ndash;100 nucleotides to well over 1000.",
          "<strong>Transcription:</strong> the synthesis of messenger RNA using a DNA template.",
          "<strong>RNA polymerase:</strong> the enzyme that catalyses the synthesis of RNA molecules from a DNA template."
        ]},
        {type:"prose", text:"Of the DNA double helix&rsquo;s two strands, only the <strong>template strand</strong> (also called the non-coding strand) is actually read to make mRNA; the other, the <strong>coding strand</strong>, is not used as a template, but its sequence matches the new mRNA (except that mRNA has uracil, U, wherever the coding strand has thymine, T)."},
        {type:"prose", text:"To begin transcription, hydrogen bonds between the two DNA strands are broken, unwinding the double helix of the gene being transcribed; free RNA nucleotides from a pool in the nucleus then align opposite their complementary bases on the template strand (with uracil pairing with adenine) and are held temporarily by hydrogen bonds, before RNA polymerase links the 5&rsquo; end of each new nucleotide to the 3&rsquo; end of the growing mRNA strand."},
        {type:"prose", text:"As RNA polymerase moves along the gene, the DNA double helix reforms behind it; once the mRNA strand is complete, it leaves the nucleus through nuclear pores and travels to ribosomes in the cytoplasm, where its information is &lsquo;read&rsquo; to build a protein."}
      ],
      notes:[{label:"Common mistake", text:"The coding strand is <em>not</em> the strand copied to make mRNA &mdash; it is called the coding strand only because its sequence matches that of the mRNA (with U in place of T). It is the template strand that RNA polymerase actually reads, in the 3&rsquo; to 5&rsquo; direction, to synthesize the new mRNA by complementary base pairing."}]
    },
    {
      icon:"book", title:"Stability of DNA Templates and Control of Gene Expression",
      blocks:[
        {type:"prose", text:"The sugar&ndash;phosphate backbone of DNA, together with the hydrogen bonds between its two strands, keeps the base sequence stable; a single strand can therefore be used repeatedly as a transcription template without the underlying DNA sequence itself changing."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"This stability matters most in long-lived, non-dividing somatic cells &mdash; such as neurons, skeletal and cardiac muscle cells, mature bone cells (osteocytes) and retinal receptor cells &mdash; where the same base sequence must be conserved for transcription and translation to keep functioning correctly throughout the cell&rsquo;s entire lifetime."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Gene expression:</strong> the process by which the information encoded in a gene is used to direct the synthesis of a protein molecule; typically fewer than 25% of a human cell&rsquo;s protein-coding genes are expressed at any one time."},
        {type:"prose", text:"Every nucleus in a multicellular organism contains the same complete genome, but not all of its genes are expressed at once: typically fewer than 25% of a human cell&rsquo;s protein-coding genes are being expressed at any given moment, and transcription &mdash; the first stage of gene expression &mdash; is a key point at which a gene can be switched on or off."},
        {type:"prose", text:"Which genes a cell expresses depends on when and where their protein products are needed: some genes (e.g. for respiration) are expressed continuously in all cells; some switch on only at a particular stage of development (e.g. as a stem cell becomes a muscle fibre or neuron); some are expressed only once a cell is fully mature (e.g. antibody genes in a cloned plasma cell); and some are expressed only on receipt of a specific internal or external signal (e.g. the insulin gene in pancreatic &beta; cells, triggered by a rise in blood glucose)."}
      ],
      side:{
        table:{
          title:"When and why genes are expressed",
          head:["Pattern of expression","Example"],
          rows:[
            ["Expressed all the time","Routine metabolic genes, e.g. for respiration"],
            ["Expressed at a selected developmental stage","Stem cell differentiating into a muscle fibre or neuron"],
            ["Expressed only in the mature cell","Antibody genes in a mature plasma cell"],
            ["Expressed on receipt of a signal","Insulin gene in pancreatic &beta; cells, on a hormonal/metabolic signal"]
          ]
        }
      }
    },
    {
      icon:"leaf", title:"Translation: mRNA, tRNA, Ribosomes and the Growing Polypeptide",
      blocks:[
        {type:"prose", text:"Translation decodes the information of mRNA into a protein&rsquo;s amino acid sequence. Before an amino acid can be used, it must be activated by covalently combining with a specific molecule of transfer RNA (tRNA), in a reaction (amino acid activation) that requires ATP and takes place in the cytoplasm; a different, specific enzyme and tRNA exist for each of the 20 amino acids, ensuring the correct amino acids are used in the right sequence."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Translation:</strong> the process by which the information of mRNA is decoded into protein, as a sequence of amino acids.",
          "<strong>Amino acid activation:</strong> the ATP-requiring process, catalysed by a tRNA-activating enzyme, that covalently attaches a specific amino acid to its corresponding tRNA before it can be used in translation."
        ]},
        {type:"heading", text:"tRNA, codons and anticodons"},
        {type:"prose", text:"Every tRNA has the same clover-leaf shape, but each type carries a different anticodon &mdash; a sequence of three bases complementary to the mRNA codon for its particular amino acid (e.g. the anticodon AAA is complementary to the mRNA codon UUU) &mdash; at one end, and its specific amino acid attached at the other."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Codon:</strong> a sequence of three consecutive bases in mRNA (or, equivalently, in the DNA coding strand) that specifies one amino acid or a start/stop signal.",
          "<strong>Anticodon:</strong> a sequence of three consecutive bases in a tRNA molecule, complementary to the codon it recognises on mRNA by base pairing."
        ]},
        {type:"heading", text:"At the ribosome"},
        {type:"prose", text:"A ribosome, built from a large and a small subunit, binds mRNA at its small subunit while two tRNAs bind simultaneously to its large subunit; the ribosome then moves along the mRNA from the start codon, reading one codon (three bases) at a time."},
        {type:"prose", text:"At each codon, the tRNA&ndash;amino acid complex whose anticodon is complementary slots into place, held briefly by hydrogen bonds; while held there, its amino acid is joined to the amino acid of the neighbouring tRNA&ndash;amino acid complex by a peptide linkage, formed by a condensation reaction."},
        {type:"prose", text:"This frees the first tRNA to return to the cytoplasm for reuse, while the ribosome steps on, three bases at a time, to the next codon; the process repeats continuously until a ribosome reaches a stop codon, by which point a polypeptide has been built up and emerges from the large subunit. Several ribosomes can translate the same mRNA strand at once, forming a <strong>polysome</strong>."}
      ],
      notes:[{label:"Described figure &mdash; the tRNA clover-leaf", text:"Every tRNA molecule folds into the same basic clover-leaf shape: a 3&rsquo; attachment site (ending in the base sequence CCA) where its specific amino acid binds; an anticodon loop, at the opposite end, exposing the three-base anticodon that pairs with an mRNA codon at the ribosome; and additional loop regions, including a variable-length extra loop, held together by internal base pairing between double-stranded sections of the molecule."}]
    },
    {
      icon:"book", title:"The Genetic Code: Universality, Degeneracy and the Codon Table",
      blocks:[
        {type:"prose", text:"The genetic code is read in non-overlapping groups of three bases, or codons, each specifying one of the 20 amino acids, a start signal, or a stop signal. A two-base code would give only 16 possible combinations &mdash; not enough for 20 amino acids &mdash; whereas a triplet code gives 64 combinations, more than enough, with room to spare for evolutionary change."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Degenerate code:</strong> the genetic code contains more codons (64) than amino acids (20) to be coded for, so most amino acids are specified by more than one codon &mdash; e.g. any codon beginning UC codes for serine, regardless of the third base."},
        {type:"prose", text:"&lsquo;Degenerate&rsquo; here does not mean &lsquo;deteriorated&rsquo;: it simply means several codons share one meaning. This degeneracy buffers the code against mutation: for some amino acids the first two bases alone already determine which amino acid is used, so a mutation changing only the third base of a codon may leave the encoded amino acid &mdash; and therefore the protein &mdash; completely unchanged."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Universality of the genetic code:</strong> all organisms, prokaryote and eukaryote alike, use the same codons to specify the same amino acids, with only the most minor variations having arisen since life began roughly 3500 million years ago &mdash; strong evidence for a single common origin of life."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"To decode a DNA sequence, the template strand is first transcribed into mRNA (replacing each T with U), and the mRNA is then read in triplets against a codon table or codon wheel: for example, the DNA template A-G-A-C-T-G-T-T-C-A-T-T transcribes to the mRNA U-C-U-G-A-C-A-A-G-U-A-A, which translates as serine (UCU), aspartic acid (GAC), lysine (AAG), then a stop codon (UAA)."}
      ],
      side:{
        table:{
          title:"Why a triplet code?",
          head:["Codon length","Possible combinations"],
          rows:[
            ["2 bases","4<sup>2</sup> = 16 (too few for 20 amino acids)"],
            ["3 bases","4<sup>3</sup> = 64 (enough for 20 amino acids, with redundancy)"]
          ]
        }
      }
    },
    {
      icon:"leaf", title:"Mutations That Change Protein Structure",
      blocks:[
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Point mutation:</strong> a change in DNA in which a single base pair is added, deleted or substituted for a different base pair (e.g. A for T, or C for G); because the DNA sequence (via mRNA) controls the amino acid sequence of a protein, altering even one amino acid can substantially change that protein&rsquo;s properties."},
        {type:"prose", text:"In the gene for &beta; haemoglobin, on chromosome 11, a point mutation that substitutes A for T in the codon for the sixth amino acid changes that amino acid from glutamic acid to valine, producing an abnormal haemoglobin called haemoglobin S."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"The non-polar valine creates a hydrophobic patch on the otherwise hydrophilic surface of the haemoglobin molecule; in tissues with low oxygen partial pressure, haemoglobin S molecules clump together into long fibres that distort red blood cells into a sickle shape, impairing oxygen transport and sometimes blocking small capillaries."},
        {type:"prose", text:"A person with just one haemoglobin S allele has sickle-cell trait and is only mildly anaemic; a person with both alleles has sickle-cell anaemia, a serious condition that can also cause heart and kidney problems."}
      ]
    },
    {
      icon:"atom", hl:true, title:"Directionality of Transcription and Translation; Initiation at the Promoter",
      blocks:[
        {type:"prose", text:"The two strands of the DNA double helix run in opposite directions (one 5&rsquo;&rarr;3&rsquo;, the other 3&rsquo;&rarr;5&rsquo;); RNA polymerase reads the template strand in the 3&rsquo;&rarr;5&rsquo; direction while synthesizing the new mRNA strand in the 5&rsquo;&rarr;3&rsquo; direction, requiring a free 3&rsquo;&ndash;OH group to add each new nucleotide. In translation, tRNAs likewise read mRNA codons from the 5&rsquo; end to the 3&rsquo; end, so a polypeptide is always built from its N-terminus towards its C-terminus."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Directionality (5&rsquo; &rarr; 3&rsquo;):</strong> RNA polymerase reads the DNA template strand 3&rsquo; to 5&rsquo; while synthesizing mRNA 5&rsquo; to 3&rsquo;; ribosomes likewise read mRNA codons 5&rsquo; to 3&rsquo;, building the polypeptide from its N-terminus to its C-terminus."},
        {type:"heading", text:"Initiation at the promoter"},
        {type:"prose", text:"Before RNA polymerase can transcribe a eukaryotic gene, it must first assemble, together with a small group of proteins called general transcription factors, at a specific DNA sequence just before the start of that gene, called the promoter &mdash; itself an example of non-coding DNA with a specific regulatory function. Only once this transcription complex has formed can RNA polymerase begin untwisting the helix and transcribing the gene."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Promoter:</strong> a DNA sequence, just before the start of a gene, that general transcription factors and RNA polymerase must assemble on before transcription of that gene can begin."},
        {type:"prose", text:"The rate of transcription can be increased or decreased by activator proteins binding at an <strong>enhancer</strong> site, often located some distance &lsquo;upstream&rsquo; of the promoter; DNA looping brings enhancer-bound activators into direct contact with the promoter-bound transcription complex, raising the rate of gene expression. Because the activators, general transcription factors and RNA polymerase involved are all themselves proteins coded for by other genes, initiating transcription depends fundamentally on protein&ndash;protein interactions."}
      ]
    },
    {
      icon:"book", hl:true, title:"Non-Coding DNA and Post-Transcriptional Modification",
      blocks:[
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", items:[
          "Protein-coding sequences make up only around <strong>1.5%</strong> of human DNA.",
          "Around <strong>70%</strong> of human DNA has no clearly identified role at all (once dismissively called &lsquo;junk&rsquo; or &lsquo;nonsense&rsquo; DNA).",
          "The remainder of the genome regulates the expression of protein-coding genes."
        ]},
        {type:"heading", text:"Non-gene regions of the genome"},
        {type:"prose", text:"Non-gene regions of eukaryotic chromosomes include introns (non-coding sequences interrupting a gene&rsquo;s coding exons); telomeres (repetitive sequences capping the ends of linear chromosomes, which stop genes eroding with each round of replication and prevent chromosome ends from triggering the cell&rsquo;s DNA-damage response and apoptosis); genes for tRNA; and major clusters of short, highly repeated sequences called variable number tandem repeats (VNTRs), exploited in DNA profiling."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Intron:</strong> a non-coding sequence within a eukaryotic gene that interrupts its coding sequence. <strong>Exon:</strong> a coding sequence of a eukaryotic gene, retained in mature mRNA after introns are spliced out.",
          "<strong>Telomere:</strong> a repetitive, non-coding DNA sequence at the end of a chromosome that protects it from degradation during repeated rounds of DNA replication."
        ]},
        {type:"heading", text:"Post-transcriptional modification"},
        {type:"prose", text:"When a gene containing introns is transcribed, the resulting pre-mRNA still contains those introns exactly as in the DNA; because introns do not code for protein, they must be cut out before translation, in a process called post-transcriptional modification."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Post-transcriptional modification:</strong> changes made to a newly transcribed pre-mRNA, before translation, including intron splicing, 5&rsquo; capping and addition of a poly-A tail."},
        {type:"prose", text:"A spliceosome &mdash; a large RNA&ndash;protein complex, itself encoded by a gene &mdash; recognises conserved splice sites at each exon&ndash;intron boundary, cleaves the sugar&ndash;phosphate backbone there, removes the introns, and joins all the exons together to form shortened, mature mRNA; this RNA splicing must happen before mRNA leaves the nucleus, since prokaryotic genes have no introns and prokaryotic cells lack the splicing machinery altogether."},
        {type:"prose", text:"Both ends of the pre-mRNA are also modified for stability: at the 3&rsquo; end, the enzyme poly-A polymerase adds a poly-A tail of roughly 100&ndash;250 adenine residues (polyadenylation), while the 5&rsquo; end receives a modified guanine nucleotide (&lsquo;5&rsquo; capping&rsquo;) &mdash; together protecting the mature mRNA from enzymatic breakdown as it is exported to the cytoplasm."}
      ],
      notes:[{label:"Common mistake", text:"Post-<em>transcriptional</em> modification (splicing, capping, polyadenylation) happens to mRNA, before translation. Do not confuse it with post-<em>translational</em> modification, which happens to a protein, after it has already been translated by a ribosome (covered later in this chapter)."}],
      side:{
        table:{
          title:"Human genome composition (approx.)",
          head:["Category","Share of genome"],
          rows:[
            ["Protein-coding sequences (exons)","~1.5%"],
            ["Regulatory and other functional non-coding DNA (introns, telomeres, tRNA genes, VNTRs)","Makes up most of the remainder"],
            ["Non-coding DNA with no known role","~70%"]
          ]
        }
      }
    },
    {
      icon:"leaf", hl:true, title:"Alternative Splicing of Exons",
      blocks:[
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Alternative splicing:</strong> splicing of exons in different combinations, so that a single gene can give rise to more than one type of polypeptide (isoform)."},
        {type:"prose", text:"After introns are removed, the remaining exons of a transcript can be spliced together in more than one combination, and even greater variety can arise when a sequence normally spliced out as an intron is instead retained and treated as an exon."},
        {type:"prose", text:"Because a single gene can therefore give rise to two or more related but distinct polypeptides (isoforms), alternative splicing helps explain why the human genome, with its relatively modest number of genes, can still produce a much larger number of distinct proteins &mdash; comparable in gene number to some much simpler invertebrate animals. Alternative splicing is itself controlled by other genes, often located on different chromosomes."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"In the troponin T (TnT) gene, which has five exons and plays a central role in vertebrate striated muscle contraction, developmentally regulated alternative splicing produces two different isoforms from one primary transcript: a foetal heart isoform (TnT&beta;) is used before birth, and a distinct adult isoform (TnT&alpha;) is used once the heart has matured, helping prepare the heart for the increased demands of life after birth."}
      ]
    },
    {
      icon:"atom", hl:true, title:"Initiation of Translation: Amino Acid Activation and Ribosome Sites",
      blocks:[
        {type:"prose", text:"Each of the 20 amino acids is first activated by a specific tRNA-activating enzyme, which uses ATP to attach that amino acid to its one matching tRNA (there are 20 different tRNA-activating enzymes, one per amino acid) &mdash; the resulting amino acid&ndash;tRNA complex is then available for use at a ribosome."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>A, P &amp; E ribosomal sites:</strong> A site &mdash; where an incoming tRNA&ndash;amino acid complex first binds to the codon being read. P site &mdash; where the amino acid is added to the growing polypeptide chain by a peptide bond. E site &mdash; where the discharged, empty tRNA exits the ribosome."},
        {type:"heading", text:"Initiation"},
        {type:"prose", text:"Translation begins (initiation) when mRNA binds the small ribosomal subunit near its 5&rsquo; end, and an initiator tRNA carrying methionine binds the start codon AUG; the large ribosomal subunit then attaches, with this initiator tRNA occupying the P site, ready for the next tRNA to bind the adjacent A site and form the first peptide bond."},
        {type:"heading", text:"Elongation and termination"},
        {type:"prose", text:"During elongation, the ribosome steps three bases along the mRNA: the spent tRNA moves from the P site to the E site and leaves, the next codon occupies the now-vacant A site, a new matching tRNA binds there, and another peptide bond forms &mdash; this cycle repeats, building the polypeptide chain in the 5&rsquo;&rarr;3&rsquo; direction, until a stop codon enters the A site, at which point the finished polypeptide is released and the ribosome disassembles (termination)."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", items:[
          "Start codon: <strong>AUG</strong> (codes for methionine), recognised by the initiator tRNA.",
          "Stop codons: <strong>UAA, UAG and UGA</strong> &mdash; none of which code for an amino acid."
        ]}
      ],
      notes:[
        {label:"Described figure &mdash; the three ribosomal sites", text:"The large and small ribosomal subunits assemble around the mRNA to create, side by side, the A site (where the next amino acid&ndash;tRNA complex binds), the P site (which holds the tRNA while a peptide bond forms with the growing chain) and the E site (where the spent, empty tRNA exits); the completed polypeptide emerges from the large subunit through a dedicated exit tunnel."},
        {label:"Nature of science &mdash; deducing the first codon", text:"In 1962, Marshall Nirenberg and Heinrich Matthaei used the enzyme polynucleotide phosphorylase to generate artificial &lsquo;poly(U)&rsquo; RNA made entirely of repeating UUU codons, then added it &mdash; together with ribosomes, tRNAs and activating enzymes &mdash; to twenty separate tubes, each containing one radioactively labelled amino acid. Only the tube containing labelled phenylalanine produced a protein product, showing that UUU codes for phenylalanine; equivalent experiments with poly(C) and poly(A) RNA showed that CCC codes for proline and AAA for lysine."}
      ]
    },
    {
      icon:"book", hl:true, title:"Post-Translational Modification and Recycling of Amino Acids by Proteasomes",
      blocks:[
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Post-translational modification:</strong> a biochemical modification made to one or more amino acids of a protein after it has already been translated by a ribosome, often converting an inactive precursor into its active form."},
        {type:"prose", text:"Some proteins fold into their final, active three-dimensional shape as soon as they leave the ribosome; many others, however, require further chemical changes afterwards before they can function."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"Producing a protein first as an inactive precursor lets a cell control exactly when and where it becomes active: the digestive enzyme trypsin, for example, is made in the pancreas as inactive trypsinogen, which cannot digest the very pancreas cells that produce it until it is later activated elsewhere; insulin similarly requires a two-stage modification, from pre-proinsulin to proinsulin and then to active insulin."},
        {type:"heading", text:"Proteolysis and the proteasome"},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Proteolysis:</strong> hydrolysis of peptide bonds, breaking a protein down into smaller peptides or amino acids. <strong>Proteasome:</strong> a protein complex that carries out proteolysis of damaged, misfolded or unneeded proteins, after they are tagged with ubiquitin."},
        {type:"prose", text:"To maintain a functioning proteome, proteins are continuously synthesized by translation and broken down again by proteolysis, which also recycles amino acids for building new proteins alongside those absorbed from the diet."},
        {type:"prose", text:"Proteins marked for breakdown are tagged with a short chain of the regulatory protein ubiquitin; the tagged protein binds to a cap (regulatory particle) at the top of a barrel-shaped proteasome, is threaded into its core particle, and is broken down there into short peptides, which are further processed into a pool of free amino acids. Proteasomes specifically target proteins that are damaged, misfolded, or simply no longer needed by the cell."}
      ],
      notes:[{label:"Common mistake", text:"Do not confuse post-translational modification (a change to a protein, after translation) with post-transcriptional modification (a change to mRNA, before translation) &mdash; the two happen to different molecules, at different stages of protein synthesis."}]
    }
  ],
  workedExamples: [
    {
      title:"From DNA template to amino acid sequence",
      question:"The sequence of bases in part of a DNA template strand is: A-G-A-C-T-G-T-T-C-A-T-T. Deduce (a) the mRNA sequence transcribed from this template, and (b) the sequence of amino acids this mRNA codes for.",
      answer:[
        "(a) Transcription copies the template strand by complementary base pairing, with uracil replacing thymine: the DNA template A-G-A-C-T-G-T-T-C-A-T-T transcribes to the mRNA U-C-U-G-A-C-A-A-G-U-A-A.",
        "(b) Reading this mRNA in triplets from the codon table: UCU = serine, GAC = aspartic acid, AAG = lysine, and UAA = a stop codon.",
        "The resulting amino acid sequence is therefore Ser&ndash;Asp&ndash;Lys, with translation then terminating at the stop codon."
      ]
    },
    {
      title:"Why the genetic code is described as degenerate",
      question:"The codons UCU, UCC, UCA and UCG all code for serine. Explain what this tells us about the genetic code, and explain why this property is biologically useful.",
      answer:[
        "This shows that more than one codon can specify the same amino acid &ndash; the genetic code is described as <strong>degenerate</strong>, since it contains more codons (64) than amino acids (20).",
        "For serine, only the first two bases (UC) actually determine the amino acid; the third base can vary without changing the result.",
        "This is useful because it buffers the code against mutation: if a point mutation changes only the third base of a codon like this, the amino acid sequence &ndash; and so the protein&rsquo;s structure and function &ndash; may remain completely unchanged."
      ]
    },
    {
      title:"Explaining sickle-cell anaemia as a point mutation",
      question:"A single point mutation in the gene for &beta; haemoglobin changes the codon for the sixth amino acid, causing valine to replace glutamic acid. Explain how this single base-level change can produce the sickle-cell phenotype.",
      answer:[
        "A point mutation substitutes one base (A for T) in the DNA, which changes the corresponding mRNA codon, so that the tRNA bringing valine is used at the ribosome instead of the tRNA bringing glutamic acid.",
        "Valine is non-polar, so its presence at this position creates a hydrophobic patch on what is normally the hydrophilic outer surface of the haemoglobin molecule.",
        "This hydrophobic patch causes haemoglobin molecules to bind to one another and clump into long fibres when oxygen levels are low, distorting red blood cells into a sickle shape.",
        "Sickled cells transport oxygen poorly and can block small capillaries, producing the anaemia (and, in those with two haemoglobin S alleles, the more serious complications) seen in sickle-cell disease &ndash; all traced back to a single substituted base pair."
      ]
    },
    {
      title:"Alternative splicing and the number of possible protein products",
      question:"A gene&rsquo;s primary transcript contains three exons (1, 2 and 3) separated by introns. After splicing, exon 2 can either be included or skipped, while exons 1 and 3 are always retained. (a) State the two possible mature mRNA sequences of exons that could result. (b) Explain why this means the number of distinct proteins an organism produces can exceed its number of genes.",
      answer:[
        "(a) The two possible mature mRNAs are exon 1&ndash;exon 2&ndash;exon 3 (all three exons included) or exon 1&ndash;exon 3 (exon 2 skipped).",
        "(b) Because this one gene&rsquo;s primary transcript can be spliced in more than one way, it can produce two related but distinct polypeptide isoforms rather than just one.",
        "If this happens across many genes in the genome, the total number of distinct proteins produced can be considerably greater than the total number of genes &ndash; alternative splicing, not just gene number, explains much of an organism&rsquo;s protein diversity."
      ]
    },
    {
      title:"Post-transcriptional vs post-translational modification",
      question:"For each example, state whether it is an example of post-transcriptional modification or post-translational modification: (a) removal of introns from a pre-mRNA by a spliceosome; (b) addition of a poly-A tail to the 3&rsquo; end of an mRNA; (c) conversion of inactive trypsinogen into active trypsin.",
      answer:[
        "(a) Post-transcriptional modification &ndash; this happens to mRNA, after transcription but before translation.",
        "(b) Post-transcriptional modification &ndash; polyadenylation also modifies the mRNA molecule itself, before it is translated.",
        "(c) Post-translational modification &ndash; this is a change made to a protein (trypsinogen) after it has already been translated by a ribosome."
      ]
    }
  ],
  summary: [
    "Transcription copies a gene&rsquo;s DNA code into mobile mRNA: RNA polymerase reads the template strand (not the coding strand) and assembles mRNA from free nucleotides by complementary base pairing, with uracil replacing thymine.",
    "DNA&rsquo;s stable double-helix structure allows its base sequence to be read repeatedly without change, which matters especially in long-lived, non-dividing cells; not all genes are expressed at once, and transcription is the key stage at which gene expression is switched on or off.",
    "Translation decodes mRNA into protein at ribosomes: tRNA activates and carries specific amino acids, its anticodon pairing with the mRNA codon being read, while peptide bonds join successive amino acids into a growing polypeptide; several ribosomes translating one mRNA form a polysome.",
    "The genetic code is a universal triplet code (64 codons for 20 amino acids plus start/stop signals) and is degenerate, since most amino acids have more than one codon &mdash; a redundancy that buffers the code against the effects of mutation.",
    "A point mutation &mdash; a single base pair added, deleted or substituted &mdash; can change one amino acid in a protein, sometimes drastically altering its function, as in the single base substitution behind sickle-cell anaemia.",
    "<strong>HL:</strong> DNA and mRNA are both read with a fixed 5&rsquo;/3&rsquo; directionality, and eukaryotic transcription of a gene can only begin once RNA polymerase and general transcription factors have assembled at its promoter, a process whose rate can be boosted by activators binding a more distant enhancer.",
    "<strong>HL:</strong> only around 1.5% of human DNA codes for protein; much of the rest is regulatory or structural non-coding DNA (introns, telomeres, tRNA genes, VNTRs), and introns must be spliced out of pre-mRNA by a spliceosome, with the mRNA also gaining a poly-A tail and a 5&rsquo; cap, before it is mature enough to leave the nucleus.",
    "<strong>HL:</strong> alternative splicing of exons lets a single gene produce more than one polypeptide isoform (e.g. the foetal and adult forms of troponin T), helping explain why an organism&rsquo;s protein count can exceed its gene count.",
    "<strong>HL:</strong> translation proceeds through three ribosomal sites (A, P and E) across initiation, elongation and termination, building the polypeptide from its N-terminus to its C-terminus until a stop codon is reached; Nirenberg and Matthaei&rsquo;s poly(U) experiment was the first to crack a codon&rsquo;s meaning.",
    "<strong>HL:</strong> many proteins require post-translational modification (e.g. trypsinogen to trypsin, pre-proinsulin to insulin) before they become functional, and proteasomes continually recycle ubiquitin-tagged, damaged or unneeded proteins back into free amino acids."
  ]
}
