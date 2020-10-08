import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')

GDP_share_pct=pd.read_csv('GDP Share in Percent.csv',index_col=0)

print(GDP_share_pct)

sectors=np.array(GDP_share_pct.columns)
year=np.array(GDP_share_pct.index)

plt.plot(year,GDP_share_pct.iloc[:,0:])
plt.xticks(rotation=90)

plt.xlabel('Year')
plt.ylabel('Percentage of GDP')
plt.title('Sector-Wise Share of GDP at 2004-05 prices')
plt.legend(sectors,prop={'size':10})
plt.tight_layout()

plt.show()
