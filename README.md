<a className="gh-badge" href="https://datahub.io/core/bond-yields-us-10y"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="badge" /></a>

10 year nominal yields on US government bonds from the Federal Reserve. The 10
year government bond yield is considered a standard indicator of long-term
interest rates.

## Data

Data comes from the [Release H.15 from the Federal Reserve - Selected Interest
Rates Daily][fed] specifically the [10 year US Treasury (monthly,
csv)][fed-csv].

[fed]: http://www.federalreserve.gov/releases/h15/data.htm
[fed-csv]: http://www.federalreserve.gov/datadownload/Output.aspx?rel=H15&series=0809abf197c17f1ff0b2180fe7015cc3&lastObs=&from=&to=&filetype=csv&label=include&layout=seriescolumn

## Preparation

You will need Python 3.6 or greater and dataflows library to run the script

To update the data run the process script locally:

```
# Install necessary libraries
pip install -r scripts/requirements.txt

# Update the data
./scripts/process.sh

# Run the script
python scripts/bond_us_flow.py
```

Note we keep a copy of the raw data from the Federal Reserve (pre-tidying) in
`archive`.

## Automation

Up-to-date (auto-updates every month) bond-yields-us-10y dataset could be found on the datahub.io: https://datahub.io/core/bond-yields-us-10y

# License

Licensed under the [Public Domain Dedication and License][pddl] (assuming
either no rights or public domain license in source data).

[pddl]: http://opendatacommons.org/licenses/pddl/1.0/
