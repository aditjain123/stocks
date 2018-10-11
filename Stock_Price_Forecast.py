# Add Program Documentaion here
# Function to predict Price based on three statistical Method
def forecast_price(stock_symbol):
    # list of all prices for the recent month's
    BAC = [29.9, 32.5, 31.48, 29.31, 29.95, 29.4, 28.28, 31.25, 30.93]
    T = [37.65, 39.16, 36, 35.1, 32.54, 32.47, 32.21, 31.9, 31.94]
    GE = [17.98, 16.02, 14.02, 13.12, 14.05, 14.1, 13.37, 13.24,12.67]
    F = [12.66, 10.92, 10.29, 10.86, 11.26, 11.71, 11.1, 9.9, 12.94, 9.48]
    TWTR = [24.51, 27.14, 32.24, 28.04, 30.3, 36.65, 44.98, 31.91, 35.18]
    C = [74.36, 79.2, 73.66, 67.71, 68.25, 67.28, 67.16, 71.93, 71.24]
    ORCL = [46.63, 51.63, 49.71, 45.01, 45.95, 47.35, 44.95, 47.25, 48.58]
    JPM = [107.95, 116.87, 113.43, 107.85, 108.78, 108.4, 105.08, 115.66, 114.58]
    PFE = [36.44, 36.83, 35.63, 35.05, 35.4, 36.25, 36.33, 40.27, 41.52]
    BABA = [183.65, 192.22, 181.99, 177.61, 179.5, 204.34, 186.36, 185.27, 175.01]
    AAPL = [172.26, 167.78, 175, 166.68, 169.1, 190.24, 187.18, 201.5, 227.63]
    MSFT = [85.95, 94.26, 92.85, 88.52, 95, 100.79, 100.01, 106.28, 112.33]
    INTC = [46.85, 47.65, 47.84, 48.92, 53.33, 57.08, 50.20, 48.81, 48.24]
    F = [12.66, 10.92, 10.29, 10.86, 11.26, 11.71, 11.10, 9.9, 9.48]
    EBAY = [38.06, 46.40, 42.27, 39.36, 37.83, 38.34, 36.67, 33.09, 34.61]
    AMZN = [1189.01, 1390, 1493.45, 1371.99, 1582.26, 1641.54, 1713.78, 1797.17, 2012.71]
    GOOGL = [1073.21, 1181.59, 1071.41, 1012.63, 1040.75, 1135, 1142.11, 1232.99, 1231.8]
    CHK = [4.1, 3.46, 2.8, 2.97, 2.98, 4.53, 5.18, 4.45, 4.43]
    CLF = [7.85, 6.8, 7.75, 6.85, 7.2, 8.67, 8.5, 10.64, 10.05]
    ABEV = [6.61, 6.95, 6.81, 7.11, 6.57, 5.27, 4.65, 5.16, 4.65]
    FCX = [19.77, 19.45, 18.54, 17.14, 14.95, 17.12, 17.16, 15.58, 14.05]
    GGP = [23.74, 22.84, 21.19, 20.41, 19.93, 20.36, 20.39, 21.17, 22.06]
    VALE = [12.77, 13.18, 13.58, 12.91, 13.54, 14.03, 12.49, 14.06, 13.2]
    HAL = [49.61, 54.51, 46.03, 46.09, 52.44, 49.08, 44.47, 42.06, 39.89]
    WFC = [61.09, 65.51, 57.31, 51.35, 52.56, 54.69, 56.32, 57.65, 58.48]
    VZ = [53.53, 54.3, 47.96, 47.16, 48.82, 47.81, 50.42, 51.73, 54.37]
    AKS = [6.24, 5, 5.65, 4.42, 4.32, 4.62, 4.45, 4.57, 4.44]
    RWT = [14.77, 15.1, 14.66, 15.28, 15.35, 16.4, 16.63, 16.53, 16.98]
    NOK = [4.76, 5.4, 5.76, 5.39, 5.93, 5.85, 5.65, 5.43, 5.55]
    PBR = [10.7, 13.95, 13.98, 13.72, 13.77, 10.13, 10.07, 11.72, 10.87]
    RF = [17.37, 19.54, 19.26, 18.16, 18.75, 18.59, 17.89, 18.83, 19.46]
    SNAP = [14.95, 13.92, 17.21, 14.46, 14.13, 11.63, 13.15, 12.38, 10.9]
    JCP = [3.5, 3.61, 3.92, 2.96, 2.93, 2.36, 2.34, 2.44, 1.77]
    RAD = [2.13, 2.13, 1.88, 1.63, 1.64, 1.57, 1.68, 1.89, 1.32]
    KO = [45.54, 47.75, 43.43, 42.67, 42.59, 43.12, 43.75, 46.39, 44.57]
    a = 0
    mae = 0

    # function selection
    if stock_symbol == 'BAC':
        stock_array_mini = BAC[:-1]
        stock_array_full = BAC
        a = 0.55
    elif stock_symbol == 'T':
        stock_array_mini = T[:-1]
        stock_array_full = T
        a = 0.45
    elif stock_symbol == 'GE':
        stock_array_mini = GE[:-1]
        stock_array_full = GE
        a = 0.3
    elif stock_symbol == 'TWTR':
        stock_array_mini = TWTR[:-1]
        stock_array_full = TWTR
        a = 0.9
    elif stock_symbol == 'C':
        stock_array_mini = C[:-1]
        stock_array_full = C
        a = 0.7
    elif stock_symbol == 'ORCL':
        stock_array_mini = ORCL[:-1]
        stock_array_full = ORCL
        a = 0.6
    elif stock_symbol == 'JPM':
        stock_array_mini = JPM[:-1]
        stock_array_full = JPM
        a = 0.68
    elif stock_symbol == 'PFE':
        stock_array_mini = PFE[:-1]
        stock_array_full = PFE
        a = 0.25
    elif stock_symbol == 'BABA':
        stock_array_mini = BABA[:-1]
        stock_array_full = BABA
        a = 0.85
    elif stock_symbol == 'AAPL':
        stock_array_mini = AAPL[:-1]
        stock_array_full = AAPL
        a = 0.75
    elif stock_symbol == 'MSFT':
        stock_array_mini = MSFT[:-1]
        stock_array_full = MSFT
        a = 0.82
    elif stock_symbol == 'INTC':
        stock_array_mini = INTC[:-1]
        stock_array_full = INTC
        a = 0.5
    elif stock_symbol == 'F':
        stock_array_mini = F[:-1]
        stock_array_full = F
        a = 0.65
    elif stock_symbol == 'EBAY':
        stock_array_mini = EBAY[:-1]
        stock_array_full = EBAY
        a = 0.55
    elif stock_symbol == 'AMZN':
        stock_array_mini = AMZN[:-1]
        stock_array_full = AMZN
        a = 0.8
    elif stock_symbol == 'GOOGL':
        stock_array_mini = GOOGL[:-1]
        stock_array_full = GOOGL
        a = 0.86

    elif stock_symbol == 'CLF':
        stock_array_mini = CLF[:-1]
        stock_array_full = CLF
        a = 0.73
    elif stock_symbol == 'ABEV':
        stock_array_mini = ABEV[:-1]
        stock_array_full = ABEV
        a = 0.56
    elif stock_symbol == 'FCX':
        stock_array_mini = FCX[:-1]
        stock_array_full = FCX
        a = 0.71
    elif stock_symbol == 'GGP':
        stock_array_mini = GGP[:-1]
        stock_array_full = GGP
        a = 0.35
    elif stock_symbol == 'VALE':
        stock_array_mini = VALE[:-1]
        stock_array_full = VALE
        a = 0.73
    elif stock_symbol == 'HAL':
        stock_array_mini = HAL[:-1]
        stock_array_full = HAL
        a = 0.81
    elif stock_symbol == 'WFC':
        stock_array_mini = WFC[:-1]
        stock_array_full = WFC
        a = 0.42
    elif stock_symbol == 'VZ':
        stock_array_mini = VZ[:-1]
        stock_array_full = VZ
        a = 0.51
    elif stock_symbol == 'AKS':
        stock_array_mini = AKS[:-1]
        stock_array_full = AKS
        a = 0.3
    elif stock_symbol == 'RWT':
        stock_array_mini = RWT[:-1]
        stock_array_full = RWT
        a = 0.35
    elif stock_symbol == 'NOK':
        stock_array_mini = NOK[:-1]
        stock_array_full = NOK
        a = 0.28
    elif stock_symbol == 'PBR':
        stock_array_mini = PBR[:-1]
        stock_array_full = PBR
        a = 0.65
    elif stock_symbol == 'RF':
        stock_array_mini = RF[:-1]
        stock_array_full = RF
        a = 0.37
    elif stock_symbol == 'SNAP':
        stock_array_mini = SNAP[:-1]
        stock_array_full = SNAP
        a = 0.7
    elif stock_symbol == 'JCP':
        stock_array_mini = JCP[:-1]
        stock_array_full = JCP
        a = 0.38
    elif stock_symbol == 'RAD':
        stock_array_mini = RAD[:-1]
        stock_array_full = RAD
        a = 0.55
    elif stock_symbol == 'KO':
        stock_array_mini = KO[:-1]
        stock_array_full = KO
        a = 0.51
    elif stock_symbol == 'CHK':
        stock_array_mini = CHK[:-1]
        stock_array_full = CHK
        a = 0.7

    print ('the price of this stock in the beginning of last month was ${}'.format(stock_array_full[-1]))

    # Expoential smoothing technique - assigns exponentially decreasing weights for newest to oldest observations newer data is seen as more relevant and is assigned more weight`
    #Smoothing parameters denoted by a determine the weights for observations.
    smoothing_2 = stock_array_full[0]
    smoothing_3 = a * stock_array_full[1] + (1 - a) * smoothing_2
    smoothing_4 = a * stock_array_full[2] + (1 - a) * smoothing_3
    smoothing_5 = a * stock_array_full[3] + (1 - a) * smoothing_4
    smoothing_6 = a * stock_array_full[4] + (1 - a) * smoothing_5
    smoothing_7 = a * stock_array_full[5] + (1 - a) * smoothing_6
    smoothing_8 = a * stock_array_full[6] + (1 - a) * smoothing_7
    smoothing_9 = a * stock_array_full[7] + (1 - a) * smoothing_8
    smoothing_10 = a * stock_array_full[8] + (1 - a) * smoothing_9


    # Weighted Moving Average Technique - Weighted moving averages assign a heavier weighting to more current data points
    # since they are more relevant than data points in the distant past.

    x = len(stock_array_full)
    x_1 = x * stock_array_full[-1]
    x_2 = (x - 1) * stock_array_full[-2]
    x_3 = (x - 2) * stock_array_full[-3]
    x_4 = (x - 3) * stock_array_full[-4]
    x_5 = (x - 4) * stock_array_full[-5]
    x_6 = (x - 5) * stock_array_full[-6]
    x_7 = (x - 6) * stock_array_full[-7]
    x_8 = (x - 7) * stock_array_full[-8]
    x_9 = (x - 8) * stock_array_full[-9]


    masum = (x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_7 + x_8 + x_9)
    madivide = (x) + (x - 1) + (x - 2) + (x - 3) + (x - 4) + (x - 5) + (x - 6) + (x - 7) + (x - 8)

    ma = masum / madivide

    # Following technique is developed by me, it is based on Z scores. First it finds the z-score with all the data except the last one. To find the next month's price
    #mulitply the z score by the standard deviation for all the values in the list and then add the product to the mean value.

    first_mean = float(sum(stock_array_mini) / max(len(stock_array_mini), 1))
    # z_score_algo
    first_var = [(num - first_mean) ** 2 for num in stock_array_mini]

    for num in first_var:
        var_sum = sum(first_var)
    mean_std = (var_sum / len(stock_array_mini))
    final_std = mean_std ** .5
    z = (stock_array_mini[-1] - first_mean) / final_std

    mean2 = float(sum(stock_array_full)) / max(len(stock_array_full), 1)
    secondvar = [(num - mean2) ** 2 for num in stock_array_full]

    for num in secondvar:

        var_sum2 = sum(secondvar)

        mean_std2 = (var_sum2 / len(stock_array_full))
        finalstd2 = mean_std2 ** .5

        final = (z * finalstd2) + mean2

        # Following section determines the best methods to predict the stock prices


        # if z score is less than 1 or greater than -1 then the stock price will solely be determained by z score technique

        if z < 1 or z > -1:
            print ("The stock price around the beginning of next month will be ${} ".format(round(final, 2)))
            if final > stock_array_full[-1]:
                print("buy the stock")
            else:

        # if z score is less than 2.2 or greater than -2.2 then find the simple average of the z-score and exponential smoothing methods to predict the stock price
                print("sell the stock")
        elif z < 2.2 or z > 2.2:

            ze = (final + smoothing_9) / 2
            if ze > stock_array_full[-1]:
                print("buy the stock")
            else:
                print("sell the stock")
            print ("The stock price around the beginning of next month would be ${} ".format(round(ze, 2)))
        else:

        # If the z score does not fit in those parameters then find the simple average of the expoential smoothing and moving average methods to predict the stock price

            mae = (smoothing_10 + ma) / 2
            if mae > stock_array_full[-1]:
                print("buy the stock")
            else:
                print("sell the stock")
            print ("The stock price around the beginning of next month would be ${} ".format(round(mae, 2)))
        break

# main program to call the forecast function
y = 0
while y == 0:
        x = input("which stock's next month's price would you like this program to predict put one of these tickers on the input BAC, T, GE, F, TWTR, C, ORCL, JPM, PFE, BABA, AAPL, MSFT, INTC, \n F, EBAY, AMZN, GOOGL, CHK, CLF, ABEV, FCX, GGP, VALE, HAL, WFC, VZ, AKS, RWT, NOK, PBR, RF, SNAP, JCP, RAD, KO and then press run\n")
        if x == 'DONE':
            break
        print ("".format((forecast_price(x))))



