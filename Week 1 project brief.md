# Project brief

## 1. Why Health care?

>Lagos State's high migration rate places continuous pressure on local healthcare systems. This project utilizes spatial data analysis to map the exact distribution of medical facilities across the state, identifying areas of high facility concentration and critical low-density zones. 

## 2. Study Area

The study area for this project is Lagos State, Nigeria.

## 3. What I mean by the terms.
- High Concentration (Hotspots) refers to a large number of items packed tightly into a small geographic space.
- Low Concentration (Coldspots) means items are spread far apart, or there are very few of them across a wide geographic area.

## 4. Datasets

| Sn | Name | What it gives me | Data type | Data Source |
|---|---|---|---| ---|
| 1 |  GADM | Boundary data | GeoJSON | [Click here](https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_NGA_2.json.zip) |
| 2 | HumanitarianDataExchange | Health facility | GeoJSON |[Click here](https://data.humdata.org/dataset/hotosm_nga_health_facilities/resource/1a951e5c-577c-449e-906f-993379a2a62b) |


## 5. What done looks like.

- The Lagos Health Heatmap: A professional map layout featuring the clipped Kernel Density raster, displaying urban hotspots (e.g., Ikeja, Surulere) in warm colors and highlighting "coldspots" in peripheral regions.

- Categorical Overlays: Distinct vector icons layered over the heatmap to differentiate primary care clinics, pharmacies, and general hospitals at a glance.

- LGA Statistical Dashboard: A supplementary chart breaking down the exact count of facilities per Local Government Area, derived from your Spatial Join attribute table.

## 6. Potential risks.

1. The Proximity vs. Accessibility Fallacy

The heatmap measures physical distance, but in the urban sprawl of Lagos, persistent traffic congestion and poorly maintained roads can transform a 1-kilometer trip into hours of travel time.

Because traffic drastically delays emergency response times, mere spatial proximity on a map is an insufficient measure of true healthcare accessibility.


2. Boundary Edge Effects

Points located near the edges of the Lagos State boundary will have fewer neighboring points contributing to their density calculations.

This creates artificially low density values along the borders, which can mislead interpretation.

3. Crowdsourced Data Bias

Because OpenStreetMap and Humanitarian Data Exchange (HDX) rely on volunteer mappers, data collection biases can easily skew the analysis.

Highly developed commercial areas might be mapped perfectly, while informal settlements or rural LGAs might appear as "coldspots" simply because volunteers have not mapped them yet, not necessarily because the facilities do not exist.

**STATUS** Week 1 completed, Data aquisation in Week 2 


**SHOWUNMI FAVOUR AYOMIDE**
