# India's Agricultural Crop Production Analysis

A **Data Analytics with Tableau capstone project** completed as part of the SkillWallet program. This project analyzes agricultural crop production in India using Tableau to identify patterns in production, cultivated area, yield, crop performance, states, and agricultural seasons.

The project includes data preparation, exploratory visualization, KPI analysis, an interactive dashboard, a Tableau story, performance testing, web integration, and project documentation.

## Live Links

| Resource | Link |
|---|---|
| Tableau Public Profile | |
| Tableau Public Dashboard | |
| Tableau Public Story | |
| Live Web Integration / Website | |
| GitHub Repository | |
| Demo Video | |
| SkillWallet Project | |

> Fill in the blank links after publishing the Tableau workbook, story, website, GitHub repository, and demo.

---

## Project Overview

Agricultural production varies considerably across crops, states, years, and growing seasons. Understanding these patterns can help stakeholders explore production trends, compare crops, examine cultivated area, and identify regional and seasonal differences.

This project uses Tableau to transform agricultural data into interactive visualizations and a consolidated dashboard.

### Objectives

- Analyze total agricultural crop production in India.
- Examine production trends across years.
- Compare production across different crops.
- Compare cultivated area across crops.
- Analyze production across Indian states.
- Compare production across agricultural seasons.
- Examine yield trends over time.
- Create KPI-based summaries for quick analysis.
- Build an interactive Tableau dashboard.
- Present the analysis through a Tableau story.
- Publish the final visualization for web access.

---

## Dataset

The project uses an Indian agricultural crop production dataset containing records related to crops, states, districts, seasons, years, cultivated area, production, and yield.

### Main fields used

- **State** – Indian state associated with the agricultural record.
- **District** – District associated with the record.
- **Crop** – Crop being analyzed.
- **Season** – Agricultural season such as Kharif, Rabi, Summer, Winter, Autumn, or Whole Year.
- **Year** – Agricultural year.
- **Area** – Cultivated area.
- **Production** – Crop production quantity.
- **Yield** – Crop yield.
- **Area Units** – Unit associated with cultivated area.
- **Production Units** – Unit associated with production.

Additional calculated/aggregated fields were used in Tableau, including:

- **Total Area**
- **Total Production**
- **Yield**
- Tableau-generated geographic fields such as **Latitude** and **Longitude** for the state-level map.

### Data Preparation

The dataset was prepared for Tableau analysis by:

1. Connecting the agricultural dataset to Tableau.
2. Reviewing the available fields and data types.
3. Using appropriate dimensions and measures for analysis.
4. Aggregating production and area where required.
5. Creating calculated/aggregated measures such as Total Production and Total Area.
6. Using Tableau's generated geographic coordinates for state-level mapping.
7. Checking the resulting visualizations for readability and consistency.

---

## Key Performance Indicators

The dashboard contains the following high-level KPIs:

| KPI | Current Dashboard Value |
|---|---:|
| Total Production | ~19.17B |
| Average Yield | ~5.126 |
| Number of Crops | 57 |
| Number of States | 36 |

> KPI values may display slightly differently depending on Tableau number formatting and aggregation settings.

---

## Tableau Visualizations

The project currently contains the following completed worksheets.

### 1. Yield Trend

Shows how agricultural yield changes over the years.

**Purpose:**  
To identify long-term changes and trends in agricultural productivity.

### 2. Total Production KPI

Displays the overall total agricultural production.

**Purpose:**  
To provide a single high-level production metric for the dashboard.

### 3. Average Yield KPI

Displays the average yield across the dataset.

**Purpose:**  
To provide a quick measure of agricultural productivity.

### 4. Number of Crops KPI

Displays the number of distinct crops represented in the dataset.

**Current value:** 57 crops.

### 5. Number of States KPI

Displays the number of states represented in the dataset.

**Current value:** 36 states.

### 6. Production Trend

Shows agricultural production across different years.

**Purpose:**  
To identify changes in total production over time.

### 7. Crop Production

Compares total production across individual crops.

**Purpose:**  
To identify crops with comparatively higher and lower production.

### 8. Cultivated Area by Crop

Compares the cultivated area associated with different crops.

**Purpose:**  
To understand which crops occupy larger cultivated areas.

### 9. State Production Map

Displays production geographically across Indian states using Tableau's generated latitude and longitude fields.

**Purpose:**  
To provide a geographic view of agricultural production and compare production levels across regions.

### 10. Season-wise Production

Compares agricultural production across seasons.

**Seasons represented include:**

- Whole Year
- Kharif
- Rabi
- Winter
- Summer
- Autumn

**Purpose:**  
To understand how production is distributed across agricultural seasons.

---

## Important Observations

The current Tableau analysis highlights several useful patterns:

