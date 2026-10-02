import pandas as pd
from sqlalchemy import create_engine 
import os           

df = pd.read_csv("customer_shopping_behavior.csv")
df.head() # top 5 rows of dataset
df.info() # summary of dataset
print(df.describe(include='all')) # statistical summary of dataset
print(df.isnull().sum()) # check for missing values

# we got to know that review rating is a categorical variable and it has missing values. We will fill the missing values with the mean or median of the review rating column.
#here the beginner will fill with overall median 
# but this skews and add outliers to the data. So we will fill with median of each product category.

#to find median in each category 
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum()) # check for missing values after filling

# this is called cleaning in right way 
# this give accurate and trustworthy data for analysis.

#since the column name contains uppercase as well as spacing , this create problem in future while calling the column name. So we will rename the column names to lowercase and replace space with underscore. (this is called snake casing)

df.columns = df.columns.str.lower().str.replace(' ', '_') # rename columns to snake case
df = df.rename(columns =  {'purchase_amount_(usd)': 'purchase_amount_usd'}) # rename the column name with special character
print(df.columns) # check the column names after renaming


#creating a new column to group by ages - young adult , adult , middle age , senior
labels = ['young adult', 'adult', 'middle age', 'senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels) # qcut is used to divide the data into equal quantiles based on the age column
print(df[['age', 'age_group']].head()) # check the new column with age and age group


# create purchase_frequency_days 
# cuurently the purchase frequency is in text quaterlt , monthly , weekly , daily. We will convert this into number of days.

frequency_mapping = {
    'Fortnightly': 14,
    'Monthly': 30,
    'Quarterly': 90,
    'Weekly': 7,
    'Daily': 1,
    'Annually': 365,
    'Every 3 Months': 90,
    'Every 6 Months': 180,
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping) # map the purchase frequency to number of days

print(df[['purchase_frequency_days', 'frequency_of_purchases']].head()) # check the new column with purchase frequency in days and original frequency column

df[['discount_applied' , 'promo_code_used']].head(10) # check the first 10 rows of discount_applied and promo_code_used columns

# since both have almost same values because if promo code is used then discount is applied. but sometimes discount will be applied without promo code , 
# so we need to check is any of the one column is redundant are the values of both column same 

print((df['discount_applied'] == df['promo_code_used']).all()) # check if both columns have same values

# since we get the above result as true , means the columns are redundant and we can drop one of the column. We will drop the promo_code_used column.
df = df.drop(columns=['promo_code_used'])
print(df.columns)

#intsall  pip install psycopg2-binary sqlalchemy 
#connect to postgresql database and create a table and insert the data into the table
username = 'postgres'
password = os.getenv('pass')  # get the password from .env file
host = 'localhost'
port = '5432'
database = 'Customer_behavior'

engine = create_engine(
    f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
)

table_name = 'customer_shopping_behavior'

df.to_sql(
    table_name,
    engine,
    if_exists='replace',
    index=False
)

print(f"Data inserted into {table_name} table in {database} database successfully!")

