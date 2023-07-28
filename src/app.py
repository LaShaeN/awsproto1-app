import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.LUX, dbc.icons.FONT_AWESOME],
)
server = app.server

# Main navbar header
navbar = dbc.NavbarSimple(
    
    children=[
        dbc.NavItem(dbc.NavLink("Contact", href="#")),
        dbc.NavItem(dbc.NavLink("Feedback", href="#")),
    ],
    brand="Multi-Variant Transcriptomic Analysis",
    brand_href="#",
    color="primary",
    dark=True,
    fluid=True,
    fixed='bottom',
    sticky='top',
)


# side bar
sidebar = html.Div(
    [
        html.Div(
            [
                html.H2("NeuroXp", style={"color": "white"}),
            ],
            className="sidebar-header d-flex justify-content-center",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="fas fa-home me-2"), html.Span("Home")],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [html.Span("— PROJECT OVERVIEW —")],
                    href="#",
                    active=False,
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-solid fa-glasses me-2"),
                        html.Span("Background"),
                    ],
                    href="/background",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-solid fa-brain me-2"),
                        html.Span("mGluR5 Signaling"),
                    ],
                    href="/grm5_signal",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-solid fa-wind me-2"),
                        html.Span("Neurovascular AD"),
                    ],
                    href="/neurovas_signal",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-brands fa-stack-overflow me-2"),
                        html.Span("Data Sets"),
                    ],
                    href="/datasets",
                    active="exact",
                ),               
                dbc.NavLink(
                    [html.Span("— EXPRESSION ANALYSIS —")],
                    href="#",
                    active="exact",
                    class_name="d-flex justify-content-center"
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-solid fa-chart-column me-2"),
                        html.Span("Gene Expression"),
                    ],
                    href="/gene_expr",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-brands fa-squarespace me-2"),
                        html.Span("Protein Structure"),
                    ],
                    href="/protein",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-solid fa-cloud-meatball me-2"),
                        html.Span("UMAP Profiles"),
                    ],
                    href="/umap",
                    active="exact",
                ),
                dbc.NavLink(
                    [html.Span("— PATHWAY ANALYSIS —")],
                    href="#",
                    active="exact",
                    class_name="d-flex justify-content-center"
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-solid fa-bacteria me-2"),
                        html.Span("Cell Chat"),
                    ],
                    href="/celltalk",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-solid fa-circle-nodes me-2"),
                        html.Span("Cytoscape"),
                    ],
                    href="/cytoscape",
                    active="exact",
                ),
                dbc.NavLink(
                    [html.Span("— MORE INFORMATION —")],
                    href="#",
                    active="exact",
                    class_name="d-flex justify-content-center"
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-solid fa-file-lines me-2"),
                        html.Span("Publications"),
                    ],
                    href="/publications",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-solid fa-envelope me-2"),
                        html.Span("Contact Us"),
                    ],
                    href="/contact",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
            fill=True),
    ],
    #className="sidebar",  # note: pass class name to container below
 )

app.layout =dbc.Container([
    dbc.Row([navbar]
            ),
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2,
                className='sidebar'),

            dbc.Col(
                [   
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10,
                className="content"
                )
        ],
        
    )
], fluid=True)


if __name__ == "__main__":
    app.run_server(debug=True)