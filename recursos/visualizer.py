import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    def __init__(self, data, style="whitegrid", palette="deep"):
        self.data = data
        self.style = style
        self.palette = palette
        sns.set_style(self.style)
        sns.set_palette(self.palette)
        
    def plot_line(self, x, y, hue=None, title="Line Plot", xlabel="X Axis", ylabel="Y Axis", **kwargs):
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=self.data, x=x, y=y, hue=hue, **kwargs)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()
    
    def plot_bar(self, x, y, hue=None, title="Bar Plot", xlabel="X Axis", ylabel="Y Axis", **kwargs):
        plt.figure(figsize=(10, 6))
        sns.barplot(data=self.data, x=x, y=y, hue=hue, **kwargs)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()
    
    def plot_scatter(self, x, y, hue=None, title="Scatter Plot", xlabel="X Axis", ylabel="Y Axis", **kwargs):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.data, x=x, y=y, hue=hue, **kwargs)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()
    
    def plot_correlation_matrix(self, title="Correlation Matrix", cmap="coolwarm", annot=True):
        plt.figure(figsize=(12, 8))
        corr = self.data.corr()
        sns.heatmap(corr, cmap=cmap, annot=annot, fmt=".2f")
        plt.title(title)
        plt.show()
    
    def set_style(self, style):
        self.style = style
        sns.set_style(self.style)
    
    def set_palette(self, palette):
        self.palette = palette
        sns.set_palette(self.palette)
