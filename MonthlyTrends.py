from pymongo import MongoClient
import matplotlib.pyplot as plt

def Draw(Year):
	conn = MongoClient();
	db = conn.AdvanceDatabase;
	collection = db.TrendsMonthly
	cursor = collection.find({})

	years = []
	increase = []
	decrease = []

	for doc in cursor:
		if(Year in doc['_id']):
			years.append(doc['_id'][5:])
			increase.append(doc['value']['AverageIncrease'])
			decrease.append(doc['value']['AverageDecrease'])
		

	plt.plot(years, increase, label = "Average Increase")
	plt.plot(years, decrease, label = "Average Decrease")
	plt.xlabel('Months')
	plt.ylabel('Difference In Open and Close Rates')
	plt.legend()
	conn.close();

def show2013():
	plt.figure(2013)
	Draw("2013")

def show2014():
	plt.figure(2014)
	Draw("2014")

def show2015():
	plt.figure(2015)
	Draw("2015")

def show2016():
	plt.figure(2016)
	Draw("2016")

