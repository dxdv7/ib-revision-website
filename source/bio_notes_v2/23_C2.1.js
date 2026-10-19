{
  unified: true,
  subtitle: "Cells communicate using chemical signals (ligands) that bind specific receptor proteins, triggering signal transduction pathways inside the target cell &mdash; from bacterial quorum sensing, to hormones and neurotransmitters acting through transmembrane or intracellular receptors, to the feedback loops that switch these pathways on and off.",
  keyTerms: [
    {icon:"atom", color:"teal", term:"Ligand", def:"A general term for a molecule that binds to a specific site on a protein &mdash; in cell signalling, the chemical signal itself."},
    {icon:"leaf", color:"green", term:"Chemical signalling &amp; signal transduction", def:"Chemical signalling: the release of ligands that bind to a specific molecule, delivering a signal within a cell or to another cell. Signal transduction: the process by which a cell converts an extracellular signal into an intracellular response."},
    {icon:"bars", color:"gold", term:"Receptor protein", def:"A protein that recognizes and binds a specific chemical signal molecule, usually on the outside of the plasma membrane, and is distinct from a sensory &lsquo;receptor&rsquo; cell."},
    {icon:"atom", color:"plum", term:"Second messenger", def:"A small intracellular ligand (e.g. cyclic AMP or Ca<sup>2+</sup>) generated or released inside a cell in response to an extracellular signal, which greatly amplifies and spreads that signal."},
    {icon:"leaf", color:"red", term:"Scaffold, relay, effector &amp; amplifier proteins", def:"Scaffold protein: holds several signalling proteins close together for a faster response. Relay protein: passes the signal to the next pathway member. Effector protein: causes the change inside the cell. Amplifier/transducer protein: boosts and converts the signal."},
    {icon:"bars", color:"teal", term:"Quorum sensing", def:"The ability of some bacteria to monitor their own cell density, via a diffusible signal molecule, and adjust gene expression accordingly once a threshold population size is reached."},
    {icon:"atom", color:"green", term:"Autoinducer", def:"A signalling molecule produced and detected by bacteria participating in quorum sensing; its own synthesis is often switched on by positive feedback once a threshold concentration is reached."},
    {icon:"leaf", color:"gold", term:"Hormone", def:"An extracellular signal molecule secreted and transported via the bloodstream (animals) or sap (plants) to distant target tissues, where it causes a specific, longer-lasting effect."},
    {icon:"bars", color:"plum", term:"Neurotransmitter &amp; cytokine", def:"Neurotransmitter: a chemical released at the presynaptic membrane of an axon when an action potential arrives, transmitting the signal across the synapse. Cytokine: a small secreted protein controlling growth and differentiation of specific target cells."},
    {icon:"atom", color:"red", term:"Transmembrane vs intracellular receptor", def:"Transmembrane receptor: spans the plasma membrane, binding polar, water-soluble ligands on the cell surface. Intracellular receptor: a soluble protein in the cytoplasm or nucleus, binding non-polar, lipid-soluble ligands that diffuse through the membrane."},
    {icon:"leaf", color:"teal", term:"Signal cascade &amp; phosphorylation cascade", def:"Signal cascade: a series of linked reactions carrying and amplifying information within a cell. Phosphorylation cascade: a sequence in which one protein kinase phosphorylates and activates the next, amplifying the signal at each step."},
    {icon:"bars", color:"green", term:"G protein &amp; GPCR", def:"G protein: a membrane-bound GTP-binding protein activated when a ligand binds a transmembrane receptor. G protein-coupled receptor (GPCR): a cell-surface receptor, built from seven transmembrane &alpha;-helices, that activates a G protein when bound to its ligand."},
    {icon:"atom", color:"plum", term:"Cyclic AMP (cAMP)", def:"A small intracellular signalling molecule generated from ATP by adenylyl cyclase in response to hormonal stimulation of a cell-surface receptor, and broken down by phosphodiesterase to end the signal."},
    {icon:"leaf", color:"red", term:"Kinase &amp; phosphorylase", def:"Kinase: an enzyme that transfers a phosphate group from ATP to a target protein, usually activating it. Phosphorylase: an enzyme that breaks down a polysaccharide such as glycogen into glucose 1-phosphate."},
    {icon:"bars", color:"gold", term:"Receptor tyrosine kinase (RTK)", def:"A transmembrane receptor with an intracellular tyrosine kinase tail; ligand binding causes two RTK monomers to dimerize and phosphorylate each other (autophosphorylation), activating multiple signalling pathways at once."},
    {icon:"atom", color:"green", term:"Nuclear receptor", def:"A eukaryotic intracellular receptor protein that, on binding its ligand, acts as a transcription factor in the nucleus, switching specific genes on or off."},
    {icon:"leaf", color:"teal", term:"Oestradiol &amp; progesterone", def:"Oestradiol: a steroid hormone controlling development and maintenance of female sex characteristics. Progesterone: a hormone from the corpus luteum that prepares and maintains the uterine lining for pregnancy."},
    {icon:"bars", color:"plum", term:"Positive &amp; negative feedback", def:"Positive feedback: a change that amplifies itself further away from the starting point (e.g. fruit ripening). Negative feedback: a change that is counteracted, restoring the original conditions (e.g. blood glucose control by insulin)."}
  ],
  theories: [
    {
      icon:"leaf", title:"Receptors and the Logic of Chemical Signalling",
      blocks:[
        {type:"prose", text:"Cells in a multicellular organism (and even bacteria) must respond to environmental stimuli and communicate with each other using chemical signalling molecules called ligands &mdash; including proteins, small peptides, amino acids, nucleotides, steroids, amines, and dissolved gases such as nitrogen monoxide (NO). In most cases the ligand cannot cross the plasma membrane and must bind a specific receptor protein, which generates a second messenger inside the cell; one ligand can activate the same receptor on many target cells simultaneously, while which cells actually respond depends on which receptors each cell expresses."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Ligand:</strong> a general term for a molecule that binds to a specific site on a protein &mdash; in cell signalling, the chemical signal itself.",
          "<strong>Receptor protein:</strong> a protein that recognizes and binds a specific chemical signal molecule, usually on the outside of the plasma membrane, and is distinct from a sensory &lsquo;receptor&rsquo; cell.",
          "<strong>Second messenger:</strong> a small intracellular ligand (e.g. cyclic AMP or Ca<sup>2+</sup>) generated or released inside a cell in response to an extracellular signal, which greatly amplifies and spreads that signal."
        ]},
        {type:"prose", text:"A chemical signalling pathway performs one or more of four functions: it can relay the signal onward through the cell; amplify it via a second messenger, so a small number of ligands produce a large response; integrate two or more incoming pathways into one signal; and distribute the signal to more than one effector protein, creating branching, complex responses. Primary transduction is the conversion of the message from extracellular to intracellular, often sped up by a scaffold protein holding several signalling proteins close together."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Scaffold protein:</strong> holds several signalling proteins close together for a faster response.",
          "<strong>Relay protein:</strong> passes the signal to the next pathway member.",
          "<strong>Effector protein:</strong> causes the change inside the cell.",
          "<strong>Amplifier/transducer protein:</strong> boosts and converts the signal."
        ]},
        {type:"heading", text:"The three stages of cell signalling"},
        {type:"prose", text:"Cell signalling itself can be divided into three stages. <strong>1. Ligand&ndash;receptor interaction:</strong> the ligand is complementary in shape to a binding site on the receptor and binds with high specificity, activating it. <strong>2. Signal transduction:</strong> a sequence of changes passes through a multistep pathway of relay molecules &mdash; mainly via protein phosphorylation in a phosphorylation cascade, and/or release of second messengers such as cyclic AMP &mdash; amplifying the signal at each step. <strong>3. Cellular response:</strong> the pathway produces a specific response, which may include regulating a protein&rsquo;s activity (e.g. opening or closing an ion channel), regulating gene expression, regulating enzyme activity, rearranging the cytoskeleton, or triggering apoptosis."},
        {type:"prose", text:"Many relay molecules are protein kinases that activate other protein kinases in turn, forming a phosphorylation cascade; relay molecules are activated when phosphorylated and deactivated when dephosphorylated, so phosphorylation/dephosphorylation acts as a molecular on/off switch."},
        {type:"prose", text:"The same ligand can trigger different responses in different cell types, because differentiated cells activate different sets of genes and so contain different collections of signalling proteins. Once a response has occurred, the signal is terminated, and a cell&rsquo;s ability to respond to a new signal depends on these changes being reversible."}
      ],
      notes:[
        {label:"Common mistake", text:"Do not confuse &lsquo;receptor protein&rsquo; with &lsquo;receptor&rsquo; in the sensory sense. Sensory receptors are specialized cells that transduce a stimulus into an electrical impulse; receptor proteins are molecules that bind ligands to convey a chemical message into a cell."},
        {label:"Described figure &mdash; intracellular signalling network (Fig. C2.1.2)", text:"A ligand binds an extracellular receptor protein, activating an amplifier/transducer protein that generates a second messenger. This activates relay proteins and a messenger protein, sometimes via adaptor and anchoring proteins linked to the cytoskeleton; a scaffold protein holds several of these together, an integrator protein combines signals from more than one pathway, and a modulator protein fine-tunes the response. The pathway ultimately activates a target protein in the cytoplasm, or passes through the nuclear envelope to alter transcription of a target gene."}
      ]
    },
    {
      icon:"book", title:"Cell Signalling by Bacteria: Quorum Sensing",
      blocks:[
        {type:"prose", text:"Bacteria are not purely solitary organisms &mdash; many species use a diffusible chemical signal to sense their own population density and switch on genes collectively once a threshold &lsquo;quorum&rsquo; is reached. Quorum sensing allows a bacterial population to coordinate gene expression as cell density rises."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Quorum sensing:</strong> the ability of some bacteria to monitor their own cell density, via a diffusible signal molecule, and adjust gene expression accordingly once a threshold population size is reached.",
          "<strong>Autoinducer:</strong> a signalling molecule produced and detected by bacteria participating in quorum sensing; its own synthesis is often switched on by positive feedback once a threshold concentration is reached."
        ]},
        {type:"prose", text:"Bacteria produce and release autoinducers, that diffuse outwards and are detected by specific receptor proteins inside the cell or in the bacterial membrane. At low population density, diffusion keeps the autoinducer concentration very low; as the population grows, the concentration rises until it reaches a threshold, triggering gene expression &mdash; which often includes genes for making more autoinducer, forming a positive feedback loop that rapidly switches the whole population&rsquo;s behaviour from individual to group mode."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"The bioluminescent marine bacterium <em>Vibrio fischeri</em> produces the light-emitting enzyme luciferase only once it reaches a critical population density inside the light organ of its host, the Hawaiian bobtail squid. Producing light is energetically costly and of little benefit to a lone cell outside the host, so the bacteria benefit from living in the squid (gaining nutrients), while the squid benefits from the camouflage or prey-attraction the light provides &mdash; a mutualistic relationship."}
      ],
      notes:[{label:"Going further &mdash; quorum sensing and disease", text:"In cystic fibrosis, frequent lung infections often involve large colonies of <em>Pseudomonas aeruginosa</em> that become antibiotic-resistant once quorum sensing detects a critical cell density and triggers production of protective enzymes and a <strong>biofilm</strong> &mdash; a complex aggregation of micro-organisms held together by a protective, adhesive extracellular matrix &mdash; which shields the bacteria from antibiotics while its enzymes damage the lung epithelium."}]
    },
    {
      icon:"leaf", title:"Signalling Chemicals in Animals: Categories and Chemical Diversity",
      blocks:[
        {type:"prose", text:"Animal ligands fall into four functional categories &mdash; hormones, neurotransmitters, cytokines and calcium ions. Hormones are secreted by endocrine glands and carried through the circulatory system to act on distant target cells; they act over a longer timescale, affecting cell metabolism and processes such as sexual reproduction."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Hormone:</strong> an extracellular signal molecule secreted and transported via the bloodstream (animals) or sap (plants) to distant target tissues, where it causes a specific, longer-lasting effect.",
          "<strong>Neurotransmitter:</strong> a chemical released at the presynaptic membrane of an axon when an action potential arrives, transmitting the signal across the synapse.",
          "<strong>Cytokine:</strong> a small secreted protein controlling growth and differentiation of specific target cells."
        ]},
        {type:"prose", text:"Neurotransmitters carry signals between neurons, or from neurons to other target cells such as muscle cells, triggered by an action potential arriving at the end of a neuron. Cytokines are a family of relatively small, secreted proteins that control growth and differentiation of specific cell types; some, such as &alpha;-interferon, are produced by many cell types following viral infection."},
        {type:"prose", text:"Calcium ions (Ca<sup>2+</sup> (aq)) are one of the few inorganic ligands: many ligands, including neurotransmitters, growth factors and some hormones, act via pathways that raise cytoplasmic Ca<sup>2+</sup> concentration, triggering responses such as muscle contraction, secretion (e.g. of the neurotransmitter acetylcholine) and cell division. Ca<sup>2+</sup> can act as a second messenger precisely because its cytoplasmic concentration is normally kept much lower than its concentration outside the cell."},
        {type:"heading", text:"Chemical classes of hormones and neurotransmitters"},
        {type:"prose", text:"There are three main chemical classes of hormone: protein/peptide hormones (e.g. insulin, a polypeptide with two chains linked by disulfide bonds), steroid hormones (e.g. oestradiol, built on cholesterol&rsquo;s four-ring carbon structure), and amine hormones (amino acid derivatives, e.g. epinephrine). Hormones can be small, non-polar, hydrophobic molecules that diffuse through the cell membrane to reach intracellular receptors (e.g. progesterone, testosterone, thyroid hormones), or water-soluble molecules that bind receptors on the plasma membrane &mdash; either proteins such as insulin and glucagon, or small charged molecules such as histamine and epinephrine."},
        {type:"prose", text:"Neurotransmitters are similarly diverse: simple amines (e.g. dopamine), amino acids (e.g. GABA, gamma-aminobutyric acid), polypeptides (e.g. endorphins) and acetylcholine (an amino acid derivative). Most neurons make and release two or more neurotransmitters at once, letting one cell exert several influences simultaneously."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"The dissolved gas nitric oxide (NO) also functions as a neurotransmitter, or as an agent that influences other neurotransmitters, in the brain and central nervous system. NO is synthesized from the amino acid arginine and diffuses rapidly across membranes into nearby cells, but acts only locally because it is quickly converted to other products on reacting with oxygen and water outside cells; it causes smooth muscle in blood vessels to relax, dilating the vessel and increasing blood flow."}
      ],
      notes:[
        {label:"Top tip &mdash; dual roles", text:"Some chemicals serve more than one functional category: epinephrine (adrenaline) acts both as a neurotransmitter and as a hormone secreted by the adrenal gland that signals glycogen breakdown in muscle cells."},
        {label:"Nature of science &mdash; discovering nitric oxide&rsquo;s role", text:"Applying acetylcholine directly to isolated smooth muscle cells made them contract, the expected effect; but applying acetylcholine to the lumen of small, intact blood vessels in culture instead made the underlying smooth muscle relax. This showed that acetylcholine was acting on the endothelial cells lining the vessel, which release a separate substance &mdash; later identified as nitric oxide &mdash; that actually caused the relaxation."}
      ],
      side:{
        table:{
          title:"Three chemical classes of hormone",
          head:["Class","Example","Chemical nature"],
          rows:[
            ["Protein/peptide","Insulin","Polypeptide chain(s); water-soluble, binds cell-surface receptors"],
            ["Steroid","Oestradiol","Lipid-derived, four-ring structure; non-polar, diffuses through the membrane"],
            ["Amine","Epinephrine (adrenaline)","Small, single amino-acid derivative; water-soluble, binds cell-surface receptors"]
          ]
        }
      }
    },
    {
      icon:"leaf", title:"Localized and Distant Effects of Signalling Molecules",
      blocks:[
        {type:"prose", text:"Depending on how far a target cell lies from the signalling cell, chemical signalling can act locally across a tiny synaptic gap, or carry a hormone right across the body through the circulatory system. Local (synaptic) signalling occurs across chemical synapses using neurotransmitters such as acetylcholine and norepinephrine: although its direct effect is localized, the overall effect is widespread, since it triggers a new electrical impulse in the postsynaptic neuron that carries the message on through the body."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", items:[
          "The presynaptic&ndash;postsynaptic gap is very small (20&ndash;40 nm), so the neurotransmitter only has to diffuse a tiny distance.",
          "Other local signalling examples include gap junctions (animals) and plasmodesmata (plants), and direct cell&ndash;cell recognition via membrane-bound surface molecules."
        ]},
        {type:"prose", text:"On reaching the postsynaptic membrane, acetylcholine binds ligand-gated sodium channels, opening them and causing an influx of Na<sup>+</sup> (aq) that generates a new impulse."},
        {type:"prose", text:"Long-distance (endocrine) signalling uses hormones secreted into a transport system &mdash; blood plasma in animals with a closed circulatory system, or sap in plants &mdash; to reach receptors far from the source. Specialized cells release hormones such as insulin and glucagon into the bloodstream to reach target cells elsewhere in the body, triggering a cascade of reactions that alters the target cell&rsquo;s metabolism."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"Plant hormones such as auxin sometimes travel in vascular tissue, but often reach their targets by moving through cells or by diffusion through the air as a gas."}
      ]
    },
    {
      icon:"atom", title:"Transmembrane vs Intracellular Receptors",
      blocks:[
        {type:"prose", text:"Whether a ligand binds a receptor on the cell surface or deep inside the cell depends entirely on one chemical property: whether the ligand is polar (and so blocked by the membrane) or non-polar (and so able to diffuse straight through it). Non-polar, lipid-soluble ligands can diffuse through the phospholipid bilayer to reach receptors inside the cell. Polar, charged, water-soluble ligands (e.g. peptide hormones like insulin and glucagon) are hydrophilic and cannot cross the bilayer, so they must bind receptors on the cell surface instead &mdash; giving two classes of receptor protein, transmembrane and intracellular."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Transmembrane receptor:</strong> spans the plasma membrane, binding polar, water-soluble ligands on the cell surface.",
          "<strong>Intracellular receptor:</strong> a soluble protein in the cytoplasm or nucleus, binding non-polar, lipid-soluble ligands that diffuse through the membrane."
        ]},
        {type:"prose", text:"A transmembrane receptor has three regions: an extracellular ligand-binding region, a hydrophobic membrane-spanning region, and an intracellular region that relays the signal inward. Hydrophobic amino acid regions help embed the receptor in the membrane, while hydrophilic regions face outward, near the phospholipid head groups, where hydrophilic ligands bind. Ligand binding changes the receptor&rsquo;s shape, relaying the signal across the membrane to the cytoplasm &mdash; the process of cell transduction."},
        {type:"prose", text:"Many lipid-soluble ligands (e.g. the steroid hormones oestradiol, progesterone and testosterone) diffuse across the membrane and bind a soluble intracellular receptor in the cytoplasm or nucleus. If the receptor is cytoplasmic, the activated ligand&ndash;receptor complex moves to the nucleus by simple diffusion, where it acts as a transcription factor, binding specific DNA regions and switching a gene on or off. If activated, new mRNA leaves the nucleus and directs the synthesis of a new protein (often an enzyme) at the ribosomes, bringing about a structural or functional change in the cell."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Nuclear receptor:</strong> a eukaryotic intracellular receptor protein that, on binding its ligand, acts as a transcription factor in the nucleus, switching specific genes on or off."}
      ],
      notes:[{label:"Common mistake", text:"It is incorrect to say that all receptor proteins sit in the plasma membrane. Cell-surface receptors respond only to charged, polar ligands; lipid-soluble ligands such as steroid hormones pass straight through the phospholipid bilayer, so their receptors are located inside the cell."}],
      side:{
        table:{
          title:"Transmembrane vs intracellular receptors",
          head:["Feature","Transmembrane receptor","Intracellular receptor"],
          rows:[
            ["Ligand polarity","Polar, water-soluble (e.g. insulin)","Non-polar, lipid-soluble (e.g. steroid hormones)"],
            ["Location","Spans the plasma membrane","Cytoplasm or nucleus"],
            ["Typical response speed","Fast (often no new transcription needed)","Slower (usually alters gene transcription)"]
          ]
        }
      }
    },
    {
      icon:"book", title:"Transmembrane Receptor Mechanisms: Ligand-Gated Channels and G Proteins",
      blocks:[
        {type:"prose", text:"Plasma-membrane receptors use two different physical strategies to convert an extracellular signal into an intracellular one: a ligand-gated ion channel opens directly to let ions flow, while a G protein-coupled receptor (GPCR) activates a separate G protein that then switches on other effector proteins."},
        {type:"prose", text:"The ligand-gated sodium ion channel (the nicotinic acetylcholine receptor) is built from five transmembrane protein subunits, forming an aqueous pore across the lipid bilayer lined by five transmembrane &alpha;-helices, with two acetylcholine-binding sites. When acetylcholine released by a motor neuron binds both sites, the channel changes conformation &mdash; hydrophobic side chains move apart and the gate opens &mdash; letting sodium ions flow down their electrochemical and concentration gradient, depolarizing the plasma membrane and changing the membrane potential."},
        {type:"prose", text:"GTP is an energy-rich nucleotide like ATP (ribose plus three phosphates), but with guanine instead of adenine as its base. G proteins are membrane-bound GTP-binding proteins, usually activated when a hormone or other ligand binds a transmembrane receptor; they respond to extracellular hormone and neurotransmitter signals and trigger intracellular cascades that regulate bodily functions, and are especially important in vision, smell and taste, coupling the primary stimulus to ion channels that generate a nerve impulse."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>G protein:</strong> a membrane-bound GTP-binding protein activated when a ligand binds a transmembrane receptor.",
          "<strong>G protein-coupled receptor (GPCR):</strong> a cell-surface receptor, built from seven transmembrane &alpha;-helices, that activates a G protein when bound to its ligand."
        ]},
        {type:"prose", text:"A GPCR has a common structure of seven hydrophobic &alpha;-helices spanning the plasma membrane, held in place by hydrophobic interactions with the lipid bilayer; G proteins bind mainly to the receptor&rsquo;s largest cytoplasmic loop."},
        {type:"prose", text:"The GPCR is inactive until a ligand binds its extracellular side; binding changes the receptor&rsquo;s conformation, which activates the associated G protein, causing it to exchange its bound GDP for GTP. The activated, GTP-bound G protein then dissociates from the receptor and binds an enzyme or other effector protein, activating it to trigger signal transduction and a cellular response."},
        {type:"prose", text:"Once the original ligand is no longer present, the G protein&rsquo;s own GTPase activity hydrolyzes its bound GTP back to GDP, so the G protein dissociates from the enzyme and returns to its inactive state &mdash; switching the signal off."}
      ],
      notes:[
        {label:"Top tip &mdash; cholinergic vs adrenergic", text:"Neurons that release acetylcholine are described as <strong>cholinergic</strong>; those that release norepinephrine are described as <strong>adrenergic</strong>."},
        {label:"Top tip &mdash; GPCR diversity", text:"GPCRs are found only in eukaryotes, never in prokaryotes. There are nearly 1000 different human GPCRs, each with its own ligand-binding specificity and its own set of downstream G proteins."}
      ]
    },
    {
      icon:"book", title:"Mechanism of Action of Epinephrine (Adrenaline) Receptors",
      blocks:[
        {type:"prose", text:"The adrenal glands release epinephrine (adrenaline), which circulates in the blood and binds adrenergic receptors (a class of GPCR) on many cell types, preparing the body for vigorous activity by increasing heart and breathing rate, delivering more oxygen and glucose to muscle for respiration."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Second messenger:</strong> a small intracellular ligand (e.g. cyclic AMP or Ca<sup>2+</sup>) generated or released inside a cell in response to an extracellular signal, which greatly amplifies and spreads that signal. Epinephrine&rsquo;s receptor activates a cascade mediated by exactly this kind of second messenger."},
        {type:"prose", text:"The hormone activates a GPCR, which activates a G protein (G<sub>S</sub>) that in turn activates the membrane enzyme adenylyl cyclase, converting ATP into many molecules of cyclic AMP &mdash; rapidly raising cytoplasmic cAMP concentration."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Cyclic AMP (cAMP):</strong> a small intracellular signalling molecule generated from ATP by adenylyl cyclase in response to hormonal stimulation of a cell-surface receptor, and broken down by phosphodiesterase to end the signal.",
          "<strong>Kinase:</strong> an enzyme that transfers a phosphate group from ATP to a target protein, usually activating it.",
          "<strong>Phosphorylase:</strong> an enzyme that breaks down a polysaccharide such as glycogen into glucose 1-phosphate."
        ]},
        {type:"prose", text:"The rise in cAMP activates PKA (cAMP-dependent protein kinase), which phosphorylates and activates phosphorylase kinase, which activates glycogen phosphorylase, the enzyme that breaks glycogen down to glucose 1-phosphate. cAMP signalling is short-lived because phosphodiesterase continuously converts cAMP back to AMP, terminating the signal."},
        {type:"prose", text:"In skeletal muscle, the rise in cAMP both activates glycogen breakdown and inhibits the enzyme that synthesizes glycogen, maximizing the glucose available as a respiratory substrate for muscular activity; epinephrine also stimulates adipose cells to break down fat into fatty acids, a further respiratory substrate."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", items:[
          "Because this cascade involves phosphorylation/dephosphorylation rather than new gene transcription or protein synthesis, it can act very rapidly.",
          "One activated receptor produces around 10<sup>4</sup> cAMP molecules,",
          "which activate around 10<sup>6</sup> phosphorylase enzyme molecules,",
          "which generate perhaps 10<sup>8</sup> molecules of glucose 1-phosphate &mdash; massive amplification at each step."
        ]}
      ],
      notes:[{label:"Nature of science &mdash; naming epinephrine/adrenaline", text:"George Oliver and Edward Sch&auml;fer first showed the adrenal glands contained a substance with strong pharmacological effects; John Abel named it &lsquo;epinephrine&rsquo; in the USA (1897), while Jokichi Takamine&rsquo;s 1901 patented extract, sold as proprietary &lsquo;Adrenaline&rsquo;, led to that name becoming standard in Britain and most other countries &mdash; a case study in how scientific naming conventions can diverge between communities even once the underlying chemistry (IUPAC name: (R)-1-(3,4-dihydroxyphenyl)-2-methylaminoethanol) is agreed."}],
      side:{
        table:{
          title:"Amplification of the epinephrine signal",
          head:["Stage","Approximate molecules produced"],
          rows:[
            ["1 activated receptor","1"],
            ["Cyclic AMP molecules formed","~10<sup>4</sup> (10 000)"],
            ["Active phosphorylase enzyme molecules","~10<sup>6</sup> (1 000 000)"],
            ["Glucose 1-phosphate molecules released","~10<sup>8</sup> (100 000 000)"]
          ]
        }
      }
    },
    {
      icon:"atom", title:"Transmembrane Receptors with Tyrosine Kinase Activity",
      blocks:[
        {type:"prose", text:"A receptor tyrosine kinase (RTK) is a single polypeptide with one transmembrane &alpha;-helix, an extracellular ligand-binding site, and an intracellular tail with tyrosine kinase activity, containing many tyrosine residues. Before a ligand binds, RTKs exist as separate monomers."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Receptor tyrosine kinase (RTK):</strong> a transmembrane receptor with an intracellular tyrosine kinase tail; ligand binding causes two RTK monomers to dimerize and phosphorylate each other (autophosphorylation), activating multiple signalling pathways at once."},
        {type:"prose", text:"Ligand binding to the extracellular sites causes two RTK monomers to associate into a dimer; dimerisation brings each tail&rsquo;s kinase active site close to the other, so each RTK adds a phosphate from ATP to tyrosine residues on its partner&rsquo;s tail &mdash; autophosphorylation. The activated RTK then assembles specific relay proteins on its phosphorylated tails, and each triggers its own signal transduction pathway, so one RTK complex can activate ten or more pathways and cellular responses at once."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"<strong>Insulin</strong> is a hormone that signals high blood glucose. Insulin binds its receptor, an RTK, on cells such as liver and muscle cells; activated relay proteins cause vesicles carrying GLUT4 glucose transporter proteins to move to, and fuse with, the plasma membrane, inserting GLUT4 into the membrane and increasing glucose uptake. Activated relay proteins also switch on many glycogen synthase molecules, driving glycogenesis (glycogen synthesis from glucose), so a single insulin&ndash;receptor binding event leads to large-scale glycogen synthesis."},
        {type:"prose", text:"The insulin signal is terminated when insulin leaves the receptor, protein phosphatases dephosphorylate the tyrosine residues (phosphatases inactivate kinases by dephosphorylation), and the dimer separates back into two monomers."}
      ],
      notes:[{label:"Described figure &mdash; insulin&ndash;RTK signalling pathway (Fig. C2.1.13)", text:"(1) Insulin activates RTK receptors on the cell surface. (2) Relay proteins are activated and travel to intracellular vesicles. (3) These vesicles carry GLUT4 glucose transporter proteins. (4) The GLUT4 vesicles fuse with the plasma membrane. (5) GLUT4 becomes incorporated into the membrane, where it transports glucose into the cell."}]
    },
    {
      icon:"leaf", title:"Intracellular Receptors and Steroid Hormone Action",
      blocks:[
        {type:"prose", text:"Steroid hormone receptors act as transcription factors inside the cell &mdash; a slower mechanism than membrane-receptor signalling. Steroid (and thyroid) hormones are lipid-soluble and pass through the plasma membrane; in a target cell&rsquo;s cytoplasm, the hormone binds and activates its receptor, and the activated ligand&ndash;receptor complex then enters the nucleus, where it acts as a transcription factor, binding a regulatory DNA sequence and promoting transcription of specific genes. Not every gene in the genome is transcribed at once: specific genes are selectively activated (gene expression) to produce the proteins a particular cell or organism needs at a given time."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"Testosterone, secreted by the testes, travels through the blood and enters cells all over the body, but only cells containing a testosterone receptor will respond; in those target cells, activation of the receptor and entry of the complex into the nucleus promotes transcription of genes giving rise to male secondary sexual characteristics."},
        {type:"heading", text:"Oestradiol and progesterone in the female reproductive cycle"},
        {type:"prose", text:"A very similar intracellular receptor pathway operates for the female steroid hormones oestradiol and progesterone. Each ovum (egg) is surrounded and nourished by an ovarian follicle, which secretes both oestradiol (made mainly in the ovary, also the placenta, testis and possibly the adrenal cortex) and progesterone."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Oestradiol:</strong> a steroid hormone controlling development and maintenance of female sex characteristics. <strong>Progesterone:</strong> a hormone from the corpus luteum that prepares and maintains the uterine lining for pregnancy."},
        {type:"prose", text:"Oestradiol production is itself controlled by a signalling cascade: the hypothalamus releases gonadotropin-releasing hormone, which acts on the pituitary gland to release luteinizing hormone (LH) and follicle-stimulating hormone (FSH), both involved in the menstrual cycle. Target cells for oestradiol lie in the pituitary, the uterine lining, the breasts and bone marrow; this interaction drives the development of female secondary sexual characteristics at puberty."},
        {type:"prose", text:"Once a month, ovulation releases one egg from a follicle, which then becomes the corpus luteum. Progesterone, produced mainly by the corpus luteum (and the placenta), prepares the endometrium (uterine lining) for implantation. If implantation fails, the corpus luteum degenerates and progesterone production stops; if implantation succeeds, the corpus luteum continues secreting progesterone (under LH and prolactin) for several months until the placenta takes over &mdash; maintaining the endometrium and preventing further ovulation throughout pregnancy."}
      ]
    },
    {
      icon:"atom", title:"Regulation of Cell Signalling by Positive and Negative Feedback",
      blocks:[
        {type:"prose", text:"Signalling pathways are themselves regulated by feedback: positive feedback drives a pathway further from its starting point for an all-or-none response, while negative feedback restores the original conditions and keeps the system stable."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Positive feedback:</strong> a change that amplifies itself further away from the starting point (e.g. fruit ripening). <strong>Negative feedback:</strong> a change that is counteracted, restoring the original conditions (e.g. blood glucose control by insulin)."},
        {type:"prose", text:"In positive feedback, a change in a signalling pathway increases and amplifies the deviation away from the starting point; in negative feedback, the pathway&rsquo;s output acts to bring the system back toward its initial conditions. Positive feedback tends to generate all-or-none, switch-like responses, while negative feedback can generate on/off oscillations, or more typically acts with a time delay to shut a pathway down once it has produced its effect."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"<strong>Fruit ripening (positive feedback):</strong> plant cells use enzyme-coupled transmembrane receptors rather than RTKs, cAMP or steroid-type nuclear receptors. In the ethylene (ethene, C<sub>2</sub>H<sub>4</sub>) signalling system that controls seed germination and fruit ripening, the <em>empty</em> receptor is the active one: without ethylene bound, the receptor activates a kinase that switches off ethylene-responsive genes; when ethylene is present, the receptor and kinase are inactivated, so ethylene-responsive genes are transcribed &mdash; and since ripening fruit produces more ethylene, this reinforces further ripening, amplifying the response."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"<strong>Blood glucose control by insulin (negative feedback):</strong> insulin causes cells to absorb glucose and store it as glycogen, lowering blood glucose concentration; as blood glucose returns to normal, the stimulus for insulin secretion by the pancreas is removed, so insulin secretion falls &mdash; restoring the original equilibrium."}
      ]
    }
  ],
  workedExamples: [
    {
      title:"Tracing a lipid-soluble vs a lipid-insoluble ligand",
      question:"A peptide hormone and a steroid hormone are both released into the bloodstream and reach the same target cell. Explain why they use different types of receptor, and outline the key difference in how quickly each produces a cellular response.",
      answer:[
        "The peptide hormone is polar and water-soluble, so it cannot cross the hydrophobic interior of the plasma membrane; it must bind a <strong>transmembrane receptor</strong> on the cell surface, which relays the signal into the cell via a second messenger and a phosphorylation cascade.",
        "The steroid hormone is non-polar and lipid-soluble, so it diffuses straight through the plasma membrane and binds an <strong>intracellular receptor</strong> in the cytoplasm or nucleus.",
        "The peptide hormone&rsquo;s response is fast, since it only involves modifying existing proteins (e.g. by phosphorylation) without any need for new transcription. The steroid hormone&rsquo;s response is slower, because the activated receptor complex must enter the nucleus, bind DNA, and alter gene transcription before new proteins can be synthesized."
      ]
    },
    {
      title:"Calculating signal amplification by a GPCR cascade",
      question:"A single epinephrine molecule binds one receptor, ultimately generating 10<sup>4</sup> molecules of cAMP, 10<sup>6</sup> molecules of active phosphorylase, and 10<sup>8</sup> molecules of glucose 1-phosphate. Explain how a single hormone molecule can produce such a large downstream effect, and name the two main structural features of the pathway responsible.",
      answer:[
        "Each enzyme activated in the cascade is itself a catalyst, so it can act on many substrate molecules before the pathway is terminated &mdash; one activated adenylyl cyclase molecule converts many ATP molecules to cAMP, each cAMP helps activate many PKA/phosphorylase kinase molecules, and so on, multiplying the effect at every step.",
        "This is an example of a <strong>phosphorylation cascade</strong>: a sequence of linked kinase-activation steps, each amplifying the signal further.",
        "It relies on <strong>second messengers</strong> (cAMP): being small and water-soluble, cAMP diffuses rapidly throughout the cytoplasm, letting one receptor-binding event at the membrane influence enzyme activity throughout the whole cell."
      ]
    },
    {
      title:"Explaining quorum sensing with positive feedback",
      question:"Explain, using the idea of positive feedback, why a population of <em>Vibrio fischeri</em> bacteria only produces light once it reaches a critical population density inside its squid host, and not before.",
      answer:[
        "Each bacterium releases a small amount of autoinducer, which diffuses away into the surroundings; at low cell density, this diffusion keeps the autoinducer concentration too low to trigger a response.",
        "As the bacterial population inside the enclosed light organ grows, the autoinducer released by all the cells accumulates faster than it can diffuse away, so its concentration rises.",
        "Once autoinducer concentration crosses a threshold, it binds its receptor and switches on genes for luciferase (light production) and for making more autoinducer itself &mdash; a positive feedback loop that rapidly and simultaneously switches the whole population from &lsquo;off&rsquo; to &lsquo;on&rsquo;, ensuring light is only produced when enough bacteria are present to make the energy cost worthwhile."
      ]
    },
    {
      title:"Distinguishing RTK dimerisation from GPCR activation",
      question:"Both receptor tyrosine kinases (RTKs) and G protein-coupled receptors (GPCRs) are transmembrane receptors activated by an extracellular ligand. Describe one key structural difference in how each receptor is switched on.",
      answer:[
        "An RTK is activated by <strong>dimerisation</strong>: ligand binding causes two separate RTK monomers to come together in the membrane, bringing their intracellular tyrosine kinase tails close enough to phosphorylate each other (autophosphorylation).",
        "A GPCR, in contrast, is a single polypeptide that does not need to pair with another receptor molecule; ligand binding simply changes its own conformation, which activates an associated G protein by causing it to exchange GDP for GTP.",
        "So RTK activation depends on bringing two receptor molecules together, while GPCR activation depends on a conformational change transmitted to a separate G protein."
      ]
    }
  ],
  summary: [
    "Chemical signalling uses specific ligands that bind complementary receptor proteins, triggering signal transduction pathways that relay, amplify, integrate and distribute the signal &mdash; usually via a second messenger &mdash; through three stages: ligand&ndash;receptor interaction, signal transduction, and cellular response.",
    "Bacterial quorum sensing uses a diffusible autoinducer and positive feedback to let a population switch on genes collectively once a threshold cell density is reached, as shown by bioluminescent <em>Vibrio fischeri</em> in its squid host, and by biofilm formation in antibiotic-resistant <em>Pseudomonas aeruginosa</em>.",
    "Animal ligands fall into four functional categories &mdash; hormones (long-distance, slow), neurotransmitters (local, fast, across synapses), cytokines (growth/differentiation signals), and calcium ions (a widespread inorganic second messenger) &mdash; and hormones/neurotransmitters themselves span protein, steroid, amine and even gaseous (nitric oxide) chemical classes.",
    "Local signalling (e.g. across a 20&ndash;40 nm synaptic gap) and long-distance endocrine signalling (via the blood or sap) differ mainly in distance travelled, not in the underlying ligand&ndash;receptor logic.",
    "Transmembrane receptors bind polar, water-soluble ligands at the cell surface and relay the signal inward by changing shape; intracellular receptors bind non-polar, lipid-soluble ligands (e.g. steroid hormones) that diffuse through the membrane and act directly as transcription factors in the nucleus.",
    "Ligand-gated ion channels (e.g. the acetylcholine receptor) open directly to change membrane potential, while G protein-coupled receptors (GPCRs) cycle a bound G protein between inactive (GDP) and active (GTP) states to activate a separate effector protein.",
    "The epinephrine&ndash;GPCR&ndash;cAMP&ndash;PKA cascade amplifies one hormone-binding event into roughly 10<sup>8</sup> molecules of glucose 1-phosphate, stimulating rapid glycogen breakdown for vigorous activity, without requiring new gene transcription.",
    "Receptor tyrosine kinases (RTKs), such as the insulin receptor, are activated by ligand-induced dimerisation and autophosphorylation, and can launch ten or more signalling pathways simultaneously; insulin signalling inserts GLUT4 transporters into the membrane and drives glycogenesis.",
    "Intracellular (nuclear) receptors for steroid hormones such as testosterone, oestradiol and progesterone act as transcription factors, switching specific genes on or off to produce slower, longer-lasting cellular responses, including the development of secondary sexual characteristics and preparation of the uterus for pregnancy.",
    "Signalling pathways are themselves regulated by positive feedback (e.g. fruit ripening via ethylene, and autoinducer production in quorum sensing) and negative feedback (e.g. insulin&rsquo;s control of blood glucose), which respectively drive a pathway to completion or restore it to its starting conditions."
  ]
}
