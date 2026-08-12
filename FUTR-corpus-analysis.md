# FUTR.tv Corpus Analysis — Phase 1 (Factual Foundation)

**Source:** `data/guests.json` (cbcbcbd/futr-guest-directory), pulled 2026-08-12.

## Scope & Counts

| Show | Episodes | Kept? |
|---|---:|---|
| **FUTR.tv (originals)** | **218** | ✅ analyzed |
| IT Visionaries (Mission cross-post) | 16 | ❌ dropped |
| The Fleet (Mission cross-post) | 13 | ❌ dropped |
| Total records in file | 247 | |

- **FUTR.tv originals analyzed:** 218 (one row per guest; multi-guest episodes counted once per guest, matching the source file's structure)
- **Date range:** 2019-03-21 → 2026-07-02 (~7.3 years)
- **Cross-posts removed:** 29 (16 IT Visionaries + 13 The Fleet)

## Distribution by Industry / Domain

| Industry / Domain | Episodes | % |
|---|---:|---:|
| Data & Cloud Infrastructure | 35 | 16% |
| Cybersecurity | 29 | 13% |
| Media/Creator | 23 | 11% |
| Social Impact & DEI | 17 | 8% |
| Enterprise SaaS | 17 | 8% |
| Startups, VC & Business | 16 | 7% |
| Personal Dev & Wellness | 16 | 7% |
| AI/ML | 12 | 6% |
| Healthtech/Biotech | 9 | 4% |
| Hardware/IoT | 8 | 4% |
| Mobility/EV | 7 | 3% |
| Climate/Energy | 7 | 3% |
| Workforce/Future of Work | 6 | 3% |
| Consumer/Retail | 5 | 2% |
| Cannabis | 3 | 1% |
| Sports | 2 | 1% |
| Gaming | 2 | 1% |
| Fintech | 2 | 1% |
| Web3/Crypto | 2 | 1% |

## Distribution by Guest Type

| Guest Type | Episodes | % |
|---|---:|---:|
| Founder/CEO | 95 | 44% |
| Operator | 59 | 27% |
| CTO/Technical | 29 | 13% |
| Author/Academic | 28 | 13% |
| Investor | 7 | 3% |

## Distribution by Topic Angle

| Topic Angle | Episodes | % |
|---|---:|---:|
| Practical | 102 | 47% |
| Business/Strategy | 63 | 29% |
| Future/Visionary | 27 | 12% |
| Human/Origin | 18 | 8% |
| Contrarian | 8 | 4% |

## Top Clusters (industry × angle)

| # | Cluster | Episodes |
|---|---|---:|
| 1 | Data & Cloud Infrastructure — *Practical* | 25 |
| 2 | Cybersecurity — *Practical* | 22 |
| 3 | Social Impact & DEI — *Business/Strategy* | 14 |
| 4 | Enterprise SaaS — *Practical* | 10 |
| 5 | Startups, VC & Business — *Business/Strategy* | 10 |

**Guest-type concentration:** Cybersecurity + Founder/CEO (15), Data & Cloud Infra + Founder/CEO (14), Data & Cloud Infra + Operator (14), Cybersecurity + CTO/Technical (9).

## Temporal Shift (top 3 industries per era)

| Era | n | #1 | #2 | #3 |
|---|---:|---|---|---|
| 2019–2021 | 91 | Data & Cloud Infrastructure (28) | Cybersecurity (15) | Personal Dev & Wellness (11) |
| 2022–2023 | 89 | Media/Creator (13) | Cybersecurity (13) | Enterprise SaaS (11) |
| 2024–2026 | 38 | AI/ML (6) | Mobility/EV (5) | Climate/Energy (4) |

## Where the Center of Gravity Actually Is

A plain read of the numbers, no naming yet:

1. **The corpus is built on enterprise tech, not consumer/frontier tech.** Data & Cloud Infrastructure (16%) + Cybersecurity (13%) + Enterprise SaaS (8%) = **37% of everything** — 81 of 218 episodes. Add the guest mix (57% of guests are Founder/CEO or CTO/Technical) and the dominant unit is *a technical leader from a B2B software or infrastructure company*.

2. **The default mode is "how it works," not "what's coming."** 47% Practical + 29% Business/Strategy = **76%** of episodes are explanatory/operational. Future/Visionary is only 12% and Contrarian just 4% — despite the "building the future" tagline, the actual content is mostly present-tense: how a product works, how a company goes to market, how a threat is stopped.

3. **The two largest single clusters are both "practical infra":** Data & Cloud Infra × Practical (25) and Cybersecurity × Practical (22) together account for **~22% of the corpus** and are heavily conference-driven (AWS re:Invent, VMWorld, NetApp Insight, HPC+AI Wall Street). This is the historical spine of the show.

4. **There is a real, visible pivot underway.** The center of gravity is *moving*. Early era (2019–2021) is infra/cyber-dominated; the recent era (2024–2026) leads with AI/ML, Mobility/EV, and Climate/Energy — physical/frontier hard-tech that barely registered before. The back catalog and the recent slate describe two different shows sharing one feed.

5. **A persistent secondary theme cuts across all eras: people and access.** Social Impact & DEI (8%) + Personal Dev & Wellness (7%) + Workforce (3%) = **18%** — a consistent human/mission strand (women in tech, DEI, mental health, workforce reskilling, leadership) that has run the entire 7 years alongside the tech interviews.

**Net:** the historical mass is *practical, founder/technical-led, enterprise infrastructure & security* — but the forward edge is bending toward *founder-led frontier hard-tech (AI, EV, energy, health)*, with a steady humanist/impact thread throughout. The gap between where the mass is and where the recent episodes point is the central tension for niche identification.

## Full Episode List — Grouped by Industry

### Data & Cloud Infrastructure (35)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2023-10-16 | Lee Blackwell | Databricks | [Highlights from Databricks' Data + AI World Tour in Chicago - Generation AI Takes Center Stage](https://futr.tv/thefeed/2023/10/16/highlights-from-databricks-data-ai-world-tour-in-chicago-generation-ai-takes-center-stage) | CTO | Practical |
| 2023-07-17 | Tom Frazier | Redivider | [Edge Computing and Environmental Impact: How Redivider is Leading the Way](https://futr.tv/thefeed/2023/7/17/edge-computing-and-environmental-impact-how-redivider-is-leading-the-way) | Founder | Practical |
| 2023-03-20 | Adi Gelvan | Speedb | [The Need for Speedb Powered by Open Source](https://futr.tv/thefeed/2023/3/20/the-need-for-speedb-powered-by-open-source) | Founder | Practical |
| 2022-10-03 | Ryan Quick | Data Vortex | [HPC + AI Wall Street 2022 Update](https://futr.tv/thefeed/2022/10/3/hpc-ai-wall-street-2022-update-96) | CTO | Practical |
| 2022-09-12 | Poojan Kumar | Clumio | [Aim For Where The Ball Is Going - With Clumio CEO Poojan Kumar](https://futr.tv/thefeed/2022/9/12/aim-for-where-the-ball-is-going-with-clumio-ceo-pujan-kumar-94) | Founder | Business |
| 2022-06-27 | Kirk Marple | Unstruk | [Unstructured Wisdom with Unstruk's CEO Kirk Marple](https://futr.tv/thefeed/2022/6/27/unstructured-wisdom-with-unstruks-ceo-kirk-marple-85) | Founder | Practical |
| 2022-02-28 | Ryan Quick | — | [The Formula 1 of Computing, HPC with Ryan Quick](https://futr.tv/thefeed/2022/2/27/the-formula-1-of-computing-hpc-with-ryan-quick-69) | CTO | Practical |
| 2021-11-08 | Chadd Kenney | Clumio | [You gotta stay focused! - Clumio's VP of product, Chadd Kenney on listening to your customers](https://futr.tv/thefeed/2021/11/8/you-gotta-stay-focused-clumios-vp-of-product-chadd-kenney-on-listening-to-your-customers-62) | CTO | Business |
| 2021-10-12 | Nick Huedecker | Cribl | [Finding Gold with Nick Huedecker of Cribl](https://futr.tv/thefeed/2021/10/12/finding-gold-with-nick-huedecker-of-cribl-58) | Operator | Practical |
| 2021-10-04 | Michael Ferranti | Portworx | [Your Portworx in a Storm, Solving the Database Challenge](https://futr.tv/thefeed/2021/10/3/your-portworx-in-a-storm-solving-the-database-challenge-56) | Operator | Practical |
| 2021-09-13 | Brian O'Shea | Clumio | [The New Go To Market with Clumio's Brian O'Shea](https://futr.tv/thefeed/2021/9/13/the-new-go-to-market-with-clumios-brian-oshea-53) | Operator | Business |
| 2021-06-28 | Jeff Dunworth | VAST | [Building A Unicorn With VAST Data Founder Jeff Denworth](https://futr.tv/thefeed/2021/6/28/48-building-an-a-hole-free-business-with-vast-data-founder-jeff-denworth) | Founder | Business |
| 2021-05-03 | Lee Blackwell | Databricks | [Data is a Team Sport - Interview with Databricks' engineer Lee Blackwell](https://futr.tv/thefeed/2021/5/2/41-data-is-a-team-sport-interview-with-databricks-engineer-lee-blackwell) | CTO | Practical |
| 2021-03-01 | Ilan Rabinovitch | Datadog | [Talking with the Big Dog, Datadog and Ilan Rabinovitch](https://futr.tv/thefeed/2021/3/1/35-talking-with-the-big-dog-datadog-and-ilan-rabinovich) | CTO | Practical |
| 2021-02-15 | Duncan Epping | VMWare | [The Future of Computing with VMWare Legend Duncan Epping](https://futr.tv/thefeed/2021/2/15/33-the-future-of-computing-with-vmware-legend-duncan-epping) | CTO | Future |
| 2020-10-13 | Mahesh Patel | Druva | [The Evolution of Druva With CFO Mahesh Patel](https://futr.tv/thefeed/2020/10/12/25-the-evolution-of-druva-with-cfo-mahesh-patel) | Operator | Business |
| 2020-09-29 | Joe Tarantino | Cohesity | [Talking Data Management and Sales With Cohesity's Joe Tarantino](https://futr.tv/thefeed/2020/9/29/24-talking-data-management-and-sales-with-cohesitys-joe-tarantino) | Operator | Business |
| 2020-09-15 | Raju Datla | CloudFabrix | [Talking AIOPs with CloudFabrix CEO Raju Datla](https://futr.tv/thefeed/2020/9/14/22-talking-aiops-with-cloudfabrix-ceo-raju-datla) | Founder | Practical |
| 2020-08-31 | Molly Presley | Qumulo | [All about Qumulo with Molly Presley](https://futr.tv/thefeed/2020/8/31/21-all-about-qumulo-with-molly-presley) | Operator | Practical |
| 2020-08-12 | Bipul Sinha | Rubrik | [The Wisdom Of Bipul Sinha](https://futr.tv/thefeed/2020/8/11/podcast-19-the-wisdom-of-bipul-sinha) | Founder | Business |
| 2020-06-04 | Tim Delisle | Datalogue | [Talking Data and Leadership with Datalogue Co-Founder and CEO Tim Delisle - Part 2](https://futr.tv/thefeed/2020/6/3/podcast-13-talking-data-and-leadership-with-datalogue-co-founder-and-ceo-tim-delisle-part-2) | Founder | Business |
| 2020-06-03 | Tim Delisle | Datalogue | [Talking Data and Leadership with Datalogue Co-Founder and CEO Tim Delisle - Part 1](https://futr.tv/thefeed/2020/6/2/podcast-13-talking-data-and-leadership-with-datalogue-co-founder-and-ceo-tim-delisle-part-1) | Founder | Business |
| 2020-04-30 | Joe Ferguson | Clumio | [SaaS & Clumio with Joe Ferguson](https://futr.tv/thefeed/2020/4/30/podcast-8-saas-amp-clumio-with-joe-ferguson) | Operator | Practical |
| 2019-12-14 | Paul Jasek | Instana | [AWS Re:Invent 2019 Interviews - Instana and Infinidat](https://futr.tv/thefeed/2019/12/13/aws-reinvent-2019-interviews-instana-and-infinidat) | Operator | Practical |
| 2019-12-14 | Erik Kaulberg | Infinidat | [AWS Re:Invent 2019 Interviews - Instana and Infinidat](https://futr.tv/thefeed/2019/12/13/aws-reinvent-2019-interviews-instana-and-infinidat) | Operator | Practical |
| 2019-12-13 | Will Pericak | FiveTran | [AWS Re:Invent 2019 Interviews - Fivetran and Perimeter81](https://futr.tv/thefeed/2019/12/12/xt825j8w633lllfa096ryc4l6vsr2d) | Operator | Practical |
| 2019-12-12 | Erik Peterson | CloudZero | [AWS Re:Invent 2019 Interviews - CloudZero](https://futr.tv/thefeed/2019/12/11/aws-reinvent-2019-interviews-cloudzero) | Founder | Practical |
| 2019-11-11 | Piyush Agarwal | Cleondris | [NetApp Insight 2019 Part 2: Interview with Igneous and Cleondris](https://futr.tv/thefeed/2019/11/10/y5w7jjio8lw65n4u43so2w77cmmp8o) | Operator | Practical |
| 2019-11-11 | Christian Smith | Igneous | [NetApp Insight 2019 Part 2: Interview with Igneous and Cleondris](https://futr.tv/thefeed/2019/11/10/y5w7jjio8lw65n4u43so2w77cmmp8o) | Operator | Practical |
| 2019-10-10 | David Hatfield | Pure Storage | [Pure Storage's Accelerate 2019 Conference Part 1](https://futr.tv/thefeed/2019/10/9/pure-storages-accelerate-2019-conference) | Founder | Practical |
| 2019-09-30 | Eric Oberhofer | Liqid | [VMWorld 2019: A Quick Interview With Liqid](https://futr.tv/thefeed/2019/9/30/vmworld-2019-a-quick-interview-with-liqid) | Operator | Practical |
| 2019-09-24 | Mohit Aron | Cohesity | [VMWorld 2019: Quick Chat with Cohesity CEO and Founder Mohit Aron](https://futr.tv/thefeed/2019/9/23/vmworld-2019-quick-chat-with-cohesity-ceo-and-founder-mohit-aron) | Founder | Practical |
| 2019-09-19 | Poojan Kumar | Clumio | [VMWorld 2019: Hands On WIth Clumio](https://futr.tv/thefeed/2019/9/19/vmworld-2019-hands-on-with-clumio) | Founder | Practical |
| 2019-09-17 | Chandra Sekar | Avi Networks | [VMWorld 2019-Avi Networks](https://futr.tv/thefeed/2019/9/16/vmworld-2019-avi-networks) | Operator | Practical |
| 2019-04-16 | Poojan Kumar | Clumio | [FUTRtech SaaS Dinner with Poojan Kumar of Clumio](https://futr.tv/thefeed/2019/4/16/futrtech-saas-dinner-with-poojan-kumar-of-clumio) | Founder | Practical |

### Cybersecurity (29)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2024-04-15 | Anthony Spiteri | Veeam | [Cybersecurity in 2024: AI's Impact on Data Protection & Recovery](https://futr.tv/thefeed/2024/4/15/cybersecurity-in-2024-ais-impact-on-data-protection-amp-recovery) | CTO | Future |
| 2023-06-12 | Nigel LeBlanc | Cyber Warrior Network | [Unleashing Cybersecurity Talent: How Gaming Translates into Real-World Cybersecurity Jobs](https://futr.tv/thefeed/2023/6/12/unleashing-cybersecurity-talent-how-gaming-translates-into-real-world-cybersecurity-jobs) | Founder | Business |
| 2023-01-30 | Brian O'Shea | Vesa | [Securing Sensitive Data in the Cloud with Veza: A FUTR Podcast](https://futr.tv/thefeed/2023/1/29/securing-sensitive-data-in-the-cloud-with-veza-a-futr-podcast-109) | Operator | Practical |
| 2023-01-23 | Jay Mar-Tang | Pentera | [Empower Your Security Strategy with Automated Validation from Pentera](https://futr.tv/thefeed/2023/1/22/empower-your-security-strategy-with-automated-validation-from-pentera-108) | Operator | Practical |
| 2022-10-17 | eric Bednash | Racktop Systems | [What is Cyberstorage? - Eric Bednash of Racktop Systems](https://futr.tv/thefeed/2022/10/14/encourage-cyberstorage-with-eric-bednash-of-racktop-systems-98) | Founder | Practical |
| 2022-07-11 | Matt Rose | Bionic | [The Bionic Man - Application Security Posture Management with Matt Rose](https://futr.tv/thefeed/2022/7/10/the-bionic-man-application-security-posture-management-with-matt-rose-8) | CTO | Practical |
| 2022-05-31 | Richard Rushing | Motorola Mobility | [FUTR Showcase with Motorola Mobility CISO, Richard Rushing and Perdoceo CIO, Dave Czeszewski Panel](https://futr.tv/thefeed/2022/5/31/futr-showcase-with-motorola-mobility-ciso-richard-rushing-and-perdoceo-cio-dave-czeszewski-panel) | CTO | Business |
| 2022-05-23 | Saket Modi | Safe Security | [Quantify Your Risk with Saket Modi, CEO of Safe Security](https://futr.tv/thefeed/2022/5/23/quantify-your-risk-with-saket-modi-ceo-of-safe-security-81) | Founder | Practical |
| 2022-05-02 | Jean-Paul Schmetz | Ghostery | [Privacy Matters with Ghostery CEO Jean-Paul Schmetz](https://futr.tv/thefeed/2022/5/2/privacy-matters-with-ghostery-ceo-jean-paul-schmetz-78) | Founder | Future |
| 2022-04-11 | Raj Datta | Oak9 | [Proactive Security with Oak9's Raj Datta and Aakash Shah](https://futr.tv/thefeed/2022/4/11/proactive-security-with-oak9s-raj-datta-and-aakash-shah-75) | Founder | Practical |
| 2022-04-11 | Aakash Shah | Oak9 | [Proactive Security with Oak9's Raj Datta and Aakash Shah](https://futr.tv/thefeed/2022/4/11/proactive-security-with-oak9s-raj-datta-and-aakash-shah-75) | Founder | Practical |
| 2022-03-29 | Mike Britton | Abnormal Security | [Battling Business Email Compromise with Abnormal Security's CISO Mike Britton](https://futr.tv/thefeed/2022/3/21/battling-business-email-compromise-with-abnormal-securitys-ciso-mike-britton-73) | CTO | Practical |
| 2022-02-21 | Eoin Hinchey | Tines | [Crack the Security Code, With Tines' No Code/LowCode](https://futr.tv/thefeed/2022/2/21/crack-the-security-code-with-tines-no-codelowcode-68) | CTO | Practical |
| 2022-02-14 | Ambuj Kumar | Fortanix | [Keep it confidential with confidential Computing and Fortanix](https://futr.tv/thefeed/2022/2/14/keep-it-confidential-with-confidential-computing-and-fortanix-67) | Founder | Practical |
| 2021-12-06 | David Hatfield | Lacework | [You've Gotta Have Hat - Lacework CEO David Hatfield](https://futr.tv/thefeed/2021/12/6/youve-gotta-have-hat-lacework-with-ceo-david-hatfield-episode-63) | Founder | Business |
| 2021-06-21 | Andrew Miller | Pure Storage | [Ransomware Is Everywhere, with Pure Storage's Ransomware expert, Andrew Miller](https://futr.tv/thefeed/2021/6/21/47-ransomware-is-everywhere-with-pure-storages-ransomware-expert-andrew-miller) | CTO | Practical |
| 2021-05-24 | Hitesh Sheth | Vectra AI | [Stopping Ransomware Threats with Vectra AI, An Interview with CEO, Hitesh Sheth](https://futr.tv/thefeed/2021/5/24/43-stopping-ransomware-threats-with-vectra-ai-an-interview-with-ceo-hitesh-sheth) | Founder | Practical |
| 2021-03-15 | Nathanael Iversen | Illumio | [Zero Trust and Microsegmentation with Illumio's Nathanael Iversen](https://futr.tv/thefeed/2021/3/15/36-zero-trust-and-microsegmentation-with-illumios-nathanael-iversen) | CTO | Practical |
| 2021-02-22 | Jared Phipps | SentinelOne | [Stopping SolarWinds Breaches with Jared Phipps from SentinelOne](https://futr.tv/thefeed/2021/2/22/34-stopping-solarwinds-breach-with-jared-phipps-from-sentinelone) | Operator | Practical |
| 2021-02-08 | Sakey Modi | Safe Security | [Talking Security with Safe Security CEO Saket Modi](https://futr.tv/thefeed/2021/2/7/32-talking-security-with-safe-security-ceo-saket-modi) | Founder | Business |
| 2021-02-01 | Brian Nesmith | Arctic Wolf | [Managing Your Security With Arctic Wolf CEO Brian NeSmith](https://futr.tv/thefeed/2021/1/31/31-managing-your-security-with-arctic-wolf-ceo-brian-nesmith) | Founder | Business |
| 2021-01-18 | Val Bercovici | Chainkit | [Chainkit CEO Val Bercovici On What You Need To Know About The Solarwinds Breach](https://futr.tv/thefeed/2021/1/18/29-chainkit-ceo-val-bercovici-on-what-you-need-to-know-about-the-solarwinds-breach) | Founder | Practical |
| 2021-01-11 | Keegan Riley | Sysdig | [Digging Deep with Keegan Riley from Sysdig](https://futr.tv/thefeed/2021/1/10/digging-deep-with-keegan-riley-from-sysdig) | Operator | Practical |
| 2020-07-07 | Daniel Nowak | — | [The Grey Side of Security with Daniel Nowak - Part 2](https://futr.tv/thefeed/2020/7/7/podcast-16-the-grey-side-of-security-with-daniel-nowak-part-2) | CTO | Practical |
| 2020-07-03 | Daniel Nowak | — | [The Grey Side of Security with Daniel Nowak - Part 1](https://futr.tv/thefeed/2020/7/2/podcast-16-the-grey-side-of-security-with-daniel-nowak-part-1) | CTO | Practical |
| 2020-05-26 | Mukesh Singh | Confluera | [Talking Security and Confluera with John Thompson and Mukesh Singh](https://futr.tv/thefeed/2020/5/26/podcast-12-talking-security-and-confluera-with-john-thompson-and-mukesh-singh) | Founder | Practical |
| 2019-12-13 | Sagi Gidali | Perimeter81 | [AWS Re:Invent 2019 Interviews - Fivetran and Perimeter81](https://futr.tv/thefeed/2019/12/12/xt825j8w633lllfa096ryc4l6vsr2d) | Founder | Practical |
| 2019-09-25 | Abhijit Ghosh | Confluera | [VMWorld 2019: A quick conversation with Abhijit Ghosh, CEO and Founder of Confluera.](https://futr.tv/thefeed/2019/9/25/vmworld-2019-a-quick-conversation-with-abhijit-ghosh-ceo-and-founder-of-confluera) | Founder | Practical |
| 2019-03-21 | Joshua "Mac" McMahon | Root9B | [Interview With Security Company Root9B at SXSW](https://futr.tv/thefeed/2019/3/21/interview-with-security-company-root9b-at-sxsw) | Operator | Practical |

### Media/Creator (23)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2023-10-02 | Scott Burton | Earnest Drinker | [Understanding Our Relationship with Alcohol: The Making of the 'Earnest Drinker' Documentary](https://futr.tv/thefeed/2023/10/2/understanding-our-relationship-with-alcohol-the-making-of-the-earnest-drinker-documentary) | Author | Human |
| 2023-05-22 | Santiago Jaramillo | Bunny Studios | [Revolutionizing Content Marketing: Insights from Bunny Studios CEO](https://futr.tv/thefeed/2023/5/22/revolutionizing-content-marketing-insights-from-bunny-studios-ceo) | Founder | Practical |
| 2023-02-06 | Reagan Fry | Kajabi | [Uncovering the Creator Economy: Insights from a Social Media Insider with Reagan Fry](https://futr.tv/thefeed/2023/2/6/uncovering-the-creator-economy-insights-from-a-social-media-insider-with-reagan-fry) | Operator | Business |
| 2022-12-05 | Ralph Andre | CANVS | [Street Art Hunting - Exploring the Best of Street Art With Ralph Andre of CANVS](https://futr.tv/thefeed/2022/12/4/exploring-street-art-cities-with-ralph-andre-of-canvs-103) | Founder | Human |
| 2022-11-14 | Donna Loughlin | LMGR | [A Genuine Moment with Master Story Teller Donna Loughlin](https://futr.tv/thefeed/2022/11/14/a-genuine-moment-with-master-story-teller-donn-loughlin-102) | Founder | Human |
| 2022-07-18 | Joel Beasley | Modern CTO | [Making Great Podcasts, With Modern CTO's Joel Beasley](https://futr.tv/thefeed/2022/7/18/making-great-podcasts-with-modern-ctos-joel-beasley-87) | Author | Practical |
| 2022-06-13 | Vasant Patel | Meet the Patels | [Meeting the Patels - Catching up with Vasant and Champa Patel](https://futr.tv/thefeed/2022/6/13/meeting-the-patels-catching-up-with-vasant-and-champa-patel-83) | Author | Human |
| 2022-06-13 | Champa Patel | Meet the Patels | [Meeting the Patels - Catching up with Vasant and Champa Patel](https://futr.tv/thefeed/2022/6/13/meeting-the-patels-catching-up-with-vasant-and-champa-patel-83) | Author | Human |
| 2022-04-25 | Lindsey Alexander | DisInfoGal | [Understanding the War in Ukraine with Disinfo Gal](https://futr.tv/thefeed/2022/4/25/understanding-the-war-in-ukraine-with-disinfo-gal-77) | Author | Practical |
| 2022-03-14 | Pedro Henriques | TheNewsroom | [It's Time For Trustworthy News with TheNewsroom](https://futr.tv/thefeed/2022/3/12/its-time-for-trustworthy-news-with-thenewsroom-71) | Founder | Future |
| 2022-03-14 | Jenny Romano | TheNewsroom | [It's Time For Trustworthy News with TheNewsroom](https://futr.tv/thefeed/2022/3/12/its-time-for-trustworthy-news-with-thenewsroom-71) | Operator | Future |
| 2022-02-07 | Lindsey Alexander | DisInfoGal | [The Dangers of Disinformation with DisInfoGal](https://futr.tv/thefeed/2022/2/7/the-dangers-of-disinformation-with-disinfogal-66) | Author | Future |
| 2022-01-31 | Jed Corenthal | Phenix | [Making the Real-Time Streaming Magic with Phenix](https://futr.tv/thefeed/2022/1/31/making-the-magic-with-phenix-64) | Operator | Practical |
| 2021-10-18 | Adam Voss | Surreal Events | [Hello Metaverse! With Surreal CMO Adam Voss](https://futr.tv/thefeed/2021/10/17/hello-metaverse-with-surreal-cmo-adam-voss-59) | Operator | Future |
| 2021-07-26 | John McGrath | LinkedIn | [Building Your Personal Brand With LinkedIn's John McGrath](https://futr.tv/thefeed/2021/7/25/51-building-your-personal-brand-with-linkedins-john-mcgrath) | Operator | Practical |
| 2021-01-04 | Josh Rush | Surreal Events | [Building Epic Events in Surreal, with Surreal Events CEO, Josh Rush](https://futr.tv/thefeed/2021/1/4/27-building-epic-events-in-surreal-with-surreal-events-ceo-josh-rush) | Founder | Business |
| 2020-08-20 | Sean Longworth | HotMic | [Sports and Pandemic Pivots with HotMic CEO Sean Longworth](https://futr.tv/thefeed/2020/8/19/20-sports-and-pandemic-pivots-with-hotmic-ceo-sean-longworth) | Founder | Business |
| 2020-08-05 | Adam Voss | — | [eMERGE Update with Adam Voss](https://futr.tv/thefeed/2020/8/4/18-emerge-update-with-adam-voss) | Operator | Practical |
| 2020-07-20 | Ravi Patel | Wonder Woman 1984 | [What It Means To Be Indian In America With Actor Ravi Patel](https://futr.tv/thefeed/2020/7/20/podcast-17-what-it-means-to-be-indian-in-america-with-actor-ravi-patel) | Author | Human |
| 2020-03-18 | Adam Voss | Surreal Events | [Out of an abundance of caution, With Adam Voss From Surreal Events - Part 2](https://futr.tv/thefeed/2020/3/17/jzsrr669arcung6s9iin3t9w4pqw45) | Operator | Practical |
| 2020-03-16 | Adam Voss | Surreal Events | [Out of an abundance of caution, With Adam Voss From Surreal Events - Part 1](https://futr.tv/thefeed/2020/3/16/futrtech-video-podcast-1-out-of-an-abundance-of-caution-part-1) | Operator | Practical |
| 2019-04-16 | Mike Alden | BYGmusic | [SXSW 2019 Interview with BYGmusic](https://futr.tv/thefeed/2019/4/15/sxsw-2019-interview-with-bygmusic) | Founder | Practical |
| 2019-04-16 | Krish Sharma | BYGmusic | [SXSW 2019 Interview with BYGmusic](https://futr.tv/thefeed/2019/4/15/sxsw-2019-interview-with-bygmusic) | Founder | Practical |

### Social Impact & DEI (17)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2024-09-23 | Ricky Marton | Open Access Ventures | [ESG Magic: Why Open Access Ventures is Investing in ESG!](https://futr.tv/thefeed/2024/9/23/esg-magic-why-open-access-ventures-is-investing-in-esg) | Investor | Business |
| 2024-08-05 | Stacey Yudin | NEP Services | [From Fundraising to Advocacy: NEP Services is Changing the Nonprofit Game](https://futr.tv/thefeed/2024/8/4/from-fundraising-to-advocacy-nep-services-is-changing-the-nonprofit-game) | Operator | Business |
| 2024-07-01 | Manali Yavaktar | Palm | [Follow your passion: Manali Yavaktar's journey from AI to sustainability](https://futr.tv/thefeed/2024/7/1/follow-your-passion-manali-yavaktars-journey-from-ai-to-sustainability) | Founder | Human |
| 2024-01-08 | Ricky Marton | Koru | [Unraveling ESG: What Every Company Needs to Know!](https://futr.tv/thefeed/2024/1/8/unraveling-esg-what-every-company-needs-to-know) | Investor | Practical |
| 2023-10-09 | Grace Yao | PerScholas | [Per Scholas: Transforming Lives Through Free Tech Training and Holistic Support](https://futr.tv/thefeed/2023/10/9/per-scholas-transforming-lives-through-free-tech-training-and-holistic-support) | Operator | Business |
| 2023-10-09 | Daniel Ponciano | PerScholas | [Per Scholas: Transforming Lives Through Free Tech Training and Holistic Support](https://futr.tv/thefeed/2023/10/9/per-scholas-transforming-lives-through-free-tech-training-and-holistic-support) | Operator | Business |
| 2023-07-31 | Loren Williams | PCs for People | [PCs for People - Solving the E-waste Problem and Getting People Connected](https://futr.tv/thefeed/2023/7/31/pcs-for-people-solving-the-e-waste-problem-and-getting-people-connected) | Operator | Business |
| 2022-06-06 | Corinne Weible | PEAT | [Talking Accessibility with PEAT The Partnership on Employment & Accessible Technology](https://futr.tv/thefeed/2022/6/6/talking-accessibility-with-peat-the-partnership-on-employment-amp-accessible-technology-82) | Operator | Business |
| 2022-06-06 | Bill Curtis-Davidson | PEAT | [Talking Accessibility with PEAT The Partnership on Employment & Accessible Technology](https://futr.tv/thefeed/2022/6/6/talking-accessibility-with-peat-the-partnership-on-employment-amp-accessible-technology-82) | Operator | Business |
| 2022-03-07 | Nancy Wang | AWIT | [Advancing Women in Tech with Nancy Wang](https://futr.tv/thefeed/2022/3/7/advancing-women-in-tech-with-nancy-wang-70) | Founder | Business |
| 2021-09-27 | Tim Frick | Mighty Bytes | [Doing the Right Thing - B-Corps With Tim Frick](https://futr.tv/thefeed/2021/9/25/doing-the-right-thing-b-corps-with-tim-frick-55) | Founder | Business |
| 2021-08-30 | Mythili Sankaran | Neythri | [Building Community With Neythri](https://futr.tv/thefeed/2021/8/29/building-community-with-neythri-52) | Operator | Business |
| 2021-06-07 | Celia Daniels | — | [Being Trans, with Celia Daniels](https://futr.tv/thefeed/2021/6/7/45-being-trans-with-celia-daniels) | Author | Human |
| 2021-05-10 | Sejal Thakkar | — | [Diversity, Equity Inclusion, We Talk With Sejal Thakkar About the Basecamp Walkout](https://futr.tv/thefeed/2021/5/10/42-diversity-equity-inclusion-we-talk-with-sejal-thakkar-about-the-basecamp-walkout) | Author | Business |
| 2021-03-29 | Dr Coleen Tartow | Starburst Data | [Talking About Women in Tech - Diversity and Data with Dr Coleen Tartow of Starburst Data](https://futr.tv/thefeed/2021/3/29/37-celebrating-women-in-tech-diversity-and-data-with-dr-coleen-tartow-of-starburst-data) | CTO | Business |
| 2020-06-25 | Sandee Kastrul | i.c.stars | [20 Years of Matter, Talking About Race With i.c.stars Founder Sandee Kastrul - Part 2](https://futr.tv/thefeed/2020/6/24/83ww7b8dpfzfhujdgr7uunvlrxrzxe) | Founder | Business |
| 2020-06-23 | Sandee Kastrul | i.c.stars | [20 Years of Matter, Talking About Race With i.c.stars Founder Sandee Kastrul - Part 1](https://futr.tv/thefeed/2020/6/22/podcast-15-20-years-of-matter-talking-about-race-with-sandee-kastrul) | Founder | Business |

### Enterprise SaaS (17)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2024-08-26 | Dr. Antonis Papatsaras | Hootsuite | [Redefining Social Media Success: Dr. Antonis Papatsaras Shares Hootsuite's Vision!](https://futr.tv/thefeed/2024/8/25/redefining-social-media-success-dr-antonis-papatsaras-shares-hootsuites-vision) | CTO | Business |
| 2024-07-08 | Vitaly Golomb | SofieLabs | [Revolutionizing Sales Pipelines with AI: An Interview with Vitaly Golomb](https://futr.tv/thefeed/2024/7/8/revolutionizing-sales-pipelines-with-ai-an-interview-with-vitaly-golomb) | Founder | Practical |
| 2024-06-03 | Kyle Roof | IMG | [The New Rules of SEO: Succeeding in an AI-Driven World](https://futr.tv/thefeed/2024/6/3/the-new-rules-of-seo-succeeding-in-an-ai-driven-world) | Founder | Practical |
| 2023-09-18 | Pat McNallan | LaunchGTM | [Sales as a Service: Transforming Your Channel Program with LaunchGTM](https://futr.tv/thefeed/2023/9/18/sales-as-a-service-transforming-your-channel-program-with-launchgtm) | Founder | Practical |
| 2023-09-18 | Craig Heile | LaunchGTM | [Sales as a Service: Transforming Your Channel Program with LaunchGTM](https://futr.tv/thefeed/2023/9/18/sales-as-a-service-transforming-your-channel-program-with-launchgtm) | Founder | Practical |
| 2023-06-19 | Josh Buxbaum | WebPurify | [Keeping Users Safe from The Dark Side of the Internet - Winning with WebPurify](https://futr.tv/thefeed/2023/6/17/keeping-users-safe-from-the-dark-side-of-the-internet-winning-with-webpurify) | Founder | Practical |
| 2023-04-24 | Dave Charest | Constant Contact | [Helping The Small Stand Tall, Constant Contact Marketing For The Small Business Market](https://futr.tv/thefeed/2023/4/24/helping-the-small-stand-tall-constant-contact-marketing-for-the-small-business-market) | Operator | Practical |
| 2023-02-27 | Stan Lequin | Insight | [Insight's Transformation: The Future of Technology Solutions in 2023](https://futr.tv/thefeed/2023/2/26/insights-transformation-the-future-of-technology-solutions-in-2023-113) | Operator | Business |
| 2023-02-13 | Kevin Dominik Korte | Univention | [The Open Source Advantage - Univention on Building a Company Around Open Source](https://futr.tv/thefeed/2023/2/12/the-open-source-advantage-univention-on-building-a-company-around-open-source-111) | Operator | Business |
| 2023-01-02 | Kyle Roof | IMG | [How Kyle Roof Reached #1 on Google With SEO](https://futr.tv/thefeed/2022/12/31/how-kyle-roof-reached-1-on-google-for-seo-105) | Founder | Practical |
| 2022-08-08 | Pete Ellis | RedBox | [This Call May Be Monitored - With Pete Ellis From RedBox](https://futr.tv/thefeed/2022/8/7/this-call-may-be-monitored-with-pete-ellis-form-redbox-90) | Operator | Practical |
| 2022-06-20 | David Rush | SmallWorld | [It's a SmallWorld After All - Talking with SmallWorld CEO David Rush](https://futr.tv/thefeed/2022/6/20/its-a-smallworld-after-all-talking-with-smallworld-ceo-david-rush-84) | Founder | Business |
| 2022-05-31 | Dave Czeszewski | Perdoceo | [FUTR Showcase with Motorola Mobility CISO, Richard Rushing and Perdoceo CIO, Dave Czeszewski Panel](https://futr.tv/thefeed/2022/5/31/futr-showcase-with-motorola-mobility-ciso-richard-rushing-and-perdoceo-cio-dave-czeszewski-panel) | CTO | Business |
| 2022-04-04 | Julian Krenge | ParcelLab | [Solve the Supply Chain Disaster with ParcelLab - Interview with Founder and CTO Julian Krenge](https://futr.tv/thefeed/2022/4/2/solve-the-supply-chain-disaster-with-parcel-lab-interview-with-founder-and-cto-julian-krenge-74) | CTO | Practical |
| 2021-04-19 | Prince Kohli | Automation Anywhere | [Here Come The Robots - Talking RPA with Automation Anywhere's Prince Kohli](https://futr.tv/thefeed/2021/4/19/39-here-come-the-robots-talking-rpa-with-automation-anywheres-prince-kohli) | CTO | Practical |
| 2020-04-17 | Dave Czeszewski | Perdoceo | [The CIO perspective with Dave Czeszewski - Part 2](https://futr.tv/thefeed/2020/4/17/podcast-6-the-cio-perspective-with-dave-czeszewski-part-2) | CTO | Business |
| 2020-04-16 | Dave Czeszewski | Perdoceo | [The CIO perspective with Dave Czeszewski - Part 1](https://futr.tv/thefeed/2020/4/16/podcast-6-the-cio-perspective-with-dave-czeszewski-part-1) | CTO | Business |

### Startups, VC & Business (16)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2024-04-29 | Kaitlyn Doyle | TechNexus | [Inside a Unique Chicago VC Firm: TechNexus' Bespoke Approach](https://futr.tv/thefeed/2024/4/29/inside-a-unique-chicago-vc-firm-technexus-bespoke-approach) | Investor | Business |
| 2024-03-25 | Fisayo Oluwadiya | Resactly | [Failure is not an Option: Inside the early days of Resactly with Fisayo Oluwadiya](https://futr.tv/thefeed/2024/3/25/failure-is-not-an-option-inside-the-early-days-of-resactly-with-fisayo-oluwadiya) | Founder | Human |
| 2024-03-18 | Mark Atkeson | — | [Risky Business: An American Entrepreneur's Journey Through China's Economic Evolution](https://futr.tv/thefeed/2024/3/18/risky-business-an-american-entrepreneurs-journey-through-chinas-economic-evolution) | Founder | Human |
| 2023-05-30 | Drew Spaventa | Spaventa Group | [Cracking the Code of Venture Funding: An Exclusive Interview with Drew Spaventa](https://futr.tv/thefeed/2023/5/29/ry60cqpuifj2q0k1hluzxzlq60iije) | Investor | Business |
| 2023-03-13 | Molly Dill | Gener8tor | [Revving Up Your Business: How Accelerators Fuel Startups - Inside the world of VC Accelerators](https://futr.tv/thefeed/2023/3/13/revving-up-your-business-how-accelerators-fuel-startups-inside-the-world-of-vc-accelerators) | Operator | Practical |
| 2022-10-07 | Sophie Theen | Soul of a Startup | [The Soul of a Startup with Sophie Theen](https://futr.tv/thefeed/2022/10/7/the-soul-of-a-startup-with-sophie-theen-97) | Author | Business |
| 2022-08-02 | Landon Campbell | Drive Capital | [In Their 20s with Landon Campbell](https://futr.tv/thefeed/2022/7/31/in-their-20s-with-landon-campbell-89) | Investor | Human |
| 2021-04-12 | Saqib Awan | Lightspeed Venture Partners | [The Business of Venture Capital with Lightspeed Venture Partners' Saqib Awan](https://futr.tv/thefeed/2021/4/11/38-the-business-of-venture-capital-with-light-speed-venture-partners-saqib-awan) | Investor | Business |
| 2020-06-17 | Andrew Dougherty | — | [What's Going On With China? An Interview With Economist Andrew Dougherty - Part 2](https://futr.tv/thefeed/2020/6/17/podcast-14-whats-going-on-with-china-an-interview-with-economist-andrew-dougherty-part-2) | Author | Business |
| 2020-06-16 | Andrew Dougherty | — | [What's Going On With China? An Interview With Economist Andrew Dougherty - Part 1](https://futr.tv/thefeed/2020/6/15/poodcast-14-whats-going-on-with-china-an-interview-with-economist-andrew-dougherty) | Author | Business |
| 2020-05-28 | John Thompson | Lightspeed Venture Partners | [Talking Venture Capital with John Thompson and Mukesh Singh](https://futr.tv/thefeed/2020/5/27/podcast-12-talking-venture-capital-with-john-thompson-and-mukesh-singh) | Investor | Business |
| 2020-05-11 | Danial Hultin | — | [Surviving COVID19 with Danial Hultin](https://futr.tv/thefeed/2020/5/11/podcast-11-surviving-covid19-with-danial-hultin) | Operator | Practical |
| 2020-05-07 | Mark Janus | Janus Travel | [Saving a Small Business During a Pandemic With Mark Janus](https://futr.tv/thefeed/2020/5/7/podcast-10-saving-a-small-business-during-a-pandemic-with-mark-janus) | Founder | Practical |
| 2020-04-28 | Phil Johanet | — | [The Sales Machine with Phil Johanet - Part 2](https://futr.tv/thefeed/2020/4/27/podcast-7-the-sales-machine-with-phil-johanet-part-2) | Operator | Business |
| 2020-04-27 | Phil Johanet | — | [The Sales Machine with Phil Johanet - Part 1](https://futr.tv/thefeed/2020/4/26/podcast-7-the-sales-machine-with-phil-johanet) | Operator | Business |
| 2019-03-23 | Halak Mehta-Shrivastava | Access Partnership | [SXSW 2019: A Talk With Access Partnership](https://futr.tv/thefeed/2019/3/23/sxsw-2019-a-talk-with-access-partnership) | Operator | Business |

### Personal Dev & Wellness (16)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2024-01-29 | Tony Martignetti | The Virtual Campfire Podcast | [Avoiding Burnout and Finding Purpose: A Deep Dive with Tony Martignetti](https://futr.tv/thefeed/2024/1/29/avoiding-burnout-and-finding-purpose-a-deep-dive-with-tony-martignetti) | Author | Practical |
| 2023-04-17 | Jenny Arrington | Rebel Human | [Free Your Mind, Body, and Spirit - How to Become a Rebel Human](https://futr.tv/thefeed/2023/4/17/free-your-mind-body-and-spirit-how-to-become-a-rebel-human) | Founder | Future |
| 2023-03-27 | Dr. Tait Medina | Rebel Human | [Unlocking the Secret to a Happier Life: An Interview with Rebel Human Co-founder Dr. Tait Medina](https://futr.tv/thefeed/2023/3/27/unlocking-the-secret-to-a-happier-life-an-interview-with-rebel-human-co-founder-dr-tait-medina) | Founder | Future |
| 2022-05-09 | Vipin Goyal | Upbuild | [2 monks and a banker - A chat with Upbuild](https://futr.tv/thefeed/2022/5/8/2-monks-and-a-banker-a-chat-with-upbuild-79) | Founder | Human |
| 2022-05-09 | Rasanath Das | Upbuild | [2 monks and a banker - A chat with Upbuild](https://futr.tv/thefeed/2022/5/8/2-monks-and-a-banker-a-chat-with-upbuild-79) | Founder | Human |
| 2021-09-20 | Ellen Barry | — | [Growing Your Network With Ellen Barry](https://futr.tv/thefeed/2021/9/20/growing-your-network-with-ellen-barry-54) | Author | Practical |
| 2021-04-26 | Rajesh "Sheik" Kapoor | NetApp | [Life Lessons from the Sheik](https://futr.tv/thefeed/2021/4/26/40-life-lessons-from-the-sheik) | Operator | Human |
| 2021-01-25 | Nick Tasler | — | [Reinventing Yourself During a Pandemic with Nick Tasler](https://futr.tv/thefeed/2021/1/24/30-reinventing-yourself-during-a-pandemic-with-nick-tasler) | Author | Practical |
| 2020-05-05 | Nick Tasler | — | [Organizational Psychology with Nick Tasler - Part 2](https://futr.tv/thefeed/2020/5/5/podcast-9-organizational-psychology-with-nick-tasler-part-2) | Author | Practical |
| 2020-05-04 | Nick Tasler | — | [Organizational Psychology with Nick Tasler - Part 1](https://futr.tv/thefeed/2020/5/3/podcast-9-organizational-psychology-with-nick-tasler-part-1) | Author | Practical |
| 2020-04-15 | Shawn O'Grady | Insight | [Leadership with Shawn O'Grady - Part 2](https://futr.tv/thefeed/2020/4/14/podcast-5-leadership-with-shawn-ogrady-part-2) | Operator | Business |
| 2020-04-13 | Shawn O'Grady | Insight | [Leadership with Shawn O'Grady - Part 1](https://futr.tv/thefeed/2020/4/13/podcast-5-leadership-with-shawn-ogrady) | Operator | Business |
| 2020-04-01 | Miguel Torres | — | [Transformation with Miguel Torres - Part 2](https://futr.tv/thefeed/2020/3/31/podcast-3-transformation-with-miguel-torres-part-2) | Operator | Business |
| 2020-03-31 | Miguel Torres | — | [Transformation with Miguel Torres - Part-1](https://futr.tv/thefeed/2020/3/30/podcast-3-transformation-with-miguel-torres) | Operator | Business |
| 2020-03-26 | Dr. Rahul Sharma | Funkadesi | [Mental Health in Tech - Part 2](https://futr.tv/thefeed/2020/3/25/podcast-2-mental-health-in-tech-part-2) | Author | Practical |
| 2020-03-25 | Dr. Rahul Sharma | Funkadesi | [Mental Health in Tech With Dr. Rahul Sharma - Part 1](https://futr.tv/thefeed/2020/3/24/podcast-2-mental-health-in-tech-with-dr-rahul-sharma-part-1) | Author | Practical |

### AI/ML (12)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2026-07-02 | Anthony Vinci | Vico | [A Former Spy Chief on How AI Really Manipulates You](https://futr.tv/thefeed/2026/7/2/a-former-spy-chief-on-how-ai-really-manipulates-you) | Author | Contrarian |
| 2026-04-13 | Greg Whalen | Prove AI | [Your AI Looks 80% Done. It's Actually 20%. Here's Why!](https://futr.tv/thefeed/2026/4/13/your-ai-looks-80-done-its-actually-20-heres-why) | CTO | Contrarian |
| 2025-09-19 | Balint Pasztor | Diffuse Drive | [$124B Data Problem: How Synthetic Data Accelerates AI](https://futr.tv/thefeed/2025/9/19/124b-data-problem-how-synthetic-data-accelerates-ai) | Founder | Practical |
| 2025-09-16 | Dr. Marcus Weller | Deep Invent | [AI Patents Itself: The Invention Machine Is Here](https://futr.tv/thefeed/2025/9/16/ai-patents-itself-the-invention-machine-is-here) | Founder | Future |
| 2024-10-14 | Mark Kurtz | Neural Magic | [AI Reality Check: What's Really Happening Behind the Hype?](https://futr.tv/thefeed/2024/10/14/ai-reality-check-whats-really-happening-behind-the-hype) | CTO | Contrarian |
| 2024-04-23 | Chuck Rinker | PRSONAS | [Enhancing Patient Experiences with Empathetic, Animated, AI-Powered Avatars](https://futr.tv/thefeed/2024/4/23/enhancing-patient-experiences-with-empathetic-animated-ai-powered-avatars) | Founder | Practical |
| 2023-10-30 | Suman Kanuganti | Personal AI | [Unlocking the Power of Personal AI: Redefining the Nature of Identity](https://futr.tv/thefeed/2023/10/30/unlocking-the-power-of-personal-ai-redefining-the-nature-of-identity) | Founder | Future |
| 2022-10-03 | Lior Balan | Run:AI | [HPC + AI Wall Street 2022 Update](https://futr.tv/thefeed/2022/10/3/hpc-ai-wall-street-2022-update-96) | CTO | Practical |
| 2022-05-16 | Richard Carriere | Cyberlink | [Facial Recognition is Everywhere, Doing it Ethically with Cyberlink's FaceMe - #80](https://futr.tv/thefeed/2022/5/15/facial-recognition-is-everywhere-doing-it-ethically-with-cyberlinks-faceme-80) | Operator | Contrarian |
| 2022-04-20 | Mike Betzer | Hypergiant | [Solving the Big Problems with AI and Hypergiant](https://futr.tv/thefeed/2022/4/17/solving-the-big-problems-with-ai-and-hypergiant-76) | Founder | Future |
| 2021-11-01 | Paige Lord | Microsoft | [Is AI the Future or the end of everything - TikTok AI Ethics Influencer Paige Lord](https://futr.tv/thefeed/2021/10/29/is-ai-the-future-or-the-end-of-everything-tiktok-ai-ethics-influencer-paige-lord-61) | Author | Contrarian |
| 2021-07-12 | Muddu Sudhakar | Aisera | [Conversational AI Saves The Day with Aisera CEO Muddu Sudhakar](https://futr.tv/thefeed/2021/7/12/49-conversational-ai-saves-the-day-with-aisera-ceo-muddu-sudhakar) | Founder | Practical |

### Healthtech/Biotech (9)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2024-09-30 | Dr. Meg Richards | Panalgo | [Saving Lives with Science: The Future of Maternal and Infant Health](https://futr.tv/thefeed/2024/9/30/saving-lives-with-science-the-future-of-maternal-and-infant-health) | Author | Future |
| 2024-08-12 | Dr. Peter Bonutti | — | [Breaking Barriers in Medicine: Dr. Peter Bonutti on Blood-Brain Breakthroughs](https://futr.tv/thefeed/2024/8/12/breaking-barriers-in-medicine-dr-peter-bonutti-on-blood-brain-breakthroughs) | Author | Future |
| 2024-05-06 | Dr. Craig Joseph | Nordic Consulting Partners | [Fixing the Broken Healthcare System: How Design Principles Can Help](https://futr.tv/thefeed/2024/5/6/fixing-the-broken-healthcare-system-how-design-principles-can-help) | Author | Contrarian |
| 2024-01-15 | Dr. Carolyn Ward | Particle Health | [Revolutionizing Healthcare: Unlocking the Power of Data Access with Dr. Carolyn Ward](https://futr.tv/thefeed/2024/1/14/revolutionizing-healthcare-unlocking-the-power-of-data-access-with-dr-carolyn-ward) | Author | Practical |
| 2023-10-23 | Luca Parisi | Citeline | [Revolutionizing Drug Development: How AI and Data Are Changing the Game](https://futr.tv/thefeed/2023/10/22/revolutionizing-drug-development-how-ai-and-data-are-changing-the-game) | Operator | Practical |
| 2023-09-11 | BE | Alinker | [Meet BE: The Creator of the Alinker, a Unique Mobility Device with Style](https://futr.tv/thefeed/2023/9/11/meet-be-the-creator-of-the-alinker-a-unique-mobility-device-with-style) | Founder | Human |
| 2023-06-05 | Ram Vempati | Wysa | [Solving the Mental Health Crisis: How AI and Wysa are Revolutionizing Access to Care](https://futr.tv/thefeed/2023/6/5/solving-the-mental-health-crisis-how-ai-and-wysa-are-revolutionizing-access-to-care) | Founder | Practical |
| 2022-11-07 | Satish Srinivasan | DiRx | [Making Medicine Affordable with Satish Srinivasan of DiRx](https://futr.tv/thefeed/2022/11/7/making-medicine-affordable-with-satish-srinivasan-of-dirx-101) | Founder | Practical |
| 2022-08-29 | Kira Dineen | DNA Today | [The Calico Cat Conundrum - Genetics with DNA Today's Kira Dineen](https://futr.tv/thefeed/2022/8/29/the-calico-cat-conundrum-genetics-with-dna-todays-kira-dineen-93) | Author | Practical |

### Hardware/IoT (8)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2024-05-13 | Daniel Reed | MxD | [The Power of Public-Private Partnerships in Revitalizing U.S. Manufacturing](https://futr.tv/thefeed/2024/5/13/the-power-of-public-private-partnerships-in-revitalizing-us-manufacturing) | Operator | Business |
| 2023-07-10 | Daniel Daoura | Pebblebee | [From Building Batteries in Bomb Shelters to Tracking Your Stuff, The amazing Pebblebee Journey!](https://futr.tv/thefeed/2023/7/10/from-building-batteries-in-bomb-shelters-to-tracking-your-stuff-the-amazing-pebblebee-journey) | Founder | Human |
| 2023-03-06 | Scott Ford | Pepper | [Behind the Scenes of Home Automation: How Pepper Makes IoT Possible](https://futr.tv/thefeed/2023/3/6/behind-the-scenes-of-home-automation-how-pepper-makes-iot-possible) | Founder | Practical |
| 2023-02-20 | Ross Blum | Skyline Robotics | [Look up in the sky, it's a bird, it's a plane, it's... Skyline Robotics!](https://futr.tv/thefeed/2023/2/19/look-up-in-the-sky-its-a-bird-its-a-plane-its-skyline-robotics) | Founder | Practical |
| 2022-08-22 | Rory San Miguel | Propeller | [Eye in the Sky Drone - Mapping with Propeller](https://futr.tv/thefeed/2022/8/21/eye-in-the-sky-drone-mapping-with-propeller-92) | Founder | Practical |
| 2021-10-25 | Pradeep Sindhu | Fungible | [Composing the Future with Fungible Co-Founder Pradeep Sindhu](https://futr.tv/thefeed/2021/10/25/composing-the-future-with-fungible-co-founder-pradeep-sindhu-60) | Founder | Future |
| 2021-06-14 | Shekar Ayyar | AdMY | [The Future is 5G with AdMY's CEO Shekar Ayyar](https://futr.tv/thefeed/2021/6/14/46-the-future-is-5g-with-admys-ceo-shekar-ayyar) | Founder | Future |
| 2021-06-01 | Charles Fan | MemVerge | [Reinventing Computing with MemVerge's CEO Charles Fan](https://futr.tv/thefeed/2021/6/1/44-reinventing-computing-with-memverges-ceo-charles-fan) | Founder | Future |

### Mobility/EV (7)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2026-02-17 | Tim Seward | Onyx Motors | [Moped Gangs Are Back - And They're Electric!](https://futr.tv/thefeed/2026/2/16/moped-gangs-are-back-and-theyre-electric) | Founder | Practical |
| 2025-09-29 | Kevin Damoa | Glīd | [SpaceX Vet's Transformer Vehicle: Road to Rail Instantly](https://futr.tv/thefeed/2025/9/29/spacex-vets-transformer-vehicle-road-to-rail-instantly) | Founder | Future |
| 2025-03-24 | Colin Godby | Dust Moto | [Dirt, Fun, and High-Tech: Dust Moto's Game-Changing Electric Dirtbikes](https://futr.tv/thefeed/2025/3/24/dirt-fun-and-high-tech-dust-motos-game-changing-electric-bikes) | Founder | Practical |
| 2025-03-17 | Nitkita Bridan | Oilstainlabs | [The Awe and Excitement of Oilstainlab's New HF11 Supercar Brings the Joy Back to Driving](https://futr.tv/thefeed/2025/3/17/the-awe-and-excitement-of-oilstainlabs-new-hf11-supercar-brings-the-joy-back-to-driving) | Founder | Future |
| 2025-03-03 | David Tyler | Artemis Technologies | [Electric Hydrofoiling into the Future: Transforming Water Travel with David Tyler!](https://futr.tv/thefeed/2025/3/1/electric-hydrofoiling-into-the-future-transforming-water-travel-with-david-tyler) | Founder | Future |
| 2023-08-21 | Alex Rawitz | Dimo | [Creating a New Era of Car Customization: The App Store for Your Vehicle](https://futr.tv/thefeed/2023/8/21/creating-a-new-era-of-car-customization-the-app-store-for-your-vehicle) | Founder | Future |
| 2023-04-10 | Jez Williman | D-Fly | [Ear To Ear Smiles with The Future of Personal Electric Vehicles - The Dragonfly](https://futr.tv/thefeed/2023/4/9/8vklaqgbl5l4acgaeewtcatrumqpmv) | Founder | Practical |

### Climate/Energy (7)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2024-10-21 | Angelo Campus | Boxpower | [Unlocking the Power of the Sun: BoxPower's Modular Solar Revolution!](https://futr.tv/thefeed/2024/10/21/unlocking-the-power-of-the-sun-boxpowers-modular-solar-revolution) | Founder | Practical |
| 2024-09-16 | Vinnie Campos | Haven Energy | [Solar Simplified: How Haven Energy Makes Going Green a Breeze!](https://futr.tv/thefeed/2024/9/13/solar-simplified-how-haven-energy-makes-going-green-a-breeze) | Founder | Practical |
| 2024-09-09 | Francis Wang | Nanograf | [Battery Breakthroughs: Nanograf's Silicon Anode Revolution!](https://futr.tv/thefeed/2024/9/9/battery-breakthroughs-nanografs-silicon-anode-revolution) | Founder | Practical |
| 2024-06-24 | Matt Krayton | Mach2 | [Reviving Hydrogen: A Conversation with Matt Krayton on the Future of Clean Energy](https://futr.tv/thefeed/2024/6/24/reviving-hydrogen-a-conversation-with-matt-krayton-on-the-future-of-clean-energy) | Founder | Future |
| 2023-11-06 | Chris Larsen | Dynapower | [The Future of Hydrogen: Storing Power at a Massive Scale](https://futr.tv/thefeed/2023/11/6/the-future-of-hydrogen-storing-power-at-a-massive-scale) | Operator | Future |
| 2023-09-05 | Herman Artinian | Upwing Energy | [The Environmental Impact of Fossil Fuel Extraction: Upwing Energy's Sustainable Solution](https://futr.tv/thefeed/2023/9/3/the-environmental-impact-of-fossil-fuel-extraction-upwing-energys-sustainable-solution) | Founder | Practical |
| 2023-08-14 | Andrew Song | Make Sunsets | [Innovative Geoengineering: How Reflective Clouds Could Buy Time Against Global Warming](https://futr.tv/thefeed/2023/8/14/innovative-geoengineering-how-reflective-clouds-could-buy-time-against-global-warming) | Founder | Contrarian |

### Workforce/Future of Work (6)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2024-04-08 | Andrew Bartlow | People Leader Accelerator | [The State of Employment in 2024: Insights and Strategies for Success from HR Guru Andrew Bartlow](https://futr.tv/thefeed/2024/4/8/the-state-of-employment-in-2024-insights-and-strategies-for-success-from-hr-guru-andrew-bartlow) | Author | Business |
| 2024-03-11 | Lindsay Murphy | Secoda | [Women Navigating a Career Path in Data & Tech: Insights from Lindsay Murphy](https://futr.tv/thefeed/2024/3/11/women-navigating-a-career-path-in-data-amp-tech-insights-from-lindsey-murphy) | CTO | Human |
| 2023-01-16 | Alex Atwood | GravyWork | [The Gig Economy Gets An Upgrade - 💰 With Alex Atwood of GravyWork](https://futr.tv/thefeed/2023/1/16/the-gig-economy-gets-an-upgrade-with-alex-atwood-of-gravywork-107) | Founder | Business |
| 2022-10-24 | Rich Mendis | Hirelogic | [The Happy Hire - Rich Mendis of Hirelogic](https://futr.tv/thefeed/2022/10/24/get-a-job-rich-mendis-of-hirelogic-99) | Operator | Practical |
| 2022-08-15 | Giancarlo Hirsch | Glocomms | [The Great Resignation- Fact or Fiction with Giancarlo Hirsch of Glocomms](https://futr.tv/thefeed/2022/8/13/algexu5qvv9zvusja9z3yv60orjaun) | Operator | Contrarian |
| 2021-07-19 | Kai Pederson | — | [The Future Is In Their Hands - Here Come The Millenials](https://futr.tv/thefeed/2021/7/19/50-the-future-is-in-their-hands-here-come-the-millenials) | Author | Future |

### Consumer/Retail (5)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2025-06-09 | Jake Nichol | Threadless | [The Art of Business and the Power of Community: 25 Years of Threadless With Founder Jake Nickell](https://futr.tv/thefeed/2025/6/9/the-art-of-business-and-the-power-of-community-25-years-of-threadless) | Founder | Human |
| 2023-08-28 | Sri Solur | Kenmore | [Innovation and Resurgence: CEO Sri Solur's Journey to Reinvent Kenmore's Brand](https://futr.tv/thefeed/2023/8/28/innovation-and-resurgence-ceo-sri-solurs-journey-to-reinvent-kenmores-brand) | Founder | Business |
| 2023-08-07 | Randy Bapst | AIBuy | [Revolutionizing Shopping: How In-Content Buying is Changing the Game](https://futr.tv/thefeed/2023/8/7/revolutionizing-shopping-how-in-content-buying-is-changing-the-game) | Founder | Practical |
| 2023-08-07 | Dalaney Thompson | AIBuy | [Revolutionizing Shopping: How In-Content Buying is Changing the Game](https://futr.tv/thefeed/2023/8/7/revolutionizing-shopping-how-in-content-buying-is-changing-the-game) | Operator | Practical |
| 2022-09-26 | Suja Chandrasekaran | Walmart | [Executive Perspective with Suja Chandrasekaran](https://futr.tv/thefeed/2022/9/26/executive-perspective-with-suja-chandrasekaran-95) | CTO | Business |

### Cannabis (3)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2023-09-25 | Daniel Huerter | PureSpectrumCBD | [Breaking New Ground: How PureSpectrumCBD Partnered with Major League Baseball](https://futr.tv/thefeed/2023/9/25/breaking-new-ground-how-purespectrumcbd-partnered-with-major-league-baseball) | Founder | Business |
| 2022-12-19 | Vanessa Gabriel | Drop Delivery | [The Modern Entrepreneur - Growing a Cannatech business with Vanessa Gabriel of Drop Delivery](https://futr.tv/thefeed/2022/12/17/the-modern-entrepreneur-growing-a-cannatech-business-with-vanessa-gabriel-of-drop-delivery-104) | Founder | Business |
| 2020-10-28 | Zachary Zises | Dispensary 33 | [How to Succeed with Weed - Interview with Cannabis Entrepreneur Zachary Zises](https://futr.tv/thefeed/2020/10/28/26-how-to-succeed-with-weed-interview-with-zachary-zises) | Founder | Business |

### Sports (2)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2025-04-21 | Evan Floersch | Texas Ranchers | [Major League Pickleball: Behind the Scenes with Texas Ranchers Owner Evan Floersch](https://futr.tv/thefeed/2025/4/21/major-league-pickleball-behind-the-scenes-with-texas-ranchers-owner-evan-floersch) | Operator | Business |
| 2024-10-07 | Josh Brown | DropShot | [Pickleball Passion and Purpose: High-Tech Pickleball Scoring with Dropshot](https://futr.tv/thefeed/2024/10/7/pickleball-passion-and-purpose-high-tech-pickleball-scoring-with-dropshot) | Founder | Practical |

### Gaming (2)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2025-02-24 | Cerisse Velasco | Zygna | [Zynga Has Our Attention](https://futr.tv/thefeed/2025/2/23/zynga-has-our-attention) | Operator | Business |
| 2023-05-15 | Beau Button | Atlas Reality | [The Atlas Tycoon, Building Location Based Mobile Games That Pay The Player](https://futr.tv/thefeed/2023/5/15/the-atlas-tycoon-building-location-based-mobile-games-that-pay-the-player) | Founder | Future |

### Fintech (2)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2022-07-25 | Earl Melivo | WorldRemit | [The Global Remittance Economy With WorldRemit's Earl Melivo](https://futr.tv/thefeed/2022/7/24/the-global-remittance-economy-with-worldremits-earl-melivo-88) | Operator | Practical |
| 2021-10-07 | Akash Khanolkar | Octane | [High Octane SaaS with Octane founder Akash Khanolkar](https://futr.tv/thefeed/2021/10/7/high-octane-saas-with-octane-founder-akash-khanolkar-57) | Founder | Business |

### Web3/Crypto (2)

| Date | Guest | Company/Title | Episode | Guest Type | Angle |
|---|---|---|---|---|---|
| 2022-03-21 | Dr. Colleen Tartow | Starburst Data | [Decentralization, Data, and Web3 a conversation with Dr. Colleen Tartow and Annika Lewis](https://futr.tv/thefeed/2022/3/19/decentralization-data-and-web3-a-conversation-with-dr-colleen-tartow-and-annika-lewis-72) | CTO | Future |
| 2022-03-21 | Annika Lewis | Gitcoin | [Decentralization, Data, and Web3 a conversation with Dr. Colleen Tartow and Annika Lewis](https://futr.tv/thefeed/2022/3/19/decentralization-data-and-web3-a-conversation-with-dr-colleen-tartow-and-annika-lewis-72) | Operator | Future |
