import pandas_datareader.data as web        
from datetime import datetime

def get_gasprices_html():
    start = datetime(2019,1,1)
    end = datetime(2022,7,22)
    gas_prices = web.DataReader('APUS37B74714', 'fred', start, end)
    gas_prices.reset_index(inplace=True)
    table_html=gas_prices.to_html(classes="query_table")

    template_html = '''
    <!DOCTYPE html>
    <html>
        <head>
                <style>
                .query_table {{
                font-size: 11pt; 
                font-family: Arial;
                border-collapse: collapse; 
                border: 1px solid silver;
                }}
                .query_table td, th {{
                    padding-top: 5px;
                    padding-bottom: 5px;
                    padding-left: 10px;
                    padding-right: 10px;
                    text-align: center;
                }}
                .query_table tr:nth-child(even) {{
                    background: #E0E0E0;
                }}
                .query_table tr:hover {{
                    background: silver;
                    cursor: pointer;
                }}
            </style>
            <title>HTML Pandas Dataframe with CSS</title>
        </head>
    <body>
        {table}
    </body>
    </html>
    '''

    response_html = template_html.format(table=table_html)
    return response_html