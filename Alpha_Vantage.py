from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
ts = TimeSeries(key='5B198LJIFDY5IEXO', output_format='pandas')
data, meta_data = ts.get_daily_adjusted(symbol='MSFT', outputsize='compact')
pprint(data)
