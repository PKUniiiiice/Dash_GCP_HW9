import pandas as pd
import json

# read data
us_dise_ind = pd.read_csv('./data/us_chronic_disease_indicators.csv')

# Question 1
def data4q1():
    us_dise_ind1 = us_dise_ind[(us_dise_ind['topic'] == 'Cardiovascular Disease') &
                (us_dise_ind['locationabbr'] == 'MI') &
                (us_dise_ind['stratification1'].isin(['Male', 'Female'])) &
                (us_dise_ind['datavaluetypeid'] == 'CRDPREV')]
    
    return (list(us_dise_ind1['question'].unique()), us_dise_ind1)

# Question 2
def data4q2():
    us_dise_ind2 = us_dise_ind[
                (~us_dise_ind['locationabbr'].isin(['US','PR', 'GU'])) &
                (us_dise_ind['question'] == 'Alcohol use among youth')  &
                (us_dise_ind['stratificationcategoryid1'] == 'OVERALL')]

    return (sorted(us_dise_ind2['yearstart'].unique()), us_dise_ind2)

# Question 3
def data4q3():
    us_dise_ind3 = us_dise_ind.loc[(us_dise_ind['locationabbr'] =='US') &
                    (us_dise_ind['datavaluetype'] == 'Average Annual Crude Rate')]

    return (list(us_dise_ind3['question'].unique()), us_dise_ind3)

# Question 4
def data4q4():
    us_dise_ind4 = us_dise_ind[(us_dise_ind['yearstart'] == 2021) & (~us_dise_ind['locationabbr'].isin(['US','PR', 'GU'])) &
           (us_dise_ind['question'] == 'Obesity among adults aged >= 18 years') &
           (us_dise_ind['datavaluetypeid'] == 'AGEADJPREV')]


    return (list(us_dise_ind4.loc[us_dise_ind4['stratificationcategory1'] == 'Race/Ethnicity']['stratification1'].unique()),
           us_dise_ind4)
    
def get_geojson():
    return json.load(open('./data/us_states_v2.geojson', 'r'))