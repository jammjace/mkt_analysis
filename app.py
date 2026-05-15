import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="KT vs HV Macro Dashboard",
    layout="wide"
)

st.title("KT vs HV Branch Performance Analysis")
st.caption("Macro environment dashboard for supervisor review")

st.markdown(
    """
    **Objective:** Identify macro-level reasons why Katong (KT) may have lower revenue/volume
    than Holland Village (HV).
    """
)

# KPI cards
col1, col2, col3, col4 = st.columns(4)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Main macro finding", "HV stronger")
    

col2.metric("KT strength", "Affluence", "Private housing + income")
col3.metric("HV strength", "Density", "Elderly + HDB + MRT")

with col4:
    st.metric("Next step", "Micro aspects")


tabs = st.tabs([
    "Overview",
    "Catchment & Footfall",
    "Resident Demographics",
    "Methodology & Direction"
])

with tabs[0]:
    st.subheader("Macro summary")

    summary = pd.DataFrame({
        "Factor": [
            "Official land use",
            "Subzone population",
            "Subzone density",
            "Age profile",
            "Housing type",
            "Income",
            "Ethnicity",
            "Transport",
            "Spillover"
        ],
        "KT": [
            "Residential with commercial",
            "Smaller",
            "Lower",
            "Fewer elderly",
            "Private/landed-heavy",
            "Higher",
            "Chinese-majority",
            "Better parking",
            "More localised"
        ],
        "HV": [
            "Commercial",
            "Larger",
            "Higher",
            "More elderly",
            "HDB-heavy",
            "More mixed",
            "Chinese-majority",
            "Better MRT/bus",
            "Wider adjacent catchment"
        ],
        "Likely implication": [
            "HV stronger for walk-ins",
            "HV larger resident pool",
            "HV stronger nearby density",
            "HV stronger recurring GP demand",
            "KT affordability; HV density",
            "KT stronger ability to pay",
            "Not major differentiator",
            "HV stronger convenience access",
            "HV stronger spillover potential"
        ]
    })

    st.dataframe(summary, use_container_width=True)

    st.info(
        "Working conclusion: HV appears stronger in volume-generation conditions, "
        "while KT appears stronger in spending-power and wellness/service-fit conditions."
    )

