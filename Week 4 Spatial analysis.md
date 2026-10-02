# Spatial Analysis of Healthcare Accessibility in Lagos State

**Week 4 deliverable.** GeoDev Lab Africa, Cohort 9.
Author: Favour Showunmi

**Data Limitation Note:** The dataset utilized (603 facility records) is a partial sample and does not cover the complete geographical extent of Lagos State. The spatial patterns, hotspots, and gaps identified in this report strictly reflect the boundaries of the provided data. Actual healthcare coverage in unmapped regions may vary.

## 1. Spatial Analysis Methodology

### 1.1 Kernel Density Estimation (Heatmap)
To visualize the concentration of healthcare services, a continuous density surface was generated:
* **Algorithm:** Kernel Density Estimation (KDE)
* **Search Radius:** 500 meters (representing a standard walkable distance)
* **Kernel Shape:** Quartic
* **Symbology:** Classified into 5 discrete categories ranging from "Zero / No Access" to "Very High Concentration" to clearly delineate hotspots and cold spots across the mapped Local Government Areas (LGAs).

### 1.2 Proximity Buffer Analysis
To statistically quantify healthcare isolation within the dataset, a proximity threshold analysis was conducted:
* **Buffer Generation:** A 500-meter vector buffer was created around every individual healthcare facility.
* **Spatial Join / Counting:** The "Count Points in Polygon" tool was utilized to determine the number of neighboring facilities within each 500m radius.
* **Classification:** Facilities were categorically coded as "Yes" (clustered with other facilities within 500m) or "No" (spatially isolated with 0 neighbors within 500m) using the Field Calculator.

## 2. Analytical Findings

* **High-Density Hotspots (The Urban Core):** The KDE heatmap reveals intense clustering of healthcare infrastructure in the central and western LGAs covered by the data, including Ikeja, Surulere, Oshodi/Isolo, Agege, and Alimosho. Residents in these zones have overlapping access to multiple facilities within a 5-to-10-minute walking radius.
* **Healthcare Deserts (The Periphery):** Significant spatial gaps exist in the peripheral mapped regions. The surveyed eastern expanses of Epe, Ibeju-Lekki, and parts of Ikorodu, as well as Badagry in the west, show negligible facility density.
* **Statistical Accessibility:** Out of the 603 documented healthcare facilities in the dataset, **543 facilities (90%)** are located within 500 meters of at least one other facility. 
* **Service Isolation:** Conversely, **60 facilities (10%)** are completely isolated, meaning there are no other documented healthcare options within a 500-meter walking radius of these specific locations. 

## 3. Map of Study Area
![Lagos Healthcare Heatmap](LagosHealth%20Heatmap.jpeg)

## 4. Conclusion
The spatial analysis confirms a pronounced inequality in healthcare distribution within the mapped regions of Lagos State. While the dense urban core enjoys highly clustered and accessible medical infrastructure, the surveyed coastal and peripheral areas face substantial service gaps. Comprehensive state-wide data collection would be required in the future to assess the full extent of spatial equity across all unmapped LGAs.

**Status**: Week 4 completed. First month completed.
