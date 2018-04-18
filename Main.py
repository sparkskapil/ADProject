import MonthlyTrends as MT
import YearlyTrends as YT
import matplotlib.pyplot as plt
import KMeans as KM
from Tkinter import *

GUI = Tk()
GUI.title("Advance Database Mini Project")
Frame1 = Frame(GUI) #Contains Name Of Project
Frame2 = Frame(GUI) #Contains Yearly Checkbox
Frame3 = Frame(GUI) #Contains Monthly(2013 2014) Checkboxes
Frame4 = Frame(GUI) #Contains Monthly(2015 2016) Checkboxes
Frame5 = Frame(GUI) #Contains Buttons

Frame1.pack()
Frame2.pack()
Frame3.pack()
Frame4.pack()
Frame5.pack()


Project = Label(Frame1,text="Insights and Analysis on Bitcoin Trends", font=(None, 20))

By = Label(Frame1,text="Project By Kapil Verma, Sushant Kamble, Durgesh Deore" , font=(None, 12))
Project.pack();
By.pack();

CheckYearly = IntVar()
Check2013 = IntVar()
Check2014 = IntVar()
Check2015 = IntVar()
Check2016 = IntVar()

C1 = Checkbutton(Frame2, text = "Yearly Trends", variable = CheckYearly, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(Frame3, text = "Monthly Trends 2013", variable = Check2013, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C3 = Checkbutton(Frame3, text = "Monthly Trends 2014", variable = Check2014, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C4 = Checkbutton(Frame4, text = "Monthly Trends 2015", variable = Check2015, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C5 = Checkbutton(Frame4, text = "Monthly Trends 2016", variable = Check2016, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)

def ShowInsights():
	plt.close("all")
	if CheckYearly.get() == 1:
		YT.YearlyShow()
	if Check2013.get() == 1:
		MT.show2013()
	if Check2014.get() == 1:
			MT.show2014()
	if Check2015.get() == 1:
			MT.show2015()
	if Check2016.get() == 1:
			MT.show2016()

	plt.show();

def ShowClusters():
	plt.close()
	KM.Cluster()
	
ShowGraphs = Button(Frame5,text = "Show ShowGraphs", command = ShowInsights);
KMeans = Button(Frame5, text = "Show KMeans Analysis", command = ShowClusters);

C1.pack()
C2.pack(side = LEFT)
C3.pack(side = LEFT)
C4.pack(side = LEFT)
C5.pack(side = LEFT)

ShowGraphs.pack(side = LEFT);
KMeans.pack(side = LEFT);
GUI.mainloop()


