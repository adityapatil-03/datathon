import pandas as pd
import numpy as np
import models.localizor_model as localizor_model
import models.detector_model as detector_model

start_msg = "Data processng step"
fault_start_msg = "Fault detection step"
no_fault_msg = "No fault detected"
fault_msg = "Fault detected"
localization_msg = "Fault localization step"
fault_localization_msg = "Fault localized at: "
end_msg = "Data analyzed for station:"


response_dict = {
    'fault': False,
    'dist': 0
}


def analyze_data(data):
    yield start_msg
    df = data       # data is a pandas dataframe asuumption
    yield fault_start_msg
    fault = detector_model.predict(df)
    if fault:
        response_dict['fault'] = True
        yield fault_msg
        yield localization_msg
        loc = localizor_model.predict(df)
        response_dict['dist'] = loc
        yield fault_localization_msg + str(loc) + "km from station"
    else:
        yield no_fault_msg
    yield end_msg + "x"     # x is the station name for now
    yield response_dict