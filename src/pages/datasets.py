import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

dash.register_page(__name__,name='Data Sets', order=[1])


# define layout components 

input_gene = html.Div(
    [
        dbc.Textarea(id='input', placeholder='Gfap, Grm5, Rock1', size='md'),
    ]
)

dropdown_study = dbc.DropdownMenu(
    [
        dbc.DropdownMenuItem('APP/PS1 Mouse Line', header=True),
        dbc.DropdownMenuItem('SAM'),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem('Double KnockIn (DKI) Mouse Line', header=True),
        dbc.DropdownMenuItem('SAM'),
        dbc.DropdownMenuItem('PrP-KO'),
        dbc.DropdownMenuItem('High Fat Diet (Diabetes)'),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem('A53T Mouse line (Parkinson\'s)'),
    ],
    label='Study'   
)

ctrl_card = dbc.Card([
    
    dbc.CardHeader('Graph Controls', className='text-center'),
    dbc.CardBody(
    [
        html.H4('Gene Expression',),
        html.P('Please provide a list of gene names \n separated by , or new line:', className='card-text'), 
        input_gene,
        html.Hr(),  
        html.P('Search Options'),
        dropdown_study,
        html.Hr(),  
        html.P('Additional Options'),
        html.Hr(),
        dbc.Button('Search', size='lg', color='success', outline=True)
    ])
])


# specify layout 
layout = dbc.Container([
        dbc.Row([
            
            dbc.Tabs(
            [
                dbc.Tab(label='Histogram', tab_id='histogram'),
                dbc.Tab(label='Dot plot', tab_id='Dot Plot'),
                dbc.Tab(label='Proportion Plot', tab_id='proportions')
            ], 
            id='tab',
            active_tab='histogram',
            ),
            html.Hr(),
        ]),
 
        
        dbc.Row([
            
            dbc.Col([
                
                ctrl_card
                
            ], width=3),
            
            dbc.Col([
                
            ],width=8)
        ])
        
], fluid=True)


