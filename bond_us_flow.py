import os

from dataflows import Flow, validate, load, set_type, update_resource
from dataflows import add_metadata, dump_to_path


def readme(fpath='README.md'):
    if os.path.exists(fpath):
        return open(fpath).read()


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
              "title": "Open Data Commons Public Domain Dedication and License v1.0",
              'name': "open_data_commons_public_domain_dedication_and_license_v1.0"
            }
        ],
        views=[
            {
              "name": "graph",
              "title": "10 year US Government Bond Yields (Monthly granuarlity)",
              "specType": "simple",
              "spec": {"type": "line","group": "Date","series": ["Rate"]}
            }
        ],
        readme=readme()
    ),
    load(
        load_source='http://www.federalreserve.gov/datadownload/Output.aspx?rel=H15&series=0809abf197c17f1ff0b2180fe7015cc3&lastObs=&from=&to=&filetype=csv&label=include&layout=seriescolumn',
        skip_rows=[i+1 for i in range(6)],
        headers=['Date', 'Rate'],
        format='csv',
        name='monthly'
    ),
    set_type('Date', type='date', format='any', descriptor='Date in ISO 8601'),
    set_type('Rate', type='number', description='Percent per year'),
    update_resource('monthly', **{'path':'data/monthly.csv', 'dpp:streaming': True}),
    validate(),
    dump_to_path(),
)


def flow(parameters, datapackage, resources, stats):
    return bond_us


if __name__ == '__main__':
    bond_us.process()
