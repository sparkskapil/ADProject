import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

from pymongo import MongoClient

def Cluster():
	conn = MongoClient();
	db = conn.AdvanceDatabase;
	collection = db.TrendsMonthly
	cursor = collection.find({})

	monthofyear = []
	increase = []
	decrease = []

	for doc in cursor:
			monthofyear.append(doc['_id'])
			increase.append(doc['value']['AverageIncrease'])
			decrease.append(doc['value']['AverageDecrease'])
		
	df = pd.DataFrame(columns=['x','y'])
	for i in range(0,len(monthofyear)):
		df.loc[monthofyear[i]] = [increase[i],decrease[i]]

	#Remove Empty Values
	df = df[np.isfinite(df['x'])]
	df = df[np.isfinite(df['y'])]	



	#Start Clustering
	data_points = df.values
	kmeans = KMeans(n_clusters=3).fit(data_points)

	df['cluster_id'] = kmeans.labels_

	sns.lmplot('x', 'y', data = df, \
		fit_reg=False, scatter_kws={"s":25},\
		hue="cluster_id")

	plt.title("K Mean Plot")

	plt.xlabel('Average Increase')

	plt.ylabel('AverageDecrease')

	plt.show()

	conn.close()

