# Data notes

Author: SHOWUNMI FAVOUR AYOMIDE

## 1. Lagos Healthcare Facilities (Humanitarian Data Exchange)

- **Source:** [Click here](https://data.humdata.org/dataset/hotosm_nga_health_facilities/resource/1a951e5c-577c-449e-906f-993379a2a62b)
- **Retrieved:** <24th September 2026>
- **File:** `data/raw/hotosm_nga_health_facilities_osm_geojson`
- **Format:** GeoJSON
- **Geometry type:** Point 
- **Feature count:** 4657 
- **CRS as downloaded:** EPSG:4326 (WGS 84)

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| `amenity` | The type of facility (e.g., hospital, clinic, pharmacy). | 310 |
| `name` | The registered name of the health facility. | 1326 |
| `operator` | Who runs the facility (public vs. private). | 4657 |

**What I noticed**
- < 100% of the operator data is missing, I cannot use this specific HOT dataset to compare public versus private healthcare distribution.>

- < This dataset covers all of Nigeria. I will need to use a spatial clip to isolate only the facilities within the Lagos State boundary before running the analysis.>


---

## 2. Lagos State Administrative Boundaries (Local Government Areas)

- **Source:**[Click here](https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_NGA_2.json.zip)
- **Retrieved:** <24th September 2026>
- **File:** `data/raw/gadm41_NGA_2.json`
- **Format:** GeoJSON
- **Geometry type:** Polygon
- **Feature count:** 775
- **CRS as downloaded:** EPSG:4326 (WGS 84)

**Key columns**

| Column | What it holds | Nulls |
|---|---|---|
| `NAME_1` | State Name  | 0 |
| `NAME_2` | Local Government Area Name | 0 |

**What I noticed**
<The file contains LGAs for all 36 states. I must filter `NAME_1` to 'Lagos' and export a new shapefile.>

---

## Cross-cutting problems

**Different Coordinate Reference Systems:** Both datasets downloaded in WGS 84 geographic coordinates (EPSG:4326). Before running the Kernel Density tool or calculating accurate areas, I must reproject both layers to WGS 84 / UTM zone 31N (EPSG:32631).

**Attribute Mismatches during Spatial Join:** If I join the HOT point data to the LGA polygons to count facilities, I need to ensure the point dataset does not have overlapping or duplicated facility points near the borders of adjoining LGAs.

**Status**: Data note completed, data preparation in week 3.
