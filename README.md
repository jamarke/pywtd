# pywtd

A minimal python interface to the www.worldtradingdata.com API

## Description

Retrieve daily historical stock data from www.worldtradingdata.com. Fields returned are open price, close price, high,
low and volume.


## Getting Started

### Dependencies

* pandas
* requests

### Installing

```
git clone https://github.com/jamarke/pywtd.git
pip install .
```

Register at https://www.worldtradingdata.com/register and get your API key.


### Examples

```
import pywtd as wtd
wtd.ApiConfig.api_key = 'YOUR_API_KEY'
```

Retrieve historical stock data, returns a pandas DataFrame:

```
data = wtd.get('AAPL', date_from='2017-01-01', date_to='2018-04-12')
data.tail()
```

Result:

date | open | close | high | low | volume
--- | --- | --- | --- | --- | --- |
2018-04-06 | 170.97 | 168.38 | 172.48 | 168.20 | 35005290
2018-04-09 | 169.88 | 170.05 | 173.09 | 169.85 | 29017718
2018-04-10 | 173.00 | 173.25 | 174.00 | 171.53 | 28614241
2018-04-11 | 172.23 | 172.44 | 173.92 | 171.70 | 22431640
2018-04-12 | 173.41 | 174.14 | 175.00 | 173.04 | 22889285

To save as `.csv`:

`data.to_csv('data.csv')`

## Notes
For ASX stocks, use the ticker format 'CBA.AX'

This is a quick and dirty work in progress

To do: add interface to detailed quote

## License

This project is licensed under the MIT License - see the LICENSE file for details