with tabs[1]:
    st.subheader("Catchment Size & Footfall Potential")

    st.markdown(
        """
        This section compares whether each branch is located in an environment that naturally supports
        patient flow. It looks at official land use, surrounding anchors, accessibility, resident catchment
        size, density, and adjacent subzone spillover.
        """
    )

    # 1. Official location context
    st.markdown("### 1. Official Location Context")

    official_context = pd.DataFrame({
        "Branch": ["KT Branch", "HV Branch"],
        "Postal Code": ["427650", "278983"],
        "Planning Area": ["Marine Parade", "Queenstown"],
        "Subzone": ["Katong", "Holland Drive"],
        "Draft Master Plan 2025 Land Use": [
            "Residential with commercial at 1st storey",
            "Commercial"
        ],
        "Likely Patient Flow": [
            "Nearby residents, planned visits, neighbourhood demand",
            "Walk-ins, commuters, workers, shoppers, errand-based patients"
        ]
    })

    st.dataframe(official_context, use_container_width=True)

    st.info(
        "Key interpretation: HV is officially located in a commercial setting, which better supports "
        "spontaneous and convenience-driven visits. KT is in a residential-commercial setting, which may "
        "support more planned or resident-based visits."
    )
    

    # 3. Area footfall / Surrounding anchors
    st.markdown("### 2. Surrounding Anchors & Likely Footfall Type")
    st.markdown("Using URA Land Use Map")

    st.image(
        "charts/onemap.png",
        caption="URA Master Plan land-use context around KT and HV",
        use_container_width=True
    )
    st.info("HV branch is inside a very centralised and dense commercial area, " \
    "while the KT branch is along a stretch of commercial stores, where some are residential with commercial at 1st storey (so area possibly not focused on commercial/services).")

    st.markdown("Nearby Landmarks")
    anchors = pd.DataFrame({
        "Category": [
            "Nearby commercial anchors",
            "Food / lifestyle traffic",
            "Hotels / tourist source",
            "Community / resident anchors",
            "Main footfall character"
        ],
        "KT Branch": [
            "Katong Point, Little Farms, nearby shops",
            "Joo Chiat / East Coast Road heritage and food area",
            "Hotels nearby; some tourist patients observed",
            "Joo Chiat CC, nearby residents",
            "Heritage, food, hotel, resident and planned neighbourhood traffic"
        ],
        "HV Branch": [
            "One Holland Village, Holland Road Shopping Centre, Holland Village Market & Food Centre",
            "Holland Village cafes, restaurants, services",
            "Less hotel-driven in immediate area",
            "MRT, market, nearby residential and work/school zones",
            "MRT, lifestyle, commercial, weekday and errand-based traffic"
        ],
        "Likely Implication": [
            "HV has more centralised commercial anchors",
            "Both have lifestyle traffic, but HV is more compact",
            "KT may capture some tourist/short-stay patients",
            "HV may convert daily errands into clinic visits more easily",
            "HV likely has stronger spontaneous footfall conversion"
        ]
    })

    st.dataframe(anchors, use_container_width=True)

    # 3. Accessibility
    st.markdown("### 3. Accessibility")

    accessibility = pd.DataFrame({
        "Access Factor": [
            "Nearest MRT",
            "Bus access",
            "Walk-in convenience",
            "Car access / parking",
            "Overall access implication"
        ],
        "KT Branch": [
            "Marine Parade MRT around 480m away",
            "Nearby bus stops, but less MRT-centred",
            "More likely requires planned visit",
            "Free parking / Katong Point parking / street parking nearby",
            "Better for car-based and planned visits"
        ],
        "HV Branch": [
            "Holland Village MRT around 139m away",
            "Bus stop opposite / near clinic",
            "Easier for MRT users and passers-by",
            "No free parking; paid carparks nearby",
            "Better for public-transport and spontaneous visits"
        ],
        "Favours": [
            "HV",
            "HV",
            "HV",
            "KT",
            "HV for walk-ins; KT for planned visits"
        ]
    })

    st.dataframe(accessibility, use_container_width=True)

    # 4. Resident population and density
    st.markdown("### 4. Resident Population & Density")

    density = pd.DataFrame({
        "Area Level": [
            "Planning Area",
            "Planning Area",
            "Subzone",
            "Subzone"
        ],
        "Branch": [
            "KT Branch",
            "HV Branch",
            "KT Branch",
            "HV Branch"
        ],
        "Area": [
            "Marine Parade",
            "Queenstown",
            "Katong",
            "Holland Drive"
        ],
        "Population": [
            47480,
            101480,
            9550,
            11990
        ],
        "Land Area km²": [
            6.12,
            20.43,
            1.079,
            0.470
        ],
        "Density residents/km²": [
            7758,
            4967,
            8851,
            25475
        ]
    })

    st.dataframe(density, use_container_width=True)

    st.markdown(
        """
        **Interpretation:**
        - At planning-area level, Queenstown has the larger broad resident pool.
        - At subzone level, Holland Drive has a larger immediate resident pool than Katong.
        - Holland Drive is much denser than Katong at subzone level, supporting stronger nearby resident footfall.
        """
    )

    # 5. Adjacent subzone spillover
    st.markdown("### 5. Adjacent Subzone Spillover")
    

    spillover = pd.DataFrame({
        "Branch": ["KT Branch", "HV Branch"],
        "Observed 400m Catchment Pattern": [
            "Mostly within Katong, with small spillover into Marine Parade",
            "Split around Holland Drive / Holland Village area, with many nearby adjacent subzones"
        ],
        "Nearby Adjacent Subzones": [
            "Marine Parade, Frankel, Geylang, Mountbatten",
            "Holland Village, Ghim Moh, Leedon Park, Commonwealth, Tanglin Halt, One North, Ulu Pandan"
        ],
        "Implication": [
            "KT catchment is more localised and resident/neighbourhood-based",
            "HV has stronger spillover potential from multiple neighbourhood profiles"
        ]
    })

    st.markdown(
        """
        Circle is the 400m radius:
        """
    )
    st.dataframe(spillover, use_container_width=True)

    st.image(
        "charts/HV_adjsubzones.png",
        caption="Adjacent subzone check around HV Branch",
        use_container_width=True
    )
    st.image(
        "charts/KT_adjsubzones.png",
        caption="Adjacent subzone check around KT Branch",
        use_container_width=True
    )

    # 6. Footfall conclusion
    st.markdown("### Footfall & Catchment Takeaway")

    st.success(
        "HV appears stronger for volume-generation because it combines commercial land use, MRT proximity, "
        "larger immediate subzone population, much higher subzone density, and stronger spillover from adjacent "
        "areas. KT has useful hotel, heritage, food and resident-based footfall, but its traffic appears more "
        "planned and dispersed rather than spontaneous."
    )


