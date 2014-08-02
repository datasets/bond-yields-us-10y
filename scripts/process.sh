# download it
curl "http://www.federalreserve.gov/datadownload/Output.aspx?rel=H15&series=0809abf197c17f1ff0b2180fe7015cc3&lastObs=&from=&to=&filetype=csv&label=include&layout=seriescolumn" > archive/h15-m.csv

echo "Date,Rate" > data/monthly.csv
cat archive/h15-m.csv | tail -n+7 | sed "s/^\(.......\)/\1-01/" | sed "s///g" >> data/monthly.csv

