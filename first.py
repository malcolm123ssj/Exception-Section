import random
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral11 
import requests
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
def make_plot(v):

    df = pd.read_csv('monthsd.csv')
    l = []
    
    for j in df.iloc[v]:
        l.append(j+5)
    
    labels = ["August","September","October","November","December","January","February","March","April","May","June"]
    counts = l

    source = ColumnDataSource(data=dict(months=labels, counts=counts, color=Spectral11))

    p = figure(x_range=labels, plot_width=920, plot_height=500, title=str(df.columns[v]),
            toolbar_location=None, tools="")

    p.vbar(x='months', top='counts', width=0.9, color='color', legend="months", source=source)

    p.line(x=labels, y=counts, color='black', line_width=2)

    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    p.y_range.start = 0
    p.legend.orientation = "horizontal"
    p.legend.location = (35, 0)
    p.outline_line_color = None
    p.background_fill_color = None
    p.border_fill_color = None
    p.sizing_mode ='scale_width'

    # p = figure(x_range=labels, plot_width=920, plot_height=500, title=str(df.columns[v]), toolbar_location=None, tools="")

    # p.vbar(x=labels, top=counts, width=0.9)

    # p.xgrid.grid_line_color = None
    # p.ygrid.grid_line_color = None
    # p.y_range.start = 0

    script, div = components(p)
    return script, div

#Route for Index
@app.route('/', methods = ['GET','POST'])
def main():
    if request.method == 'POST':
        city = request.form.get('city')
        if city.lower() == 'bangalore' or city.lower() == 'bengaluru':
            #labels = ["January","February","March","April","May","June","July","August","September","October","November"]
            
            plots = []
            
            for i in range(0,11):
                plots.append(make_plot(i))

            return render_template('graph.html', scroll = 'about', plots=plots, message = "Successfully Fetched Data for " + city.upper() + "!")

        else:
            return render_template('index.html', scroll = 'about', message = "Not Found! Try again!")
    return render_template('index.html')

if __name__== '__main__':
    app.run(debug = True)
    
