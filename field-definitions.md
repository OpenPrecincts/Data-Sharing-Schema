# Schema Field Definitions

## Elections

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
id              | *         | unique ID for election    | OPEID:1360711279
state           | *         | state USPS abbrev         | NC
date            | *         | date of election          | 2016-11-08
type            | *         | primary|general           | primary


## Division

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
shape_id        | *         | link to Shape             | OPSID:1360703401
state           | *         | state USPS abbrev         | NC
type            | *         | type of shape (enum)      | cd, sldl, sldu, census_block
district_plan   |           | identifier for plan(?)    | NC5.1
name            | *         | name of division          | U.S. House District 2
source_id       | *         | link to Source            | OPSRCID:1360703401


## Candidates

Field Name          | Required  | Description               | Example
--------------------|-----------|---------------------------|-------------------
election_id         | *         | link to Election          | OPEID:1360711279
division_id         | *         | link to Division          | OPDID:1360711285
name                | *         | candidate name            | David E. Price
party               | *         | party name                | Democratic
is_incumbent        | *         | is candidate incumbent?   | Yes
is_winner           | *         | did candidate win?        | Yes
source_id           | *         | link to Source            | OPSRCID:1360703401


## Precincts

Field Name          | Required  | Description               | Example
--------------------|-----------|---------------------------|-------------------
election_id         | *         | link to Election          | OPEID:1360711279
cd_division_id      |           | link to CD Division       | OPDID:1360711285
sldu_division_id    |           | link to SLDU Division     | OPDID:1360711286
sldl_division_id    |           | link to SLDL Division     | OPDID:1360711287
county_id           |           | FIPS id for county        | FIPS:37001
county_name         |           | name of county            | Alamance
name                | *         | name for precinct         | 035_BOONE 5
source_id           | *         | link to Source            | OPSRCID:1360703401
shape_id            | *         | link to Shape             | OPSID:1360703482


## Sources

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
id              | *         | unique ID for source      | OPSRCID:1360711211
name            | *         | name for source           | NC State Board of Elections
url             | *         | URL for source            | https://dl.ncsbe.gov/index.html?prefix=PrecinctMaps/


## Shapes

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
id              | *         | unique ID for shape       | OPSID:1360711211
geometry        | *         | (multi)polygon            | ...
