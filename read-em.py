import geopandas

#prec12 = geopandas.read_file('/vsizip/SBE_PRECINCTS_09012012.zip/SBE_PRECINCTS_09012012.shp')
#prec14 = geopandas.read_file('/vsizip/SBE_PRECINCTS_20141016.zip/PRECINCTS.shp')
prec16 = geopandas.read_file('/vsizip/SBE_PRECINCTS_20160826.zip/Precincts.shp')
dist16 = geopandas.read_file('/vsizip/tl_2016_us_cd115-2264.zip/tl_2016_us_cd115.shp')

print(prec16.total_bounds)
print(dist16.total_bounds)

joined = geopandas.sjoin(prec16, dist16, how='inner', rsuffix='districts')

for index in prec16.index:
    precinct = prec16.loc[index]
    joined_districts = joined.loc[index]
    if joined_districts.ndim != 2:
        # just one yay
        continue
    districts = dist16.loc[joined_districts.index_districts]
    intersections = districts.intersection(precinct.geometry)
    districts['Fraction'] = intersections.area / precinct.geometry.area
    if districts.Fraction.max() > .99:
        # probably just a sliver
        continue
    print(precinct)
    print(districts[districts.Fraction > .01])
