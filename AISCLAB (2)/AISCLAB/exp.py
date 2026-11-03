import numpy as np
import matplotlib.pyplot as plt
from sklearn.dataset import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
x=StandardScaler().fit_transform(load_iris().data)
som=MiniSom(10,10,4,sigmoid=1.5,learning_rate=0.5,random_seed=42)
som.pca_weights_init(x)
som.train_random(x,1000)
weights=som.get_weights().reshape(-1,4)
clusters=KMeans(n_clusters=4,random_state=42,n_init=10).fit_predict(weights)

x,y=np.meshgrid(range(10),range(10))
plt.scatter(x,y,c=clusters)
plt.title("SOM - 4 Clusters")
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar()
plt.show()
