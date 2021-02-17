#Project 2
#Author: Josh Gervich
#Purpose: To analyze time complexity of Insertion Sort, Merge Sort,
#quicksort, and selection sort
import sys
import time
from random import randint
import xlwt
from xlwt import Workbook
from sort import Sort
sys.setrecursionlimit(2000)

bestCase = []
worstCase = []
averageCase = []

# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

#get the columns and row headers in order  
sheet1.write(0, 0, 'n')
sheet1.write(0, 1, 'Time(best case)')
sheet1.write(0, 2, 'Time(average case')
sheet1.write(0, 3, 'Time(worst case') 

  

n = 100
j = 1

#loop to time multiple time values at increasing n and
#output that to an excel file
while(n < 2000):
    sheet1.write(j, 0, n)
    #worst case array building
    for i in range(0,n):
        worstCase.append(i)
    #average case array building
    for i in range(n, 0, -1):
        averageCase.append(randint(0,n))
    #best case array building    
    for i in range(n, 0, -1):
        bestCase.append(i)

    #best case timing and output to excel
    startBest = time.time_ns()
    Sort.QuickSort(bestCase, 0, len(bestCase) //2)
    endBest = time.time_ns()
    sheet1.write(j,1,endBest - startBest)

    #average case timing and output to excel
    startAve = time.time_ns()
    Sort.QuickSort(averageCase, 0, len(averageCase)//2)
    endAve = time.time_ns()
    sheet1.write(j, 2, endAve - startAve)

    #worst case timing and output to excel
    startWorst = time.time_ns()
    Sort.QuickSort(worstCase, 0, len(worstCase) //2)
    endWorst = time.time_ns()
    sheet1.write(j, 3, endWorst - startWorst)

    j = j + 1
    n = n + 100
    #clears lists to be used again
    bestCase.clear()
    averageCase.clear()
    worstCase.clear()

#saves the files to excel
wb.save('xlwt2 example.xls')
