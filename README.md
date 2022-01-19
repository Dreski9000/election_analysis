# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local
congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.9, Visual Studio Code

## Summary
The analysis of the election determined that:
- There were 369,711 votes cast in the election
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham recevied 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes.

## Challenge Overview
The purpose of this challenge is to create a Python script that can be used to perform automated election audits, by totalling the vote counts and breaking them into categories by distinct candidates and counties, and determining the winning candidate (by number of votes and %) and the county with the largest voter turnout.


## Election Audit Results
The following was determined by the election analysis:

- There were 369,711 votes cast in the election
- The county turnout results: 
  - The largest county turnout was Denver County, with 82.8% of the votes and a total of 306,055 votes cast.
  - Second place was Jefferson County, with 10.5% of the votes and 38,855 votes cast. 
  - This place was Arapahoe County, with 6.7% of the votes and 24,801 votes cast.

- The candidate results were:
  - Charles Casper Stockham recevied 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes.

## Election Audit Summary
The script created for this challenge can be used to perform quick audits of elections by automatically tallying votes and showing various breakdowns such as candidate and county brackets. 

The script can easily be modified to include a greater range of candidates and counties; it include additional metrics such as margin of victory; the script can be modified to include data from multiple files, and potentially compare elections with historical data (if such data is included.)