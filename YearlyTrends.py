from pymongo import MongoClient
import matplotlib.pyplot as plt

def YearlyShow():
	conn = MongoClient();
	db = conn.AdvanceDatabase;
	collection = db.TrendsYearly
	cursor = collection.find({})


	years = []
	increase = []
	decrease = []

	for doc in cursor:

		years.append(doc['_id'])
		increase.append(doc['value']['AverageIncrease'])
		decrease.append(doc['value']['AverageDecrease'])
		
	plt.figure("Yearly Trends");
		
	plt.plot(years, increase, label = "Average Increase")

	plt.plot(years, decrease, label = "Average Decrease")

	# naming the x axis
	plt.xlabel('Years')

	# naming the y axis
	plt.ylabel('Difference In Open and Close Rates')

	plt.legend()

	conn.close()

