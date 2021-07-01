import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('agg')
import numpy as np

def pieGraph(data, labels, path):
    plt.autoscale()
    plt.pie(data, labels=labels, labeldistance=1.15)
    plt.savefig('front/web/static/' + path)
    plt.cla()

def barsGraph(data, labels, path):
    bars = np.arange(len(labels))
    plt.autoscale()
    plt.bar(bars, data)
    plt.xticks(bars, labels = labels, rotation=90)
    plt.subplots_adjust(bottom=0.3)
    plt.savefig('front/web/static/' + path)
    plt.cla()

def donutGraph(data, labels, path):
    plt.autoscale()
    plt.pie(data, labels = labels, labeldistance=1.15)
    my_circle=plt.Circle( (0,0), 0.7, color='white')
    p=plt.gcf()
    p.gca().add_artist(my_circle)
    plt.savefig('front/web/static/' + path)
    plt.cla()