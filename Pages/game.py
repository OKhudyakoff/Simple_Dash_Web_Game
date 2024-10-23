from dash import Dash, dcc, html, Input, Output, callback, State, no_update, ctx
from server import app
from city_check import check_city

def game_layout(): 
    return html.Div([
    dcc.Location(id='game-url', pathname='/game'),
    html.Div([
        html.H2('GamePage', id='header-title', className='ten columns'),
        html.H3('last_city', id='city_result', className='ten columns'),
        dcc.Input(id='new_city', value='', type='text'),
        html.Button(id='check-city', type='submit', children='Check'),
        html.Button(id='to_home_button', type='submit', children='Home'),
    ]),
    html.Div(id='dummy-input', style={'display': 'none'}),
])

@app.callback(Output('game-url','pathname',allow_duplicate=True),
        Input('to_home_button', 'n_clicks'),
         prevent_initial_call=True,
                  )
def return_to_login(clicks):
    if clicks is None or clicks==0:
        return no_update
    return '/home'

@app.callback(
    Output('city_result','children'),
    Input('check-city','n_clicks'),
    State('city_result', 'children'),
     State('new_city','value'),
    prevent_initial_call = True
)
def check(clicks, old_city, new_city):
    if(check_city(old_city, new_city)):
        print('ok')
        return new_city
    else:
        print('no')
        return old_city