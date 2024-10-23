from dash import Dash, dcc, html, Input, Output, callback, State, no_update, ctx

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

from server import app
from Pages.login import login_layout
from Pages.game import game_layout
from Pages.home import home_layout

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
@app.callback(
    Output('page-content','children'),
    [Input('url','pathname')],
    prevent_initial_call = True
)
def router(url):
    if url=='/home':
        return home_layout()
    elif url=='/login':
        return login_layout()
    elif url =='/game':
        return game_layout()

if __name__ == '__main__':
    app.run(debug=True)