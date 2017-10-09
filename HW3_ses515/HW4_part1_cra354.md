###Assignment 1:###

**Colin Andrus (cra354, colinandrus) reviewing citibike proposal from Sarah Schoengold (ses515, sebscho)**

#Experiment:

Sarah's question is "Is the average trip time for citibike affected by the gender of the person?". Both the null and alternate hypotheses are formulated correctly and have appropriate formulas.  The data needed to answer the question is present and was pre-processed to leave the necessary variables for trip duration and gender.

#Suggestions:

There's a small typo in the "F=" lines for the hypotheses where 'gender' should be 'female'.  Instead of creating df1, df2 you could drop columns and rows from df (maybe useful if we eventually use more data?).

#Significance Test:

This will be testing the significance of difference between two groups, with numeric, non-parametric data and one treatment variable.  I would reccomend using a 2 tailed z-test for unpaired data.  Since the data is non-parametric first you would want to use an F-test to make sure the variances of male and female values are not drastically different.
