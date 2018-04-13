# py-wtd

A minimal python interface to the www.worldtradingdata.com API

## Description

Retrieve historical stock data from www.worldtradingdata.com

## Getting Started

### Dependencies

pandas
requests

### Installing

```
git clone https://github.com/jamarke/py-wtd.git`
pip install .
```

Register at https://www.worldtradingdata.com/register and get your API key.


### Examples

```
import py-wtd as wtd
wtd.ApiConfig.api_key = YOUR_API_KEY
```

Retrieve historical stock data, returns a pandas DataFrame:

`data = wtd.get('CBA.AX', date_from='2017-01-01', date_to='2018-01-01')`



## License

This project is licensed under the MIT License - see the LICENSE.md file for details
