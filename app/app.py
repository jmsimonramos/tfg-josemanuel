import dash
import numpy as np
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime, timedelta

from modules.FlightData import FlightData
from modules.DashUtils import generate_figure
from modules.Metricas import Metricas
from modules.Evaluacion import Evaluacion

flight = FlightData()
metricas = Metricas()
evaluacion = Evaluacion()


external_stylesheets = ["https://codepen.io/chriddyp/pen/dZVMbK.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

        
app.layout = html.Div([
    dcc.ConfirmDialog(
        id='error-metricas',
    ),
    dcc.ConfirmDialog(
        id='error-evaluacion',
    ),
    html.H3("Dashboard Configuración de Pistas"),
    html.Div([
        dcc.Tabs(id='tabs', value='data', children=[
            dcc.Tab(
                id = 'data',
                value= 'data',
                label= 'Datos',
                children= [
                    html.Div(
                        style= {'margin-top':'25px'},
                        children=[html.H5('Registro de los vuelos'),]
                        ),
                    html.Div(
                        style={'display':'flex', 'margin-bottom':'155px', 'justify-content':'center', 'align-items':'center', 'flex-direction': 'column',
                        'margin-left': '20px', 'margin-right':'20px'},
                        children=[
                            html.Br(),
                            html.Div(
                                children=[
                                    flight.fight_table,
                                ],
                                className='twelve columns',
                            ),
                            html.Br(),
                            html.Div(
                                style={'display':'flex', 'flex-direction': 'row', 'justify-content':'center', 'align-items':'center', "margin-top":"50px"},
                                children=[
                                    html.H6("Seleccionar una configuración: ", style={'margin-right': '10px', 'margin-top':'-35px'}),
                                    dcc.Dropdown(
                                        id='dropdown-configuracion',
                                        options=[
                                            {'label': "Distribución Pistas (Configuración Base)", 'value':'Base'},
                                            {'label': "Configuración Norte", 'value':'Norte'},
                                            {'label': "Configuración Sur", 'value':'Sur'},
                                        ],
                                        value='Base',
                                        placeholder='Configuraciones Disponibles',
                                        style={"width": '500px', "margin-top":"-20px"},
                                    ),
                                ],
                            ),                            
                            html.Div(
                                id = 'div-img-pistas'
                            )
                    ]),
                ]
            ),
            dcc.Tab(
                id = 'metricas',
                value= 'metricas',
                label= 'Métricas',
                children= [                
                    html.Div([
                        dcc.Dropdown(
                            id='dropdown_model',
                            options=[
                                {'label': "Bosques Aleatorios", 'value':'RandomForest'},
                                {'label': "K-Vecinos Más Cercanos", 'value':'KNN'},
                                {'label': "Redes Neuronales", 'value':'RedesNeuronales'},
                                {'label': "Clasificador de Votación", 'value':'Ensemble'},
                            ],
                            placeholder='Selecciona un Modelo',
                            className='four columns',
                        ),
                        dcc.Dropdown(
                            id='dropdown_metric',
                            options=[
                                {'label': "Precisión", 'value':'Precision'},
                                {'label': "Curva de Validación", 'value':'ValidationCurve'},
                                {'label': "Matriz de Confusión", 'value':'ConfusionMatrix'},
                                {'label': "Validación Cruzada", 'value':'CV'},
                            ],
                            placeholder='Selecciona una métrica',
                            className='four columns',
                        ),

                        html.Button(
                            children='Visualizar',
                            id='botonVisualizar',
                            className='two columns, button-primary',
                            n_clicks=0,
                            n_clicks_timestamp=-1,
                            hidden=False,
                            style={'margin-bottom':'50px'}, 
                        ),
               
                    ],style={'margin-top':'30px'}),
                    html.Div(
                        id = 'result-metrics',
                        className = 'twelve columns',
                        children=[],
                        
                    ),
                ]
            ),
            dcc.Tab(
                id = 'evaluacion',
                value= 'evaluacion',
                label= 'Evaluación',
                children= [
                html.Div(
                    children=[
                        html.Div(
                            style={'display':'flex', 'justify-content':'center', 'align-items':'center', 'flex-direction': 'row', 'margin-top':'20px'},
                            id='form-callsign',
                            children = [
                            dcc.Input(
                                id='callsign',
                                placeholder='Callsgin del vuelo',
                                className='',
                                style={'margin-right':'20px'},
                            ),
                            dcc.Dropdown(
                                id='operation',
                                options=[
                                    {'label': "Aterrizaje", 'value':'0'},
                                    {'label': "Despegue", 'value':'1'},
                                ],
                                placeholder='Tipo de Operación',
                                style={'width': '300px', 'margin-right': '20px'},
                            ),

                            dcc.DatePickerSingle(
                                id='fecha-operacion',
                                initial_visible_month=datetime(datetime.today().year, datetime.today().month, datetime.today().day),
                                display_format='YYYY/MM/DD',
                                placeholder='Fecha de la Operación',
                                min_date_allowed=datetime(2018,1,1),
                                first_day_of_week=1,
                                style={'margin-right':'20px'},
                            ),
                            dcc.Dropdown(
                                id='time-hour',
                                options=[
                                    {'label':str(i), 'value':i} for i in range(0,24)
                                ],
                                placeholder='Hora',
                                style={'width': '100px', 'margin-right':'20px'},
                            ),
                            dcc.Dropdown(
                                id='time-minute',
                                options=[
                                    {'label':str(i), 'value':i} for i in range(1,60)
                                ],
                                placeholder='Minutos',
                                style={'width': '100px'},
                            ),

                        ],),

                        html.Div(
                            id='form-vuelos',
                            children=[
                                html.H6('Altitud', style={'text-align': 'left', 'margin-left': '20px'}),
                                    dcc.Slider(
                                        id='altitud',
                                        min=0,
                                        max=2000,
                                        step=5,
                                        marks= {int(i): f"{i}m" for i in range (0,2001,100)},
                                    ),
                                html.H6('Velocidad (tierra)', style={'text-align': 'left', 'margin-left': '20px'}),
                                dcc.Slider(
                                    id='ground_speed',
                                    min=0,
                                    max=200,
                                    step=1,
                                    marks= {int(i): f"{i}km/h" for i in range (0,201,20)},
                                ),
                            ]),

                            html.Div(
                                id='form-meteo',
                                children=[
                                    html.H6('Temperatura', style={'text-align': 'left', 'margin-left': '20px'}),
                                    dcc.Slider(
                                        id='temperatura',
                                        min=-10,
                                        max=60,
                                        step=5,
                                        marks= {int(i): f"{i}ºC" for i in range (-10,60,5)},
                                    ),
                                    html.H6('Dirección del viento', style={'text-align': 'left', 'margin-left': '20px'}),
                                    dcc.Slider(
                                        id='wind_dir',
                                        min=0,
                                        max=360,
                                        step=5,
                                        marks= {int(i): f"{i}º" for i in range (0,361,10)},
                                    ),
                                    html.H6('Velocidad del viento', style={'text-align': 'left', 'margin-left': '20px'}),
                                    dcc.Slider(
                                        id='wind_sp',
                                        min=0,
                                        max=3500,
                                        step=5,
                                        marks= {int(i): f"{i}km/h" for i in range (0,3501,200)},
                                    ),
                                    html.H6('Visibilidad', style={'text-align': 'left', 'margin-left': '20px'}),
                                    dcc.Slider(
                                        id='visib',
                                        min=0,
                                        max=10,
                                        step=1,
                                        marks= {int(i): f"{i}" for i in range (0,11,1)},
                                    ),    
                                    html.H6('Presión', style={'text-align': 'left', 'margin-left': '20px'}),
                                    dcc.Slider(
                                        id='press',
                                        min=800,
                                        max=1200,
                                        step=5,
                                        marks= {int(i): f"{i}hPa" for i in range (800,1201,50)},
                                    ),                                                                    
                                ],
                            ),
                            html.Div(
                                id='visibilidad',
                                style={'display':'flex', 'justify-content':'center', 'align-items':'center', 'flex-direction': 'row', 'margin-top':'20px'},
                                children=[
                                    html.H6("Climatología:", style={'margin-right':'30px'}),
                                    dcc.Checklist(
                                        style={'margin-right':'40px'},
                                        id='visib-meteo',
                                        options=[                                
                                        {'label': "¿Llovizna?", 'value':'drizzle'},
                                        {'label': "¿Lluvia?", 'value':'rain'},
                                        {'label': "¿Niebla?", 'value':'fog'},                                        
                                        {'label': "¿Nieve?", 'value':'snow'},
                                        ],
                                        labelStyle={'display':'inline-block', 'margin-right':'20px'},
                                    ),
                                    html.Button(
                                        children='Predicción',
                                        id='botonEvaluar',
                                        className='two columns, button-primary',
                                        n_clicks=0,
                                        n_clicks_timestamp=-1,
                                        hidden=False,
                                        style={'witdh':'150px'},
                                    ),
                                ],
                            ),        
                            
                ]
            ),
            html.Div(
                id = 'resultado-modelo',
                children=[
                ],
            ),
        ]),
    ]),
],),
])
@app.callback(
    [
        dash.dependencies.Output('error-evaluacion', 'displayed'),
        dash.dependencies.Output('error-evaluacion', 'message'),
        dash.dependencies.Output('resultado-modelo', 'children'),
    ],

    [dash.dependencies.Input('botonEvaluar', 'n_clicks')],
    
    [
    dash.dependencies.State('callsign', 'value'),
    dash.dependencies.State('operation', 'value'),
    dash.dependencies.State('fecha-operacion', 'date'),
    dash.dependencies.State('time-hour', 'value'),
    dash.dependencies.State('time-minute', 'value'),
    dash.dependencies.State('altitud', 'value'),
    dash.dependencies.State('ground_speed', 'value'),
    dash.dependencies.State('temperatura', 'value'),
    dash.dependencies.State('wind_dir', 'value'),
    dash.dependencies.State('wind_sp', 'value'),
    dash.dependencies.State('visib', 'value'),
    dash.dependencies.State('press', 'value'),
    dash.dependencies.State('visib-meteo', 'value'),   
    ],
)
def make_prediction(n_clicks, callsign, operation, fecha_operacion, hour, minute, altitud, ground_speed, temperatura, wind_dir, wind_sp, visib, press, visib_meteo):
    
    if callsign is None:
        return [False , "", ""]
    else:
        diccionario = {0: 'Norte', 1:'Sur'}

        try:
            fecha_operacion = datetime.strptime(fecha_operacion, '%Y-%m-%d')

            try:
                id_leg, hexid, callsign_norm, tipo, origen, destino = evaluacion.get_values_from_callsign(callsign)
            except Exception as e: # No se ha encontrado el callsign que se buscaba
                return [True , f"ERROR. No existe ningún vuelo con el Callsign: {callsign}" , ""]
            
            time_class = evaluacion.get_time_class(hour, minute)
            rain, snow, drizzle, fog = evaluacion.climatolgy_values(visib_meteo)
            month = fecha_operacion.month
            time_ref = fecha_operacion.hour
            day_week = fecha_operacion.weekday()
            vertical_rate, dew_pt, rel_hum, wind_gust = evaluacion.get_values_restantes(callsign)
        
            flight = np.array((id_leg, int(operation), hexid, callsign_norm, tipo, origen, destino, altitud, ground_speed, vertical_rate, temperatura, dew_pt, rel_hum, wind_dir, wind_sp, wind_gust, visib, press, rain, snow, drizzle, fog, time_class, day_week, month, time_ref), dtype=object)
            
            flight = np.expand_dims(flight, axis=1)
            flight = flight.T

            resultado = evaluacion.final_model.predict(flight)[0]

            print(f"RESULTADO --> {resultado}")

            if resultado == 0:
                path = './img/ConfiguracionNorte.jpg'
            else:
                path = './img/ConfiguracionSur.jpg'

            element = html.Div(
                style={'display':'flex', 'margin-bottom':'155px', 'justify-content':'center', 'align-items':'center', 'flex-direction': 'column', 'margin-left': '20px', 'margin-right':'20px'},
                children=[
                    html.H3(f'Configuración de pista: {diccionario[resultado]}', style={'font-weight':'bold'}),
                    dcc.Graph(
                        id= 'configBase',
                        figure= generate_figure(path),
                    ),
                ],
            )

            return [True, f"Configuración determinada: CONFIGURACIÓN {diccionario[resultado].upper()}" , element]
        
        except Exception as e:
            return [True , f"ERROR. Se ha producido un error al predecir la pista." , ""]



@app.callback(
    [
        dash.dependencies.Output('error-metricas', 'displayed'),
        dash.dependencies.Output('error-metricas', 'message'),
        dash.dependencies.Output('result-metrics', 'children'),
    ],

    [dash.dependencies.Input('botonVisualizar', 'n_clicks')],
    
    [dash.dependencies.State('dropdown_model', 'value'),
    dash.dependencies.State('dropdown_metric', 'value')],
)
def update_value(n_clicks, model , metric):
    if model is None or metric is None:
        return [False, "", ""]
        
    else:
        dictionary = {'Precision': 0, 'ConfusionMatrix':1 , 'ValidationCurve':2, 'CV':3}
        try:
            element = html.Div(
                children=[
                    metricas.generate_metric_table(model, metric),
                    metricas.generate_metric_graph(model, dictionary[metric]),
                ],
                style={'display':'flex', 'justify-content': 'center', 'flex-wrap':'wrap', 'margin-top':'-20px'},
                className='twelve columns',
            ),
            return [False, "", element]
        except Exception as e:
            return [True, f"La métrica: {metric} del modelo {model}, no se encuentra disponible. \nError: {e}" , ""]

        

@app.callback(
    [dash.dependencies.Output('div-img-pistas', 'children')],

    [dash.dependencies.Input('dropdown-configuracion', 'value')]
)
def cargar_imagen_configuracion(configuracion):
    if configuracion is None:
        return [""]
        
    diccionario_pistas = {"Base": "Distribución de las pistas del Aeropuerto de Barajas", "Norte": "Distribución de las pistas del Aeropuerto de Barajas: (Configuración Norte)", "Sur": "Distribución de las pistas del Aeropuerto de Barajas: (Configuración Sur)"}

    print(f"CONFIGURACION!!! --> {configuracion}")
    path = f'./img/Configuracion{configuracion}.jpg'

    element = html.Div(
        children = [
            html.H3(f"{diccionario_pistas[configuracion]}" , style={'text-align':'center'}),
            dcc.Graph(
                id= 'configuracion-barajas',
                figure= generate_figure(path),
            ),
        ],
        style={'margin-top':'40px'}
    ),
    return [element]

if __name__ == "__main__":

    app.run_server(debug=True)