- The dataset contains **57 different crops**.
- The dataset represents **36 states**.
- Total production is approximately **19.17 billion** according to the current KPI.
- Average yield is approximately **5.126** according to the current KPI.
- Production varies substantially between crops.
- Cultivated area also differs significantly between crops.
- Production differs across Indian states, which is visible in the geographic visualization.
- Production is distributed unevenly across agricultural seasons.
- Production and yield can be examined across multiple years to identify changing agricultural patterns.

### Crop-level observations

The current crop-production visualization shows substantial differences between crops. Some crops contribute considerably more to the recorded production than others.

The cultivated-area visualization separately shows that crops such as **rice and wheat** occupy comparatively large cultivated areas in the dataset.

> These observations describe patterns in the supplied dataset and should not automatically be interpreted as causal agricultural conclusions.

---

## Dashboard

The main Tableau dashboard brings together the project's most important KPIs and visualizations.

### Dashboard Components

#### KPI Section

- Total Production
- Average Yield
- Number of Crops
- Number of States

#### Analysis Section

- Production Trend
- Crop Production
- Cultivated Area by Crop
- State Production Map
- Season-wise Production
- Yield Trend, where included in the final dashboard layout

### Dashboard Goals

The dashboard is designed to allow users to:

- Quickly understand overall production.
- Compare agricultural performance across crops.
- Examine cultivated area.
- Explore state-level production.
- Compare seasonal production.
- Observe production and yield trends over time.

---

## Tableau Story

A Tableau Story is used to present the analysis in a sequence of views so that the major findings can be understood progressively.

### Planned Story Flow

1. **Introduction / Overview**
   - Project objective
   - Dataset overview
   - Key KPIs

2. **Production Overview**
   - Total production
   - Production trend

3. **Crop Analysis**
   - Crop production
   - Cultivated area by crop

4. **Geographical Analysis**
   - State production map

5. **Seasonal Analysis**
   - Season-wise production

6. **Yield Analysis**
   - Yield trend
   - Interpretation of agricultural productivity

7. **Conclusion**
   - Main observations
   - Key insights from the dataset

> Update this section if the final Tableau Story uses a different number or order of story points.

---

## Performance Testing

Performance testing is part of the project to ensure that the Tableau dashboard remains usable and responsive.

The dashboard was reviewed for:

- Visualization loading.
- Filter responsiveness.
- Chart readability.
- Dashboard object alignment.
- Excessive visual clutter.
- Overlapping dashboard objects.
- Appropriate aggregation of measures.
- Overall dashboard usability.

### Performance Considerations

To maintain reasonable dashboard performance:

- Only required visualizations are included.
- Aggregated measures are used for high-level analysis.
- Visualizations are kept focused on specific analytical questions.
- Unnecessary complexity is avoided where possible.
- Dashboard layout is organized to improve usability.

---

## Web Integration

The Tableau dashboard/story can be integrated into a website or web page after publishing to Tableau Public.

### Integration Link

**Website:** 

**Embedded Tableau Dashboard:** 

**Embedded Tableau Story:** 

> Add the final website and published Tableau URLs here after completing web integration.

---

## Project Demonstration

A final demonstration should show:

1. Dataset connection and preparation.
2. Important Tableau worksheets.
3. KPI calculations.
4. Main dashboard.
5. Interactive visualizations.
6. Tableau Story.
7. Published Tableau Public result.
8. Web integration, if completed.

### Demo Video

**Video Link:** 

---

## Tools & Technologies

- **Tableau Desktop** – Data analysis and visualization
- **Tableau Public** – Publishing the final dashboard/story
- **GitHub** – Source-code and project documentation hosting
- **Web technologies** – For optional dashboard/story integration
- **SkillWallet** – Capstone project submission and tracking

## Conclusion

This project demonstrates how Tableau can be used to analyze Indian agricultural data and convert raw crop-production records into meaningful visual insights.

The analysis covers production trends, crop-level production, cultivated area, state-level production, seasonal production, yield, and high-level KPIs.

The final dashboard is intended to provide a concise and interactive overview of agricultural production patterns, while the Tableau Story presents the analysis in a structured narrative.

The results should be interpreted as patterns within the supplied dataset and not as definitive explanations of agricultural outcomes.

---

## Author

**Name:** Shruti Pandita

**Course / Program:** Data Analytics with Tableau - India’s Agricultural Crop Production Analysis

**Platform:** Tableau Public 

**Project Title:** India's Agricultural Crop Production Analysis 

**Tableau Public:** 
- Dashboard: https://public.tableau.com/views/Book1_Shruti_Agricultural_Dashboard/IndiaAgriculturalCropAnalysisDashboard?:language=en-US&:sid=&:redirect=auth&publish=yes&showOnboarding=true&:display_count=n&:origin=viz_share_link

- Story: https://public.tableau.com/views/Shruti_Agricultural_story/AgriculturalOverview?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
 
