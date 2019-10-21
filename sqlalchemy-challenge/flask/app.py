import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/yy-mm-dd<br/>"
        f"/api/v1.0/yy-mm-dd/yy-mm-dd"

    )


@app.route("/api/v1.0/precipitation")
def precip():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    precipitation = session.query(Measurement.date,Measurement.prcp).all()

    session.close()

    all_prcp = list(np.ravel(precipitation))

    return jsonify(all_prcp)



@app.route("/api/v1.0/stations")
def stations():

    session = Session(engine)


    station = session.query(Station.station,Station.name,Station.latitude,Station.longitude,Station.elevation).all()

    session.close()

    all_stations = list(np.ravel(station))

    return jsonify(all_stations)



@app.route("/api/v1.0/tobs")
def tobs():

    session = Session(engine)

    tobs = session.query(Measurement).order_by(Measurement.date.desc()).limit(1).all()

    for to in tobs:
        print("station: {0}, date: {1}, precip: {2}".format(to.station , to.date , to.prcp))
        filter_date = to.date
    
    from datetime import datetime

    format_string = "%Y-%m-%d"

    datetime_object = datetime.strptime(filter_date, format_string).date()

    filter_date = datetime_object.replace(year = datetime_object.year - 1)

    print(filter_date)


    tobs = session.query(Measurement.date,Measurement.tobs).filter(Measurement.date > filter_date).all()

    session.close()

    all_tobs = list(np.ravel(tobs))

    return jsonify(all_tobs)


@app.route("/api/v1.0/<startdate>")
def dates1(startdate):

    session = Session(engine)

    format_string = "%Y-%m-%d"
    from datetime import datetime
    datetime_object = datetime.strptime(startdate, format_string).date()
    
 
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    temprange = session.query(*sel).filter(Measurement.date >= datetime_object).all()
    
    all_trange = list(np.ravel(temprange))

    return jsonify(all_trange)



@app.route("/api/v1.0/<startdate>/<enddate>")
def dates2(startdate,enddate):

    session = Session(engine)

    format_string = "%Y-%m-%d"
    from datetime import datetime
    datetime_object = datetime.strptime(startdate, format_string).date()
    datetime_object_2 = datetime.strptime(enddate, format_string).date() 
 
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    temprange = session.query(*sel).filter(Measurement.date >= datetime_object).filter(Measurement.date < datetime_object_2).all()
    
    all_trange = list(np.ravel(temprange))

    return jsonify(all_trange)



if __name__ == '__main__':
    app.run(debug=True)
