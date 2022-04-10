from datetime import datetime, timedelta
import pandas as pd
import joblib

class Evaluacion(object):

    def __init__(self):
        self.data = pd.read_csv('./data/flights/dataCallsign.csv', sep=';')
        
        # Cargamos el modelo de votacion
        self.final_model = joblib.load('./models/votingClasifier.bin')
    

    def get_values_from_callsign(self, callsign):
        valores = self.data[self.data['callsign_original'] == callsign].values[0]
        id_leg, hexid, callsign_norm, tipo, origen, destino = valores[0], valores[3], valores[4], valores[5], valores[6], valores[7]
        return id_leg, hexid, callsign_norm, tipo, origen, destino

    def get_values_restantes(self, callsign):
        valores = self.data[self.data['callsign_original'] == callsign].values[0]
        
        vertical_rate, dew_pt, rel_hum, wind_gust = valores[10], valores[12], valores[13], valores[16]
        return vertical_rate, dew_pt, rel_hum, wind_gust

    def get_time_class(self, hour, minutes):
        date = datetime(2020, 1, 1, hour, minutes)
        date_base = datetime(2020,1,1,0,0)
        time_ref = 0

        while True:
            if date_base > date:
                break
            else:
                date_base = date_base + timedelta(minutes=30.0)
                time_ref += 1

        return time_ref

    def climatolgy_values(self, cheklist):
        rain, snow, drizzle, fog = 0, 0, 0, 0
        try:
            if 'rain' in cheklist:
                rain = 1
            if 'snow' in cheklist:
                snow = 1
            if 'drizzle' in cheklist:
                drizzle = 1
            if 'fog' in cheklist:
                fog = 1
            
            return rain, snow, drizzle, fog
        except Exception:
            return 0, 0, 0, 0
    