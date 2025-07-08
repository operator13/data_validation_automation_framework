import pandas as pd
from jinja2 import Environment, FileSystemLoader
import os

def generate_html_report(mismatches: pd.DataFrame, summary: dict, output_path: str):
    env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))
    template = env.get_template('report_template.html')
    html = template.render(summary=summary, mismatches=mismatches.to_html(index=False))
    with open(output_path, 'w') as f:
        f.write(html) 