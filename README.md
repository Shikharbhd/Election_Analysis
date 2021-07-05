# Election Audit

## Overview
In this project, the election data from a congressional district in Colorado state has been audited to retrieve results as described in the following paragraphs.

## Election Audit Results
A python script PyPoll_Challenge.py was run using VSCode text editor on the dataset stored as election_results.csv to retrieve following information when the script was run

  a. Total number of votes cast
  
  b. The voter turnout for each county
  
  c. The percentage of votes from each county in the precinct
  
  d. The county with the highest turnout
  
  e. Total number of votes each candidate received
  
  f. Percentage of votes each candidate won
  
  g. The winner of the election based on popular vote
  
The information retrieved has been shown in the image below

![Code_Terminal_Print](https://user-images.githubusercontent.com/85258893/124411952-816a1280-dd1b-11eb-94dd-cd8308f5160b.png)

## Election Audit Summary
This audit retrieved election results for 3 counties in Colorado state. The Election commission may use this .py script with some modification to retrieving any election results in any county/State(s) in the Country. For example:

a.	Where there are might be more than 3 columns of information, we need to specify the index correctly to retrieve required data from specific column while the code iterates through each row of the dataset.
