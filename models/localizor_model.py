import pickle

model = pickle.load(open('models/et_model.sav', 'rb'))

fields = ['energy_phase_A_current','energy_phase_B_current','energy_phase_C_current','distance_phase_A_current','distance_phase_B_current',
          'distance_phase_C_current','rms_phase_A_current','rms_phase_B_current','rms_phase_C_current','kurtosis_phase_A_current',
          'kurtosis_phase_B_current','kurtosis_phase_C_current','skewness_phase_A_current','skewness_phase_B_current','skewness_phase_C_current',
          'maxFrequency_phase_A_current','maxFrequency_phase_B_current','maxFrequency_phase_C_current','powerBandwidth_phase_A_current',
          'powerBandwidth_phase_B_current','powerBandwidth_phase_C_current','auc_phase_A_current','auc_phase_B_current','auc_phase_C_current',
          'pk_pk_distance_phase_A_current','pk_pk_distance_phase_B_current','pk_pk_distance_phase_C_current','slope_phase_A_current','slope_phase_B_current',
          'slope_phase_C_current','shannon_entropy_phase_A_current','shannon_entropy_phase_B_current','shannon_entropy_phase_C_current',
          'mean_phase_A_current','mean_phase_B_current','mean_phase_C_current','geometric_mean_phase_A_current','geometric_mean_phase_B_current',
          'geometric_mean_phase_C_current','harmonic_mean_phase_A_current','harmonic_mean_phase_B_current','harmonic_mean_phase_C_current',
          'variance_phase_A_current','variance_phase_B_current','variance_phase_C_current','stdev_phase_A_current','stdev_phase_B_current',
          'stdev_phase_C_current','median_phase_A_current','median_phase_B_current','median_phase_C_current','covariance_phase_A_B_current',
          'covariance_phase_A_C_current','covariance_phase_B_C_current','correlation_phase_A_B_current','correlation_phase_A_C_current',
          'correlation_phase_B_C_current','max_phase_A_current','max_phase_B_current','max_phase_C_current','min_phase_A_current','min_phase_B_current',
          'min_phase_C_current','energy_phase_A_voltage','energy_phase_B_voltage','energy_phase_C_voltage','distance_phase_A_voltage',
          'distance_phase_B_voltage','distance_phase_C_voltage','rms_phase_A_voltage','rms_phase_B_voltage','rms_phase_C_voltage','kurtosis_phase_A_voltage',
          'kurtosis_phase_B_voltage','kurtosis_phase_C_voltage','skewness_phase_A_voltage','skewness_phase_B_voltage','skewness_phase_C_voltage',
          'maxFrequency_phase_A_voltage','maxFrequency_phase_B_voltage','maxFrequency_phase_C_voltage','powerBandwidth_phase_A_voltage',
          'powerBandwidth_phase_B_voltage','powerBandwidth_phase_C_voltage','auc_phase_A_voltage','auc_phase_B_voltage','auc_phase_C_voltage',
          'pk_pk_distance_phase_A_voltage','pk_pk_distance_phase_B_voltage','pk_pk_distance_phase_C_voltage','slope_phase_A_voltage','slope_phase_B_voltage',
          'slope_phase_C_voltage','shannon_entropy_phase_A_voltage','shannon_entropy_phase_B_voltage','shannon_entropy_phase_C_voltage',
          'mean_phase_A_voltage','mean_phase_B_voltage','mean_phase_C_voltage','geometric_mean_phase_A_voltage','geometric_mean_phase_B_voltage',
          'geometric_mean_phase_C_voltage','harmonic_mean_phase_A_voltage','harmonic_mean_phase_B_voltage','harmonic_mean_phase_C_voltage',
          'variance_phase_A_voltage','variance_phase_B_voltage','variance_phase_C_voltage','stdev_phase_A_voltage','stdev_phase_B_voltage',
          'stdev_phase_C_voltage','median_phase_A_voltage','median_phase_B_voltage','median_phase_C_voltage','covariance_phase_A_B_voltage',
          'covariance_phase_A_C_voltage','covariance_phase_B_C_voltage','correlation_phase_A_B_voltage','correlation_phase_A_C_voltage',
          'correlation_phase_B_C_voltage','max_phase_A_voltage','max_phase_B_voltage','max_phase_C_voltage','min_phase_A_voltage','min_phase_B_voltage',
          'min_phase_C_voltage']

def predict(data):
    x = data[fields].values
    return model.predict(x)[0]