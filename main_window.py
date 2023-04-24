import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#kaggle url for data set=https://www.kaggle.com/code/rtatman/datasets-for-regression-analysis/notebook
data=pd.read_csv("Fish.csv")

Species=data['Species'].value_counts()

index =Species.index
values_count=Species.values

def create_plot(index,values_count):
    sns.set_palette('pastel')
    plt.figure(figsize=(12, 8))
    sns.barplot(x=Species.index, y=Species.values)
    plt.title('Values of Species')
    plt.xlabel('Names')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    return plt.gcf()


layout =[
    [sg.Text("Fish Species and count")],
    [sg.Canvas(size=(1000,1000),key="_CANVAS_")],
    [sg.Exit()]
]

def draw_figure(canvas,figure):
    figure_canvas_agg=FigureCanvasTkAgg(figure,canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top',fill='both',expand=1)
    return figure_canvas_agg

window=sg.Window("PySimpleGUI+MatPlotlib barplot",size=(720,720),layout=layout,finalize=True)

draw_figure(window['_CANVAS_'].TKCanvas,create_plot(index,values_count))

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED or event=='Exit':
        break
window.close()