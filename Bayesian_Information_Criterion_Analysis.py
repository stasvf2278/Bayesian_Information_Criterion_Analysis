#-------------------------------------------------------------------------------
# Name:        Bayesian Information Criterion Analysis
# Purpose:     Comparing Power Laws of a data set
#
# Author:      Stanley
#
# Created:     07/03/2018
# Copyright:   (c) Stanley 2020
#-------------------------------------------------------------------------------
import math
import pandas as pd
import numpy as np
from numpy import pi, r_
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.stats import linregress

def main():

    df1 = pd.read_csv("PorPerm2ABLM.csv")                                           ##########CHANGE FILE NAME HERE ## Imports .csv file

    por_list = df1["porosity"].tolist()                                             ## Converts column labeled "porosity" to porosity list
    perm_list = df1["permeability"].tolist()                                        ## Converts column labeled "permeability" to permeability list

    for i in range(len(por_list)):                                                  ## Converts lab values to log base 10 values without changing list names
        por_list[i] = math.log10(por_list[i])
        perm_list[i] = math.log10(perm_list[i])
        i = i + 1

    model = linregress(por_list, perm_list)                                         ##calulates linear model (slope, intercept), x and y are arrays or lists
    slope, intercept = model.slope, model.intercept                                 ##defines variables for slope and intercept

    SSE = 0
    i = 0
    for i in range(len(por_list)):                                                  ##Calculates SSE of entire dataset
        SSE = SSE + ((perm_list[i]-(slope*por_list[i]+intercept))**2)
        i = i + 1

    BICR = len(por_list)*math.log(SSE)/2-(1.5*math.log(len(por_list)/(2*math.pi)))
    ##BICR = (len(por_list)*math.log(SSE)/2)                                        ##troubleshooting BICR, ignore
    ##BICR = 1.5*math.log(len(por_list)/(2*math.pi))                                ##troubleshooting BICR, ignore
    print("BICR: " + str(BICR))

    x_star = min(por_list)                                                          ## Defines x* as min log_10_porosity from

    while x_star < max(por_list):                                                   ## Iteration process that steps through x* values to calculate BIC
        lessthanpor = []
        lessthanperm = []
        morethanpor = []
        morethanperm = []
        for z in range(len(por_list)):                                              ## Seperates dataset into < and > x* log_10_porosity
            if por_list[z] < x_star:
                lessthanpor.append(por_list[z])
                lessthanperm.append(perm_list[z])
            if por_list[z] > x_star:
                morethanpor.append(por_list[z])
                morethanperm.append(perm_list[z])
        ltslope = 0
        ltintercept = 0
        mtslope = 0
        mtintercept = 0
        SSElt = 0
        SSEmt = 0
        if len(lessthanpor) > 2:                                                    ## Defines m and b for two linear functions (y = mx + b)
            lessthanmodel = linregress(lessthanpor,lessthanperm)                    ## This is the guts of the analysis. See Farquharson et al. (2015) in the README.txt for a detailed explanation
            ltslope, ltintercept = lessthanmodel.slope, lessthanmodel.intercept
            for p in range(len(lessthanpor)):
                SSElt = SSElt + (((lessthanperm[p] - (ltslope*lessthanpor[p]+ltintercept)))**2)
            if len(morethanpor) > 2:
                morethanmodel = linregress(morethanpor,morethanperm)
                mtslope, mtintercept = morethanmodel.slope, morethanmodel.intercept
                q = 0
                for q in range(len(morethanpor)):
                    SSEmt = SSEmt + (((morethanperm[q] - (ltintercept+x_star*(ltslope-mtslope)+(mtslope*morethanpor[q])))))**2
                BICx_star = len(por_list)*math.log(SSEmt+SSElt)/2 - 2.5*math.log(len(por_list)/(2*math.pi))
    ##            fhalf = len(por_list)*math.log(SSEmt+SSElt)/2                     ## Trouble shooting BICx*, ignore
    ##            shalf = 2.5*math.log(len(por_list)/(2*math.pi))                   ## Trouble shooting BICxI, ignore

        if ltslope > 0:
            if mtslope > 0:                                                     ## With enough scatter, low-x data points can produce negative slopes, making this line necessary
                if ltslope > mtslope:                                           ## This line was important for my rock mechanics study as the lower x-value power law needed to be greater than the higher x-value power law. Depending on your data, this line may need to be removed and identation corrected.
                    if(BICx_star-BICR) > 1:                                     ## Ensures the power laws are statistically different
                        print("")
                        print("BICx* - BICR: " + str(BICx_star-BICR))           ## Gives BICx* - BICR
                        print("x*: " + str(x_star))
                        print("Porosity: " + str(10**x_star))                   ## Porosity (or x-value) that corresponds to x*
                        print("")
                        print("xi < x* slope " + str(ltslope))                  ## Slope of the lower x-value power law
                        print("xi > x* slope " + str(mtslope))                  ## Slope of the higher x-value power law
                        print("")
            ##            print("SSElt " + str(SSElt))
            ##            print("SSEmt " + str(SSEmt))
            ##            print fhalf
            ##            print shalf
                        print("BICx*: " + str(BICx_star))                       ## Gives BICx*
                        print("xi < x* n = " + str(len(lessthanpor)))           ## Gives population number of data for lower power law
                        print("xi < x* intercept " + str(ltintercept))          ## Y-itercept of the lower x-value power law
                        print("xi > x* intercept " + str(mtintercept))          ## Y-itercept of the higher x-value power law
                        print("*******************************END OF SERIES*******************************")
        x_star = x_star + 0.01

if name == "main":
    main()




