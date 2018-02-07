import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the measurements and stations tables
Measurements = Base.classes.measurements
Stations = Base.classes.stations

# Create our session (link) from Python to the DB
session = Session(engine)

# Flask Setup
app = Flask(__name__)

# Flask Route
@app.route("/")
def welcome():
    """List available api routes."""
    return (
        f"Precipitation:<br/>"
        f"/api/v1.0/precipitation<br/>"

        f"/api/v1.0/stations"
        f"- List of Stations<br/>"

        f"/api/v1.0/tobs"
        f"- List of Temperature Observations(tobs)<br/>"

        f"/api/v1.0/<start>"
        f"- Minimum Temperature, Average Temperature, and Max Temperature for Start<br/>"

        f"/api/v1.0/<start>/<end>"
        f"- Minimum Temperature, Average Temperature, and Max Temperature for Start/End<br/>"
    )


if __name__ == '__main__':
    app.run()
