{
  subtitle: "Gregor Mendel&rsquo;s pea-breeding experiments uncovered the basic rules of inheritance long before genes or chromosomes were known to exist. This chapter traces those rules from genotype and phenotype, through dominance, multiple alleles, sex linkage and pedigree analysis, to the statistics &mdash; and, at HL, gene linkage and the chi-squared test &mdash; needed to test them rigorously.",
  keyTerms: [
    {icon:"atom", color:"green", term:"Genotype", def:"The combination of alleles inherited by an organism, present in every cell of its body."},
    {icon:"leaf", color:"teal", term:"Phenotype", def:"The observable traits of an organism, resulting from its genotype and/or environmental factors."},
    {icon:"atom", color:"gold", term:"Dominant &amp; recessive allele", def:"Dominant allele: has the same effect on the phenotype whether homozygous or heterozygous. Recessive allele: affects the phenotype only when homozygous."},
    {icon:"bars", color:"plum", term:"Homozygous &amp; heterozygous", def:"Homozygous: an organism with two identical alleles of a gene. Heterozygous: an organism with two different alleles of a gene."},
    {icon:"leaf", color:"red", term:"Monohybrid cross", def:"A breeding experiment (cross) involving one pair of contrasting characters, exhibited by homozygous parents."},
    {icon:"atom", color:"teal", term:"Punnett grid", def:"A diagram used to show and calculate all the combinations and frequencies of genotypes and phenotypes among the offspring of a genetic cross."},
    {icon:"bars", color:"green", term:"Test cross", def:"A cross between an individual of unknown genotype (but dominant phenotype) and a homozygous recessive individual, used to reveal whether the unknown individual is homozygous or heterozygous."},
    {icon:"leaf", color:"gold", term:"P, F1 &amp; F2 generations", def:"P (parental generation): the first parents in a cross. F1: the first-generation offspring of the P cross. F2: the offspring produced when F1 individuals are selfed or sibling-crossed."},
    {icon:"atom", color:"plum", term:"Phenotypic plasticity", def:"The capacity to develop traits suited to the environment experienced by an organism, by varying patterns of gene expression, without any change in genotype."},
    {icon:"leaf", color:"red", term:"Phenylketonuria (PKU)", def:"A recessive genetic condition caused by mutation in the autosomal gene for phenylalanine hydroxylase, the enzyme needed to convert phenylalanine to tyrosine."},
    {icon:"bars", color:"green", term:"Carrier", def:"An individual with one copy of a recessive allele that causes a genetic disease in those homozygous for it; a carrier does not show the disease itself."},
    {icon:"atom", color:"teal", term:"Single-nucleotide polymorphism (SNP)", def:"A difference of a single nucleotide at one position in the genome, which can create an alternative allele of a gene."},
    {icon:"leaf", color:"gold", term:"Multiple alleles", def:"The existence of more than two alternative forms of a gene within a gene pool, e.g. the three alleles (I<sup>A</sup>, I<sup>B</sup>, i) of the human ABO blood-group gene."},
    {icon:"bars", color:"plum", term:"Codominance", def:"A condition in which both alleles of a heterozygote are expressed equally in the phenotype, e.g. the AB blood group."},
    {icon:"atom", color:"red", term:"Incomplete dominance", def:"A condition in which a dominant allele does not completely mask the effect of a recessive allele, giving heterozygotes an intermediate, third phenotype."},
    {icon:"leaf", color:"teal", term:"Sex chromosome &amp; autosome", def:"Sex chromosome: X or Y, determining the sex of the individual. Autosome: any of the other, numbered chromosome pairs (1&ndash;22 in humans)."},
    {icon:"bars", color:"gold", term:"Sex linkage", def:"A special case of linkage occurring when a gene is located on a sex chromosome, usually the X chromosome."},
    {icon:"atom", color:"green", term:"Haemophilia", def:"A rare, sex-linked recessive condition in which the blood does not clot normally, due to failure to produce adequate amounts of a specific blood-clotting protein."},
    {icon:"leaf", color:"plum", term:"Pedigree chart", def:"A diagram representing the familial relationships and phenotypes of several generations of a family, used to deduce patterns of inheritance of genetic disorders."},
    {icon:"bars", color:"red", term:"Polygenic inheritance", def:"Inheritance of a phenotypic characteristic (such as height or skin colour) determined by the collective effect of several different genes, often producing continuous variation."},
    {icon:"atom", color:"teal", term:"Box-and-whisker plot &amp; IQR", def:"A plot showing the median, quartiles and range of a data set. The interquartile range (IQR) spans the first to the third quartile, covering the middle 50% of the data."},
    {icon:"leaf", color:"gold", term:"Locus", def:"<strong>HL</strong> &mdash; The fixed position of a gene on a chromosome; plural loci. Each eukaryotic chromosome is a linear series of gene loci."},
    {icon:"bars", color:"plum", term:"Gene linkage", def:"<strong>HL</strong> &mdash; The phenomenon in which two or more genes located on the same chromosome do not segregate independently during meiosis, but tend to be inherited together."},
    {icon:"atom", color:"red", term:"Recombinant", def:"<strong>HL</strong> &mdash; A chromosome, gamete or offspring genotype in which the genetic information has been rearranged compared with the parental combinations, typically by crossing over."},
    {icon:"leaf", color:"green", term:"Chi-squared (&chi;<sup>2</sup>) test", def:"<strong>HL</strong> &mdash; A statistical test used to estimate the probability that a difference between observed and expected results is due to chance alone."},
    {icon:"bars", color:"teal", term:"Null &amp; alternative hypothesis", def:"<strong>HL</strong> &mdash; Null hypothesis: there is no real difference between observed and expected results. Alternative hypothesis: a real difference or association exists."}
  ],
  theories: [
    {
      icon:"leaf", title:"Gametes, Mendel and the Monohybrid Cross",
      coreIdea:"Meiosis and fertilisation together keep an organism&rsquo;s chromosome number constant from one generation to the next, and it was by crossing large numbers of true-breeding pea plants that Gregor Mendel first uncovered the mathematical rules by which this inheritance actually works.",
      steps:[
        "In the diploid life cycle, a diploid (2n) adult produces haploid (n) gametes by meiosis; at fertilisation, a haploid sperm fuses with a haploid egg to restore the diploid zygote, which develops into the adult by mitosis &mdash; a pattern common to all eukaryotes with a sexual life cycle.",
        "Diploid cells carry two copies of each <strong>autosomal gene</strong> (a gene on one of the numbered, non-sex chromosomes), one on each homologous chromosome; the sex chromosomes additionally carry the genes that determine the sex of the offspring.",
        "Gregor Mendel, a monk at a monastery in Brno, cross-bred over 30,000 garden pea (<em>Pisum</em> sp.) plants over eight years, studying contrasting characteristics such as round versus wrinkled seeds, yellow versus green cotyledons, and tall versus dwarf stems &mdash; and succeeded where others failed because his experiments used large samples, expressed results as ratios, studied easily-recognised traits each controlled (by chance) by a single gene on a separate chromosome from the others, and applied mathematics to interpret the results.",
        "Mendel began with <strong>true-breeding</strong> tall and dwarf pea lines (each producing only its own type when self-fertilised). Pollination (needed because pollen carries the male gametes and the ovary holds the female gametes) let him cross a true-breeding tall line with a true-breeding dwarf line; the <strong>P generation</strong> cross produced an <strong>F1 generation</strong> that was entirely tall. Allowing the F1 to self-pollinate produced an <strong>F2 generation</strong> of both tall and dwarf plants, in a ratio close to 3 tall : 1 dwarf (Mendel&rsquo;s own count: 787 tall to 277 dwarf, a ratio of 2.84:1).",
        "Because the dwarf characteristic disappeared in the F1 but reappeared in the F2, Mendel reasoned that a factor for dwarfness must persist, unexpressed, alongside a factor for tallness &mdash; tallness is <strong>dominant</strong>, dwarfness <strong>recessive</strong>, and each parent contributes one of two independent factors (now called alleles) for height, with each gamete carrying only one.",
        "Mendel&rsquo;s first law, the <strong>Law of Segregation</strong>, states: the characteristics of an organism are controlled by pairs of alleles which separate in equal numbers into different gametes as a result of meiosis &mdash; because alleles are located on homologous chromosomes, which move to opposite poles of the spindle during meiosis."
      ],
      notes:[{label:"Nature of science &mdash; before Mendel", text:"Before Mendel, scientists assumed inheritance worked by &lsquo;blending&rsquo; (like mixing paints) &mdash; a tall and a short parent producing children of medium height. This explained some traits reasonably well (height, skin colour) but failed for others, such as eye colour, where a blue-eyed and a brown-eyed parent do not produce all medium-brown-eyed children."}],
      side:{
        title:"Mendel&rsquo;s later cross data",
        table:{
          title:"Mendel&rsquo;s later monohybrid crosses",
          head:["Character","Cross","F2 counted","Dominant","Recessive"],
          rows:[
            ["Flower position","axial &times; terminal","858","651 axial","207 terminal"],
            ["Seed-coat colour","grey &times; white","929","705 grey","224 white"],
            ["Cotyledon colour","yellow &times; green","8023","6022 yellow","2001 green"]
          ]
        }
      }
    },
    {
      icon:"book", title:"Genotype, Phenotype and the Test Cross",
      coreIdea:"Organisms with different genotypes can share an identical phenotype, since a dominant allele masks a recessive one completely &mdash; so a test cross against a known homozygous recessive is needed to reveal which genotype is actually present.",
      steps:[
        "<strong>Genotype</strong> is the combination of alleles an organism inherits, present in every cell; <strong>phenotype</strong> is the observable traits resulting from genotype and/or environmental factors. In Mendel&rsquo;s cross, TT and Tt plants share the same (tall) phenotype but different genotypes, because both carry at least one dominant T allele.",
        "An organism showing a <strong>recessive</strong> characteristic must be homozygous for the recessive allele (tt); one showing the <strong>dominant</strong> characteristic may be either homozygous dominant (TT) or heterozygous (Tt) &mdash; these genotypes cannot be told apart just by looking.",
        "A <strong>test cross</strong> breeds the plant of unknown genotype with a homozygous recessive (tt) plant: if all the offspring show the dominant phenotype, the tested plant is homozygous (TT); if about half show the recessive phenotype, it is heterozygous (Tt). Sufficient offspring must be produced to see these ratios clearly.",
        "Phenotype can be determined by genotype alone (e.g. eye colour, blood type), by environment alone (e.g. a suntan), or by an interaction between the two (e.g. height and body weight, explored through monozygotic twin studies)."
      ],
      notes:[{label:"Common mistake", text:"It is incorrect to assume dominant alleles are always advantageous or produce the most common phenotype. Huntington&rsquo;s disease (progressive mental deterioration and involuntary muscle movements) and six fingers (polydactyly) are both caused by dominant alleles, yet neither is advantageous or the most common form."}],
      side:{
        title:"A test cross reveals the hidden genotype",
        table:{
          title:"Tt (unknown, tall) &times; tt (homozygous recessive)",
          head:["Gametes","1/2 T","1/2 t"],
          rows:[["1/2 t","Tt (tall)","tt (dwarf)"],["1/2 t","Tt (tall)","tt (dwarf)"]]
        }
      }
    },
    {
      icon:"leaf", title:"Phenotypic Plasticity and Phenylketonuria",
      coreIdea:"Phenotype is not fixed by genotype alone: some traits are adjusted reversibly to suit the environment through altered gene expression, while others &mdash; like phenylketonuria &mdash; are rigidly determined by a single recessive mutant allele, unless the environment (diet) is deliberately controlled.",
      steps:[
        "<strong>Phenotypic plasticity</strong> is the capacity to develop traits suited to the environment experienced by an organism, by varying patterns of gene expression rather than by any change in genotype; the resulting changes in traits &mdash; such as the effects of exercise and diet on human morphology and physiology &mdash; may be reversible within an individual&rsquo;s lifetime.",
        "<strong>Phenylketonuria (PKU)</strong> is a rare inherited disorder caused by a mutation in the <em>PAH</em> gene on chromosome 12, which codes for phenylalanine hydroxylase &mdash; the enzyme that converts the amino acid phenylalanine into tyrosine. Without the enzyme, phenylalanine accumulates in the body.",
        "High phenylalanine levels interfere with melanin production, giving untreated infants unusually light eye, skin and hair colour, and disrupt neurotransmitters such as serotonin and dopamine, causing seizures, abnormal muscle movements, tremors and, without treatment, severe brain damage.",
        "PKU is recessive, so two copies of the faulty allele are needed to develop the disease; a person with one faulty and one working copy is an unaffected <strong>carrier</strong>. Treatment is a carefully controlled, phenylalanine-restricted diet begun in the first days or weeks of life."
      ],
      notes:[{label:"Common mistake", text:"Do not confuse &lsquo;carrier&rsquo; (one copy of a recessive allele, unaffected because the working allele masks it) with &lsquo;affected&rsquo; (two copies of the recessive allele, showing the disease&rsquo;s symptoms)."}]
    },
    {
      icon:"atom", title:"SNPs, Multiple Alleles and the ABO Blood Groups",
      coreIdea:"Because any single base change can create a new allele, most genes exist as many different alleles across a gene pool rather than just two &mdash; and the three-allele, codominant ABO blood-group locus is the model example.",
      steps:[
        "A <strong>single-nucleotide polymorphism (SNP)</strong> is a difference at just one base position in the genome (e.g. guanine replaced by adenine); this can create a new allele of a gene. Many different alleles of one gene can accumulate in a gene pool over time, but because only one allele occupies each chromosome, any individual inherits just two of them (one from each parent).",
        "Most genes in reality have more than two alleles &mdash; <strong>multiple alleles</strong>. With multiple alleles, a single capital letter represents the locus, and each individual allele is shown as an extra letter in superscript, as with the human <strong>ABO blood group</strong> system: blood group A (genotype I<sup>A</sup>I<sup>A</sup> or I<sup>A</sup>i), B (I<sup>B</sup>I<sup>B</sup> or I<sup>B</sup>i), AB (I<sup>A</sup>I<sup>B</sup>), or O (ii).",
        "I<sup>A</sup> and I<sup>B</sup> are <strong>codominant</strong> &mdash; both show through in the phenotype together, as blood group AB &mdash; and both are dominant to the recessive i. Crossing a blood-group-A parent (I<sup>A</sup>i) with a blood-group-B parent (I<sup>B</sup>i) gives offspring in equal 25% proportions of genotypes I<sup>A</sup>I<sup>B</sup>, I<sup>A</sup>i, I<sup>B</sup>i and ii &mdash; phenotypes AB, A, B and O."
      ],
      notes:[{label:"Common mistake", text:"It is incorrect to call i a &lsquo;recessive allele&rsquo; in quite the usual sense: it has no phenotypic effect because it simply does not code for the carbohydrate antigen on the red blood cell surface, not because a dominant allele is actively masking it. Also, do not confuse a person&rsquo;s blood &lsquo;group&rsquo; (A, B, AB or O) with their blood &lsquo;allele&rsquo; (I<sup>A</sup>, I<sup>B</sup> or i)."}],
      side:{
        title:"A cross between blood groups A and B",
        charts:[{title:"I<sup>A</sup>i &times; I<sup>B</sup>i offspring", caption:"Offspring genotype classes, 25% each", axis:"Offspring blood group", svg: bv2BarChartSvg([
          {label:"AB", v:0.25, color:"var(--hv-green)"},
          {label:"A", v:0.25, color:"var(--teal)"},
          {label:"B", v:0.25, color:"var(--gold)"},
          {label:"O", v:0.25, color:"var(--red)"}
        ], "Bar chart of offspring blood groups from an IAi by IBi cross, showing four equal 25% classes: AB, A, B and O")}]
      }
    },
    {
      icon:"atom", title:"Incomplete Dominance and Codominance",
      coreIdea:"Not every heterozygote simply shows the dominant parent&rsquo;s phenotype: codominant alleles are both fully expressed together, while incompletely dominant alleles blend into a brand-new, intermediate third phenotype &mdash; and either case breaks the standard 3:1 monohybrid ratio.",
      steps:[
        "In <strong>codominance</strong>, both alleles of a heterozygote are expressed equally in the phenotype &mdash; as with the AB blood group, where both the I<sup>A</sup> and I<sup>B</sup> antigens appear on the red blood cell surface together.",
        "In <strong>incomplete dominance</strong>, the dominant allele does not completely mask the recessive one, so heterozygotes show an intermediate phenotype distinct from both homozygous parents. Such alleles are shown with a capital letter for the gene and different superscript capital letters for the two alleles (e.g. F<sup>R</sup> and F<sup>W</sup>), since neither one fully masks the other.",
        "In <em>Mirabilis jalapa</em> (the four o&rsquo;clock flower), crossing a pure-breeding red-flowered plant (F<sup>R</sup>F<sup>R</sup>) with a pure-breeding white-flowered plant (F<sup>W</sup>F<sup>W</sup>) gives F1 offspring that are all pink (F<sup>R</sup>F<sup>W</sup>), because both a red and a white pigment system are expressed together in the heterozygote.",
        "Selfing the pink F1 plants gives an F2 generation of red, pink and white flowers in the ratio 1:2:1 &mdash; not the 3:1 ratio of ordinary dominant/recessive monohybrid crosses &mdash; because the heterozygote&rsquo;s phenotype is now visibly distinct, not hidden."
      ],
      notes:[{label:"Common mistake", text:"Do not confuse codominance (both alleles show through equally, as in AB blood group) with incomplete dominance (the dominant allele only partially masks the recessive one, producing a blended, intermediate third phenotype, as in pink <em>Mirabilis</em> flowers)."}],
      side:{
        title:"Incomplete dominance in Mirabilis jalapa",
        charts:[{title:"F2 from a pink &times; pink self-cross", caption:"F<sup>R</sup>F<sup>W</sup> &times; F<sup>R</sup>F<sup>W</sup>, verified 1:2:1 ratio", axis:"F2 phenotype", svg: bv2BarChartSvg([
          {label:"Red", v:0.25, color:"var(--red)"},
          {label:"Pink", v:0.50, color:"var(--plum)"},
          {label:"White", v:0.25, color:"var(--teal)"}
        ], "Bar chart of F2 Mirabilis jalapa flower colours from a pink self-cross, showing a 1:2:1 ratio of red to pink to white")}]
      }
    },
    {
      icon:"leaf", title:"Sex Determination and Sex-Linked Inheritance: Haemophilia",
      coreIdea:"The X and Y sex chromosomes not only decide an embryo&rsquo;s sex but also carry ordinary genes that are inherited differently from autosomal genes, because a male has only one X chromosome and so only one copy of every X-linked gene &mdash; as haemophilia demonstrates.",
      steps:[
        "In a karyogram, the unnumbered 23rd pair of human chromosomes are the <strong>sex chromosomes</strong>, X and Y; all other pairs (1&ndash;22) are <strong>autosomes</strong>. The X chromosome is much longer than the Y and carries far more genes.",
        "All egg cells carry an X chromosome, but sperm are of two types: 50% X-carrying, 50% Y-carrying. An X-carrying sperm fertilising the egg produces a female (XX); a Y-carrying sperm produces a male (XY) &mdash; so the father&rsquo;s gamete determines the offspring&rsquo;s sex, and equal numbers of males and females are expected over time.",
        "Male and female embryos initially develop identically. In week seven, a gene on the Y chromosome coding for <strong>testis-determining factor (TDF)</strong> acts as a molecular switch: on reaching the embryonic gonad tissue it triggers testosterone production, which inhibits female genital development and causes testes, scrotum and penis to form instead. Without a Y chromosome, the gonad tissue forms an ovary and female structures develop under ovarian hormone influence.",
        "The <strong>non-homologous region</strong> of the X chromosome has no equivalent sequence on the Y, so in a male (XY) any allele there &mdash; even a recessive one &mdash; shows up in the phenotype, since there is no second allele to mask it. In a female (XX), a recessive allele on one X can still be masked by a dominant allele on the other, so a female can be a <strong>carrier</strong> of a sex-linked recessive condition without showing it.",
        "<strong>Haemophilia</strong> is a rare X-linked recessive condition in which insufficient clotting protein is produced, causing frequent, excessive bleeding; it is treated today by administering the missing clotting factor. Because the responsible gene is on the X chromosome, a single copy of the recessive allele (X<sup>h</sup>Y) causes the disease in males, while a female would need to be homozygous (X<sup>h</sup>X<sup>h</sup>) to be affected &mdash; a genotype usually fatal before birth. A female with one copy (X<sup>H</sup>X<sup>h</sup>) is an unaffected carrier.",
        "Crossing a carrier mother (X<sup>H</sup>X<sup>h</sup>) with a normal father (X<sup>H</sup>Y) gives four equally likely offspring classes: normal female (X<sup>H</sup>X<sup>H</sup>), carrier female (X<sup>H</sup>X<sup>h</sup>), normal male (X<sup>H</sup>Y) and haemophiliac male (X<sup>h</sup>Y) &mdash; a 50% chance for any daughter to be a carrier and a 50% chance for any son to have haemophilia."
      ],
      notes:[{label:"Common mistake", text:"The condition that determines a female is the <em>absence</em> of a Y chromosome, not the presence of an X chromosome (every individual, male or female, carries at least one X). Also, sex-linked allele symbols are always shown as superscripts on an uppercase X &mdash; the Y chromosome is not associated with these genes."}],
      side:{
        title:"Carrier mother &times; normal father",
        charts:[{title:"X<sup>H</sup>X<sup>h</sup> &times; X<sup>H</sup>Y offspring", caption:"Four genotype classes, 25% each", axis:"Offspring class", svg: bv2BarChartSvg([
          {label:"Normal F", v:0.25, color:"var(--hv-green)"},
          {label:"Carrier F", v:0.25, color:"var(--teal)"},
          {label:"Normal M", v:0.25, color:"var(--gold)"},
          {label:"Affected M", v:0.25, color:"var(--red)"}
        ], "Bar chart of offspring from a carrier mother and normal father cross, showing four equal 25% classes: normal female, carrier female, normal male, affected male")}]
      }
    },
    {
      icon:"book", title:"Pedigree Charts and Patterns of Inheritance",
      coreIdea:"Because controlled breeding experiments are impossible with humans, family pedigree charts let us infer whether a trait follows a dominant or a recessive pattern of inheritance directly from the generations already lived.",
      steps:[
        "A <strong>pedigree chart</strong> uses a standard set of conventions: individuals on the same horizontal line belong to the same generation (numbered I, II, III&hellip;); squares and circles typically represent males and females; a horizontal line linking two individuals shows a mating, with their offspring (siblings) dropping below in birth order; and a marked union between related individuals (such as cousins) indicates consanguinity.",
        "A characteristic controlled by a <strong>dominant</strong> allele tends to appear in at least one member of every generation. A characteristic controlled by a <strong>recessive</strong> allele is seen only occasionally, often skipping several generations altogether, since it requires both parents to pass on the allele.",
        "<strong>Albinism</strong> (a block in the pathway that produces the pigment melanin, giving white hair, very light skin and pink eyes) follows a recessive pattern: in one pedigree, an affected individual in generation I (genotype pp) has only carrier (Pp) children in generation II, and albinism does not reappear until generation IV &mdash; skipping two generations &mdash; once both a generation-III carrier and her partner happen to carry the recessive allele.",
        "<strong>Brachydactyly</strong> (an unusually short-fingered condition caused by a dominant mutant allele) instead follows a dominant pattern, appearing in roughly half the offspring of every generation; in one pedigree, the generation-I parents (a normal male, nn, and a heterozygous brachydactylous female, Nn) produce offspring in a ratio resembling a test cross, as expected for this heterozygous-by-homozygous-recessive dominant cross.",
        "Many societies prohibit marriage between close relatives partly for genetic reasons: because related individuals share a smaller pool of common ancestors, their offspring are more likely to inherit two copies of the same harmful recessive allele than the offspring of unrelated parents &mdash; so inbreeding increases the risk of homozygous-recessive genetic disorders."
      ],
      notes:[
        {label:"Described figure &mdash; a human pedigree chart", text:"A four-generation (I&ndash;IV) pedigree chart shows parents connected by a horizontal line, their children ranked below in birth order, and (where it occurs) a marked union between cousins indicating consanguinity &mdash; the standard layout used to trace any inherited trait through a family."},
        {label:"Nature of science &mdash; inductive reasoning", text:"A pattern of inheritance is deduced from only part of a pedigree chart by inductive reasoning (generalising from some, not all, cases); this inferred pattern can then be used to deduce the genotypes of specific, otherwise-untested individuals in the pedigree."}
      ]
    },
    {
      icon:"atom", title:"Continuous Variation, Polygenic Inheritance and Statistics",
      coreIdea:"Most human characteristics are controlled not by one gene but by several acting together (polygenic inheritance), producing continuous variation that must be summarised with statistical tools &mdash; mean, median, mode and the box-and-whisker plot &mdash; rather than with a simple whole-number ratio.",
      steps:[
        "<strong>Polygenic inheritance</strong> is the inheritance of a characteristic (such as height or skin colour) determined by the collective effect of several different genes, often (but not always) on different chromosomes; each gene has only a small individual effect, but their combined effect produces continuous variation among offspring. Human skin colour, for example, depends on melanin production controlled by three, four or more separately inherited genes, giving an almost continuous range of skin tones.",
        "Data that follow a <strong>normal distribution</strong> produce a symmetrical, bell-shaped curve when frequency is plotted against the measured classes, with the mode, median and mean all coinciding at the centre; a <strong>skewed distribution</strong> is asymmetrical, with values falling away faster on one side of the peak, so the mean and mode differ (a measure of the skew).",
        "Three measures of central tendency summarise how clustered a data set is: the <strong>mode</strong> (the most frequent value), the <strong>median</strong> (the middle value when data are ranked in order; the mean of the two middle values if there is an even number of values), and the <strong>mean</strong> (the sum of all values divided by the number of values, x&#772; = &Sigma;x &divide; n).",
        "For data that are not normally distributed, <strong>quartiles</strong> and a <strong>box-and-whisker plot</strong> are more appropriate than the mean: quartiles split an ordered data set into four equal parts (the median of the lower half gives the first quartile, the median of the upper half gives the third quartile); the box spans the <strong>interquartile range (IQR)</strong>, the first to the third quartile, covering the middle 50% of the data, with a line at the median and whiskers reaching to the minimum and maximum. A value more than 1.5 &times; IQR beyond either quartile is an outlier."
      ],
      notes:[{label:"Top tip", text:"The mode is not typically used as a measure of central tendency in biology, but is useful for describing a bimodal distribution (two peaks), which can result from disruptive selection. Box-and-whisker plots may be drawn either vertically or horizontally."}],
      side:{
        title:"A continuous variable: fruit length",
        charts:[{title:"Fruit length in a crop sample", caption:"A sample of 350 fruits, grouped into 10 mm length classes, gives an approximately bell-shaped frequency distribution", axis:"Fruit length (mm)", svg: bv2HistogramSvg("Histogram of fruit length in a sample of 350 fruits, showing an approximately bell-shaped continuous distribution peaking around 100-109 mm")}]
      }
    },
    {
      icon:"atom", hl:true, title:"Dihybrid Crosses and the Law of Independent Assortment",
      coreIdea:"When two gene pairs are carried on separate chromosomes, they assort into gametes completely independently of one another &mdash; so a cross between two double heterozygotes reliably produces offspring in the classic 9:3:3:1 ratio.",
      steps:[
        "Mendel crossed pure-breeding round, yellow-cotyledon pea plants (RRYY) with pure-breeding wrinkled, green-cotyledon plants (rryy). Because both parents are homozygous, each produces only one gamete type (RY or ry), so all F1 offspring are heterozygous for both genes (RrYy) and &mdash; since round and yellow are both dominant &mdash; all round and yellow.",
        "Because the R/r and Y/y genes lie on separate chromosomes, independent assortment during meiosis means each RrYy F1 individual produces four gamete types in equal proportions: RY, Ry, rY and ry (1/4 each).",
        "Self-fertilising the F1 combines these four gamete types from both parents in a 4 &times; 4 Punnett grid of 16 equally likely offspring, giving an F2 phenotype ratio of 9 round, yellow : 3 round, green : 3 wrinkled, yellow : 1 wrinkled, green &mdash; including two new, recombinant phenotype combinations not seen in either parent.",
        "Mendel&rsquo;s second law, the <strong>Law of Independent Assortment</strong>, states: two or more pairs of alleles segregate independently of each other as a result of meiosis, provided the genes concerned are not linked by being on the same chromosome. This reflects meiosis directly: the random orientation of each homologous pair at the equatorial plate means that, over many divisions, all possible combinations of maternal and paternal chromosomes occur in equal numbers."
      ],
      notes:[{label:"Common mistake", text:"In a dihybrid cross, the gametes from each parent must each carry one allele of every gene involved (e.g. ry, rY, Ry or RY) &mdash; it is incorrect to show one parent contributing only the alleles of one gene and the other parent contributing only the alleles of the other gene."}],
      side:{
        title:"Law of independent assortment and meiosis",
        table:{
          title:"How Mendel&rsquo;s dihybrid cross relates to meiosis",
          head:["Mendel&rsquo;s dihybrid cross","Feature of meiosis"],
          rows:[
            ["Breeding factors control characteristics and remain intact across generations.","Each chromosome holds a fixed, linear sequence of gene loci."],
            ["Two factors exist for each characteristic in each cell, one from each parent.","Chromosomes occur in homologous pairs, one of each pair from each parent."],
            ["Factors separate in reproduction; only one factor can be in any gamete.","Each gamete ends up with a single member of every homologous pair."],
            ["The 9:3:3:1 ratio shows all four gamete types are equally common.","Random orientation of homologous pairs at the equatorial plate gives all chromosome combinations in equal numbers over many divisions."]
          ]
        }
      }
    },
    {
      icon:"leaf", hl:true, title:"Gene Linkage, Recombinants and the Evidence from Drosophila",
      coreIdea:"Genes positioned close together on the same chromosome are inherited as a package rather than independently &mdash; and it took William Bateson and Reginald Punnett&rsquo;s sweet peas, followed by Thomas Morgan&rsquo;s fruit flies, to reveal gene linkage and the crossing-over process that occasionally breaks a linked package apart.",
      steps:[
        "Each gene occupies a fixed <strong>locus</strong> on a chromosome, so every eukaryotic chromosome is a linear series of gene loci; online databases (e.g. NCBI Gene) can be used to look up a human gene&rsquo;s locus and its polypeptide product, and to find genes that sit close together on the same chromosome versus genes on entirely different chromosomes.",
        "Bateson and Punnett crossed pure-breeding sweet pea plants (purple flower, long pollen &times; red flower, round pollen); the F1 were all purple, long-pollen, as expected. But self-crossing the F1 gave an F2 strongly skewed away from the 9:3:3:1 ratio &mdash; mostly parental-type offspring (296 purple/long, 85 red/round, versus 240 and 27 expected) with far fewer recombinant types (19 purple/round and 27 red/long, versus 80 and 80 expected) &mdash; evidence that these two genes are <strong>linked</strong> on the same chromosome rather than assorting independently.",
        "When linked genes are heterozygous, a chiasma (crossover point) forming <em>between</em> the two gene loci during meiosis exchanges alleles between homologous chromatids, creating new <strong>recombinant</strong> gamete types; a chiasma forming elsewhere on the chromosome leaves the parental allele combinations intact, so only parental-type gametes form. Because a chiasma between two particular loci is a comparatively rare event, most F2 offspring are of the parental type, with recombinants in the minority.",
        "Thomas Morgan chose the fruit fly <em>Drosophila melanogaster</em> for breeding experiments from 1908, winning a Nobel Prize in 1933; working with its four chromosome pairs, ~10-day generation time at 25&deg;C and hundreds of offspring per female, he established the Chromosome Theory of Inheritance (that Mendel&rsquo;s &lsquo;factors&rsquo; are linear sequences of genes on chromosomes), discovered sex linkage, and demonstrated crossing over directly.",
        "Crossing wild-type flies with a mutant strain homozygous for vestigial wing and ebony body (genes on separate autosomes) gave the expected unlinked 9:3:3:1 F2 ratio. But a test cross between a male homozygous for ebony body and curled wing and a heterozygous female carrying the dominant alleles together on one chromosome (GS/gs) gave 536 normal-body/straight-wing and 481 ebony/curled offspring (parental types) alongside only 101 normal/curled and 152 ebony/straight offspring (recombinants) &mdash; parental types far outnumbering recombinants, showing that few chiasmata form between these particular linked loci."
      ],
      notes:[
        {label:"Common mistake", text:"Do not confuse <strong>gene linkage</strong> (two or more genes together on the same, typically autosomal, chromosome) with <strong>sex linkage</strong> (a gene specifically located on a sex chromosome, usually the X). In diagrams, linked alleles are conventionally drawn as vertical pairs beside lines representing the homologous chromosomes, not written together as a single genotype string."},
        {label:"Nature of science &mdash; naming the mutants precisely", text:"The <em>Drosophila</em> mutant &lsquo;curled wing&rsquo; (used in the linked-gene test cross) is a different mutation from &lsquo;vestigial wing&rsquo; (used in the unlinked-gene cross) &mdash; a reminder to read experimental results carefully rather than assuming two similarly-described mutants are the same gene."}
      ],
      side:{
        title:"Parental types vastly outnumber recombinants",
        table:{
          title:"Drosophila linked-gene test cross (GS/gs &times; gs/gs)",
          head:["Offspring phenotype","Genotype","Class","Number"],
          rows:[
            ["Normal body, straight wing","GS/gs","Parental","536"],
            ["Ebony body, curled wing","gs/gs","Parental","481"],
            ["Normal body, curled wing","Gs/gs","Recombinant","101"],
            ["Ebony body, straight wing","gS/gs","Recombinant","152"]
          ]
        }
      }
    },
    {
      icon:"book", hl:true, title:"The Chi-Squared Test for Genetic Crosses",
      coreIdea:"Because random chance alone can shift real breeding results slightly away from Mendel&rsquo;s predicted ratios, the chi-squared test gives a rigorous, repeatable way to judge whether an observed deviation is just that chance variation, or large enough to force a rethink of the underlying genetics.",
      steps:[
        "A result is <strong>statistically significant</strong> if there is less than a 5% probability (p = 0.05) that it arose by chance alone. All statistical tests examine a <strong>null hypothesis</strong> (typically, that there is no real difference between observed and expected results) against an <strong>alternative hypothesis</strong> (that a real difference or association exists).",
        "The exact 9:3:3:1 ratio of a dihybrid cross is only guaranteed if fertilisation is entirely random, all offspring have equal survival chances, and very large numbers of offspring are produced; in practice, factors such as unequal fertilisation success, differential mortality, or uneven pollen/gamete transport can shift the observed numbers away from the exact prediction.",
        "The <strong>chi-squared (&chi;<sup>2</sup>) test</strong> estimates the probability that a difference between observed (O) and expected (E) results is due to chance: &chi;<sup>2</sup> = &Sigma; [(O &minus; E)<sup>2</sup> &divide; E]. If the deviation is unlikely to be due to chance, an alternative explanation (such as gene linkage) must be investigated instead.",
        "Applied to a <em>Drosophila</em> dihybrid cross (expected 9:3:3:1 of 556 offspring: 312.75, 104.25, 104.25, 34.75; observed: 315, 108, 101, 32), &chi;<sup>2</sup> = 0.016 + 0.135 + 0.101 + 0.218 = 0.47.",
        "The <strong>degrees of freedom</strong> (df) equal the number of phenotype categories minus 1 &mdash; here, 4 &minus; 1 = 3. Looking up df = 3 in a &chi;<sup>2</sup>-distribution table gives a critical value of 7.81 at p = 0.05; since the calculated &chi;<sup>2</sup> of 0.47 is far smaller than 7.81, the deviation from 9:3:3:1 is not statistically significant and is attributed to chance &mdash; the data conform to a Mendelian ratio."
      ],
      notes:[{label:"How to interpret a chi-squared result", text:"If the calculated &chi;<sup>2</sup> is smaller than the critical value at p = 0.05 for the relevant degrees of freedom, the difference between observed and expected results is not significant (likely due to chance). If it is larger, the difference is significant, and the original hypothesis (e.g. that the two genes are unlinked) must be reconsidered."}],
      side:{
        title:"Chi-squared worked calculation",
        table:{
          title:"&chi;<sup>2</sup> for a Drosophila dihybrid cross",
          head:["Category","O","E","O&minus;E","(O&minus;E)<sup>2</sup>&divide;E"],
          rows:[
            ["Normal wing, normal body","315","312.75","2.25","0.016"],
            ["Normal wing, ebony body","108","104.25","3.75","0.135"],
            ["Vestigial wing, normal body","101","104.25","&minus;3.25","0.101"],
            ["Vestigial wing, ebony body","32","34.75","&minus;2.75","0.218"],
            ["Total","556","&nbsp;","&nbsp;","&chi;<sup>2</sup> = 0.47"]
          ]
        }
      }
    }
  ],
  workedExamples: [
    {
      title:"Interpreting a monohybrid test cross (brachydactyly)",
      question:"A homozygous normal-handed parent (nn) has a child with a heterozygous brachydactylous parent (Nn), where brachydactyly is caused by a dominant mutant allele (N). Using a Punnett grid, calculate the probability that a child of this cross has brachydactylous hands.",
      answer:[
        "The nn parent produces only n gametes; the Nn parent produces n and N gametes in equal proportions (1/2 each).",
        "Combining these gametes gives offspring genotypes Nn and nn, each with a probability of 1/2.",
        "Since N is dominant, any child with at least one N allele (Nn) shows brachydactyly; a child with nn is normal-handed.",
        "The probability of a brachydactylous child is therefore 1/2, or 50%."
      ]
    },
    {
      title:"Predicting offspring blood groups",
      question:"A parent with blood group A (genotype I<sup>A</sup>i) has children with a parent of blood group B (genotype I<sup>B</sup>i). Determine the possible blood groups of their children and the proportion expected for each.",
      answer:[
        "The blood-group-A parent (I<sup>A</sup>i) produces gametes I<sup>A</sup> and i, each with probability 1/2; the blood-group-B parent (I<sup>B</sup>i) produces gametes I<sup>B</sup> and i, each with probability 1/2.",
        "Combining these gametes in a Punnett grid gives four equally likely genotypes: I<sup>A</sup>I<sup>B</sup>, I<sup>A</sup>i, I<sup>B</sup>i and ii, each with probability 1/4.",
        "Since I<sup>A</sup> and I<sup>B</sup> are codominant and both dominant to i, these genotypes correspond to phenotypes AB, A, B and O respectively.",
        "Each of the four blood groups &mdash; AB, A, B and O &mdash; is therefore expected in 25% of the children."
      ]
    },
    {
      title:"Predicting F2 flower colours in Mirabilis jalapa",
      question:"Two pink-flowered <em>Mirabilis jalapa</em> plants (genotype F<sup>R</sup>F<sup>W</sup>) are crossed. Predict the phenotype ratio of their offspring, explaining why a 3:1 ratio is not obtained.",
      answer:[
        "Each F<sup>R</sup>F<sup>W</sup> parent produces gametes F<sup>R</sup> and F<sup>W</sup>, each with probability 1/2.",
        "The Punnett grid gives offspring genotypes F<sup>R</sup>F<sup>R</sup>, F<sup>R</sup>F<sup>W</sup>, F<sup>R</sup>F<sup>W</sup> and F<sup>W</sup>F<sup>W</sup> in the ratio 1:2:1.",
        "Because F<sup>R</sup> and F<sup>W</sup> show incomplete dominance, the heterozygote F<sup>R</sup>F<sup>W</sup> has its own intermediate (pink) phenotype rather than resembling either homozygous parent.",
        "The resulting phenotype ratio is therefore 1 red : 2 pink : 1 white, not the 3:1 ratio seen with ordinary complete dominance."
      ]
    },
    {
      title:"Predicting the inheritance of haemophilia",
      question:"A woman who is a carrier for haemophilia (genotype X<sup>H</sup>X<sup>h</sup>) has children with a man who does not have haemophilia (genotype X<sup>H</sup>Y). Calculate the probability that (a) a daughter is a carrier, and (b) a son has haemophilia.",
      answer:[
        "The mother (X<sup>H</sup>X<sup>h</sup>) produces gametes X<sup>H</sup> and X<sup>h</sup>, each with probability 1/2; the father (X<sup>H</sup>Y) produces gametes X<sup>H</sup> and Y, each with probability 1/2.",
        "The Punnett grid gives four equally likely offspring genotypes: X<sup>H</sup>X<sup>H</sup> (normal female), X<sup>H</sup>X<sup>h</sup> (carrier female), X<sup>H</sup>Y (normal male) and X<sup>h</sup>Y (haemophiliac male).",
        "(a) Of the two possible female genotypes (X<sup>H</sup>X<sup>H</sup> and X<sup>H</sup>X<sup>h</sup>, each equally likely), half are carriers &mdash; so any daughter has a 50% chance of being a carrier.",
        "(b) Of the two possible male genotypes (X<sup>H</sup>Y and X<sup>h</sup>Y, each equally likely), half have haemophilia &mdash; so any son has a 50% chance of having haemophilia."
      ]
    },
    {
      title:"Predicting the ratio from a dihybrid test cross",
      question:"A pea plant heterozygous for both seed shape and cotyledon colour (RrYy) is crossed with a pea plant that is homozygous recessive for both genes (rryy). Determine the phenotype ratio of the offspring.",
      answer:[
        "The heterozygous parent (RrYy) produces four gamete types in equal proportions, since the genes are on separate chromosomes and assort independently: RY, Ry, rY and ry, each with probability 1/4.",
        "The homozygous recessive parent (rryy) produces only one gamete type, ry.",
        "Combining these gametes gives four offspring genotypes, each with probability 1/4: RrYy (round, yellow), Rryy (round, green), rrYy (wrinkled, yellow) and rryy (wrinkled, green).",
        "The phenotype ratio is therefore 1 round yellow : 1 round green : 1 wrinkled yellow : 1 wrinkled green (1:1:1:1) &mdash; the classic signature of a dihybrid test cross between unlinked genes."
      ]
    },
    {
      title:"Using the chi-squared test on a dihybrid test cross",
      question:"A dihybrid test cross between homozygous dwarf, terminal-flowered pea plants (ttaa) and heterozygous tall, axial-flowered plants (TtAa) produced the following progeny: 55 tall, axial; 51 tall, terminal; 49 dwarf, axial; 53 dwarf, terminal (total = 208). Use the chi-squared test to determine whether the difference between these observed results and the expected 1:1:1:1 ratio is significant.",
      answer:[
        "Since this is a test cross between a double heterozygote and a double homozygous recessive, the expected ratio is 1:1:1:1 &mdash; with 208 total offspring, the expected number in each of the four classes is 208 &divide; 4 = 52.",
        "Calculating (O &minus; E)<sup>2</sup> &divide; E for each class: tall/axial (55&minus;52)<sup>2</sup>&divide;52 = 0.173; tall/terminal (51&minus;52)<sup>2</sup>&divide;52 = 0.019; dwarf/axial (49&minus;52)<sup>2</sup>&divide;52 = 0.173; dwarf/terminal (53&minus;52)<sup>2</sup>&divide;52 = 0.019.",
        "Summing these gives &chi;<sup>2</sup> = 0.173 + 0.019 + 0.173 + 0.019 = 0.38.",
        "With 4 categories, degrees of freedom = 4 &minus; 1 = 3; the critical value at p = 0.05 for df = 3 is 7.81.",
        "Because the calculated &chi;<sup>2</sup> of 0.38 is far smaller than the critical value of 7.81, the difference between observed and expected results is not significant &mdash; it is due to chance, confirming that the two genes assort independently (are unlinked) and conform to the predicted 1:1:1:1 ratio."
      ]
    },
    {
      title:"Deducing genotypes from an albinism pedigree",
      question:"In a family pedigree, one grandparent in generation I has albinism (a recessive condition). None of that grandparent&rsquo;s children (generation II) have albinism, but one grandchild in generation IV does. Explain what this tells you about the genotypes of the generation II and generation III individuals involved.",
      answer:[
        "Because the generation-I individual has albinism, they must be homozygous recessive (pp); each of their children (generation II) must inherit one recessive allele (p) from this parent, so every generation-II child must be at least a carrier (Pp), even though none of them shows albinism themselves (the dominant allele from their other parent masks it).",
        "Albinism re-appears only in generation IV, two generations later, which means the generation-III individual in that line of descent must also be a carrier (Pp), having inherited the recessive allele from their generation-II parent.",
        "For a generation-IV child to have albinism (pp), their generation-III partner (who married into the family) must also happen to be a carrier (Pp), even though this cannot be deduced from their own ancestry on the chart.",
        "This illustrates why recessive conditions can skip multiple generations entirely before reappearing: the allele persists, unexpressed, in a long chain of heterozygous carriers until two carriers happen to have children together."
      ]
    }
  ],
  summary: [
    "Meiosis halves the chromosome number to produce haploid gametes, and fertilisation restores the diploid number &mdash; the pattern of inheritance common to all eukaryotes with a sexual life cycle.",
    "Gregor Mendel&rsquo;s large-scale pea-breeding experiments revealed that characteristics are controlled by discrete, paired factors (alleles) that segregate into gametes during meiosis (the Law of Segregation), overturning the earlier &lsquo;blending&rsquo; model of inheritance.",
    "<strong>Genotype</strong> is the combination of alleles an organism carries; <strong>phenotype</strong> is the observable result of genotype and/or environment. Homozygous genotypes (TT, tt) and heterozygous genotypes (Tt) can share the same dominant phenotype, distinguishable only by a <strong>test cross</strong> against a homozygous recessive.",
    "<strong>Phenotypic plasticity</strong> lets an organism develop environment-suited traits through varying gene expression, without any genotype change; <strong>phenylketonuria</strong>, by contrast, is a recessive single-gene disorder (mutated <em>PAH</em> gene) causing a fixed, serious phenotype unless diet is deliberately controlled.",
    "A <strong>single-nucleotide polymorphism (SNP)</strong> can create a new allele; most genes exist as <strong>multiple alleles</strong> in a population&rsquo;s gene pool, as shown by the three-allele, codominant human ABO blood-group system (I<sup>A</sup>, I<sup>B</sup>, i).",
    "<strong>Codominance</strong> (both alleles expressed together, e.g. AB blood group) and <strong>incomplete dominance</strong> (a blended, intermediate heterozygote phenotype, e.g. pink <em>Mirabilis</em> flowers, giving a 1:2:1 F2 ratio) both depart from the standard dominant/recessive 3:1 pattern.",
    "Sex is determined by the sex chromosomes (XX female, XY male); a gene on the X chromosome&rsquo;s non-homologous region is expressed in a male even if recessive, while a female can be an unaffected <strong>carrier</strong> &mdash; the basis of X-linked recessive conditions such as <strong>haemophilia</strong>.",
    "<strong>Pedigree charts</strong> let dominant traits (appearing in every generation) and recessive traits (skipping generations, as in albinism) be distinguished from family history alone, since controlled human breeding experiments are impossible.",
    "<strong>Polygenic inheritance</strong> (several genes acting together, as in human skin colour or height) produces continuous variation, summarised using the mean, median and mode, or &mdash; for non-normal data &mdash; quartiles and a box-and-whisker plot (median, IQR and outliers beyond 1.5 &times; IQR).",
    "<strong>HL:</strong> when two genes lie on separate chromosomes, they assort into gametes independently (Mendel&rsquo;s Law of Independent Assortment), so a double-heterozygote self-cross gives the classic 9:3:3:1 dihybrid ratio.",
    "<strong>HL:</strong> genes positioned close together on the same chromosome are <strong>linked</strong> and do not assort independently, as Bateson and Punnett first showed in sweet peas; a <strong>recombinant</strong> gamete only arises when a chiasma forms between the two linked loci during meiosis.",
    "<strong>HL:</strong> Thomas Morgan&rsquo;s <em>Drosophila</em> experiments established the Chromosome Theory of Inheritance, discovered sex linkage, and demonstrated crossing over directly &mdash; his linked-gene test cross produced far more parental-type than recombinant-type offspring.",
    "<strong>HL:</strong> the chi-squared test (&chi;<sup>2</sup> = &Sigma;[(O&minus;E)<sup>2</sup>&divide;E]) estimates whether a deviation between observed and expected cross results is due to chance; if the calculated value is below the critical value for the relevant degrees of freedom at p = 0.05, the deviation is not significant.",
    "<strong>HL:</strong> each gene occupies a fixed <strong>locus</strong> on a chromosome; online gene databases can locate a human gene&rsquo;s locus and its polypeptide product, and reveal whether two genes sit on the same chromosome (and so might show linkage) or on different chromosomes."
  ]
}
