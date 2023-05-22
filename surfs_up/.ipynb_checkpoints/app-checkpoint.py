import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from sqlalchemy.ext.declarative import declarative_base


from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
con = engine.connect()
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
#Base.prepare(autoload_with=engine)
# reflect the tables
Base.prepare(engine, reflect=True)


# Import the dependencies.
from sqlalchemy import create_engine, inspect
from sqlalchemy import Column, Integer, String, Float, Date

from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarating class definitions to produce Table objects
Base = declarative_base()
inspector = inspect(engine)
inspector.get_table_names()



#Save references to the table. Join measurement and station keys.
# View all of the classes that automap found
Base.classes.keys()
# Get the table names using `inspect()`.
inspector = inspect(engine)
inspector.get_table_names()

# Get a list of column names and types
columns = inspector.get_columns('measurement')
for c in columns:
    print(c['measure'], c["station"])
# Join all the order names for the measurement and station classes. 
# This returns a warning so the query should be filtered on a common order name.
session.query(measurement.order, station.order).limit(200).all()


# Create our session (link) from Python to the DB
session = Session(engine)
#----------------------------#
# 1. Start at the homepage. List all the available routes.

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def home():
    return "Hello there!"

@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/api/v1.0/stations<br/>"
        f"//api/v1.0/tobs<br/>"
        f"/api/api/v1.0/<start<br/>"
        f"/api/api/v1.0/<start>/<end><br/>")


#----------------------------#
# 2. /api/v1.0/precipitation
# Convert the query results from your precipitation analysis
# (i.e. retrieve only the last 12 months of data) to a dictionary 
 def retrieve_precipitation_data():
    precip_data = [
        {"Precipitation Data": "precip_df"}]

        return precipitation_data

# Define what to do when a user hits the precipitation route.
@app.route("/api/v1.0/precipitation>")
def get_precipitation_data():
    precipitation_data = retrieve_precipitation_data()

# Use date as the key and prcp as the value.
    analysis_dict = {"date": "prcp"}
#Return the JSON representation of your dictionary.
    return jsonify(analysis_dict)


#----------------------------#
# 3. /api/v1.0/stations
# Return a JSON list of stations from the dataset.

@app.route("/api/api/v1.0/stations>")
station_list = [
    {'Stations': station_list}

]
def stations():
    """Return the stations data as json"""

    return jsonify(station_list)

if __name__ == '__main__':
    app.run()
#----------------------------#
# 4. /api/v1.0/tobs
#Query the dates and temperature observations of the most-active station for the previous year of data.
#Return a JSON list of temperature observations for the previous year.


#----------------------------#
# 5. /api/v1.0/<start> and /api/v1.0/<start>/<end>
#Return a JSON list of :
        # the minimum temperature, the average temperature, and the maximum temperature
        #  for a specified start or start-end range.

# For a specified start, calculate:
        # TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

# For a specified start date and end date, calculate:
        # TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

#----------------------------#
#Hints
#Join the station and measurement tables for some of the queries.

#Use the Flask jsonify function to convert your API data to a valid JSON response object.