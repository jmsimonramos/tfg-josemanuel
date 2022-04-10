import pandas as pd

import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import string

class Metricas(object):

    def __init__(self):
        self.metric_df = pd.DataFrame()
        
    def adaptarDataFrame(self, model):
        diccionario = {"RandomForest": "Bosques Aleatorios", "KNN" : "K-Vecinos Más Cercanos", "RedesNeuronales":"Redes Neuronales", "Ensemble": "Clasificación por Votación"}
        
        self.metric_df = self.metric_df.T
        self.metric_df.columns = self.metric_df.iloc[0]
        self.metric_df = self.metric_df.drop(self.metric_df.index[0])
        self.metric_df.insert(loc=0, column='Valor', value=['Precision', 'Recall' , 'F1'])
        self.metric_df.columns = ['Valor', diccionario[model]]      
        
    def generate_metric_table(self, model, metric):
    
        path = './data/metrics/' + model + '_' +metric + '.csv'

        print(f'PATH!!!! {path}')
        
        if metric == "ConfusionMatrix":
            self.metric_df = pd.read_csv('./data/metrics/metrics.csv', sep=';')
            self.metric_df = self.metric_df[self.metric_df['Model'] == model]
            self.metric_df['Precision'] = self.metric_df['Precision'].map('{:,.5f}'.format)
            self.metric_df['Recall'] = self.metric_df['Recall'].map('{:,.5f}'.format)
            self.metric_df['F1'] = self.metric_df['F1'].map('{:,.5f}'.format)

            self.adaptarDataFrame(model)

            return html.Div(
                    children = [
                        html.H4("Tabla de Métricas"),
                        dt.DataTable(
                        id='metric_table',
                        columns=[{'name':string.capwords(i), 'id':i} for i in self.metric_df.columns],
                        data=self.metric_df.to_dict('records'),
                        fixed_columns={'headers':True},
                        fixed_rows={'headers':True},
                        style_table= {
                            'width': '500px',
                            'minWidth': '50%',
                            'height': '300px',
                        }, 
                        style_header= {
                            'fontWeight': 'bold',
                        },
                        style_cell={
                            'textAlign': 'center',
                            'fontWeight': 'bold',
                            'minWidth': '150px',
                            },        
                    ),
                ],
                style = {'text-align':'center', 'display':'flex', 'justify-content':'center', 'align-items':'center', 'flex-direction': 'column', 'flex-grow':'5', 'margin-right':'40px'},
            )

        else:           
            self.metric_df = pd.read_csv(path , sep=';')
            self.metric_df['Precision'] = self.metric_df['Precision'].map('{:,.5f}'.format)
            
            return html.Div(
                    children = [
                        html.H4("Tabla de Datos"),
                        dt.DataTable(
                        id='metric_table',
                        columns=[{'name':string.capwords(i), 'id':i} for i in self.metric_df.columns],
                        data=self.metric_df.to_dict('records'),
                        fixed_columns={'headers':True},
                        fixed_rows={'headers':True},
                        sort_action='native',
                        sort_mode='multi',
                        style_table= {
                            'width': '500px',
                            'minWidth': '50%',
                            'height': '300px',
                        }, 
                        style_header= {
                            'fontWeight': 'bold',
                        },
                        style_cell={
                            'textAlign': 'center',
                            'fontWeight': 'bold',
                            'minWidth': '150px',
                            },        
                    ),
                ],
                style = {'text-align':'center', 'display':'flex', 'justify-content':'center', 'align-items':'center', 'flex-direction': 'column', 'flex-grow':'5', 'margin-right':'40px'},
            )

    def generate_metric_graph(self, model, item):
        
        dictionary = {'RandomForest':'Árboles', 'KNN':'Vecinos', 'RedesNeuronales':'Épocas', 'Ensemble': 'Modelos'}
        dictionary_model = {'RandomForest': 'Bosques Aleatorios', 'KNN': 'K-Vecinos Más Cercanos', 'RedesNeuronales': 'Redes Neuronales', 'Ensemble':'Clasificador de Votación'}
        
        print(f'MODELO!!! {model}')
        print(f"DICIONARY: {dictionary[model]}")
        print(f'Item!!! {item}')
        
        if item == 0: # Precision
            data = []
            try:
                data = [
                    {'x': self.metric_df['Parameter'][self.metric_df['Tipo'] == "FULL"].values.tolist(),
                    'y':self.metric_df['Precision'][self.metric_df['Tipo'] == "FULL"].values.tolist(),
                    'type': 'line',
                    'name': 'FULL'
                    },
                    {'x': self.metric_df['Parameter'][self.metric_df['Tipo'] == "FNORM"].values.tolist(),
                    'y':self.metric_df['Precision'][self.metric_df['Tipo'] == "FNORM"].values.tolist(),
                    'type': 'line',
                    'name': 'FNORM'
                    },
                    {'x': self.metric_df['Parameter'][self.metric_df['Tipo'] == "RELATED"].values.tolist(),
                    'y':self.metric_df['Precision'][self.metric_df['Tipo'] == "RELATED"].values.tolist(),
                    'type': 'line',
                    'name': 'RELATED'
                    },
                    {'x': self.metric_df['Parameter'][self.metric_df['Tipo'] == "RNORM"].values.tolist(),
                    'y':self.metric_df['Precision'][self.metric_df['Tipo'] == "RNORM"].values.tolist(),
                    'type': 'line',
                    'name': 'RNORM'
                    }
                ]
                layout = {
                'title':f'<b>Precisión del Modelo: {dictionary_model[model]}</b>',
                'xaxis':{'title':f'Número de {dictionary[model]}'},
                'yaxis':{'title':'Precisión'},
                }
            except Exception:
                data = [
                    {'x': self.metric_df['Neurons'][self.metric_df['Layers'] == 1].values.tolist(),
                    'y':self.metric_df['Precision'][self.metric_df['Layers'] == 1].values.tolist(),
                    'type': 'line',
                    'name': '1 Capa Oculta'
                    },
                    {'x': self.metric_df['Neurons'][self.metric_df['Layers'] == 2].values.tolist(),
                    'y':self.metric_df['Precision'][self.metric_df['Layers'] == 2].values.tolist(),
                    'type': 'line',
                    'name': '2 Capas Ocultas'
                    },
                    {'x': self.metric_df['Neurons'][self.metric_df['Layers'] == 3].values.tolist(),
                    'y':self.metric_df['Precision'][self.metric_df['Layers'] == 3].values.tolist(),
                    'type': 'line',
                    'name': '3 Capas Ocultas'
                    },
                    {'x': self.metric_df['Neurons'][self.metric_df['Layers'] == 4].values.tolist(),
                    'y':self.metric_df['Precision'][self.metric_df['Layers'] == 4].values.tolist(),
                    'type': 'line',
                    'name': '4 Capas Ocultas'
                    }
                ]
                layout = {
                'title':f'<b>Precisión del Modelo: {dictionary_model[model]}</b>',
                'xaxis':{'title':'Número de Neuronas'},
                'yaxis':{'title':'Precisión'},
            }

        elif item == 1: # Confusion Matrix
                try:
                    correlation_matrix_dict = {"RandomForest": [[509, 34948], [110714, 594]], "KNN": [[5121, 33735], [101107, 6802]],
                    "RedesNeuronales": [[7125, 30912], [101127, 7601]] , "Ensemble":[[354, 34903], [110994, 514]]}

                    z = correlation_matrix_dict[model]
                    x= ['<b>Falsos Positivos</b>', '<b>Verdaderos Negativos</b>']
                    y= ['<b>Falsos Positivos</b>', '<b>Verdaderos Positivos</b>']

                    annotations = go.Annotations()
                    for n, row in enumerate(z):
                        for m, val in enumerate(row):
                            annotations.append(go.Annotation(
                                    text="<b>" + str(z[n][m]) + "</b>", 
                                    font=dict(size=16, color='#FFFFFF'), 
                                    x=x[m], 
                                    y=y[n],
                                    xref='x1', yref='y1', showarrow=False))
                    
                    trace = go.Heatmap(
                        x = x,
                        y = y,
                        z = z,
                        type = 'heatmap',
                        colorscale = 'blackbody'
                    )
                    
                    
                    fig = go.Figure(data = [trace])

                    fig['layout'].update(
                        title=f"<b>Matriz de Confusión para el modelo: {dictionary_model[model]}</b>",
                        annotations=annotations,
                        width=700,
                        height=600,
                        autosize=False,
                        showlegend = False,
                    )
                except Exception as e:
                    print(e)
                return html.Div(children=dcc.Graph(figure=fig), style={'display':'flex', 'margin-bottom':'155px', 'justify-content':'center', 'align-items':'center', 'flex-direction': 'column',
                'margin-left': '20px', 'margin-right':'20px'},)

        elif item == 2: # Validation Curve
            data = [
                {'x': self.metric_df['Parameter'][self.metric_df['Tipo'] == "ENTRENAMIENTO"].values.tolist(),
                'y':self.metric_df['Precision'][self.metric_df['Tipo'] == "ENTRENAMIENTO"].values.tolist(),
                'type': 'line',
                'name': 'ENTRENAMIENTO'
                },
                {'x': self.metric_df['Parameter'][self.metric_df['Tipo'] == "TEST"].values.tolist(),
                'y':self.metric_df['Precision'][self.metric_df['Tipo'] == "TEST"].values.tolist(),
                'type': 'line',
                'name': 'TEST'
                }
            ]

            layout = {
                'title':f'<b>Curva de Validación del Modelo: {dictionary_model[model]}</b>',
                'xaxis':{'title':f'Número de {dictionary[model]}'},
                'yaxis':{'title':'Precisión'},
            }
        
        elif item == 3: # CV Curve
            data = [
                {'x': self.metric_df['Fold'][self.metric_df['Tipo'] == "ENTRENAMIENTO"].values.tolist(),
                'y':self.metric_df['Precision'][self.metric_df['Tipo'] == "ENTRENAMIENTO"].values.tolist(),
                'type': 'line',
                'name': 'ENTRENAMIENTO'
                },
                {'x': self.metric_df['Fold'][self.metric_df['Tipo'] == "TEST"].values.tolist(),
                'y':self.metric_df['Precision'][self.metric_df['Tipo'] == "TEST"].values.tolist(),
                'type': 'line',
                'name': 'TEST'
                }
            ]

            layout = {
                'title':f'<b>Validación Cruzada del Modelo: {dictionary_model[model]}</b>',
                'xaxis':{'title':'Número de Fold'},
                'yaxis':{'title':'Precisión'},
            }


        return html.Div(
            children=[
                dcc.Graph(
                    id='graph',
                    figure={
                        'data': data,
                        'layout': layout,
                    },
                    style={'width':'800px', 'minWidth':'0px'},
                )
            ],
            style={'flex-grow':'6', 'margin-top':'45px'},
        )

