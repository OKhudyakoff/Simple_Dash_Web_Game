from dash import Dash, dcc, html, Input, Output, callback, State, no_update, ctx
from server import app
from database import validate_login

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

@app.callback(Output('url','pathname'),
                  [Input('submit-button', 'n_clicks')],
                  [State('login', 'value'),
                  State('password', 'value')],
                  )
def update_output(clicks, login, password):
    if clicks is None or clicks==0:
        return no_update
    if(validate_login(login, password)):
        return '/home'
    else:
        return '/login'