#%% 
import pandas as pd 
import time 
import client

pd.set_option('display.max_columns',100)
pd.set_option('precision', 3)
pd.set_option('display.float_format', lambda x: '%.3f' % x)


api_key = ""
api_secret = ""
subaccount_name = ""  # Main Account

rest_api = client.FtxClient(api_key, api_secret, subaccount_name)

response = rest_api.get_market('LUNA-PERP')
df_market = pd.Series(response)
# %% 
end_time = time.time()
start_time = end_time - 86400 # 1 day
response = rest_api.get_historical_price('LUNA-PERP', 3600, start_time, end_time)
df_candles = pd.DataFrame(response)

# %% requires authentication
response = rest_api.get_positions()
df_positions = pd.DataFrame(response)

# %%
response = rest_api.get_balances()
df_balance = pd.DataFrame(response)
