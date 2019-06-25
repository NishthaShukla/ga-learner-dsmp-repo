# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here

df = pd.read_csv(path)

mask = df['fico']>700

fico = len(df[mask])

total = len(df['fico'])

p_a = fico/total

print(p_a)

mask = df['purpose']=='debt_consolidation'

purpose = len(df[mask])

p_b = purpose/total

print(p_b)

df1 = df[df['purpose']=='debt_consolidation']

mask =  df1['fico']>700

both = len(df1[mask])

p_b_a = both/total

print(p_b_a)

p_a_b = p_b_a*p_a/p_b

print(p_a_b)

result = p_a_b==p_a

print(result)
# code ends here


# --------------
# code starts here

mask = df['paid.back.loan'] == 'Yes'

pbl = len(df[mask])

total = len(df)

prob_lp = pbl/total

print(prob_lp)

mask =df['credit.policy'] =='Yes'

cs = len(df[mask])

prob_cs = cs/total

new_df = df[df['paid.back.loan'] == 'Yes']

mask =new_df['credit.policy'] == 'Yes'

cs_pd = len(new_df[mask])

new_df_total = len(new_df)

prob_pd_cs = cs_pd/new_df_total

p_cs_pd = prob_pd_cs*prob_lp/prob_cs

print(prob_pd_cs)

bayes = p_cs_pd

print(bayes)
# code ends here


# --------------
# code starts here
purpose= df['purpose'].value_counts()

purpose.plot.bar()

df1 = df[df['paid.back.loan']=='No']

purpose_pd_n = df1['purpose'].value_counts()

purpose_pd_n.plot.bar()
# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()

inst_mean = df['installment'].mean()

df['installment'].hist()

df['log.annual.inc'].hist()
# code ends here