with tabs[2]:
    st.subheader("Resident Demographic Profile")

    st.markdown(
        """
        This section assesses whether the residents around KT and HV match the likely target patients
        for private GP, chronic care, wellness, and TCM services. It uses subzone data for the immediate
        neighbourhood profile and planning area data for broader affordability and income context.
        """
    )

    # -----------------------------
    # 1. Age Profile
    # -----------------------------
    st.markdown("### 1. Age Profile")

    st.markdown(
        """
        Age profile is used to estimate likely healthcare needs. Older residents are more likely to require
        chronic care, medication refills, regular GP follow-ups and health screening.
        """
    )

    st.image(
        "charts/age_profile.png",
        caption="Age Group Counts: Immediate Subzone vs Broader Planning Area",
        use_container_width=True
    )

    age_takeaways = pd.DataFrame({
        "Finding": [
            "HV has a larger elderly and older-adult base",
            "HV has more residents in most adult age groups",
            "KT has relatively more children/teens at subzone level",
            "Planning area comparison also favours HV in absolute age-group counts"
        ],
        "Implication": [
            "Supports stronger recurring GP and chronic-care demand at HV",
            "Supports stronger weekday and repeat healthcare demand",
            "KT may have some family/child-related GP demand",
            "HV has a larger broad patient pool across age groups"
        ]
    })

    st.dataframe(age_takeaways, use_container_width=True)

    st.success(
        "Age profile favours HV for recurring GP volume because HV has a larger elderly and older-adult resident base."
    )

    # -----------------------------
    # 2. Health Profile
    # -----------------------------
    st.markdown("### 2. Health Profile")

    st.markdown(
        """
        Direct disease prevalence data is not available at KT/HV subzone level. Therefore, health demand is
        inferred using local age profile and housing composition, supported by external research on
        cardiometabolic screening patterns in Singapore.
        """
    )

    health_proxy = pd.DataFrame({
        "Evidence used": [
            "Older age is associated with higher chronic disease and screening needs",
            "HV has a larger elderly base than KT",
            "Housing type can be used as a socioeconomic proxy",
            "Higher-SES residents may use private clinics/hospitals for screening"
        ],
        "Relevance to KT/HV": [
            "Age profile can be used as a proxy for recurring GP demand",
            "HV may have stronger demand for chronic care, health checks and repeat GP visits",
            "Housing composition helps interpret healthcare access and private-care tendency",
            "KT's private-housing-heavy profile may support private GP and wellness/screening demand"
        ]
    })

    st.dataframe(health_proxy, use_container_width=True)

    st.info(
        "Health profile takeaway: HV may have stronger recurring GP and screening demand due to its older resident base, "
        "while KT may have stronger private screening/wellness potential due to its private-housing and higher-income profile."
    )

    # -----------------------------
    # 3. Affluence
    # -----------------------------
    st.markdown("### 3. Affluence / Ability to Pay")

    st.markdown(
        """
        Affluence is assessed using planning-area income distribution and housing type. Income data is only
        available at planning-area level, so it should be treated as broad affordability context rather than
        exact subzone income.
        """
    )

    st.image(
        "charts/income_profile.png",
        caption="Household Income Profile by Planning Area",
        use_container_width=True
    )

    affluence_takeaways = pd.DataFrame({
        "Finding": [
            "KT / Marine Parade has a higher share of $20,000+ households",
            "KT also has a higher share of $10,000+ and $15,000+ households",
            "HV / Queenstown has a higher below-$5,000 share",
            "HV still has a larger overall household base"
        ],
        "Implication": [
            "KT has stronger high-income concentration and private healthcare affordability",
            "KT likely has stronger ability to pay for GP, health screening, wellness and TCM",
            "HV has a more mixed-income catchment",
            "HV may still generate higher volume due to density/accessibility despite lower income profile"
        ]
    })

    st.dataframe(affluence_takeaways, use_container_width=True)

    st.success(
        "Affluence takeaway: Income data favours KT, so KT's slower volume is unlikely to be mainly due to weak affordability."
    )

    # -----------------------------
    # 4. Housing Type
    # -----------------------------
    st.markdown("### 4. Housing Type / Residential Character")

    st.markdown(
        """
        Housing type is used to understand the residential character of each branch's catchment.
        HDB-heavy areas suggest denser public-housing catchments, while condo/apartment and landed-heavy
        areas suggest stronger private-residential and ability-to-pay signals.
        """
    )

    st.image(
        "charts/housing_composition.png",
        caption="Housing Type Composition: Immediate Subzone vs Broader Planning Area",
        use_container_width=True
    )

    housing_takeaways = pd.DataFrame({
        "Finding": [
            "Katong subzone is private-housing heavy",
            "Holland Drive subzone is HDB-heavy",
            "Marine Parade remains more private-housing oriented than Queenstown",
            "Queenstown has a much larger HDB-based resident base"
        ],
        "Implication": [
            "KT has stronger private-residential and affordability signals",
            "HV has stronger dense mass-residential catchment",
            "KT has stronger spending/service-fit potential",
            "HV has stronger volume-generation potential from nearby residents"
        ]
    })

    st.dataframe(housing_takeaways, use_container_width=True)

    st.info(
        "Housing takeaway: KT is stronger in private-housing profile, while HV is stronger in dense HDB-resident volume potential."
    )

    # -----------------------------
    # 5. Ethnicity / TCM Relevance
    # -----------------------------
    st.markdown("### 5. Ethnicity / TCM Relevance")

    st.markdown(
        """
        Ethnicity is used only as a possible service-fit indicator for TCM / Chinese medicine. It should not
        be treated as proof of patient behaviour.
        """
    )

    st.image(
        "charts/ethnic_composition.png",
        caption="Ethnic Composition by Subzone",
        use_container_width=True
    )

    ethnicity_takeaways = pd.DataFrame({
        "Finding": [
            "Both Katong and Holland Drive are Chinese-majority subzones",
            "Katong has a slightly higher Chinese share",
            "Holland Drive has more Chinese residents in absolute terms because its population is larger",
            "HV has a more mixed ethnic profile due to higher Malay share"
        ],
        "Implication": [
            "TCM relevance exists in both areas",
            "Supports the local relevance of Regis Wellness at KT",
            "Ethnicity alone does not prove KT has stronger TCM demand than HV",
            "Ethnicity is not a strong explanation for the GP volume/revenue gap"
        ]
    })

    st.dataframe(ethnicity_takeaways, use_container_width=True)

    st.success(
        "Ethnicity takeaway: KT's Chinese-majority profile supports TCM service fit, but ethnicity is not a major differentiator because HV is also Chinese-majority."
    )

    # -----------------------------
    # Final demographics conclusion
    # -----------------------------
    st.markdown("### Resident Demographic Summary")

    demographic_summary = pd.DataFrame({
        "Dimension": [
            "Age / healthcare need",
            "Health demand proxy",
            "Affluence",
            "Housing type",
            "Ethnicity / TCM relevance"
        ],
        "KT Branch": [
            "Smaller elderly base; some family/child demand",
            "Private-housing profile may support private screening/wellness",
            "Higher income profile",
            "Private/landed-heavy",
            "Chinese-majority; supports TCM relevance"
        ],
        "HV Branch": [
            "Larger elderly and older-adult base",
            "Stronger chronic-care and repeat GP demand",
            "More mixed-income profile",
            "HDB-heavy and denser",
            "Also Chinese-majority; TCM relevance exists too"
        ],
        "Likely implication": [
            "HV stronger for recurring GP volume",
            "HV stronger for chronic care; KT stronger for private wellness/screening",
            "KT stronger ability to pay",
            "KT stronger spending potential; HV stronger volume potential",
            "Ethnicity supports KT service fit but does not explain volume gap"
        ]
    })

    st.dataframe(demographic_summary, use_container_width=True)

    st.warning(
        "Overall demographic conclusion: HV is stronger for volume-driven GP demand due to age and density. "
        "KT is stronger for affordability and wellness/service-fit. This supports the idea that KT's issue is "
        "not weak spending power, but weaker conversion into high GP volume."
    )

