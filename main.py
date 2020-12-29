from handlers import aei
from handlers import atlantic_council
import pandas as pd

atlantic_council_data=atlantic_council.get_data()
aei_data=aei.get_data()

main_data=pd.DataFrame()
main_data=main_data.append(atlantic_council_data)
main_data=main_data.append(aei_data)

main_data.to_csv('./outputs/main_data.csv', index=False)
