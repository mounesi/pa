import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app.layout = html.Div([
    html.H1('Hello, World!')
])

application = app.server

if __name__ == '__main__':
    application.run(debug=True, port=8080)