with tabs[3]:
    st.subheader("Methodology & Planned Direction")

    st.markdown(
        """
        This dashboard summarises the current **macro analysis** for the KT vs HV branch comparison.
        The aim is to check whether the surrounding environment of each branch helps explain differences
        in revenue and patient volume.
        """
    )

    st.markdown("### 1. Current Methodology")

    methodology = pd.DataFrame({
        "Step": [
            "Define comparison scope",
            "Identify official branch context",
            "Measure catchment size and density",
            "Assess resident demographic profile",
            "Assess affluence and housing profile",
            "Assess accessibility and footfall",
            "Use external health research as proxy",
            "Prepare for micro-factor validation"
        ],
        "What was done": [
            "Compared KT branch against HV branch using macro area-level indicators.",
            "Used URA Master Plan, planning area and subzone classifications.",
            "Compared planning area population, subzone population and population density.",
            "Analysed age, ethnicity and housing type using Census/SingStat data.",
            "Used income distribution and housing type as ability-to-pay indicators.",
            "Compared MRT access, bus access, parking, surrounding anchors and spillover subzones.",
            "Used cardiometabolic screening research to support age/housing as health-demand proxies.",
            "Planned staff interviews and competitor analysis to test whether macro findings match ground reality."
        ],
        "Purpose": [
            "Understand why KT may be slower than HV.",
            "Identify whether each branch is in a commercial or residential-commercial setting.",
            "Estimate potential patient pool and nearby resident concentration.",
            "Understand likely patient needs and service relevance.",
            "Assess whether affordability is likely to explain the volume gap.",
            "Assess whether the area naturally converts people into clinic visits.",
            "Avoid claiming direct disease prevalence without local health data.",
            "Move from macro potential to branch-level capture ability."
        ]
    })

    st.dataframe(methodology, use_container_width=True)

    st.markdown("### 2. Current Direction of Findings")

    st.info(
        """
        Current macro findings suggest that **HV has stronger volume-generation conditions**:
        higher immediate density, stronger elderly base, commercial land use, MRT access and wider spillover catchment.

        **KT appears stronger in spending/service-fit conditions**:
        higher income profile, private-housing catchment, hotel/tourist potential, parking and TCM/wellness relevance.
        """
    )

    st.markdown("### 3. Planned Next Steps")

    next_steps = pd.DataFrame({
        "Next step": [
            "Validate macro assumptions with staff",
            "Analyse local competition",
            "Compare branch visibility and frontage",
            "Check service mix and patient source",
            "Review operational factors",
            "Clarify internal data availability",
            "Consider scoring model as optional extension"
        ],
        "What to check": [
            "Ask whether HV actually receives more MRT/walk-in/elderly patients"
            " and whether KT receives more planned/tourist/wellness patients.",
            "Count nearby GP, TCM, wellness and chain clinics within 400m/800m.",
            "Compare signage, storefront visibility, entrance clarity and ease of discovery.",
            "Check whether KT’s Medical vs Wellness split affects GP volume or patient "
            "understanding.",
            "Check doctor availability, opening hours, waiting time, staffing and appointment flow.",
            "Ask if patient postal codes, walk-in vs appointment data, service-level revenue and "
            "panel-patient data are available.",
            "Propose a weighted branch potential scoring model to supervisors, "
            "but avoid using arbitrary weights without review."
        ]
    })

    st.dataframe(next_steps, use_container_width=True)

   
    st.markdown("### 4. Full Report Link")

    st.markdown(
        """
        Full working report: [Open Word Document](https://essexbio-my.sharepoint.com/:w:/g/personal/jacelyn_tay_essexbio_com_sg/IQBsHlFnYEITQYmQFo7tcDEOAfQmIBW6r4w-ACCxpIaTVNE?e=MPSAam)
        """
    )

    

   