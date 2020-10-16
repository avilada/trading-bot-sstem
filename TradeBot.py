import robin_stocks as rp
import matplotlib.pyplot as plt
import math
import numpy as np
from shapely.geometry import LineString

# Login
with open("robinhood_login.txt", "r") as f:
    rp.login(f.readline(), f.readline())

# Stock info

stock_list = ["AAPL","TSLA"]
stocks = rp.stocks.get_quotes(stock_list)

for i in range(0, len(stocks)):
    ##print(stocks[i].get("ask_price"))
    break

stonks = rp.stocks.get_stock_historicals(stock_list, interval="day", span="year")

for i in range(0, len(stonks)):
    ##print(stonks[i].get("symbol"), stonks[i].get("begins_at"), stonks[i].get("open_price"), stonks[i].get("close_price"))
    break

"""
def simulate(pointpairs):
    buy = True
    basemoney = 1000
    startmoney = math.log(basemoney)
    currentstocks = 0
    lastbuy = 0
    #print(startmoney)
    for i in range(1, len(pointpairs)):
        if pointpairs[i][0] - pointpairs[i-1][0] > 15:
            if buy:
                currentstocks += startmoney/pointpairs[i][1]
                startmoney = 0
                lastbuy = pointpairs[i][1]
                #print(startmoney, currentstocks, "B", pointpairs[i][1])
                buy = False
            if not buy and lastbuy < pointpairs[i][1]-0.01:
                startmoney += currentstocks*pointpairs[i][1]
                currentstocks = 0
                #print(startmoney, currentstocks, "S", pointpairs[i][1])
                buy = True
        if(i == len(pointpairs)-1):
            startmoney += currentstocks*pointpairs[i][1]
            currentstocks = 0
    finalmoney = startmoney - math.log(basemoney)
    print(math.exp(finalmoney))
"""






price = []
day =  []
# special1 = []
# special2 = []
# weirdchamp = [0,0]
# first = True

for i in range(0, len(stonks)):
    if stonks[i].get("symbol") == "TSLA":
        day.append(i)
        price.append(float(stonks[i].get("open_price")))
        # if first == True:      
        #     special1.append(i)
        #     special2.append(math.log(float(stonks[i].get("open_price"))))
        # first = False
        # weirdchamp[0] = i
        # weirdchamp[1] = math.log(float(stonks[i].get("open_price")))

# special1.append(weirdchamp[0])
# special2.append(weirdchamp[1])

# X then Y
#plt.plot(special2[0], special2[0]+(gradient*len(stonks)/2))

#plt.plot(day, price)

"""
plt.plot(special1, special2)
first_line = LineString(np.column_stack((day, price)))
second_line = LineString(np.column_stack((special1, special2)))
intersection = first_line.intersection(second_line)
if intersection.geom_type == 'MultiPoint':
    plt.plot(*LineString(intersection).xy, 'o')
elif intersection.geom_type == 'Point':
    plt.plot(*intersection.xy, 'o')

x, y = LineString(intersection).xy

pointpairs = []

for i in range(0, len(x)):
    temp = [x[i], y[i]]
    pointpairs.append(temp)
profits = simulate(pointpairs)
"""




# Idea: divide the graph into chunks of size on chunk 1: Do nothing
# From chunk 1 onwards, if average is + then look to sell, if - then look to buy, else wait.
# determine the peak using gradients if possibe.


# chunksize = 10
# start = True
# firstrandom = True

# currentbal = 1000
# stockstotal = 0

# for i in range(0, int(len(price)/chunksize)):
#     points = []
#     for j in range(0, chunksize):
#         if start:
#             points.append(price[(i*j) + j])
#             average = average(points)
#         else:
#             if average > 4:
#                 points.append(price[(i*j) + j])
#                 average = average(points)

#                 if firstrandom:
#                     for k in range(0, 3):
#                         points.append(price[(i*j) - k])
#                     firstrandom = False

#                 gradient1 = (points[j+1]-points[j])/2
#                 gradient2 =  (points[j+2]-points[j+1])/2
                
#                 if gradient1 - gradient2 < 0:
#                     stockstotal = currentbal/price[(i*j) + j]
#                     currentbal = 0

