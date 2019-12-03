import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String
import glob
import os
from sqlalchemy import MetaData
from sqlalchemy.orm import mapper

# SQL Alchemy setup

# Create engine that will allow us to communicate with database
engine = create_engine('sqlite:///product_dbase.sqlite', echo=False)

# Creating session which is the middle ground to talk to our engine
Session = sessionmaker(bind=engine)
session = Session()

# Map which table in database will be related to each class
Base = declarative_base()

# Create a metadata instance
# A metadata is an object container that will store attributes and name of table
metadata = MetaData(engine)

# Define structure of table


class product_table(object):
    def __init__(self, number, description, ref_des):
        self.product_id = product_id
        self.station = station
        self.time = time
        self.result = result
        self.employee_id = employee_id

    def __repr__(self):
        return f'{self.product_id,self.station,self.time,self.result,self.employee_id}'


# Declaring a table
# Defining a function that defines table, we define this function so that we can keep table names dynamic
# That is, we can have multiple tables in database and each table can have a different name
def table_definition(table_name):
    # Define table structure, here table_name varies
    # We want to make table_define available outside function so we declare it as a function attribute
    table_definition.table_define = Table(table_name, metadata,
                                          Column('id', Integer,
                                                 primary_key=True),
                                          Column('product_id', String),
                                          Column('station', String),
                                          Column('time', String),
                                          Column('result', String),
                                          Column('employee_id', String)
                                          )

    # Create table
    # Note that we used the engine from function
    metadata.create_all(engine)

    # Use mapper to define components of class as well as table definition together at once
    mapper(product_table, table_definition.table_define, non_primary=True)


# CREATING A DUMMY BLANK TABLE FOR PRIMARY MAPPER
# This avoids error: Class already has a primary mapper defined
# We made non_primary=True in table_definition function mapper
# This is the work around I could use, maybe there is another way

# Define table structure, here table_name varies
table_define_dummy = Table('dummy_table', metadata,
                           Column('id', Integer, primary_key=True),
                           Column('product_id', String),
                           Column('station', String),
                           Column('time', String),
                           Column('result', String),
                           Column('employee_id', String)
                           )

# Create table
metadata.create_all(engine)

# Use mapper to define components of class as well as table definition together at once
mapper(product_table, table_define_dummy)

# This function will create a separate table for each csv file, if you have multiple csv files
# Name of table will be extracted from file name. File name contains product name.
# Each table will be identified by product name
# It will read each excel file in the folder and insert bom into table


def create_table(folder_of_files):

    # Get list of files in folder
    files = glob.glob(os.path.join(folder_of_files, "*.csv"))

    # Loop through all files in list
    for file_name in files:

        # Read file into dataframe
        csv_data = pd.read_csv(file_name)

        # Convert dataframe to list and store in same variable
        csv_data = csv_data.values.tolist()

        # Get table name from file name. This will be our table name.
        table_name_from_file = file_name.split('/')[8][:-4]

        # Use table_definition function to define table structure
        table_definition(table_name_from_file)

        # Loop through list of lists, each list in create_bom_table.xls_data is a row
        for row in csv_data:

            # Each element in the list is an attribute for the table class
            # Iterating through rows and inserting into table
            ins = table_definition.table_define.insert().values(
                product_id=row[0], station=row[1], time=row[2], result=row[3], employee_id=row[4])
            conn = engine.connect()
            conn.execute(ins)


# Calling function, argument is path of folder where all CSV files are stored
create_table("path of folder where csv files are stored")
