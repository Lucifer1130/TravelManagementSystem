import tkinter
import tkinter as tk
import tkinter.scrolledtext as st
import matplotlib.pyplot as plt
import pandas
import seaborn as sb
from PIL import Image, ImageTk
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import auth as auth
import pyodbc


def main():

    cn = pyodbc.connect('Driver={SQL Server};'
                        'Server=CHIKU;'
                        'Database=tours;'
                        'Trusted_Connection=yes;')
    cursor = cn.cursor()

    # reading dataset
    dset = pandas.read_csv(r'C:\Users\User\Desktop\projdset.csv')
    print(dset.head(30))
    print(dset.isnull().sum())

    # cleaning dataset
    dset.drop('party', inplace=True, axis=1)
    dset.drop('BOOKED BY', inplace=True, axis=1)
    dset = dset.rename(columns={'T K.m': 'Total_km', 'T. Amt.': 'Total_amt'})
    print(dset.isnull().sum())
    dset.interpolate()
    dset['NT'].fillna(method='pad', inplace=True)
    dset.fillna(method='bfill', inplace=True)
    print(dset.isnull().sum())

    # relationship analysis
    dset.Total_km.describe()
    dset['Total_km'] = dset.Total_km.map(lambda x: 1 if x == 0 else x)
    dset = dset[dset.Total_km <= 5000]

    # linear regression
    # Fitting the Simple Linear Regression model to the training dataset
    X = dset['Total_km'].values.reshape(-1, 1)
    y = dset['Total_amt'].values.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    from sklearn.linear_model import LinearRegression

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)  # training the algorithm
    # To retrieve the intercept:
    print("Value of intercept is = ", regressor.intercept_)
    # For retrieving the slope:
    print("Value of coefficient is = ", regressor.coef_)
    x_pred = regressor.predict(X_train)
    y_pred = regressor.predict(X_test)
    df = pandas.DataFrame({'Actual Amount': y_test.flatten(), 'Predicted Amount': y_pred.flatten()})
    df1 = df.head(25)

    window = tkinter.Tk()
    window.geometry("1130x300")
    window.resizable(0, 0)
    window.title("Vehicle Detailer")
    window.config(bg="RosyBrown")


    # function ez
    def ez():
        cursor.execute("SELECT Veh_type, COUNT(Veh_No) AS MOST_FREQUENT from "
                       "projdset1 GROUP BY Veh_type ORDER BY COUNT("
                       "Veh_type) DESC")

        # Creating tkinter window
        win = tk.Tk()
        win.title("ToursNTravels")

        # Title Label
        tk.Label(win,
                 text="OutPut",
                 font=("Times New Roman", 15),
                 bg="RosyBrown",
                 foreground="white").grid(column=0,
                                          row=0)
        text_area = st.ScrolledText(win,
                                    width=30,
                                    height=8,
                                    font=("Times New Roman",
                                          15), bg="RosyBrown")

        text_area.grid(column=10, pady=10, padx=10)

        for row in cursor:
            text_area.insert(tk.INSERT, row)
            text_area.insert(tk.INSERT, "\n")

        text_area.configure(state='disabled')


    def ra1():
        pandas.options.display.float_format = '{:.2f}'.format
        plt.figure(figsize=(15, 5))
        sb.boxplot(dset.Total_km)
        plt.show()


    def ra2():
        sb.countplot(dset.Total_km)
        plt.show()


    def vds():
        plt.scatter(X_test, y_test, color="green")
        plt.plot(X_train, x_pred, color="red")
        plt.title("Total_km vs Total_amt (Test Dataset)")
        plt.xlabel("total distance covered")
        plt.ylabel("Amount to be paid(In Rupees)")
        plt.show()


    def tds():
        plt.scatter(X_train, y_train, color="green")
        plt.plot(X_train, x_pred, color="red")
        plt.title("Total_km vs Total_amt (Training Dataset)")
        plt.xlabel("total distance covered")
        plt.ylabel("Amount to be paid(In Rupees)")
        plt.show()


    def mse():
        accuracy = mean_squared_error(y_test, y_pred)
        b3 = tkinter.Label(window, text=str(accuracy)).grid(row=4, column=1)


    def aim_bot():
        win3 = tk.Tk()
        win3.title("Predictions")
        win3.geometry("230x400")
        b4 = tkinter.Label(win3, text=str(df1)).grid()


    def gg():
        win1 = tk.Tk()
        win1.title("Check Amount")
        win1.geometry("250x160")
        win1.config(bg="RosyBrown")

        def gg1():
            x = int(z1.get())
            new_amt = regressor.predict([[x]])
            y = new_amt[0][0]
            a3 = tkinter.Label(win1, text=str(y)).pack()

        z1 = tkinter.Entry(win1)
        z1.pack()
        a2 = tkinter.Button(win1, text="Check Amount", command=gg1).pack()


    def close_window():
        window.destroy()





    a = tkinter.Label(window, justify="center", text="Tours and Travels Management System", bg="RosyBrown",
                      font=("Arial", 20))
    a.config(justify='center')
    a.grid(row=0, column=2)
    c = tkinter.Button(window, text="Get most frequent vehicle used", command=ez).grid(row=4, column=2)
    d = tkinter.Button(window, text="Relationship Analysis", command=ra1).grid(row=3, column=0)
    d2 = tkinter.Button(window, text="Relationship Analysis 2", command=ra2).grid(row=3, column=5, )
    e = tkinter.Button(window, text="The Mean Squared Error", command=mse).grid(row=4, column=0)
    e2 = tkinter.Label(window, text="                                    ", bg='RosyBrown').grid(row=4, column=1)
    f = tkinter.Button(window, text="Actual and Predicted Values", command=aim_bot).grid(row=4, column=5)
    f1 = tkinter.Label(window, text="                       ", bg='RosyBrown').grid(column=4)
    g = tkinter.Button(window, text="Visualization of Training DataSet", command=tds).grid(row=5, column=0, padx=20)
    h = tkinter.Button(window, text="Visualization of Test DataSet", command=vds).grid(row=5, column=5)
    i = tkinter.Button(window, text="Enter KM. to check amount", command=gg).grid(row=6, column=2)
    z = tkinter.Button(window, text="Exit", command=close_window, height=2, width=30).grid(row=10, column=2)


    window.mainloop()
