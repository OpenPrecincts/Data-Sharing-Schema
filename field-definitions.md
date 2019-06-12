# Schema Field Definitions

## Elections

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
election_id     | *         | unique ID for election    | OPID:1360711279
state_id        | *         | state FIPS code           | FIPS:37
election_date   | *         | date of election          | 2016-11-08
election_type   | *         | primary|general           | primary


## Districts

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
district_id     | *         | unique ID for district    | OPID:1360711279
state_id        | *         | state FIPS code           | FIPS:37
district_plan   | *         | identifier for plan(?)    | NC5.1
district_name   | *         | name of district          | U.S. House District 2
chamber_name    | *         | name of chamber           | U.S. House of Representatives
shape_id        | *         | link to Shape             | PSID:1360703401
source_id       | *         | link to Source            | OPID:1360703401


## Candidates

Field Name          | Required  | Description               | Example
--------------------|-----------|---------------------------|-------------------
election_id         | *         | link to Election          | OPID:1360711279
district_id         | *         | link to District          | OPID:1360711285
candidate_name      | *         | candidate name            | David E. Price
candidate_party     | *         | party name                | Democratic
candidate_incumbent | *         | is candidate incumbent?   | Yes
candidate_winner    | *         | did candidate win?        | Yes
source_id           | *         | link to Source            | OPID:1360703401


## Precincts

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
election_id     | *         | link to Election          | OPID:1360711279
district_id     | *         | link to District          | OPID:1360711285
county_id       | *         | FIPS id for county        | FIPS:37001
county_name     | *         | name of county            | Alamance
precinct_name   | *         | name for precinct         | 035_BOONE 5
source_id       | *         | link to Source            | OPID:1360703401
shape_id        | *         | link to Shape             | PSID:1360703482


## Sources

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
source_id       | *         | unique ID for source      | OPID:1360711211
source_name     | *         | name for source           | NC State Board of Elections
source_url      | *         | URL for source            | https://dl.ncsbe.gov/index.html?prefix=PrecinctMaps/
