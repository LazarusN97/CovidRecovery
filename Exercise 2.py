#====================================================================================#
# PURPOSE: Simple intoduction in pandas & numpy - HW2
# 
# Date:   May 2024           
# Author: Lazaros Nikolaos
#====================================================================================#
#import the forementioned libraries
import pandas as pd
import numpy as np

#Laod the data but only 10000 first rows from each csv file
df1 = pd.read_csv('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/public_up_to_150k_1_230930.csv',nrows=1000000)
print(df1.head())
df2 = pd.read_csv('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/public_up_to_150k_2_230930.csv',nrows=1000000)
df3 = pd.read_csv('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/public_up_to_150k_3_230930.csv',nrows=1000000)
df4 = pd.read_csv('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/public_up_to_150k_4_230930.csv',nrows=1000000)
df5 = pd.read_csv('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/public_up_to_150k_5_230930.csv',nrows=1000000)
df6 = pd.read_csv('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/public_up_to_150k_6_230930.csv',nrows=1000000)
df7 = pd.read_csv('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/public_up_to_150k_7_230930.csv',nrows=1000000)
df8 = pd.read_csv('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/public_up_to_150k_8_230930.csv',nrows=1000000)
df9 = pd.read_csv('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/public_up_to_150k_9_230930.csv',nrows=1000000)
df10 = pd.read_csv('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/public_up_to_150k_10_230930.csv',nrows=1000000)
df11 = pd.read_csv('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/public_up_to_150k_11_230930.csv',nrows=1000000)
df12 = pd.read_csv('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/public_up_to_150k_12_230930.csv',nrows=1000000)

jobCity = pd.read_csv('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/Job Postings - City - Weekly.csv')
jobCounty = pd.read_csv('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/Job Postings - County - Weekly.csv')
jobNational = pd.read_csv('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/Job Postings - National - Weekly.csv')
dfState = pd.read_csv('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/Job Postings - State - Weekly.csv')
dfIndustry = pd.read_csv('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/Job Postings Industry Shares - National - 2020.csv')

pop = pd.read_excel('/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/RawData/co-est2023-pop.xlsx')
pop.head()





# Concatenate DataFrames by rows
df_concat = pd.concat([df1, df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12], axis=0, ignore_index=True)
print(df_concat)

##lets convert the data types to save more memory
# Function to convert data types
def convert_dtypes(df):
    for col in df.columns:
        if df[col].dtype == np.float64:
            df[col] = df[col].astype(np.float32)
        elif df[col].dtype == np.int64:
            df[col] = df[col].astype(np.int32)
        # Optionally handle string conversion if needed
        # elif df[col].dtype == object:
        #     try:
        #         df[col] = df[col].astype(np.str_)
        #     except:
        #         pass
    return df

df_concat = convert_dtypes(df_concat)
df_concat.info()

#lets see our variables
print(df_concat.columns)
#basic summary of our df
# Get a summary of the DataFrame
df_concat.info()
df_concat.head()

#Clean the data
#lets check for NAs
#number of na
print(df_concat.isna().sum())

#we want to work on columns that have to do with loan risk assesment and the borrowers capability of paying the loan back.
#So for loan risk assessment we focus on columns that provide insight into the financial health and stability of the borrower.
#some of these columns are subsetted in the data frame bellow

columns_to_keep = [
    'DateApproved',
    'CurrentApprovalAmount',
    'LoanNumber',
    'BorrowerCity',
    'BorrowerState',
    'BorrowerZip',
    'LoanStatus',
    'Term',
    'SBAGuarantyPercentage',
    'InitialApprovalAmount',
    'UndisbursedAmount',
    'BusinessAgeDescription',
    'JobsReported',
    'NAICSCode',
    'Race',
    'Ethnicity',
    'Gender',
    'Veteran',
    'BusinessType',
    'ForgivenessAmount',
    'ForgivenessDate'
]

df_final = df_concat[columns_to_keep]
len(df_final)
df_final.info()
print(df_final.isna().sum())

#lets drop the rest of the NA left
df_final= df_final.dropna()
df_final.info()




##EDA
##import packages for EDA
import seaborn as sns
import matplotlib.pyplot as plt
#simple describe command to see some metrics like the mean, median, min and max calue for each variable.
df_final.describe()


##some histograms to gain insight on our data
df_final.hist(figsize=(14, 10), bins=30, edgecolor='black')
plt.tight_layout()
plt.show()

#lets merge the data based on geography and time
df_final.head()
pop.head()


##lets calculate the loan pef 100k


# Analyze Data
# Merge PPP and population data by state
df_final['BorrowerState'] = df_final['BorrowerState'].str.upper()
state_loan_sum = df_final.groupby('BorrowerState')['CurrentApprovalAmount'].sum().reset_index()

pop['geographic area'] = pop['geographic area'].astype(str).str.zfill(2)
pop['geographic area'] = pop['geographic area'].str.split(',').str[-1].str.strip()
state_population = pop.groupby('geographic area').sum().reset_index()

# State abbreviation to full name mapping
state_mapping = {
    'CA': 'California', 'NY': 'New York', 'TX': 'Texas', 'FL': 'Florida', 'WA': 'Washington',
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CO': 'Colorado',
    'CT': 'Connecticut', 'DE': 'Delaware', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho',
    'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky',
    'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan',
    'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska',
    'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NC': 'North Carolina',
    'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania',
    'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'UT': 'Utah',
    'VT': 'Vermont', 'VA': 'Virginia', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
}

# Add full state names to df_abbrev using the mapping
state_loan_sum['geographic area'] = state_loan_sum['BorrowerState'].map(state_mapping)

#aggregate
merged_df = pd.merge(state_loan_sum, state_population, on='geographic area')

#save the cleaned merged data to output folder
output_file_path = '/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/Output/CleanMergeData.csv'
merged_df.to_csv(output_file_path, index=False)
#loan ammount per capita
merged_df['percapita'] = merged_df['CurrentApprovalAmount'] / merged_df.iloc[:, 4]

#per 100.000 
merged_df['LoanAmount_per_100k'] = merged_df['percapita'] * 100000



###lets create the csv file

# create
output_df = merged_df[['geographic area','LoanAmount_per_100k']]

#save to csv
output_file_path = '/Users/lazarus/Library/Mobile Documents/com~apple~CloudDocs/MSc Statistics/Data Engineer/CovidRecovery/CSV/loan_amount_per_100k.csv'
output_df.to_csv(output_file_path, index=False)


