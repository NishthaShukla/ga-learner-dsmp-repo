# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)

data['Gender'].replace('-','Agender',inplace=True)

gender_count= data['Gender'].value_counts()

gender_count.plot(kind='bar')
#Code starts here 




# --------------
#Code starts here
alignment = data['Alignment'].value_counts()

plt.pie(alignment)

plt.title('Character Alignment')


# --------------
#Code starts here
sc_df = data[['Strength','Combat']].copy()

sc_covariance = sc_df.cov().iloc[0,1]

sc_strength = sc_df['Strength'].std()

sc_combat = sc_df['Combat'].std()

sc_pearson = sc_covariance / (sc_strength*sc_combat)

ic_df = data[['Intelligence','Combat']].copy()

ic_covariance = ic_df.cov().iloc[0,1]

ic_intelligence = ic_df['Intelligence'].std()

ic_combat = ic_df['Combat'].std()

ic_pearson = ic_covariance/(ic_intelligence*sc_combat)

print(ic_pearson)
print(sc_pearson)


# --------------
#Code starts here

total_high = data['Total'].quantile(0.99)

super_best = data[data['Total']>total_high]

super_best_names = super_best['Name'].tolist()

print(super_best_names)


# --------------
#Code starts here

fig, (ax_1,ax_2,ax_3) = plt.subplots(nrows=1, ncols=3,figsize=(20,10))

ax_1.boxplot(data['Intelligence'])

ax_1.set_title('Intelligence')

ax_2.boxplot(data['Speed'])

ax_2.set_title('Speed')

ax_3.boxplot(data['Power'])

ax_3.set_title('Power')




