# NHL Data Analytics Project

## Project Overview
The purpose of this Data Analytics project is to demonstrate skills in the following areas of data analytics:
- ETL (Extract, Transform, Load) through API's
- Data Cleaning
- Data Exploration
- Data Visualization

Tools Used: Python, Excel, Tableau.

## Introduction
As someone who's both an avid sports fan and passionate about data analytics, I've seen data be used in fascinating ways to gain insight into players and teams across my favourite leagues. One of those leagues is the National Hockey League (NHL). I grew up in a ice hockey-crazed town in northern Sweden, which has turned me into the hockey fan I am today. All teams in the NHL have an analytics department tasked with gathering as much useful data about players and teams, and to turn them into actionable insights. 

An example of this is how advanced analytics can help determine if a certain player that's about to be a free agent can be expected to regress after a strong season. If a player scored 30 goals this year, but had a previous career high of 16 goals, it's possible that this year is either an outlier and the player will regress down to their expected level of 16 goals. However, it is also possible that this is a breakout year and that the player can be expected to continue producing at a 30 goal pace for future seasons to come. Before spending a lot of the budget on recruiting said player, it is crucial for management to determine which scenario is more likely. An example of how data analytics can assist in determining this is by looking at factors such as how many goals this player scored "above expected", which is measured by how many goals one can expect from the total volume of shots from this player this season, taking factors into account such as where the puck was shot from on the ice and how likely the average goaltender is to make the save or not. Perhaps this player has simply been very lucky this season due to opposing goaltenders making mistakes and letting in low-danger shots that is unlikely to be reproduced at the same rate in any future season. 

While advanced analytics such as expected goals per shot for any given puck position on the ice is beyond the scope of this project, this above example is given to demonstrate the power of sports analytics and why it's an interesting world to delve into. For my own project I want to demonstrate more simple data analytics insights by exploring the 2015 NHL Draft Class. While there are many resources out there for compiled data analytics, I want to show how to perform data analytics by myself "from scratch" by using the publically available NHL API.

### Why the 2015 NHL Draft Class?
There are a few reasons. Firstly it is particularily interesting to me since it is the draft class I would have been apart of in a parallel universe where I had an athletic bone in my body, which unfortunately is not this one. But more generally, the 2015 NHL Draft Class is widely regarded as one of the strongest draft classes in NHL history, featuring players such as Connor McDavid, who is widely regarded as the best player in the world. It's also a good balance of being relevant today since most of these players should be in their "prime" age-wise, while simultaneously being far enough out to account for concerns such as players not yet having come over from KHL, or still being used in farm leagues such as the AHL to be developed into NHL starters. It would be extremely rare for a player drafted nearly a decade ago to break into the NHL. Either the player made it at this point, or they didn't and are most likely playing overseas in lesser leagues or currently retired. 

### Project Purpose
My objective is to gather data on every single player who got drafted in the 2015 NHL Draft, and explore the draft class by comparing which nationalities and positions that seem to be the best performers. Data will be extracted through the NHL API with Python, and later transformed into a csv file for data cleaning and exploration in Microsoft Excel. Excel is more than enough for this portion of the project since the dataset I'll be working with is very small, as the draft class only consists of a total of 211 players. Finally, an interactive dashboard will be built in Tableau to showcase the gathered insights.

## ETL
This section aims to provide a description of the API used for the analysis with an overview of what data was available for use. I will also explain which data was selected for use and the reasoning behind it, and the exclusion of other data. Python was used with the requests and pandas libraries in order to preview the gathered data and to save it as a csv file to be worked on in Microsoft Excel.

### API Documentation
The NHL player data was accessed through the official NHL APIs. While these APIs are active and open for use, there doesn't seem to be any official API documentation accessible to the public. Instead I used an unofficial NHL API Documentation created by github user Zmalski accessible here: [NHL API Documentation](https://github.com/Zmalski/NHL-API-Reference/blob/main/README.md) 



## Data Cleaning

## Data Exploration

## Data Visualization

## Conclusion