#             elif average < -4:
#                 points.append(price[(i*j) + j])
#                 average = average(points)

#                 if firstrandom:
#                     for k in range(0, 3):
#                         points.append(price[(i*j) - k])
#                     firstrandom = False

#                 gradient1 = (points[j+1]-points[j])/2
#                 gradient2 =  (points[j+2]-points[j+1])/2
                
#                 if gradient1 - gradient2 > 0:
#                     currentbal = stockstotal*price[(i*j) + j]
#                     stockstotal = 0

#             else:
#                 points.append(price[(i*j) + j])
#                 average = average(points)

#     start = False
#     firstrandom = True


# print(currentbal, stockstotal)

# plt.show()


def show_prices(holdings, interval="day", time_span = "year", trading_bounds = "regular"):
    stock_symbols = holdings.keys()
    price = []
    for stck in stock_symbols:
        meme = []
        oldervals = rp.stocks.get_stock_historicals(stck, interval="day", span = time_span)
        for i in range(len(oldervals)):
            meme.append(float(oldervals[i].get("open_price")))
        price.append(meme)
    day = [x for x in range(len(price[0]))]
    for label, pr in enumerate(price):
        plt.plot(day, pr, label = label)
    plt.show()

def average(list):
    min = 0
    max = 0

    edit1 = []
    edit2 = []

    for x in list:
        if x > max:
            max = x
        if x < min:
            min = x
    
    for x in list:
        edit1.append(x-min)

    for x in edit1:
        edit2.append(x/max)

    average = 0
    for x in edit2:
        average += x
    average /= len(edit2)

    return average




def run_algorithm(holdings, time_span = "year", interval="day"):
    stock_symbols = holdings.keys()
    price = []
    for stck in stock_symbols:
        meme = []
        oldervals = rp.stocks.get_stock_historicals(stck, interval= interval, span = time_span)
        for i in range(len(oldervals)):
            meme.append(float(oldervals[i].get("open_price")))
        price.append(meme)

    step_size = 10
    start = True

    currentbal = 1000
    stockamount = 0
    for stck, price in zip(stock_symbols,price):
        average = 0
        for i in range( int(len(price)/step_size) ):
            if start:
                temp = []
                for j in range(step_size):
                    temp.append(price[j])
                start = False
                average = average(temp)
            else:
                if average > 0.75 or average < 0.25:
                    temp = []
                    for j in range(step_size/2):
                        temp.append(price[j+i*step_size])
                    average = average(temp)
                    

                    grad1 = temp[step_size/2] - temp[(step_size/2)-1]
                    grad2 = 0

                    # Sell
                    if average > 0.75:
                        if grad2 == 0 :
                            temp.append(price[(step_size/2)+i*step_size])
                            grad2 = temp[(step_size/2)+1] - temp[(step_size/2)]
                        k = (step_size/2)+1 
                        while k != step_size:
                            if grad2 < 0 and grad1 > 0:
                                ## Action is sell
                                currentbal = stockamount*price[k-1+i*step_size]
                            temp.append(price[k+i*step_size])
                            grad1 = temp[k-1] - temp[k-2]
                            grad2 = temp[k] - temp[k-1]
                            k += 1
                        
                    # Buy
                    elif average < 0.25:
                        if grad2 == 0 :
                            temp.append(price[(step_size/2)+i*step_size])
                            grad2 = temp[(step_size/2)+1] - temp[(step_size/2)]
                        k = (step_size/2)+1 
                        while k != step_size:
                            if grad2 > 0 and grad1 < 0:
                                ## Action is buy
                                stockamount = currentbal/price[k-1+i*step_size]
                            temp.append(price[k+i*step_size])
                            grad1 = temp[k-1] - temp[k-2]
                            grad2 = temp[k] - temp[k-1]
                            k += 1
                    average = average(temp)
                else:
                    temp = []
                    for j in range(step_size):
                        temp.append(price[j+i*step_size])
                    average = average(temp)     
    return currentbal - 1000               
                    


    
holdings = {
    "AAPL" : "SMH"
}



show_prices(holdings)
weirdchamp = run_algorithm(holdings)
print(weirdchamp)


            










# Logout
rp.logout()
