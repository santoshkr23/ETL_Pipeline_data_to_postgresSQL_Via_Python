import pandas as pd
from sqlalchemy import create_engine

# Database connection parameters
db_username = "postgres"
db_password = "postgres"
db_host = "localhost"
db_port = "5432"
db_name = "My_database"

# Database connection URL
db_url = f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create SQLAlchemy engine
engine = create_engine(db_url)

# Load data from Excel file
excel_file = r"C:\Users\santo\Downloads\sales.xlsx"
with pd.ExcelFile(excel_file) as xls:
    df = pd.read_excel(xls)
# Convert "Review Rating" column to string
df['Review Rating'] = df['Review Rating'].astype(str)
# Write DataFrame to PostgreSQL
table_name = 'Salesdata'
df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

print("Data loaded into PostgreSQL successfully.")
