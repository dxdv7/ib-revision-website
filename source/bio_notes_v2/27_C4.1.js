{
  unified: true,
  subtitle: "Populations of a single species interact with their environment and with each other &mdash; growing, competing and cooperating within limits set by their habitat &mdash; while many different populations together form a community, bound together by interspecific relationships from mutualism to predation that regulate each species&rsquo; abundance.",
  keyTerms: [
    {icon:"leaf", color:"green", term:"Population", def:"Interacting groups of organisms of the same species living in an area, with the chance to interbreed; reproductive isolation distinguishes one population of a species from another."},
    {icon:"atom", color:"teal", term:"Community", def:"A group of different species living in an area &mdash; the total of all the populations of all species present in an ecosystem."},
    {icon:"bars", color:"gold", term:"Quadrat", def:"A square frame outlining a known area, used to estimate the abundance of plants and sessile animals; quadrat size is matched to the size of the organisms being sampled."},
    {icon:"leaf", color:"plum", term:"Random, stratified &amp; systematic sampling", def:"Random: choosing a sample without bias, suited to a uniform habitat. Stratified: sampling two or more distinct habitat types in proportion to their area. Systematic: sampling at fixed intervals along a transect across an environmental gradient."},
    {icon:"atom", color:"red", term:"Sampling error", def:"The difference between an estimate of population size obtained from a sample and the true size of the whole population."},
    {icon:"bars", color:"green", term:"Standard deviation (SD)", def:"A measure of how spread out normally distributed data are from the mean; about 68% of data lie within one SD of the mean and over 95% within two SDs. A small SD indicates more reliable, closely clustered data."},
    {icon:"leaf", color:"teal", term:"Carrying capacity", def:"The maximum number of individuals of a species, or &lsquo;load&rsquo;, that a given environment can sustainably support."},
    {icon:"atom", color:"gold", term:"Limiting factor", def:"A factor that restricts population growth or prevents it increasing further, e.g. light, water or soil nutrients in plants; space, food, mates or nesting sites in animals."},
    {icon:"bars", color:"plum", term:"Density-dependent factor", def:"A biotic factor (e.g. competition, predation, disease) whose effect on birth or death rate scales with population density; density-independent factors (e.g. weather) affect populations regardless of density."},
    {icon:"leaf", color:"red", term:"Negative feedback", def:"Feedback that counteracts any deviation from equilibrium and promotes stability, e.g. returning a population towards its carrying capacity."},
    {icon:"atom", color:"green", term:"Lincoln index", def:"The formula population size = (M &times; N) &divide; R, used to estimate the size of a motile population from capture&ndash;mark&ndash;release&ndash;recapture data."},
    {icon:"bars", color:"teal", term:"Exponential growth", def:"An accelerating rate of population increase occurring in an ideal, unlimited environment with no restricting limiting factors."},
    {icon:"leaf", color:"gold", term:"Sigmoid growth curve", def:"An S-shaped population growth curve showing an exponential phase, a transition phase, and a plateau phase as the population approaches carrying capacity."},
    {icon:"atom", color:"plum", term:"Natality, mortality, immigration &amp; emigration", def:"Natality: birth rate. Mortality: death rate. Immigration: movement of new individuals into a population. Emigration: departure of individuals from a population."},
    {icon:"bars", color:"red", term:"Intraspecific competition", def:"Competition between individuals of the same species, for resources such as food, mates, territory, water and space."},
    {icon:"leaf", color:"green", term:"Interspecific competition", def:"Competition between individuals of different species, generally less intense than intraspecific competition since different species occupy different niches."},
    {icon:"atom", color:"teal", term:"Cooperation &amp; altruism", def:"Cooperation: individuals of a population working together, e.g. in dominance hierarchies or hunting packs. Altruism: behaviour that benefits another individual at the altruist&rsquo;s own expense, increasing the recipient&rsquo;s offspring and decreasing the altruist&rsquo;s."},
    {icon:"bars", color:"gold", term:"Mutualism", def:"A type of symbiotic interspecific relationship in which both species derive benefit, able to increase the carrying capacity of both."},
    {icon:"leaf", color:"plum", term:"Parasitism", def:"A relationship in which the parasite benefits, at the expense of the host from which it derives its food, lowering the host&rsquo;s carrying capacity."},
    {icon:"atom", color:"red", term:"Pathogenicity", def:"The capacity of a microbe (bacterium, virus, fungus or protistan) to cause damage to a host, resulting in disease."},
    {icon:"bars", color:"green", term:"Competitive exclusion", def:"The outcome of interspecific competition in which one species outcompetes and excludes another from part of its niche."},
    {icon:"leaf", color:"teal", term:"Fundamental &amp; realized niche", def:"Fundamental niche: the full range of conditions and resources a species could potentially occupy. Realized niche: the narrower range it actually occupies once interspecific competition is accounted for."},
    {icon:"atom", color:"gold", term:"Predator&ndash;prey relationship", def:"The inter-relationship of population sizes due to the predation of one species (the predator) on another (the prey)."},
    {icon:"bars", color:"plum", term:"Top-down &amp; bottom-up control", def:"Top-down: a higher trophic level affects community structure at lower trophic levels through predation. Bottom-up: a lower trophic level (producers) affects higher trophic levels through resource restriction."},
    {icon:"leaf", color:"red", term:"Allelopathy", def:"Chemical inhibition of one plant (or other organism) by another, through the release of chemicals (allelochemicals) that act as germination or growth inhibitors."},
    {icon:"atom", color:"green", term:"Null hypothesis", def:"The hypothesis tested statistically that there is no significant difference, or no association, between two variables; rejecting it supports a real difference or association."}
  ],
  theories: [
    {
      icon:"leaf", title:"Populations, Sampling and Avoiding Bias",
      blocks:[
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Population:</strong> interacting groups of organisms of the same species living in an area, with the chance to interbreed; reproductive isolation distinguishes one population of a species from another."},
        {type:"prose", text:"Because a whole population or habitat is too large to examine individual by individual, ecologists study a <strong>sample</strong> &mdash; a subset used to estimate the values that would have been obtained had every individual been measured."},
        {type:"heading", text:"Sampling strategies"},
        {type:"prose", text:"<strong>Random sampling</strong> gives every individual an equal chance of selection and avoids the bias of, for example, choosing only unusually biodiverse-looking areas; it is appropriate when a study area is homogeneous. <strong>Stratified sampling</strong> instead samples two or more distinct habitat types in proportion to the area each occupies. <strong>Systematic sampling</strong> is used along an environmental gradient: transect positions are located at random, but sample points along the transect are then taken at fixed, regular intervals (e.g. every 5 m)."},
        {type:"heading", text:"Random and systematic error"},
        {type:"prose", text:"Comparing samples to the real population reveals two types of error: <strong>random error</strong>, caused by unknown or unpredictable differences, which creates imprecision but can be reduced (never eliminated) by repeating and averaging measurements; and <strong>systematic error</strong>, caused by flaws in an investigation&rsquo;s design, which shifts every measurement in the same direction, creating inaccuracy rather than imprecision. Systematic error is reduced by careful experimental design, by cross-checking with a different method, and by peer review."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Sampling error:</strong> the difference between an estimate of population size obtained from a sample and the true size of the whole population. If a sample does not represent the whole population well, conclusions drawn from it may not apply to the wider population."}
      ],
      notes:[
        {label:"Standard deviation as a measure of reliability", text:"<strong>Standard deviation (SD)</strong> measures how spread out a set of normally distributed data is from its mean: about 68% of data lie within one SD of the mean, and over 95% within two SDs. A small SD means data are clustered closely around the mean and are more reliable; a large SD means a wider spread. SD is more reliable than the <strong>range</strong> (the difference between the largest and smallest values), which depends on only two data points and so is skewed badly by outliers. Dividing by n gives the <em>population</em> SD; dividing by n&minus;1 instead (the usual case, since biological data are normally a sample) corrects for a sample&rsquo;s tendency to underestimate the true population variability."},
        {label:"Common mistake", text:"A larger sample size does not automatically give a smaller standard deviation &mdash; SD depends on how much genuine variation exists in the measurements themselves, and can increase or decrease as sample size grows."}
      ],
      side:{
        title:"The normal distribution",
        charts:[
          {title:"Standard deviation", caption:"68% of data lie within 1 SD of the mean; over 95% within 2 SD", axis:"Measured value", svg: bv2HistogramSvg("Histogram showing a bell-shaped normal distribution, with 68% of data within one standard deviation of the mean and over 95% within two standard deviations")}
        ],
        table:{
          title:"Three sampling strategies",
          head:["Strategy","Used when&hellip;"],
          rows:[
            ["Random","Habitat is uniform throughout the study area"],
            ["Stratified","Area contains two or more distinct habitat types"],
            ["Systematic","Sampling along an environmental gradient (transect)"]
          ]
        }
      }
    },
    {
      icon:"bars", title:"Estimating Population Size: Quadrats for Sessile Organisms",
      blocks:[
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Quadrat:</strong> a square frame outlining a known area, used to estimate the abundance of plants and sessile animals; quadrat size is matched to the size of the organisms studied."},
        {type:"prose", text:"A 10 cm&sup2; quadrat suits a single-celled alga such as epiphytic <em>Pleurococcus</em> on damp walls, while a 1 m&sup2; quadrat suits herbaceous grassland plants, or earthworms and slugs extracted from the soil beneath it."},
        {type:"prose", text:"The habitat is first mapped with gridlines along two edges, creating x- and y-axes; coordinate pairs are then generated as sequences of random numbers (by calculator, computer software, or published tables) to decide where each quadrat is placed, avoiding the bias of a researcher choosing &lsquo;convenient&rsquo; or visually striking locations."},
        {type:"prose", text:"Within each placed quadrat, the species present are identified, and the density, frequency, cover or abundance of the species under investigation is recorded."},
        {type:"callout", style:"tip", icon:"bolt", title:"Tip", text:"The total habitat area occupied by the population is measured, and population size is then calculated as: <strong>population size = (mean density per quadrat &times; total area) &divide; area of each quadrat</strong>."}
      ],
      notes:[{label:"Described figure &mdash; random quadrat placement", text:"A rectangular habitat map is marked with numbered gridlines (0&ndash;100) along both the x- and y-axes; quadrats are positioned only at coordinate pairs generated by a random number source, never chosen by eye, so the sample fairly represents the whole site."}],
      side:{
        table:{
          title:"Matching quadrat size to organism size",
          head:["Quadrat size","Suited to"],
          rows:[
            ["10 cm&sup2;","Epiphytic alga (e.g. <em>Pleurococcus</em>) on walls or bark"],
            ["1 m&sup2;","Grassland herbaceous plants; soil earthworms and slugs"]
          ]
        }
      }
    },
    {
      icon:"atom", title:"Estimating Population Size: Capture&ndash;Mark&ndash;Release&ndash;Recapture and the Lincoln Index",
      blocks:[
        {type:"prose", text:"A random sample of the population is captured, marked in a way appropriate to the organism (e.g. pen on insect wing cases, enamel paint on snail shells, fur clipping in mammals), and released back into the population; marks must be inconspicuous, since a highly visible mark would increase an individual&rsquo;s risk of being caught by a predator."},
        {type:"prose", text:"After enough time has passed for the marked individuals to mix evenly through the population (e.g. 24 hours), a second random sample is captured from the same location, and the number of marked individuals within it is counted."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Lincoln index:</strong> the formula population size = (M &times; N) &divide; R, used to estimate the size of a motile population from capture&ndash;mark&ndash;release&ndash;recapture data, where M = number of animals captured, marked and released; N = number of animals recaptured in the second sample; R = the number of marked animals found within that second sample."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"In a population of woodlice where M = 5 (captured, marked, released), N = 8 (recaptured), and R = 1 (marked animals among those recaptured), the estimated population size = (5 &times; 8) &divide; 1 = 40."}
      ],
      notes:[{label:"Assumptions of the Lincoln index", text:"The method assumes: mixing is complete, so marked individuals spread evenly through the population between capture and recapture; marks are not removed and do not disappear; marks are not harmful and do not increase predation risk by increasing visibility; every individual is equally easy to catch; and the population is <strong>closed</strong> &mdash; no immigration, emigration, births or deaths occur between the two sampling events."}],
      side:{
        table:{
          title:"Worked example (woodlice)",
          head:["Symbol","Meaning","Value"],
          rows:[
            ["M","Captured, marked, released","5"],
            ["N","Recaptured (2nd sample)","8"],
            ["R","Marked animals recaptured","1"],
            ["Population size","(M &times; N) &divide; R","40"]
          ]
        }
      }
    },
    {
      icon:"leaf", title:"Carrying Capacity and Density-Dependent Control",
      blocks:[
        {type:"prose", text:"As a population grows, abiotic and biotic <strong>limiting factors</strong> eventually restrict further increase &mdash; in plants these include light, soil nutrients, water, carbon dioxide and temperature; in animals, space, food, mates, nesting sites and water."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Carrying capacity:</strong> the maximum number of individuals of a species, or &lsquo;load&rsquo;, that a given environment can sustainably support."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"Rabbits introduced to a new meadow, for example, grow exponentially at first, but once their consumption of vegetation outpaces its regrowth, food becomes limiting and numbers stabilise at the meadow&rsquo;s carrying capacity."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Negative feedback:</strong> feedback that counteracts any deviation from equilibrium and promotes stability, e.g. returning a population towards its carrying capacity &mdash; the predator&ndash;prey relationship is a clear example."},
        {type:"prose", text:"Negative feedback control of population size operates through <strong>density-dependent factors</strong> &mdash; biotic factors whose effect on birth or death rate scales with population density. <strong>Internal</strong> density-dependent factors include fertility and territory size; <strong>external</strong> density-dependent factors include increased predation risk and the spread of pathogens or pests, both of which rise in denser populations."},
        {type:"prose", text:"<strong>Density-independent factors</strong> (e.g. weather, climate, natural disasters) affect populations of all species in an ecosystem regardless of density, and so cause fluctuations in population size without affecting carrying capacity itself; density-dependent factors, by contrast, define the upper limit to growth and tend to push a population back towards it."}
      ],
      notes:[{label:"Concept: Interaction", text:"Density-dependent factors interact with organisms to cause population numbers to fluctuate, ultimately pushing populations back to carrying capacity."}],
      side:{
        table:{
          title:"Density-dependent vs density-independent factors",
          head:["Feature","Density-dependent","Density-independent"],
          rows:[
            ["Effect scales with population size?","Yes","No"],
            ["Affects carrying capacity?","Yes &mdash; defines it","No"],
            ["Examples","Competition, predation, disease","Weather, climate, natural disaster"]
          ]
        }
      }
    },
    {
      icon:"bars", title:"Population Growth Curves: Exponential and Sigmoid Growth",
      blocks:[
        {type:"prose", text:"<strong>Exponential growth</strong> is an accelerating rate of increase that occurs in an ideal, unlimited environment &mdash; where limiting factors are not restricting growth, resources (light, space, food) are plentiful, competition is low, abiotic conditions are favourable, and predators or disease are scarce. Growth starts slowly but becomes increasingly rapid and does not level off as the population grows."},
        {type:"heading", text:"The sigmoid growth curve"},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Sigmoid growth curve:</strong> an S-shaped population growth curve showing an exponential phase, a transition phase, and a plateau phase as the population approaches carrying capacity."},
        {type:"prose", text:"In three stages: (1) an <strong>exponential stage</strong>, where limiting factors are minimal and both numbers and growth rate increase rapidly; (2) a <strong>transition phase</strong>, where growth slows as limiting factors begin to bite &mdash; increased competition, more predators attracted by the large population, and higher disease and mortality rates from crowding; (3) a <strong>plateau phase</strong>, where the population fluctuates around the <strong>carrying capacity (K)</strong> as limiting factors, predation, disease and abiotic conditions interact."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Natality, mortality, immigration &amp; emigration:</strong> natality (N) is birth rate; mortality (M) is death rate; immigration (I) is the movement of new individuals into a population; emigration (E) is the departure of individuals from a population."},
        {type:"prose", text:"During the exponential stage, I + N &gt; E + M as abundant resources favour reproduction over death; during the transition, I + N is still &gt; E + M but the gap narrows as resources grow scarcer; at the plateau, I + N = E + M on average, with the population fluctuating slightly either side of this set point."},
        {type:"heading", text:"Modelling growth mathematically"},
        {type:"prose", text:"The logistic sigmoid function, F(x) = 1 &divide; (1 + e<sup>&minus;x</sup>), is the standard mathematical model of this S-shaped pattern. Because real biological data can span a very wide range of values (e.g. yeast counted with a haemocytometer), plotting population size on a logarithmic y-axis against a linear time x-axis compresses large values and expands small ones &mdash; a population growing exponentially then appears as a straight line."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"Duckweed (<em>Lemna</em>), a fast-reproducing free-floating pond plant, is commonly used to model sigmoid growth experimentally: a small starting number of thalli is grown in replicate containers of pond water, counted twice weekly for at least six weeks, and the mean plotted against time &mdash; carrying capacity is reached once no room remains for further thalli and competition for space limits growth."}
      ],
      notes:[
        {label:"Nature of science &mdash; models", text:"The population growth curve is an idealized graphical model: real populations rarely show such smooth curves, since density-independent and density-dependent factors cause constant fluctuation. Models simplify complex systems to reveal overall patterns rather than the fine detail of any one case, and allow predictions of the pattern expected under given conditions."},
        {label:"Described figure &mdash; coral regrowth after disturbance (Lady Musgrave Island)", text:"Field data recording the percentage of hard coral cover over roughly 4000 days following disturbance by tropical cyclones follows a typical sigmoid response: near-exponential growth while coral cover is low, followed by a gradual slowdown in net growth rate as cover approaches its carrying capacity."}
      ],
      side:{
        table:{
          title:"Relative rates across the sigmoid curve",
          head:["Phase","Relationship","What is happening"],
          rows:[
            ["Exponential","I + N &gt; E + M","No limiting factors; abundant resources; low competition; high reproduction"],
            ["Transition","I + N &gt; E + M (narrowing)","Resources grow scarcer; competition increases"],
            ["Plateau","I + N = E + M (on average)","Population fluctuates around carrying capacity K"]
          ]
        }
      }
    },
    {
      icon:"leaf", title:"Communities, Intraspecific Competition and Cooperation",
      blocks:[
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Community:</strong> a group of different species living in an area &mdash; the total of all the populations of all species present in an ecosystem."},
        {type:"prose", text:"Examples include the wildebeest, lions, hyenas, giraffes, elephants and zebras of an African savannah, or the plant, fish, invertebrate and surface-dwelling populations of a pond. Communities include every biotic part of an ecosystem: plants, animals and fungi. In ecology, &lsquo;community&rsquo; (many species) and &lsquo;population&rsquo; (one species) are not interchangeable."},
        {type:"prose", text:"<strong>Intraspecific competition</strong> (within a species) can be the most intense form of competition, because individuals of the same species share exactly the same niche and so compete for precisely the same resources &mdash; food, mates, territory, water and space (e.g. two male blue wildebeest fighting over territory)."},
        {type:"prose", text:"<strong>Interspecific competition</strong> (between different species) is generally less intense, since different species occupy different niches and so overlap less in the resources they need."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Intraspecific competition:</strong> competition between individuals of the same species, for resources such as food, mates, territory, water and space.",
          "<strong>Interspecific competition:</strong> competition between individuals of different species, generally less intense than intraspecific competition since different species occupy different niches."
        ]},
        {type:"prose", text:"Competition is not the only option: many species have evolved cooperation to reduce its costs. Dominance hierarchies reduce fighting and injury within a group; hyena clans hunt cooperatively under a dominant female (&lsquo;queen&rsquo;), with every member benefiting from more effective, group-based kills than any individual could achieve alone."},
        {type:"prose", text:"<strong>Social insects</strong> (bees, wasps, ants, termites) take cooperation furthest: a single reproductive female is supported by large numbers of non-breeding workers, all her genetically similar offspring, so the colony behaves as one &lsquo;superorganism&rsquo;."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Cooperation &amp; altruism:</strong> cooperation is individuals of a population working together, e.g. in dominance hierarchies or hunting packs; altruism is behaviour that benefits another individual at the altruist&rsquo;s own expense, increasing the recipient&rsquo;s offspring and decreasing the altruist&rsquo;s."},
        {type:"prose", text:"Seemingly altruistic behaviour &mdash; risking oneself to defend the colony, or raising others&rsquo; offspring instead of one&rsquo;s own &mdash; is explained by this shared genetic inheritance between colony members."}
      ],
      notes:[{label:"Described figure &mdash; leafcutter ant agriculture", text:"Leafcutter ants (<em>Atta</em> sp.) of Central and South American rainforests build nests of thousands of compartments covering up to 0.5 km&sup2;, housing colonies of over 8 million individuals. Workers, able to carry 20&ndash;50 times their own body weight, cut and transport up to 17% of a forest&rsquo;s vegetation back to the nest, feeding it to a cultivated fungus, <em>Leucoagaricus gongylophorus</em>, that can digest the cellulose in the leaves&rsquo; cell walls, which the ants cannot &mdash; the fungus in turn feeds the ant larvae."}],
      side:{
        table:{
          title:"Intraspecific vs interspecific competition",
          head:["Feature","Intraspecific","Interspecific"],
          rows:[
            ["Between","Same species","Different species"],
            ["Niche overlap","Complete (same niche)","Partial"],
            ["Typical intensity","Highest","Lower"]
          ]
        }
      }
    },
    {
      icon:"atom", title:"Interspecific Relationships and Mutualism",
      blocks:[
        {type:"prose", text:"<strong>Herbivory</strong> (an organism feeding on a plant) ties herbivore carrying capacity to plant abundance &mdash; areas rich in plant material support a higher carrying capacity for herbivores than areas with less."},
        {type:"prose", text:"<strong>Predation</strong> (one animal, occasionally a plant, eating another animal) reduces the prey&rsquo;s carrying capacity by removing individuals, while the predator&rsquo;s own carrying capacity depends on prey availability, falling when prey become scarce."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Mutualism:</strong> a form of symbiosis in which both species derive benefit, able to increase the carrying capacity of both.",
          "<strong>Parasitism:</strong> a relationship in which the parasite benefits, at the expense of the host from which it derives its food, lowering the host&rsquo;s carrying capacity.",
          "<strong>Pathogenicity:</strong> the capacity of a microbe (bacterium, virus, fungus or protistan) to cause damage to a host, resulting in disease."
        ]},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"The fungus <em>Batrachochytrium dendrobatidis</em>, which causes chytridiomycosis, has driven significant population declines (even extinctions) in over 200 amphibian species over the past 30 years, including the evergreen robber frog (<em>Craugastor gollmeri</em>) of Costa Rica and Panama."},
        {type:"heading", text:"Rhizobium and legume mutualism"},
        {type:"prose", text:"In the <em>Rhizobium</em>&ndash;legume mutualism, <em>Rhizobium</em> bacteria living in the root nodules of legumes (e.g. clover) fix nitrogen gas into ammonium ions (later converted to nitrates by other bacteria); the plant gains usable nitrate it could not otherwise obtain in nitrate-poor soils, and supplies the bacteria with carbohydrate in return &mdash; a nutritionally costly trade for the plant, but one that opens up a niche other plants cannot exploit. Because the nitrogenase enzyme that catalyses nitrogen fixation is inhibited by oxygen (which competes with nitrogen for the enzyme&rsquo;s active site, being similar in size and shape), the nodule must stay low in oxygen: <em>Rhizobium</em> has an unusually fast aerobic metabolism that prevents oxygen build-up, and the nodule contains <strong>leghaemoglobin</strong>, an oxygen-scavenging pigment (like haemoglobin) with a high affinity for oxygen."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"<strong>Mycorrhizae</strong> &mdash; fungi growing symbiotically with plant roots &mdash; supply germinating orchids (family Orchidaceae) with nutrients and water that their tiny, food-poor seeds cannot otherwise obtain, in exchange for photosynthetically-derived glucose; the rare lady-slipper orchid (<em>Cypripedium calceolus</em>) depends on this relationship so specifically that lab-grown seedlings are difficult to reintroduce to the wild, where the particular mycorrhizal partner may be absent."},
        {type:"heading", text:"Coral and zooxanthellae"},
        {type:"prose", text:"<strong>Corals</strong> (cnidarians related to sea anemones and jellyfish) form colonies of interconnected polyps that house photosynthetic algae, <strong>zooxanthellae</strong>, within their endodermis. The coral supplies the algae with a protected habitat and waste carbon dioxide from respiration; the algae supply the coral with oxygen and glucose (as much as 90% of the organic material they photosynthesise), and give the coral its colour (golden-yellow to brown, depending on the algal pigments)."}
      ],
      notes:[{label:"Described figure &mdash; anatomy of a coral polyp", text:"Each coral polyp has stinging tentacles (bearing nematocysts) around a central mouth leading to a gastrovascular (digestive) cavity; zooxanthellae live within the polyp&rsquo;s tissue, and the polyp secretes a limestone skeleton beneath itself, with living tissue connecting it to its neighbouring polyps across the colony."}],
      side:{
        table:{
          title:"Interspecific relationships and carrying capacity",
          head:["Relationship","Effect on carrying capacity"],
          rows:[
            ["Herbivory","Herbivore K depends on plant abundance"],
            ["Predation","Prey K falls; predator K depends on prey"],
            ["Mutualism","K of both species can increase"],
            ["Parasitism","Host K falls"],
            ["Pathogenicity","Host population K can fall through disease"]
          ]
        }
      }
    },
    {
      icon:"bars", title:"Invasive Species, Niches and Tests for Interspecific Competition",
      blocks:[
        {type:"prose", text:"An <strong>alien species</strong> is introduced to an area by human activity; an <strong>invasive species</strong> is an alien species that increases rapidly in number and negatively affects the environment and native species."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"The grey squirrel (<em>Sciurus carolinensis</em>), native to eastern North America, was introduced to the UK in the 1800s and has since restricted the native red squirrel (<em>Sciurus vulgaris</em>) to just two UK locations, from previously being widespread &mdash; the grey squirrel can digest the polyphenolic substances in oak acorns that the red squirrel cannot, giving it a broader diet that let it outbreed the red squirrel even for resources both use (hazelnuts, pine cones)."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", items:[
          "<strong>Competitive exclusion:</strong> the outcome of interspecific competition in which one species outcompetes and excludes another from part of its niche.",
          "<strong>Fundamental &amp; realized niche:</strong> the fundamental niche is the full range of conditions and resources a species could potentially occupy; the realized niche is the narrower range it actually occupies once interspecific competition is accounted for."
        ]},
        {type:"prose", text:"Because the grey and red squirrel occupy overlapping niches, this is an example of competitive exclusion. Introducing an alien species can also squeeze both the alien and native species into smaller realized niches, and if the alien lacks natural predators it may become invasive &mdash; understanding a species&rsquo; fundamental niche helps predict dispersal and invasion success for conservation planning."},
        {type:"prose", text:"Interspecific competition is only <em>indicated</em>, not <em>proven</em>, by one species thriving in another&rsquo;s absence; stronger evidence comes from laboratory experiments, field observation by random sampling, or &mdash; most powerfully &mdash; field manipulation by removing one species. American ecologist Joseph Connell used removal experiments on two rocky-shore barnacle species in Scotland, <em>Semibalanus balanoides</em> (normally abundant lower on the shore) and <em>Chthamalus stellatus</em> (normally abundant higher up), even though both species&rsquo; free-swimming larvae can settle anywhere on the shore."},
        {type:"heading", text:"Connell&rsquo;s barnacle removal experiment"},
        {type:"prose", text:"Removing <em>Semibalanus</em> from the <strong>upper</strong> shore did not allow <em>Chthamalus</em> to spread there &mdash; <em>Semibalanus</em> simply cannot tolerate the desiccation of the upper shore at low tide, so its realized niche there matches its fundamental niche (it is excluded physiologically, not by competition)."},
        {type:"prose", text:"Removing <em>Semibalanus</em> from the <strong>middle</strong> shore, however, let <em>Chthamalus</em> expand into that zone &mdash; showing that <em>Chthamalus</em>&rsquo;s fundamental niche covers both zones, but interspecific competition from the superior competitor, <em>Semibalanus</em>, normally restricts <em>Chthamalus</em> to just its smaller, observed realized niche on the upper shore."},
        {type:"prose", text:"Competitive exclusion (as in Connell&rsquo;s barnacles) is only one possible outcome of interspecific competition; competing species can instead coexist with both restricted, as when lions and leopards in Africa feed on overlapping prey &mdash; each reducing the other&rsquo;s food availability without eliminating it."},
        {type:"heading", text:"Testing for association: the chi-squared test"},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Null hypothesis:</strong> the hypothesis tested statistically that there is no significant difference, or no association, between two variables; rejecting it supports a real difference or association."},
        {type:"prose", text:"A testable <strong>hypothesis</strong> is a provisional, falsifiable explanation of how an independent variable causally affects a dependent variable; hypotheses can be tested by controlled experiments (stronger evidence) or by observation (qualitative, weaker evidence) &mdash; Connell&rsquo;s removal experiments, not mere observation of where each barnacle naturally lived, were what actually demonstrated the role of competition."},
        {type:"prose", text:"The presence or absence of two species recorded across many quadrats can be tested statistically for association using the <strong>chi-squared (&chi;&sup2;) test</strong>, comparing numbers observed (O) against numbers expected (E) under the null hypothesis that there is no association (the two species&rsquo; distributions are independent): &chi;&sup2; = &sum; [(O &minus; E)&sup2; &divide; E], with degrees of freedom = (columns &minus; 1) &times; (rows &minus; 1); the calculated value is compared against a critical value from a &chi;&sup2; table at a chosen significance level (e.g. p = 0.05) to decide whether to reject the null hypothesis."}
      ],
      notes:[{label:"Worked example", text:"See the bell heather and ling moorland chi-squared calculation in the worked examples below."}],
      side:{
        title:"Observed association data",
        charts:[
          {title:"Observed quadrat counts", caption:"Ling and bell heather across 200 moorland quadrats", axis:"Number of quadrats (of 200)", svg: bv2BarChartSvg([
            {label:"Both present", v:89, color:"var(--hv-green)"},
            {label:"Ling only", v:45, color:"var(--teal)"},
            {label:"Heather only", v:31, color:"var(--gold)"},
            {label:"Neither", v:35, color:"var(--plum)"}
          ], "Bar chart of observed quadrat counts for ling and bell heather: both present 89, ling only 45, heather only 31, neither 35")}
        ],
        table:{
          title:"Connell&rsquo;s barnacle removal experiment",
          head:["Shore zone","Result for Chthamalus when Semibalanus removed","Explanation"],
          rows:[
            ["Upper shore","No change &mdash; Chthamalus did not spread further","Semibalanus excluded by desiccation (a physiological limit), not by competition"],
            ["Middle shore","Chthamalus expanded into the zone","Semibalanus normally wins the competition there, restricting Chthamalus to a smaller realized niche"]
          ]
        }
      }
    },
    {
      icon:"leaf", title:"Predator&ndash;Prey Relationships and Top-down versus Bottom-up Control",
      blocks:[
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Predator&ndash;prey relationship:</strong> the inter-relationship of population sizes due to the predation of one species (the predator) on another (the prey), e.g. the lynx (predator) and snowshoe hare (prey) of the North American boreal forest."},
        {type:"prose", text:"This is a density-dependent, negative-feedback relationship: when predators are relatively scarce, the prey population increases; the resulting greater availability of prey allows the predator population to increase too, after a time-lag; as predator numbers rise, the prey population then declines (again after a lag); with fewer prey, predator numbers fall once more, allowing prey numbers to begin recovering &mdash; and the cycle repeats."},
        {type:"prose", text:"Predation can actually benefit a prey population overall: predators tend to remove old and sick individuals first, since these are the easiest to catch, leaving a healthier remaining population with a stronger breeding pool."},
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Top-down &amp; bottom-up control:</strong> in top-down control, a higher trophic level affects community structure at lower trophic levels through predation; in bottom-up control, a lower trophic level (producers) affects higher trophic levels through resource restriction."},
        {type:"prose", text:"In <strong>top-down control</strong> (a &lsquo;predator-controlled food web&rsquo;), effects cascade downward from the top of the food chain &mdash; e.g. hunting that reduces top marine predators allows their prey, forage fish, to increase, which increases predation on zooplankton (reducing it), which in turn allows phytoplankton (under reduced grazing pressure) to increase."},
        {type:"prose", text:"In <strong>bottom-up control</strong>, effects instead cascade upward from the base of the food chain &mdash; e.g. extreme weather that reduces phytoplankton reduces zooplankton (less food), which reduces forage fish, which reduces top predator numbers. Both forms of control are possible within a single community, but typically one dominates over the other."}
      ],
      notes:[
        {label:"Common mistake", text:"&lsquo;Negative&rsquo; feedback does not mean the feedback loop is harmful &mdash; it usually counteracts deviation away from a steady-state equilibrium. &lsquo;Positive&rsquo; feedback does not mean a beneficial effect either &mdash; it increases change in a system, moving it further from equilibrium."},
        {label:"Described figure &mdash; snowshoe hare and lynx cycle", text:"Population numbers (in thousands) plotted against year from 1845&ndash;1945 show the snowshoe hare and lynx populations oscillating together in roughly repeating cycles, with each lynx population peak lagging slightly behind the corresponding hare population peak &mdash; graphical evidence of the time-lagged negative feedback described above."}
      ],
      side:{
        table:{
          title:"Top-down vs bottom-up control (4-level marine food chain)",
          head:["Control type","Trigger","Cascade direction"],
          rows:[
            ["Top-down","Hunting reduces top predators","Predators &darr;, forage fish &uarr;, zooplankton &darr;, phytoplankton &uarr;"],
            ["Bottom-up","Extreme weather reduces phytoplankton","Phytoplankton &darr;, zooplankton &darr;, forage fish &darr;, predators &darr;"]
          ]
        }
      }
    },
    {
      icon:"atom", title:"Allelopathy and Secretion of Antibiotics",
      blocks:[
        {type:"callout", style:"definition", icon:"book", title:"Definition", text:"<strong>Allelopathy</strong> (from Greek <em>allelon</em>, &lsquo;each other&rsquo;, and <em>pathos</em>, &lsquo;to suffer&rsquo; &mdash; the same root as &lsquo;pathogen&rsquo;): chemical inhibition of one plant (or other organism) by another, through the release of chemicals (allelochemicals) that act as germination or growth inhibitors."},
        {type:"prose", text:"Interspecific plant competition can be severe, reducing the carrying capacity of both competing species. An allelochemical creates adverse conditions that reduce a competitor&rsquo;s seed germination, seedling growth, or overall growth; some allelochemicals specifically reduce chlorophyll production, slowing or stopping photosynthesis in the affected plant."},
        {type:"prose", text:"Plants achieve this in three main ways: releasing allelochemicals from their roots into the soil, which suppress or kill neighbouring plants on absorption; releasing gaseous allelochemicals from leaf stomata, which suppress or kill plants that absorb them; and shedding leaves containing toxic chemicals, which are released as the fallen leaves decompose."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"All brassica plants (cabbage, mustard, kale, radish, broccoli) show allelopathic properties &mdash; mustard extracts, for example, suppress fungal pathogens and limit the germination of some legumes (e.g. lentils) and oats, while broccoli is allelopathic towards later-planted broccoli or other brassica crops, which is why farmers rotate crops and avoid replanting brassicas where broccoli recently grew. Bracken (<em>Pteridium aquilinum</em>) competitively excludes other plants through allelopathy, becoming dominant and reducing local biodiversity wherever it grows densely."},
        {type:"prose", text:"Fungi can achieve a similar effect by secreting <strong>antibiotics</strong> &mdash; chemicals that kill or inhibit competing bacteria, itself a form of allelopathy."},
        {type:"callout", style:"example", icon:"leaf", title:"Example", text:"Penicillin, derived from <em>Penicillium</em> fungi, was the first mass-produced antibiotic for treating human bacterial disease; it was discovered accidentally by Alexander Fleming in 1929 while studying <em>Staphylococcus</em> (the bacterium causing boils and sore throats)."},
        {type:"prose", text:"Such fungal antibiotic properties have since been exploited to produce antibiotic medicines."}
      ],
      notes:[{label:"Top tip", text:"Allelopathy and antibiotic secretion are fundamentally the same kind of process: both release a chemical substance into the environment specifically to deter potential competitors."}]
    }
  ],
  workedExamples: [
    {
      title:"Estimating population size by quadrat sampling",
      question:"An ecologist estimates the population of daisies (<em>Bellis perennis</em>) in a 1000 m&sup2; meadow using fifty randomly placed 1 m&sup2; quadrats. The mean number of daisies recorded per quadrat is 8. Estimate the total population size of daisies in the meadow, and state one assumption the method relies on.",
      answer:[
        "Apply the formula: population size = (mean density per quadrat &times; total area) &divide; area of each quadrat.",
        "Substitute the values: population size = (8 &times; 1000) &divide; 1 = 8000 daisies.",
        "Assumption: the quadrats were placed using genuinely random coordinates (not chosen by eye), and the daisies are distributed evenly enough across the meadow for fifty quadrats to give a representative mean density."
      ]
    },
    {
      title:"Estimating population size with the Lincoln index",
      question:"In a capture&ndash;mark&ndash;release&ndash;recapture study of a woodlice population, 5 individuals are captured, marked and released (M). Twenty-four hours later, a second random sample of 8 individuals is recaptured (N), of which 1 is found to be marked (R). (a) Calculate the estimated population size. (b) State two assumptions this estimate relies on.",
      answer:[
        "(a) Population size = (M &times; N) &divide; R = (5 &times; 8) &divide; 1 = 40 woodlice.",
        "(b) The estimate assumes the population is closed (no immigration, emigration, births or deaths between the two samples) and that the marked individuals mixed completely and evenly back into the population before the second sample was taken &mdash; other valid assumptions include that marks neither fall off nor harm the animal nor increase its risk of predation, and that every individual is equally easy to catch."
      ]
    },
    {
      title:"Testing for association using the chi-squared test",
      question:"In a survey of 200 randomly placed quadrats on an area of moorland, the presence or absence of ling (<em>Calluna vulgaris</em>) and bell heather (<em>Erica cinerea</em>) was recorded: 89 quadrats contained both species, 45 contained ling only, 31 contained bell heather only, and 35 contained neither. Using the corresponding expected values 80, 54, 40 and 26 for these same four categories, calculate &chi;&sup2; and state, with reference to a critical value of 3.84 (1 degree of freedom, p = 0.05), whether the two species are associated.",
      answer:[
        "&chi;&sup2; = &sum; [(O &minus; E)&sup2; &divide; E] = (89&minus;80)&sup2;&divide;80 + (45&minus;54)&sup2;&divide;54 + (31&minus;40)&sup2;&divide;40 + (35&minus;26)&sup2;&divide;26.",
        "= 81&divide;80 + 81&divide;54 + 81&divide;40 + 81&divide;26 = 1.01 + 1.50 + 2.03 + 3.11 = 7.65.",
        "Degrees of freedom = (columns &minus; 1) &times; (rows &minus; 1) = (2&minus;1) &times; (2&minus;1) = 1.",
        "Since the calculated &chi;&sup2; (7.65) is greater than the critical value (3.84) at p = 0.05 for 1 degree of freedom, the null hypothesis (no association) is rejected: ling and bell heather show a statistically significant association &mdash; their distributions are not independent of each other."
      ]
    },
    {
      title:"Interpreting the sigmoid growth curve",
      question:"A small population of deer is introduced to a predator-free island with abundant vegetation. (a) State the relationship between natality (N), mortality (M), immigration (I) and emigration (E) during the population&rsquo;s initial exponential growth phase. (b) State the relationship once the population has reached the plateau phase of the sigmoid curve. (c) Explain, in terms of resources and competition, why the relationship changes between (a) and (b).",
      answer:[
        "(a) I + N &gt; E + M &mdash; natality greatly exceeds mortality because resources are abundant, limiting factors are minimal, and there is little competition or predation.",
        "(b) I + N = E + M (on average) &mdash; the population fluctuates around a set point, the carrying capacity, with natality and mortality roughly balanced.",
        "(c) As the deer population grows, the same food and space must be shared between more individuals, so intraspecific competition for limited resources increases; this raises mortality and/or lowers natality until the two rates come into balance at the island&rsquo;s carrying capacity."
      ]
    },
    {
      title:"Classifying interspecific relationships",
      question:"For each scenario below, name the type of interspecific relationship described and briefly justify your answer: (a) <em>Rhizobium</em> bacteria in a legume&rsquo;s root nodules fix nitrogen for the plant and receive carbohydrates in return. (b) The fungus <em>Batrachochytrium dendrobatidis</em> has caused significant population declines in the evergreen robber frog. (c) A lion kills and eats a zebra. (d) In a UK woodland, grey squirrels and red squirrels both feed on the same hazelnuts and pine cones.",
      answer:[
        "(a) Mutualism &mdash; both the bacteria (which gain carbohydrate) and the plant (which gains usable nitrate) benefit from the relationship.",
        "(b) Pathogenicity &mdash; <em>B. dendrobatidis</em> is a microbial pathogen causing a disease (chytridiomycosis) that reduces the frog population&rsquo;s carrying capacity, rather than directly consuming the frogs as food or living inside them as a classic parasite would.",
        "(c) Predation &mdash; the lion (predator) kills and consumes the zebra (prey), directly reducing the prey population.",
        "(d) Interspecific competition &mdash; the two squirrel species have an overlapping niche (sharing the same food resources), which can lead to competitive exclusion of the less successful competitor (the red squirrel)."
      ]
    }
  ],
  summary: [
    "A population is an interacting group of one species in an area; a community is all the interacting populations of different species in an ecosystem.",
    "Random sampling avoids bias when estimating population size; stratified sampling suits areas with multiple habitat types, and systematic sampling (along a transect) suits an environmental gradient.",
    "Quadrats estimate population size for sessile organisms using the formula population size = (mean density per quadrat &times; total area) &divide; area of each quadrat.",
    "Capture&ndash;mark&ndash;release&ndash;recapture estimates population size for motile organisms using the Lincoln index, (M &times; N) &divide; R, which assumes a closed population with complete mixing, harmless/persistent marks and equal catchability.",
    "Carrying capacity is the maximum population size an environment can sustain; limiting factors (e.g. food, space, water) and density-dependent factors push population size back towards it by negative feedback.",
    "Density-dependent factors (e.g. competition, predation, disease) have effects that scale with population density and set carrying capacity; density-independent factors (e.g. weather) affect all population sizes regardless of density and do not affect carrying capacity.",
    "Exponential growth is an accelerating, unrestricted increase; sigmoid (S-shaped) growth shows an exponential phase, a transition phase, and a plateau phase around carrying capacity, describable via natality, mortality, immigration and emigration rates.",
    "Intraspecific competition (within a species, sharing the same niche) is typically more intense than interspecific competition (between species, with different niches); many species balance competition with cooperation (dominance hierarchies, cooperative hunting, social insect colonies) and altruism.",
    "Interspecific relationships include herbivory, predation, interspecific competition, mutualism, parasitism and pathogenicity &mdash; each differently affecting the carrying capacities of the species involved.",
    "Mutualism benefits both species, as in <em>Rhizobium</em> root nodules fixing nitrogen for legumes, mycorrhizae supplying orchids with nutrients, and zooxanthellae photosynthesising for corals.",
    "Invasive alien species (e.g. the grey squirrel displacing the red squirrel in the UK) can outcompete endemic species with overlapping niches, driving competitive exclusion.",
    "Connell&rsquo;s barnacle experiments showed that a species&rsquo; realized niche can be smaller than its fundamental niche because of interspecific competition; the chi-squared test can detect a statistically significant association between two species&rsquo; distributions.",
    "Predator&ndash;prey relationships (e.g. snowshoe hare and lynx) show density-dependent, negative-feedback population cycles; populations can also be controlled top-down (by predation from higher trophic levels) or bottom-up (by resource limitation from producers).",
    "Allelopathy (e.g. in brassicas and bracken) and antibiotic secretion by fungi (e.g. penicillin) are both chemical mechanisms by which one organism suppresses potential competitors."
  ]
}
