# !/usr/bin/python

import matplotlib.pyplot as plt
num_Area = input("Enter the no. of Areas to Cover : ")
ar_list = []
im_list = []
ar_num = []
c = 1
d = 3
for i in range(num_Area):
        ar_num.append(d)
        Area_name = raw_input("Enter name of Area : ")

        ar_list.append(Area_name)

        A = float(input("Enter the Regime C/S Area of affected places of Area in squared km" + str(c) +" : "))
        ha = float(input("Enter the height of affected area from Sea level in km: "))
        hs = float(input("Enter the height of source from Sea level 3in km: "))
        X = float(input("Enter the Displacement from the flood source in Area in km " + str(c) + " : "))
        R = float(input("Enter the total amount of rainfall in the last 4 days at the affected Area in mm" + str(c) + " : "))
        N = float(input("Enter the number of rivers in affected Area " + str(c) + " : "))
        T = float(input("Enter the Density of Trees in the affected Area in percentage of the total land area" + str(c) + " : "))
        L = float(input("Enter the gross length of main channel in Area in km" + str(c) + " : " ))
        H = ha - hs
        if H == 0 :
                H = 1
        S = abs(H/X)
        Tc = (0.605 * (L/((S**0.2)*(A**0.1))))

        if A > 0 and A <= 10 :
                f = 1
        elif A > 10 and A <= 20 :
                f = 0.950
        elif A > 20 and A <= 30 :
                f = 0.900
        elif A > 30 and A <= 40 :
                f = 0.875
        elif A > 40 and A <= 50 :
                f = 0.845
        elif A > 50 and A <= 60 :
                f = 0.820
        elif A > 60 and A <= 70 :
                f = 0.800
        elif A > 70 and A <= 80 :
                f = 0.775
        elif A > 80 and A <= 90 :
                f = 0.760
        elif A > 90 and A <= 100 :
                f = 0.745
        elif A > 100 and A <= 150 :
                f = 0.730
        elif A > 150 and A <= 200 :
                f = 0.675
        elif A > 200 and A <= 300 :
                f = 0.645
        elif A > 300 and A <= 400 :
                f = 0.625
        elif A > 400 and A <= 2000 :
                f = 0.620
        elif A > 2000 :
                f = 0.600
        else :
                print "Enter Valid value of A"

        print "Enter the type of Soil in the Area : (Enter No.)\n\n 1.Steep, bare rock\n2.Rock, steep but with woods\n3.Pleatue, lightly covered\n4.Densly built up areas of cities with metal roads\n5.Residential areas not densely built up, with metalled roads\n6.Residential areas not densely built up, with unmetalled roads\n7.Clayay soils, stiff and bare\n8.Clayay soils, lightly covered\n9.Loam, lightly cultivated\n10.Loam, largely Cultivated\n11.Suburbs with gardens, lawns and macadamized roads\n12.Sandy soils, light growth\n13.Sandy soils, covered, heavy bush\n14.Jungle area\n15.Parks, lawns, meadows, gardens, cultivated area\n"

        st = input("Enter Choice from above list : ")
        if st == 1 :
                P = 0.90
        elif st == 2 :
                P = 0.80
        elif st == 3 :
                P = 0.70
        elif st == 4 :
                P = 0.80
        elif st == 5 :
                P = 0.60
        elif st == 6 :
                P = 0.35
        elif st == 7 :
                P = 0.60
        elif st == 8 :
                P = 0.50
        elif st == 9 :
                P = 0.40
        elif st == 10 :
                P = 0.30
        elif st == 11 :
                P = 0.30
        elif st == 12 :
                P = 0.20
        elif st == 13 :
                P = 0.10
        elif st == 14 :
                P = 0.175
        elif st == 15 :
                P = 0.375
        else :
                print "Enter valid choice from above list"

        lmda = ((2*f*P)/(Tc+1))
        W = (A*R*lmda)
        if H > 0 and H < 1 :
                I = abs((N*R*W)/(A*X*T))


        elif H < 0 :
                I= abs((N*R*W)/(A*X*T*H))

        else :
                I = abs((N*R*W*H)/(A*X*T))

        print "I = ",I,"K"
        im_list.append(I)
        c += 1
        d += 1
print ar_list
print im_list

xs = [i + 0.1 for i, _ in enumerate(ar_num)]
plt.plot(xs,im_list,'ro')
plt.plot(xs,im_list) 
plt.grid(True)
plt.xlabel("Areas")
plt.ylabel("Impact")
plt.xticks(xs,ar_list)
plt.show()

xs = [i + 0.1 for i, _ in enumerate(ar_list)]
plt.grid(True)
plt.xlabel("Areas")
plt.ylabel("Impact")
plt.bar(xs,im_list,0.5)
plt.xticks([i +0.3 for i, _ in enumerate(ar_list)],ar_list)
plt.show()
