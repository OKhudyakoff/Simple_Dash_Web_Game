from dash import Dash, dcc, html, Input, Output, callback, State, no_update, ctx
from server import app

def home_layout(): 
    return html.Div([
    dcc.Location(id='home-url', pathname='/home'),
    html.Div([
        html.H2('HomePage', id='header-title', className='ten columns'),
        html.Button(id='logout-button', type='submit', children='Logout'),
        html.Button(id='play_button', type='submit', children='Play'),
    ]),
    html.Div(id='dummy-input', style={'display': 'none'}),
])

@app.callback(Output('home-url','pathname',allow_duplicate=True),
        Input('logout-button', 'n_clicks'),
         prevent_initial_call=True,
                  )
def return_to_login(clicks):
    if clicks is None or clicks==0:
        return no_update
    return '/login'

@app.callback(Output('home-url','pathname'),
        Input('play_button', 'n_clicks'),
                  )
def go_to_game(clicks):
    if clicks is None or clicks==0:
        return no_update
    return '/game'