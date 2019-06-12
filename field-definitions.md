# Schema Field Definitions

## Elections

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
id              | *         | unique ID for election    | OPEID:1360711279
state_id        | *         | state FIPS code           | FIPS:37
date            | *         | date of election          | 2016-11-08
type            | *         | primary|general           | primary


## Districts

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
id              | *         | unique ID for district    | OPDID:1360711279
state_id        | *         | state FIPS code           | FIPS:37
district_plan   | *         | identifier for plan(?)    | NC5.1
name            | *         | name of district          | U.S. House District 2
chamber_name    | *         | name of chamber           | U.S. House of Representatives
shape_id        | *         | link to Shape             | OPSID:1360703401
source_id       | *         | link to Source            | OPSRCID:1360703401


## Candidates

Field Name          | Required  | Description               | Example
--------------------|-----------|---------------------------|-------------------
election_id         | *         | link to Election          | OPEID:1360711279
district_id         | *         | link to District          | OPDID:1360711285
name                | *         | candidate name            | David E. Price
party               | *         | party name                | Democratic
is_incumbent        | *         | is candidate incumbent?   | Yes
is_winner           | *         | did candidate win?        | Yes
source_id           | *         | link to Source            | OPSRCID:1360703401


## Precincts

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
election_id     | *         | link to Election          | OPEID:1360711279
district_id     | *         | link to District          | OPDID:1360711285
county_id       | *         | FIPS id for county        | FIPS:37001
county_name     | *         | name of county            | Alamance
name            | *         | name for precinct         | 035_BOONE 5
source_id       | *         | link to Source            | OPSRCID:1360703401
shape_id        | *         | link to Shape             | OPSID:1360703482


## Sources

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
id              | *         | unique ID for source      | OPSRCID:1360711211
name            | *         | name for source           | NC State Board of Elections
url             | *         | URL for source            | https://dl.ncsbe.gov/index.html?prefix=PrecinctMaps/
