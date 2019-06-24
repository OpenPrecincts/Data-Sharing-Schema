# Schema Field Definitions

## Elections

An election in a single state.

It may be worth noting that this does not link elections in different states
that take place on the same day.

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
election_id     | *         | unique ID for election    | OPEID:1360711279
state           | *         | state USPS abbrev         | NC
date            | *         | date of election          | 2016-11-08
election_type   | *         | primary|general           | primary


## Division

An administrative division such as a congressional district or census block.

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
division_id     | *         | unique ID for division    | OPDID:8283923911
shape_id        | *         | link to Shape             | OPSID:1360703401
state           | *         | state USPS abbrev         | NC
division_type   | *         | type of shape (enum)      | cd, sldl, sldu, census_block
district_plan   |           | identifier for plan(?)    | NC5.1
division_name   | *         | name of division          | U.S. House District 2
source_id       | *         | link to Source            | OPSRCID:1360703401


## Candidacy

A participant in a given election.

(Note: this is a candidacy not candidate since no attempt is made to reconcile
individuals that run in multiple years.)

Field Name          | Required  | Description               | Example
--------------------|-----------|---------------------------|-------------------
id                  | *         | unique ID for candidacy   | OPCID:1489228290
election_id         | *         | link to Election          | OPEID:1360711279
division_id         | *         | link to Division          | OPSID:1360711285
candidate_name      |           | candidate name            | David E. Price
candidate_party     | *         | party name                | Democratic
is_incumbent        |           | is candidate incumbent?   | Yes
is_winner           |           | did candidate win?        | Yes
source_id           |           | link to Source            | OPSRCID:1360703401


## Precincts

A voting tabulation district.  Represents the smallest area at which votes are
counted in a given jurisdiction.

Field Name          | Required  | Description               | Example
--------------------|-----------|---------------------------|-------------------
id                  | *         | unique ID for precinct    | OPPID:1485829328
election_id         | *         | link to Election          | OPEID:1360711279
cd_division_id      |           | link to CD Division       | OPDID:1360711285
sldu_division_id    |           | link to SLDU Division     | OPDID:1360711286
sldl_division_id    |           | link to SLDL Division     | OPDID:1360711287
county_id           |           | FIPS id for county        | FIPS:37001
county_name         |           | name of county            | Alamance
precinct_name       | *         | name for precinct         | 035_BOONE 5
source_id           | *         | link to Source            | OPSRCID:1360703401
shape_id            | *         | link to Shape             | OPSID:1360703482


## Sources

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
source_id       | *         | unique ID for source      | OPSRCID:1360711211
source_name     | *         | name for source           | NC State Board of Elections
source_url      | *         | URL for source            | https://dl.ncsbe.gov/index.html?prefix=PrecinctMaps/


## Shapes

A shape that can be used for a precinct or division.

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
shape_id        | *         | unique ID for shape       | OPSID:1360711211
geometry        | *         | (multi)polygon            | ...


## Demographic

A demographic measurement for a given area.

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
shape_id        | *         | link to shape             | OPSID:1360711211
demographic_type| *         | demographic type (enum)   | BVAP, TOTALPOP
value           | *         | numeric value for stat    | 61386
source_id       | *         | link to a source          | OPSRCID:1253282902


## VoteTotal

A number of votes for a candidacy in a given precinct.

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
precinct_id     | *         | link to precinct          | OPPID:1360711211
candidate_id    | *         | link to candidate         | OPCID:1410711331
vote_count      | *         | number of votes           | 724
source_id       | *         | link to a source          : OPSRCID:1258282921
