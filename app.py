from dash import Dash, dcc, html, Input, Output, callback, State, no_update, ctx
from database import connect_to_db

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

from server import app, server

VALID_USERNAME_PASSWORD_PAIRS = {
    'admin': 'admin'
}

def login_layout(): 
    return html.Div(className='container', children=[

    html.Div([
        dcc.Location(id='login-url',pathname='/login',refresh=False),
        html.H2('LoginPage', id='header-title', className='ten columns'),

        dcc.Input(id='login', value='admin', type='text'),
        dcc.Input(id='password', value='admin', type='text'),
        html.Button(id='submit-button', type='submit', children='Submit'),
    ]),
    html.Div(id='dummy-input', style={'display': 'none'}),
])

def app_layout(): 
    return html.Div([
    dcc.Location(id='home-url', pathname='/home'),
    html.Div([
        html.H2('HomePage', id='header-title', className='ten columns'),
        html.Button(id='logout-button', type='submit', children='Logout'),
        html.Button(id='play_button', type='submit', children='Play'),
    ]),
    html.Div(id='dummy-input', style={'display': 'none'}),
])

def game_layout(): 
    return html.Div([
    dcc.Location(id='home-url', pathname='/home'),
    html.Div([
        html.H2('GamePage', id='header-title', className='ten columns'),
        html.H3('last_city', id='city_result', className='ten columns'),
        dcc.Input(id='new_city', value='', type='text'),
        html.Button(id='check-city', type='submit', children='Check'),
    ]),
    html.Div(id='dummy-input', style={'display': 'none'}),
])

# main app layout
app.layout = html.Div(
    [
        dcc.Location(id='url',refresh=False),
        html.Div(
            login_layout(),
            id='page-content'
        ),
    ]
)


# router
@callback(
    Output('page-content','children'),
    [Input('url','pathname')],
    prevent_initial_call = True
)
def router(url):
    if url=='/home':
        return app_layout()
    elif url=='/login':
        return login_layout()
    elif url =='/game':
        return game_layout()
    else:
        return login_layout()


@callback(Output('url','pathname'),
                  [Input('submit-button', 'n_clicks')],
                  [State('login', 'value'),
                  State('password', 'value')],
                  )
def update_output(clicks, login, password):
    if clicks is None or clicks==0:
        return no_update
    if(login in VALID_USERNAME_PASSWORD_PAIRS and VALID_USERNAME_PASSWORD_PAIRS[login] == password):
        return '/home'
    else:
        return '/login'

@app.callback(Output('home-url','pathname',allow_duplicate=True),
        Input('logout-button', 'n_clicks'),
         prevent_initial_call=True,
                  )
def return_to_login(clicks):
    return '/login'

@app.callback(Output('home-url','pathname'),
        Input('play-button', 'n_clicks'),
                  )
def go_to_game(clicks):
    return '/login'

if __name__ == '__main__':
    app.run(debug=True)