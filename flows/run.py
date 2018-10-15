from dataflows import Flow, PackageWrapper, ResourceWrapper, validate
from dataflows import add_metadata, dump_to_path, load, set_type, printer


def rename(package: PackageWrapper):
    package.pkg.descriptor['resources'][0]['name'] = 'monthly'
    package.pkg.descriptor['resources'][0]['path'] = 'data/monthly.csv'
    yield package.pkg
    res_iter = iter(package)
    first: ResourceWrapper = next(res_iter)
    yield first.it
    yield from package


bond_us = Flow(
    add_metadata(
        name="bond-yields-us-10y",
        title="10 year US Government Bond Yields (long-term interest rate)",
        version="0.2.0",
        sources=[
            {
              "name": "Federal Reserve (Release H.15)",
              "path": "http://www.federalreserve.gov/releases/h15/data.htm",
              "title": "Federal Reserve (Release H.15)"
            }
        ],
        licenses=[
            {
              "id": "odc-pddl",
              "path": "http://opendatacommons.org/licenses/pddl/",
              "name": "Open Data Commons Public Domain Dedication and License v1.0"
            }
        ],
        views=[
            {
              "name": "graph",
              "title": "10 year US Government Bond Yields (Monthly granuarlity)",
              "specType": "simple",
              "spec": {"type": "line","group": "Date","series": ["Rate"]}
            }
        ]
    ),
    load(
        load_source='http://www.federalreserve.gov/datadownload/Output.aspx?rel=H15&series=0809abf197c17f1ff0b2180fe7015cc3&lastObs=&from=&to=&filetype=csv&label=include&layout=seriescolumn',
        skip_rows=[i+1 for i in range(6)],
        headers=['Date', 'Rate']
    ),
    set_type('Date', type='date', format='any', descriptor='Date in ISO 8601'),
    set_type('Rate', type='number', description='Percent per year'),
    rename,
    validate(),
    printer(),
    dump_to_path(),
)


if __name__ == '__main__':
    bond_us.process()
