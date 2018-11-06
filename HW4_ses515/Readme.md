# Readme

## Homework Scope

**Assignment 1**
* commented on cra354's citi bike experimental set up, created pull request with suggested test
* Find [pull request here](https://github.com/colinandrus/PUI2017_cra354/blob/master/HW3_cra354/HW4_A1_Review_Proposal.md)

**Assignment 2**
* searched plos.org and read abstracts to identify specified tests

**Assignment 3: Reproducing research**
* used skeleton notebook and wiki documentation to reporduce experiement and expand upon findings

**Assignment 4: CitiBike data exploration**
* Part one
  * created new colum for day/night rider using datetime
  * said "night" was 7pm - 7am
  * used KS test, Pearsons, and Spearmans tests
* Part two - comparing Manhattan to Brooklyn riders using geolocator*
  * we made an imperfect box around manhattan, saying that anything within those bounds is manhattan, and out of it is Brooklyn. This made it so several stations in Manhattan were actually assigned to Brooklyn.
  * We also noticed that some people lied about their ages! If we were digging in further, I'd want to filter out those older than ~70
  

## Assignment 2: Literature choices of statistical tests - (making us do Markdown gymnastics)

| **Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var| Question to be answered | _H0_ | alpha | link to paper | 
|:----------:|:----------|:------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
Chi-square	| 1, counselor type | ordinal | 1, patients offered HIV testing | categorical | 0| Does shifting program flow and advocacy responsibilities from counselors to volunteer parents of HIV-infected children affect patients offered HIV testing? | Introducing patient advocates will result in the same or decreased number of children tested | 0.01 | [Task Shifting Routine Inpatient Pediatric HIV Testing Improves Program Outcomes in Urban Malawi](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0009626) |
Multiple Regression	| rate of death | continuous | Body Shape Index, smoking, diabetes, blood pressure, and serum cholesterol | continuous | 0 | What's better for predicting premature deaths: body mass index or body shape index?  | The difference between the actual amount of deaths and the prediction using ABSI is the same as those predicted with BMI | .05  | [A New Body Shape Index Predicts Mortality Hazard Independently of Body Mass Index](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0039504) |
Logistic Regression	| Hand size | categorical | demographic features | dichitomous | 0 | 	Is there a relationship between measurements of the human hand and a range of demographic features | There is no relationship between human hand measurements and the subjects' demo features | 0.05 | [Comparing Machine Learning Classifiers and Linear/Logistic Regression to Explore the Relationship between Hand Dimensions and Demographic Characteristics](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0165521) |
  |||||||||
  
# FBB good
