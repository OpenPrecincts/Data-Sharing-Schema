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


## Divisions

An administrative division such as a congressional district or census block.

Field Name          | Required  | Description               | Example
--------------------|-----------|---------------------------|-------------------
division_id         | *         | unique ID for division    | OPDID:8283923911
shape_id            | *         | link to Shape             | OPSID:1360703401
state               | *         | state USPS abbrev         | NC
division_type       | *         | type of shape (enum)      | cd, sldl, sldu, census_block, precinct
district_plan       |           | identifier for plan(?)    | NC5.1
division_name       | *         | name of division          | U.S. House District 2
source_id           | *         | link to Source            | OPSRCID:1360703401


If division_type is precinct, the following are also available:

Field Name          | Required  | Description                   | Example
--------------------|-----------|-------------------------------|-----------------
election_id         | *         | link to Election              | OPEID:1360711279
cd_division_id      |           | link to CD Division           | OPDID:1360711285
sldu_division_id    |           | link to SLDU Division         | OPDID:1360711286
sldl_division_id    |           | link to SLDL Division         | OPDID:1360711287
locality_id         |           | FIPS id for county-equivalent | FIPS:37001
locality_name       |           | name of county-equivalent     | Alamance


## Candidacies

A participant in a given election.

(Note: this is a candidacy not candidate since no attempt is made to reconcile
individuals that run in multiple years.)

Field Name          | Required  | Description               | Example
--------------------|-----------|---------------------------|-------------------
candidacy_id        | *         | unique ID for candidacy   | OPCID:1489228290
election_id         | *         | link to Election          | OPEID:1360711279
office_type         | *         | type of office            | cd|sldl|sldu|pres|gov|ltgov
division_id         |           | link to Division          | OPSID:1360711285
candidate_name      |           | candidate name            | David E. Price
candidate_party     | *         | party name                | Democratic
is_incumbent        |           | is candidate incumbent?   | Yes
is_winner           |           | did candidate win?        | Yes
source_id           |           | link to Source            | OPSRCID:1360703401


## Sources

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
source_id       | *         | unique ID for source      | OPSRCID:1360711211
source_name     | *         | name for source           | NC State Board of Elections
source_url      | *         | URL for source            | https://dl.ncsbe.gov/index.html?prefix=PrecinctMaps/


## Shapes

A shape that can be used for a division.

Field Name      | Required  | Description               | Example
----------------|-----------|---------------------------|-------------------
shape_id        | *         | unique ID for shape       | OPSID:1360711211
geometry        | *         | (multi)polygon            | ...


## Statistic

A statistical measurement for a given area.  Can also be used to aggregate vote totals with an optional candidate_id.

Field Name      | Required  | Description                 | Example
----------------|-----------|-----------------------------|-------------------
division_id     | *         | link to division            | OPDID:1360711211
statistic_type  | *         | statistic type (enum)       | BVAP, TOTALPOP, VOTE
candidate_id    |           | link to candidate           | OPCID:1410711331
value           | *         | numeric value for stat      | 61386
source_id       | *         | link to a source            | OPSRCID:1253282902
