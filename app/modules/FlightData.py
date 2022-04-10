import dash_table as dt
import pandas as pd
import string


class FlightData(object):
    def __init__(self):
        self.df_vuelos = pd.read_csv('./data/flights/flightData.csv', sep=';')
        self.fight_table = self.generateFightTable()

    
    def generateFightTable(self):
        return dt.DataTable(
            id='vuelos',
            columns=[{'name':string.capwords(i), 'id':i} for i in self.df_vuelos.columns],
            data=self.df_vuelos.to_dict('records'),
            fixed_columns={'headers':True, 'data':5},
            fixed_rows={'headers':True},
            sort_action='native',
            sort_mode='multi',
            filter_action='native',
            style_header= {
                'fontWeight': 'bold',
            },
            style_cell={
                'textAlign': 'center',
                'fontWeight': 'bold',
                'minWidth': '200px',
                },
            style_table= {
                'width': '100%',
                'minWidth': '100%',
            },                            
            style_data_conditional=[{
                'if':{
                    'filter_query':'{operation} eq "Aterrizaje"'
                },
                'backgroundColor': '#efe9ae',
            },
            {
                'if':{
                    'filter_query':'{operation} eq "Despegue"'
                },
                'backgroundColor': '#cdeac0',
            },
        ]
    )