import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

penguins = sns.load_dataset('penguins').dropna()

x = 'flipper_length_mm'
y = 'body_mass_g'
bill_len = 'bill_length_mm'

def scatterplot():
    plt.scatter(penguins['flipper_lenght_mm'], penguins['body_mass_g'])
    plt.xlabel('Flipper length')
    plt.ylabel('Body mass')
    plt.title('Flipper length vs Body mass')
    plt.savefig('penguins_matplotlib.png', dpi=300)

def histplot():
    plt.hist(penguins[bill_len],)  
    plt.xlabel('Bill length')
    plt.ylabel('count')
    plt.title('Bill lenght')
    plt.savefig('bill_leng.png', dpi=300)

def barplot():
    mean_body_mass = penguins.groupby("island")["body_mass_g"].mean().reset_index()
    print(mean_body_mass)
    plt.bar(mean_body_mass['island'], mean_body_mass['body_mass_g'])
    plt.xlabel('Islands')
    plt.ylabel('average body mass (g)')
    plt.title('average penguin body mass by island')
    plt.savefig('average_bodymass_penguin.png', dpi=300)

    

