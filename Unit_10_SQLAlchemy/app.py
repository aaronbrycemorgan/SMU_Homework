from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
engine = create_engine("sqlite:///Desktop/SMUGitLab/SMU_Homework/Unit_10_SQLAlchemy/Resources//hawaii.sqlite")
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Welcome to the Weater API!<br/>"
        f"<br/>"
        f"Available Routes:<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation"
        f"<br/>"
        f"*this query looks at all the precipation measurements in the database"
        f"<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation/2016-08-23/2017-08-23"
        f"<br/>"
        f"*this query looks at all the precipation measurments between the date frame"
        f"<br/>"
        f"<br/>"
        f"/api/v1.0/stations"
        f"<br/>"
        f"*this query looks at how many measurments each station had"
        f"<br/>"
        f"<br/>"
        f"/api/v1.0/year"
        f"<br/>"
        f"*this query looks at a years worth of measurements for the most active station"
        f"<br/>"
        f"<br/>"
        f"/api/v1.0/min_max_avg_trip/2012-02-28/2012-03-05"
        f"<br/>"
        f"*this query will look at the min, max, and average temp for a specific date frame"
        f"<br/>"
        f"<br/>"
        f"/api/v1.0/rainfall_trip/2011-02-28/2011-03-05"
        f"<br/>"
        f"*this query will look at the amount of rainfall per weather station for the date frame"


    )
@app.route("/api/v1.0/precipitation/")
def get_precipitation():
    conn = engine.connect()
    precipQuery = f"""
                SELECT
                    date,
                    prcp
                FROM
                    measurement
                """
    df = pd.read_sql(precipQuery, conn)
    return jsonify(df.to_json())

@app.route("/api/v1.0/precipitation/<start_date>/<end_date>")
def get_precipitation_forDates(start_date, end_date):
    conn = engine.connect()
    precipQuery = f"""
                SELECT
                    date,
                    prcp
                FROM
                    measurement
                WHERE
                    date > '{start_date}'
                    AND date <= '{end_date}'
                """
    df = pd.read_sql(precipQuery, conn)
    return jsonify(df.to_json())

@app.route("/api/v1.0/stations")
def get_stations():
    conn = engine.connect()
    station_query = f"""
    SELECT station.station, COUNT(measurement.station)
    FROM station 
	JOIN measurement
    ON station.station = measurement.station
	GROUP BY station.station
	ORDER BY COUNT(measurement.id) DESC;
    """
    result = pd.read_sql(station_query, conn)
    return jsonify(result.to_json())

@app.route("/api/v1.0/year")
def get_year():
    conn = engine.connect()
    year_query = f"""
    SELECT date, tobs FROM measurement
    WHERE station = "USC00519281"
    AND date > "2016-08-23"
    AND date < "2017-08-23";
    """
    result = pd.read_sql(year_query, conn)
    return jsonify(result.to_json())

@app.route("/api/v1.0/min_max_avg_trip/<start_date>/<end_date>")
def get_min_max_avg(start_date, end_date):
    conn = engine.connect()
    trip_query = f"""
    SELECT min(tobs), avg(tobs), max(tobs) FROM measurement
    WHERE date >= '{start_date}'
    AND date <= '{end_date}';
    """
    result = pd.read_sql(trip_query, conn)
    return jsonify(result.to_json())

@app.route("/api/v1.0/rainfall_trip/<start_date>/<end_date>")
def get_rainfall(start_date, end_date):
    conn = engine.connect()
    rainfall_query = f"""
    SELECT SUM(measurement.prcp), station.station, station.name, station.latitude, station.longitude, station.elevation
    FROM station 
	JOIN measurement
    ON station.station = measurement.station
	WHERE date >= '{start_date}'
	AND date <= '{end_date}'
	GROUP BY station.station
	ORDER BY SUM(measurement.prcp) DESC;
    """
    result = pd.read_sql(rainfall_query, conn)
    return jsonify(result.to_json())

if __name__ == "__main__":
    app.run(debug=True)