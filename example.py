import pywtd as wtd

wtd.ApiConfig.api_key = 'YOUR_API_KEY'

# using just a start date
aapl = wtd.get('AAPL', '2010-01-01')

print(aapl.tail())

# using a start and end date:
cba = wtd.get('CBA.AX', '2017-01-01', '2018-01-01')

print(cba.tail())