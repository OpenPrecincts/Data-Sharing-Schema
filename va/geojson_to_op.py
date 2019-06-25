import uuid
import csv
import random
import json


FIELD_NAMES = {
    "elections": ("election_id", "state", "date", "election_type"),
    "divisions": (
        "division_id",
        "shape_id",
        "state",
        "division_type",
        "district_plan",
        "division_name",
        "source_id",
    ),
    "candidacies": (
        "candidacy_id",
        "election_id",
        "office_type",
        "division_id",
        "candidate_name",
        "candidate_party",
        "is_incumbent",
        "is_winner",
        "source_id",
    ),
    "precincts": (
        "precinct_id",
        "election_id",
        "cd_division_id",
        "sldu_division_id",
        "sldl_division_id",
        "locality_id",
        "locality_name",
        "precinct_name",
        "source_id",
        "shape_id",
    ),
    "sources": ("source_id", "source_name", "source_url"),
    "demographics": ("shape_id", "demographic_type", "value", "source_id"),
    "vote_totals": ("precinct_id", "candidate_id", "vote_count", "source_id"),
}


def generate_id(letter):
    """ for demo, to be replaced with something better """
    n = random.randint(100_000_000, 999_999_999)
    return f"OP{letter}ID:{n}"


def write_csv(type_, data):
    with open(type_ + ".csv", "w") as f:
        out = csv.DictWriter(f, FIELD_NAMES[type_])
        out.writeheader()
        out.writerows(data)


def process_geojson(fname):
    ignored_properties = set()
    precincts = []
    vote_totals = []

    with open(fname) as f:
        gj = json.load(f)
    for feature in gj["features"]:
        shape_id = feature["properties"]["shape_id"] = generate_id("S")
        locality_name = feature["properties"].pop("locality")
        precinct_name = feature["properties"].pop("precinct")
        for e in [ge2016, ge2017, ge2018]:
            precinct_id = generate_id("P")
            precincts.append(
                {
                    "precinct_id": precinct_id,
                    "election_id": e,
                    "locality_name": locality_name,
                    "precinct_name": precinct_name,
                    "shape_id": shape_id,
                    # TODO: district -> cd_division_id
                }
            )

        # add Vote Totals
        for propname, cid in CANDIDATES.items():
            count = feature["properties"].pop(propname)
            if count:
                count = int(float(count))
            vote_totals.append(
                {"precinct_id": precinct_id, "candidate_id": cid, "vote_count": count}
            )

    write_csv("precincts", precincts)
    write_csv("vote_totals", vote_totals)
    with open("shapes.json", "w") as f:
        json.dump(gj, f)


# write elections data
ge2016 = generate_id("E")
ge2017 = generate_id("E")
ge2018 = generate_id("E")
write_csv(
    "elections",
    [
        {
            "election_id": ge2016,
            "state": "VA",
            "date": "2016-11-08",
            "election_type": "general",
        },
        {
            "election_id": ge2017,
            "state": "VA",
            "date": "2017-11-07",
            "election_type": "general",
        },
        {
            "election_id": ge2018,
            "state": "VA",
            "date": "2018-11-06",
            "election_type": "general",
        },
    ],
)


kaine = generate_id("C")
stewart = generate_id("C")
waters = generate_id("C")
northam = generate_id("C")
gillespie = generate_id("C")
hyra = generate_id("C")
fairfax = generate_id("C")
vogel = generate_id("C")
herring = generate_id("C")
adams = generate_id("C")
trump = generate_id("C")
clinton = generate_id("C")
johnson = generate_id("C")

CANDIDATES = {
    "G18DSEN": kaine,
    "G18OSEN": waters,
    "G18RSEN": stewart,
    "G17DGOV": northam,
    "G17RGOV": gillespie,
    "G17OGOV": hyra,
    "G17DLTG": fairfax,
    "G17RLTG": vogel,
    "G17DATG": herring,
    "G17RATG": adams,
    "G16DPRS": clinton,
    "G16RPRS": trump,
    #    "G16OPRS": johnson,
}

write_csv(
    "candidacies",
    [
        {
            "candidacy_id": kaine,
            "election_id": ge2018,
            "candidate_name": "Tim Kaine",
            "candidate_party": "Democratic",
            "is_incumbent": "yes",
            "is_winner": "yes",
            "office_type": "sen",
        },
        {
            "candidacy_id": waters,
            "election_id": ge2018,
            "candidate_name": "Matt Waters",
            "candidate_party": "Libertarian",
            "is_incumbent": "no",
            "is_winner": "no",
            "office_type": "sen",
        },
        {
            "candidacy_id": stewart,
            "election_id": ge2018,
            "candidate_name": "Corey Stewart",
            "candidate_party": "Republican",
            "is_incumbent": "no",
            "is_winner": "no",
            "office_type": "sen",
        },
        {
            "candidacy_id": northam,
            "election_id": ge2017,
            "candidate_name": "Ralph Northam",
            "candidate_party": "Democratic",
            "is_incumbent": "no",
            "is_winner": "yes",
            "office_type": "gov",
        },
        {
            "candidacy_id": gillespie,
            "election_id": ge2017,
            "candidate_name": "Ed Gillespie",
            "candidate_party": "Republican",
            "is_incumbent": "no",
            "is_winner": "no",
            "office_type": "gov",
        },
        {
            "candidacy_id": hyra,
            "election_id": ge2017,
            "candidate_name": "Corey Stewart",
            "candidate_party": "Libertarian",
            "is_incumbent": "no",
            "is_winner": "no",
            "office_type": "gov",
        },
        {
            "candidacy_id": fairfax,
            "election_id": ge2017,
            "candidate_name": "Justin Fairfax",
            "candidate_party": "Democratic",
            "is_incumbent": "no",
            "is_winner": "yes",
            "office_type": "ltgov",
        },
        {
            "candidacy_id": vogel,
            "election_id": ge2017,
            "candidate_name": "Jill Vogel",
            "candidate_party": "Republican",
            "is_incumbent": "no",
            "is_winner": "no",
            "office_type": "ltgov",
        },
        {
            "candidacy_id": herring,
            "election_id": ge2017,
            "candidate_name": "Mark Herring",
            "candidate_party": "Democratic",
            "is_incumbent": "yes",
            "is_winner": "yes",
            "office_type": "ag",
        },
        {
            "candidacy_id": adams,
            "election_id": ge2017,
            "candidate_name": "John Adams",
            "candidate_party": "Republican",
            "is_incumbent": "no",
            "is_winner": "no",
            "office_type": "ag",
        },
        {
            "candidacy_id": clinton,
            "election_id": ge2018,
            "candidate_name": "Tim Kaine",
            "candidate_party": "Democratic",
            "is_incumbent": "no",
            "is_winner": "no",
            "office_type": "pres",
        },
        {
            "candidacy_id": trump,
            "election_id": ge2018,
            "candidate_name": "Donald Trump",
            "candidate_party": "Republican",
            "is_incumbent": "no",
            "is_winner": "yes",
            "office_type": "pres",
        },
    ],
)

process_geojson("VA.geojson")
