import pandas as pd

period = pd.Period('2024-01', freq='M')
future_period = period + 3
print("Future Period:", future_period)
past_period = period - 2
print("Past Period:", past_period)

#Constructing range of periods
periods_range = pd.period_range(start='2024-01', end='2024-12', freq='M')
print("Periods Range:", periods_range)
