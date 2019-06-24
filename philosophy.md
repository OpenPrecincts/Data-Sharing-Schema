# Open Precincts Data Schema

For background, see [Michal Migurski's December 2018 Medium Post](https://medium.com/planscore/open-precinct-data-schema-0-1-proposal-a1eb576bfe7).


## Intended Use Cases

This is an attempt to provide a data schema for the interchange of precinct and precinct-related data.

Intended users would be:

* developers of citizen-driven redistricting apps such as [Districtr](https://districtr.org/), [Dave's Redistricting App](http://gardow.com/davebradlee/redistricting/default.html), and [DistrictBuilder](http://www.districtbuilder.org/).
* scoring and analysis tools like [PlanScore](https://planscore.org/) and [GerryChain](https://github.com/mggg/GerryChain)
* automated redistricting tools

This is *not* meant to be a comprehensive database of election results nor a replacement for Census data.  Though limited support for election results and census statistics exists, it is only present to serve the needs of the above purposes.


## Technical Guidelines

* Reasonable effort should be made to make the data easy to work with via tools like pandas.  One example of this is having some redundant information in column names (e.g. the division CSV header is named division_name, not name).  This is done so that when joined with other CSVs, there aren't ambiguous field names.
* The goal of the schema is to define common attributes and vocabularies for common fields. If a group has a specific need they should be able to add additional data as needed, additionally, most information is optional.
