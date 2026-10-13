{
  subtitle: "DNA replication produces exact copies of DNA ahead of every cell division, and understanding how it works &mdash; semi-conservatively, directionally, and with built-in proofreading &mdash; has also given biotechnology two of its most powerful tools: PCR and gel electrophoresis.",
  keyTerms: [
    {icon:"leaf", color:"green", term:"DNA replication", def:"Production of exact copies of DNA, with identical base sequences, required for reproduction and for growth and tissue replacement."},
    {icon:"atom", color:"teal", term:"Semi-conservative replication", def:"Each strand of an existing DNA double helix acts as a template for synthesis of a new strand from free nucleotides, so each daughter molecule keeps one original (&lsquo;parent&rsquo;) strand and gains one newly made strand."},
    {icon:"bars", color:"gold", term:"Helicase", def:"An enzyme that unwinds the DNA double helix at replication forks, breaking the hydrogen bonds between the two strands."},
    {icon:"atom", color:"plum", term:"DNA polymerase", def:"An enzyme that links nucleotides together to form a new DNA strand, using a pre-existing strand as a template, and proofreads as it goes."},
    {icon:"leaf", color:"red", term:"Polymerase chain reaction (PCR)", def:"A technique for amplifying selected regions of DNA by multiple, automated cycles of heating and cooling, doubling the number of copies each cycle."},
    {icon:"atom", color:"green", term:"Taq polymerase", def:"A heat-stable DNA polymerase used in PCR, extracted from the thermophilic bacterium <em>Thermus aquaticus</em>; unlike most DNA polymerases, it survives the repeated heating to 95&deg;C used to separate DNA strands."},
    {icon:"bars", color:"teal", term:"DNA primer", def:"A short, synthetic, single strand of DNA with a base sequence complementary to one end of a target sequence, used to give DNA polymerase a starting point."},
    {icon:"atom", color:"gold", term:"Gel electrophoresis", def:"A technique that separates fragments of DNA or protein on a polymer gel according to size and overall charge, by migration through the gel in an electric field."},
    {icon:"leaf", color:"plum", term:"Restriction enzyme", def:"An enzyme that cuts DNA at a specific base sequence wherever it occurs, producing fragments of different lengths for electrophoresis."},
    {icon:"bars", color:"red", term:"Gene probe", def:"A single strand of DNA, made radioactive or fluorescently labelled, with a base sequence complementary to a particular fragment or gene, used to reveal its position after electrophoresis."},
    {icon:"atom", color:"teal", term:"Genetic profiling", def:"The identification of individual organisms or species using DNA, combining PCR and gel electrophoresis; also called genetic fingerprinting."},
    {icon:"leaf", color:"gold", term:"VNTRs and STRs", def:"Variable number tandem repeats (10&ndash;100-nucleotide repeat units) and short tandem repeats (2&ndash;13-nucleotide repeat units): non-coding DNA sequences that vary between individuals in the number of repeats present, making each person&rsquo;s profile unique (except identical twins)."},
    {icon:"bars", color:"plum", term:"Southern blotting", def:"A technique that transfers DNA fragments separated by electrophoresis from a gel onto a nylon membrane, where they can be probed and visualised by autoradiography."},
    {icon:"atom", color:"red", term:"Replication fork", def:"<strong>HL</strong> &mdash; A point where the two DNA strands have separated and both act as templates; replication spreads outward from many forks along the helix."},
    {icon:"leaf", color:"green", term:"Primase", def:"<strong>HL</strong> &mdash; An RNA polymerase that synthesizes a short RNA primer complementary to the template DNA, giving DNA polymerase the free 3&prime;&ndash;OH end it needs to begin synthesis."},
    {icon:"atom", color:"teal", term:"Leading strand", def:"<strong>HL</strong> &mdash; At a replication fork, the new DNA strand made by continuous synthesis in the 5&prime; to 3&prime; direction, immediately behind the advancing helicase."},
    {icon:"bars", color:"gold", term:"Lagging strand", def:"<strong>HL</strong> &mdash; The new DNA strand synthesized discontinuously, in short, separately primed Okazaki fragments, in the direction opposite to the moving replication fork."},
    {icon:"atom", color:"plum", term:"Okazaki fragments", def:"<strong>HL</strong> &mdash; Short lengths of DNA produced on the lagging strand, each started by its own RNA primer, later joined together by DNA ligase."},
    {icon:"leaf", color:"red", term:"DNA polymerase I and III", def:"<strong>HL</strong> &mdash; DNA polymerase III is the main enzyme that extends new DNA strands from each primer; DNA polymerase I removes the RNA primer at the start of each Okazaki fragment and replaces it with DNA."},
    {icon:"bars", color:"green", term:"DNA ligase", def:"<strong>HL</strong> &mdash; An enzyme that joins two DNA fragments together by forming a phosphodiester bond, sealing adjacent Okazaki fragments into one continuous lagging strand."},
    {icon:"atom", color:"teal", term:"DNA gyrase and single-strand binding proteins", def:"<strong>HL</strong> &mdash; DNA gyrase relieves the strain caused as the double helix is unwound; single-strand binding proteins attach to the separated strands and stop them rejoining."},
    {icon:"leaf", color:"gold", term:"Proofreading", def:"<strong>HL</strong> &mdash; The process by which DNA polymerase removes a mismatched base it has just added from the 3&prime; end of the new strand and replaces it with the correct, complementary base."}
  ],
  theories: [
    {
      icon:"leaf", title:"Semi-Conservative DNA Replication",
      coreIdea:"DNA replication produces exact copies of DNA with identical base sequences by a semi-conservative mechanism, in which each new double helix is made of one original strand and one newly synthesized strand &mdash; a model confirmed experimentally by Meselson and Stahl.",
      steps:[
        "A copy of each chromosome must pass into every daughter cell formed by cell division, so chromosomes must first be copied (replicated); this is required both for reproduction and for growth and tissue replacement in multicellular organisms.",
        "At the end of replication, each new pair of DNA strands reforms as a double helix. In this <strong>semi-conservative replication</strong>, one strand of each new helix comes from the original chromosome and one is newly synthesized &mdash; so half of the original molecule is conserved in each daughter helix.",
        "This contrasts with a hypothetical &lsquo;conservative&rsquo; model, in which an entirely new double helix would form alongside an untouched original, so that one complete original molecule would remain intact rather than being distributed between the daughter molecules.",
        "Watson and Crick proposed the semi-conservative model, but had no direct evidence for it. Meselson and Stahl tested it by growing <em>E. coli</em> in a medium containing only the heavy nitrogen isotope <sup>15</sup>N, so that all of the bacterium&rsquo;s DNA became &lsquo;heavy&rsquo;.",
        "The bacteria were then transferred to a medium containing only the lighter, more abundant isotope <sup>14</sup>N (both stable, non-radioactive forms of nitrogen); new DNA made from this point on was built of <sup>14</sup>N. Because <em>E. coli</em> cultures divide synchronously (every 60 minutes), the change in the ratio of heavy to light DNA could be tracked generation by generation.",
        "DNA from each generation was separated by density in a centrifuge, using a salt solution of increasing density: heavier DNA settled nearer the base of the tube, lighter DNA stayed nearer the top. The resulting pattern &mdash; all-heavy DNA giving way to all-hybrid DNA after one generation, then a mix of hybrid and all-light DNA after a second generation &mdash; matched the semi-conservative model exactly, and ruled out the conservative alternative."
      ],
      notes:[{label:"Why this mattered", text:"Scientific knowledge must be supported by evidence: Watson and Crick&rsquo;s proposal was only a hypothesis until Meselson and Stahl&rsquo;s experiment gave it direct experimental support, illustrating how a model can be rigorously tested rather than simply assumed."}]
    },
    {
      icon:"atom", title:"How Helicase and DNA Polymerase Replicate DNA",
      coreIdea:"Replication proceeds in three linked steps &mdash; unwinding, base pairing, and strand synthesis &mdash; carried out by two key enzymes, helicase and DNA polymerase, in the simpler prokaryotic system described at SL.",
      steps:[
        "<strong>Helicase</strong> unwinds the DNA double helix at one region, breaking the hydrogen bonds holding the two strands together and temporarily keeping them separated &mdash; exposing unpaired nucleotides surrounded by a pool of free-floating nucleotides.",
        "Both exposed strands now act as templates: complementary free nucleotides line up opposite each exposed base by complementary base pairing (adenine with thymine, cytosine with guanine), and hydrogen bonds form to hold them in place.",
        "A condensation reaction then links the sugar and phosphate groups of adjacent nucleotides together, forming the new strand&rsquo;s sugar&ndash;phosphate backbone; this reaction is catalysed by <strong>DNA polymerase</strong>.",
        "DNA polymerase also proofreads as it goes, correcting mistakes such as incorrectly paired bases, so that the two strands finally formed are identical in sequence to the two original strands."
      ],
      notes:[
        {label:"Common mistake", text:"It is incorrect to say that &lsquo;helicase is in charge of elongation of DNA&rsquo; &mdash; helicase only unwinds the DNA; DNA polymerase then acts on the exposed single strands to build the new ones."},
        {label:"Nature of science &mdash; tools shape the knowledge produced", text:"Research using the DNA virus SV40 <em>in vitro</em> first identified replication polymerases, but entirely missed helicase, since that activity was supplied by a viral protein (the SV40 large T-antigen) instead &mdash; the tool used gave only partial knowledge. More recently, cryogenic electron microscopy (CEM) has given atomic-resolution, three-dimensional images of replication proteins as they change shape while working."}
      ]
    },
    {
      icon:"book", title:"PCR: Amplifying DNA in the Laboratory",
      coreIdea:"The polymerase chain reaction copies a chosen DNA sequence repeatedly and automatically, doubling the amount of DNA with every heating-and-cooling cycle &mdash; allowing a usable amount of DNA to be produced from as little as a single starting molecule.",
      steps:[
        "Often only a tiny sample of DNA is available, such as at a crime scene or in genetic engineering; PCR solves this by amplifying (copying) a chosen region of double-stranded DNA with known end sequences many times over, entirely automatically, <em>in vitro</em>.",
        "The DNA sample is heated to about 95&deg;C to separate (denature) the two strands, then cooled to about 40&deg;C so that short, synthetic <strong>DNA primers</strong> &mdash; complementary to the end sequences of the target fragment &mdash; can bind to each strand.",
        "Heat-tolerant <strong>Taq polymerase</strong> and excess free nucleotides are then added, and the mixture is heated to about 72&deg;C: Taq polymerase extends each primer, using the single strands as templates, to build two new complementary strands.",
        "The cycle is then repeated using the two new double strands as additional templates, so the number of copies of the target sequence doubles with every cycle.",
        "PCR has two main limitations: it requires prior knowledge of the DNA (or amino acid) sequence of the target region in order to design the flanking primers, and because primers are short sequences, they may not be specific enough, so a non-target sequence can sometimes be amplified by mistake."
      ],
      notes:[{label:"Why Taq polymerase specifically", text:"Taq polymerase is named after the heat-tolerant bacterium it was isolated from, <em>Thermus aquaticus</em>, which lives in hot springs and hydrothermal vents. Its heat stability makes it ideal for PCR, where repeated heating to separate strands would destroy an ordinary DNA polymerase. Unlike DNA polymerase in a living cell, Taq polymerase does not proofread, so errors in base pairing can occasionally occur during PCR."}],
      side:{
        title:"The PCR cycle",
        table:{
          title:"One cycle of the polymerase chain reaction",
          head:["Step","Approx. temperature","What happens"],
          rows:[
            ["Denaturation","95&deg;C","Hydrogen bonds break; the double strand separates into two single strands"],
            ["Annealing","40&deg;C","Short DNA primers bind to their complementary sequence at each strand&rsquo;s end"],
            ["Extension","72&deg;C","Taq polymerase adds nucleotides to each primer, building two new strands"]
          ]
        }
      }
    },
    {
      icon:"atom", title:"Gel Electrophoresis and Visualizing DNA Fragments",
      coreIdea:"Gel electrophoresis separates DNA fragments by size and charge in an electric field, and once separated, the otherwise invisible fragments are revealed using gene probes or stains.",
      steps:[
        "A sample of DNA is first cut into fragments of different lengths using one or more <strong>restriction enzymes</strong>, each of which cuts the DNA wherever a particular base sequence occurs along its length.",
        "The fragments are loaded into wells cut near one end of a gel (agarose, a very pure form of agar, or polyacrylamide), which is submersed in a conducting buffer solution; several different samples can be loaded and separated on one gel at once.",
        "Separation then depends on two factors together: the gel&rsquo;s tiny pores act as a molecular sieve, through which small fragments move faster than large ones, and the phosphate groups of DNA give it a net negative charge, so in the applied electric field all fragments migrate towards the positive electrode (anode).",
        "After the current has run for long enough, DNA has separated into bands of different-sized fragments (an electrophoretogram); because the fragments are tiny and transparent, they are not immediately visible.",
        "Fragments can then be identified with <strong>gene probes</strong> &mdash; single strands of DNA complementary to a particular fragment, made radioactive (detected by exposing X-ray film) or fluorescently labelled (detected under UV light) &mdash; or with stains that reveal all DNA fragments at once, such as ethidium bromide (fluorescent under UV, though a potential carcinogen) or methylene blue (less sensitive, fading quickly)."
      ],
      side:{
        title:"Revealing separated DNA",
        table:{
          title:"Gene probes vs general stains",
          head:["Method","How it reveals DNA"],
          rows:[
            ["Gene probe","Binds only to one complementary target sequence; detected by autoradiography or UV fluorescence"],
            ["Ethidium bromide","Binds any DNA present; fluoresces under short-wave UV light"],
            ["Methylene blue","Stains any DNA and the gel itself; less sensitive, fades quickly"]
          ]
        }
      }
    },
    {
      icon:"leaf", title:"DNA Profiling and Its Forensic Applications",
      coreIdea:"Genetic profiling exploits the fact that each person&rsquo;s non-coding DNA contains a unique pattern of repeated sequences, giving PCR and gel electrophoresis a powerful set of real-world identification applications.",
      prose:[
        "Most of our DNA does not code for protein. These extensive non-gene regions include short sequences of bases repeated many times &mdash; called <strong>VNTRs</strong> (variable number tandem repeats, with repeating units of 10&ndash;100 nucleotides) and <strong>STRs</strong> (short tandem repeats, with repeating units of 2&ndash;13 nucleotides). We each inherit a distinctive combination of these apparently non-functional repeats, half from each parent, giving every person (except identical twins) a unique nucleotide pattern.",
        "To produce a genetic profile, a DNA sample is cut with a restriction enzyme acting close to the VNTR/STR regions, and gel electrophoresis separates the resulting fragments by length into a pattern of bands. In <strong>Southern blotting</strong>, these separated fragments are made single-stranded, transferred (blotted) from the gel onto a nylon membrane, and then probed with radioactively or fluorescently labelled DNA probes that bind to particular bands and reveal their positions.",
        "In forensic science, DNA profiling can identify suspects from samples (blood, other body fluids, hair, pollen or plant fragments) recovered at a crime scene, compared against profiles from victims, suspects and uninvolved control individuals &mdash; with great care taken to avoid cross-contamination. It can also identify corpses too decomposed for visual recognition, by comparing DNA from body tissue with that of close relatives or from the person&rsquo;s own belongings.",
        "In determining paternity, profiles from a child, mother and possible father are compared side by side: because a child inherits half its DNA from each parent, any bands in the child&rsquo;s profile that do not match the mother&rsquo;s profile must have come from the father. Profiling can also confirm whether individuals of an endangered species were bred in captivity or taken from the wild."
      ],
      notes:[{label:"Nature of science &mdash; reliability through repeated measurement", text:"Increasing the number of markers used (DNA sequences with a known physical location, including SNPs and STRs) reduces the probability of a false match, because each additional band gives one more independent point of comparison between two profiles."}]
    },
    {
      icon:"atom", hl:true, title:"Directionality of DNA Polymerase",
      coreIdea:"The two strands of the DNA double helix are antiparallel, and DNA polymerase can only build a new strand in one direction &mdash; a constraint that shapes every later detail of replication.",
      steps:[
        "The two strands of the DNA double helix run in opposite directions: one from 5&prime; to 3&prime;, the other from 3&prime; to 5&prime;. These <strong>antiparallel</strong> strands matter both for replication and for later transcription of the genetic code into mRNA.",
        "DNA polymerase requires an existing free 3&prime;&ndash;OH group to begin synthesis, adding the 5&prime; end of each new nucleotide on to the 3&prime; end of the growing strand. This means it can synthesize a new strand in only one direction: moving along the template strand from 3&prime; to 5&prime;, while building the new strand from 5&prime; to 3&prime;.",
        "This one-way synthesis is also required for proofreading to work: a hypothetical polymerase synthesizing 3&prime; to 5&prime; could not proofread, because removing an incorrectly paired nucleotide would leave a chain with no free end that could be elongated further.",
        "Because a self-correcting polymerase must be able to keep extending the chain after removing its own errors, DNA polymerase must proceed exclusively in the 5&prime; to 3&prime; direction &mdash; the single rule from which the very different behaviour of the leading and lagging strands follows."
      ]
    },
    {
      icon:"atom", hl:true, title:"Leading and Lagging Strand Replication",
      coreIdea:"Because DNA polymerase can only synthesize 5&prime; to 3&prime;, and the two parental strands run in opposite directions, one new strand is made continuously while the other must be made discontinuously, in short, separately primed fragments.",
      steps:[
        "Replication begins at many points along the double helix, called <strong>replication forks</strong>, where <strong>helicase</strong> separates the strands (forming a &lsquo;bubble&rsquo;); <strong>DNA gyrase</strong> relieves the strain this unwinding causes, and <strong>single-strand binding proteins</strong> attach to the separated strands to stop them rejoining.",
        "Both strands are replicated simultaneously, but since DNA polymerase III can only add nucleotides to a free 3&prime; end, both new strands can only elongate 5&prime; to 3&prime; &mdash; so the details of replication differ between the two antiparallel template strands.",
        "On the exposed 5&prime; to 3&prime; template, the <strong>leading strand</strong> is built continuously, immediately behind the advancing helicase as fresh template is exposed; it only needs one RNA primer, made once by the enzyme <strong>primase</strong>, to give DNA polymerase III its starting 3&prime; end.",
        "On the other, antiparallel template, the <strong>lagging strand</strong> must be built discontinuously, in short <strong>Okazaki fragments</strong> running in the direction opposite to the moving fork; because each fragment needs its own starting point, primase repeatedly lays down new RNA primers at intervals along this strand.",
        "<strong>DNA polymerase I</strong> then removes each RNA primer and replaces it with DNA, and <strong>DNA ligase</strong> seals the gaps between adjacent Okazaki fragments into one continuous lagging strand &mdash; so, in summary: primase primes, DNA polymerase III extends, DNA polymerase I repairs the primer gaps, and ligase joins the pieces together."
      ],
      notes:[
        {label:"Common mistake", text:"An RNA primer begins replication on <em>both</em> the lagging strand and the leading strand &mdash; not only on the lagging strand; the leading strand simply needs just one primer rather than several."},
        {label:"Nature of science &mdash; discovering Okazaki fragments", text:"Reiji and Tsuneko Okazaki discovered these fragments using a pulse&ndash;chase experiment: replicating DNA was exposed to a brief &lsquo;pulse&rsquo; of isotope-labelled nucleotides, followed by a &lsquo;chase&rsquo; period of unlabelled ones. With short chases, labelled radioactivity appeared mostly in small, slowly sedimenting DNA fragments; with longer chases, it increasingly appeared in larger, faster-sedimenting DNA &mdash; showing that short lagging-strand fragments are progressively joined into longer, continuous strands over time."}
      ],
      side:{
        title:"Enzymes of replication",
        table:{
          title:"Table D1.1.1 &mdash; enzymes that bring about DNA replication",
          head:["Enzyme","Role"],
          rows:[
            ["Helicase","Separates the two DNA strands to expose a replication fork, preventing them rejoining"],
            ["DNA gyrase","Relieves the strain caused as the double helix is unwound"],
            ["Single-strand binding proteins","Attach to separated strands and prevent them from rejoining"],
            ["Primase","Forms RNA primers &mdash; once on the leading strand, repeatedly on the lagging strand"],
            ["DNA polymerase III","Builds new DNA, beginning at each RNA primer"],
            ["DNA polymerase I","Replaces the RNA primer at the start of each Okazaki fragment with DNA"],
            ["DNA ligase","Joins adjacent Okazaki fragments together"]
          ]
        }
      }
    },
    {
      icon:"book", hl:true, title:"DNA Proofreading",
      coreIdea:"DNA polymerase does not just build new DNA strands &mdash; it also checks its own work, removing incorrectly paired bases as it goes, and this proofreading ability depends entirely on replication running only 5&prime; to 3&prime;.",
      steps:[
        "Proofreading is carried out by both prokaryotes and eukaryotes. DNA polymerase III occasionally adds an incorrect (mismatched) base to the growing strand, which does not pair correctly with the template base opposite it.",
        "A nuclease activity within the polymerase detects this mismatch and removes the incorrect base from the 3&prime; end of the new strand, by cleaving the phosphodiester bond that attached it.",
        "The polymerase then adds the correct, complementary base in its place, and normal 5&prime; to 3&prime; synthesis continues; polymerization and proofreading are coordinated, carried out by different catalytic domains within the same polymerase molecule.",
        "This mechanism is only possible because DNA polymerase always synthesizes 5&prime; to 3&prime;: removing a wrongly added base leaves a free 3&prime; end that can still be extended, so proofreading and continued synthesis do not conflict with one another."
      ]
    }
  ],
  workedExamples: [
    {
      title:"Predicting DNA density after Meselson&ndash;Stahl-style replication",
      question:"<em>E. coli</em> is grown in a medium where the only available nitrogen is the heavy isotope <sup>15</sup>N, so that all of its DNA becomes &lsquo;heavy&rsquo;. It is then transferred to a medium containing only the light isotope <sup>14</sup>N and allowed to divide twice. Using the semi-conservative model, predict the proportions of heavy, hybrid (one heavy strand + one light strand) and fully light DNA molecules present after (a) one generation and (b) two generations.",
      answer:[
        "(a) After one round of replication, each original heavy strand acts as a template and pairs with a newly made light strand &mdash; so 100% of the DNA molecules are hybrid (one heavy, one light strand); no fully heavy or fully light molecules remain.",
        "(b) After a second round, each hybrid molecule&rsquo;s two strands separate and each acts as a template: the heavy strand pairs with a new light strand (forming another hybrid molecule), while the light strand pairs with a new light strand (forming a fully light molecule) &mdash; giving 50% hybrid and 50% fully light DNA; no heavy DNA molecules remain.",
        "This pattern matches what Meselson and Stahl actually observed by density-gradient centrifugation, confirming semi-conservative replication as proposed by Watson and Crick."
      ]
    },
    {
      title:"Calculating DNA yield after PCR cycles",
      question:"A forensic scientist begins PCR with a single double-stranded DNA molecule recovered from a crime scene. Calculate the number of copies of the target sequence present after 10 complete PCR cycles, and explain why Taq polymerase, rather than a standard DNA polymerase, is used for this process.",
      answer:[
        "Each PCR cycle doubles the number of copies present, so after <em>n</em> cycles, copies = 1 &times; 2<sup>n</sup>.",
        "After 10 cycles, copies = 2<sup>10</sup> = 1024 copies.",
        "Taq polymerase is a heat-stable DNA polymerase extracted from the thermophile <em>Thermus aquaticus</em>. Because PCR requires repeated heating to about 95&deg;C to separate the DNA strands, an ordinary DNA polymerase would be denatured (destroyed) at this temperature, whereas Taq polymerase tolerates it and remains active through many repeated cycles."
      ]
    },
    {
      title:"Identifying leading and lagging strand synthesis",
      question:"At a replication fork, one new DNA strand is synthesized continuously in the same direction the fork is opening, while the other is synthesized as a series of short, separately primed fragments in the opposite direction. (a) Name each strand. (b) Explain, in terms of DNA polymerase directionality, why the second strand must be made this way. (c) Name the enzyme that joins the short fragments into one continuous strand.",
      answer:[
        "(a) The continuously synthesized strand is the leading strand; the strand made in short fragments is the lagging strand.",
        "(b) DNA polymerase III can only add nucleotides to a free 3&prime; end, so it synthesizes new DNA only in the 5&prime; to 3&prime; direction. Because the two parental template strands are antiparallel, only one of them is oriented so that its complementary strand can be built continuously towards the fork; the other template forces synthesis of its complementary strand to run away from the fork, so DNA polymerase must restart repeatedly on short, separately primed Okazaki fragments as more template is exposed.",
        "(c) DNA ligase joins the Okazaki fragments together, after DNA polymerase I has replaced each fragment&rsquo;s RNA primer with DNA."
      ]
    },
    {
      title:"Interpreting a DNA profile for paternity testing",
      question:"A gel electrophoresis DNA profile shows a child&rsquo;s bands at positions 2, 5, 7 and 9. The mother&rsquo;s profile shows bands at 2, 5, 6 and 8. A possible father&rsquo;s profile shows bands at 1, 3, 7 and 9. Using this information, explain whether this man could be the child&rsquo;s biological father.",
      answer:[
        "A child inherits half of its DNA bands from its mother and half from its father. Bands 2 and 5 in the child&rsquo;s profile match bands in the mother&rsquo;s profile, so these came from her.",
        "The remaining bands in the child&rsquo;s profile, at 7 and 9, did not come from the mother and so must have come from the biological father.",
        "The possible father&rsquo;s profile does show bands at both 7 and 9, so his profile is consistent with him being the biological father &mdash; although in a real case, many more markers would need to be compared before the match could be considered statistically reliable."
      ]
    }
  ],
  summary: [
    "DNA replication produces exact copies of DNA with identical base sequences; it underlies reproduction, growth and tissue replacement, and occurs during interphase, ahead of nuclear division.",
    "Replication is semi-conservative: each new double helix keeps one original strand and gains one newly synthesized strand; this was confirmed experimentally by Meselson and Stahl using <sup>15</sup>N/<sup>14</sup>N-labelled <em>E. coli</em> DNA.",
    "Helicase unwinds (&lsquo;unzips&rsquo;) the double helix at replication forks; DNA polymerase then builds new strands by complementary base pairing and condensation, and proofreads mismatches as it goes.",
    "PCR uses heat-stable Taq polymerase to amplify tiny DNA samples exponentially &mdash; copies double each heating/cooling cycle &mdash; but needs known primer sequences and can occasionally amplify non-target DNA.",
    "Gel electrophoresis separates restriction-enzyme-cut DNA fragments by size and charge in an electric field; gene probes or stains such as ethidium bromide then reveal the otherwise invisible bands.",
    "Genetic profiling exploits individual variation in non-coding VNTRs/STRs to produce a unique banding pattern for each person (except identical twins), used in forensic suspect identification, identifying corpses, and paternity testing.",
    "Southern blotting transfers separated DNA fragments from a gel onto a nylon membrane, where labelled gene probes bind to and reveal specific sequences by autoradiography.",
    "<strong>HL:</strong> DNA strands are antiparallel (5&prime;&rarr;3&prime; and 3&prime;&rarr;5&prime;); DNA polymerase can only extend a strand 5&prime;&rarr;3&prime; from a free 3&prime;&ndash;OH, so it moves along the template strand 3&prime;&rarr;5&prime;.",
    "<strong>HL:</strong> At each replication fork, the leading strand is synthesized continuously towards the fork using a single primer; the lagging strand is synthesized discontinuously, away from the fork, as Okazaki fragments, each starting with its own RNA primer made by primase.",
    "<strong>HL:</strong> DNA polymerase III extends both new strands; DNA polymerase I removes RNA primers and replaces them with DNA; DNA ligase joins adjacent Okazaki fragments; DNA gyrase and single-strand binding proteins assist unwinding.",
    "<strong>HL:</strong> DNA polymerase proofreads by removing a mismatched base from the 3&prime; end of the new strand and replacing it correctly &mdash; a mechanism only possible because synthesis proceeds exclusively 5&prime;&rarr;3&prime;."
  ]
}
