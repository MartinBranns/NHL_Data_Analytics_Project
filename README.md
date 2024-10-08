# NHL Data Analytics Project

## Project Overview
The purpose of this Data Analytics project is to demonstrate skills in the following areas of data analytics:
- ETL (Extract, Transform, Load) through API's
- Data Cleaning
- Data Exploration
- Data Visualization

Tools Used: 
- Python
- Excel
- Tableau

## Introduction
As someone who's both an avid sports fan and passionate about data analytics, I've seen data be used in fascinating ways to gain insight into players and teams across my favourite leagues. One of those leagues is the National Hockey League (NHL). I grew up in a ice hockey-crazed town in northern Sweden, which has turned me into the hockey fan I am today. All teams in the NHL have an analytics department tasked with gathering as much useful data about players and teams, and to turn them into actionable insights. 

An example of this is how advanced analytics can help determine if a certain player that's about to be a free agent can be expected to regress after a strong season. If a player scored 30 goals this year, but had a previous career high of 16 goals, it's possible that this year is either an outlier and the player will regress down to their expected level of 16 goals. However, it is also possible that this is a breakout year and that the player can be expected to continue producing at a 30 goal pace for future seasons to come. Before spending a lot of the budget on recruiting said player, it is crucial for management to determine which scenario is more likely. An example of how data analytics can assist in determining this is by looking at factors such as how many goals this player scored "above expected", which is measured by how many goals one can expect from the total volume of shots from this player this season, taking factors into account such as where the puck was shot from on the ice and how likely the average goaltender is to make the save or not. Perhaps this player has simply been very lucky this season due to opposing goaltenders making mistakes and letting in low-danger shots that is unlikely to be reproduced at the same rate in any future season. 

While advanced analytics such as expected goals per shot for any given puck position on the ice is beyond the scope of this project, this above example is given to demonstrate the power of sports analytics and why it's an interesting world to delve into. For my own project I want to demonstrate more simple data analytics insights by exploring the 2015 NHL Draft Class. While there are many resources out there for compiled data analytics, I want to show how to perform data analytics "from scratch" by using the publically available NHL API.

### Why the 2015 NHL Draft Class?
There are a few reasons. Firstly it is particularily interesting to me since it is the draft class I would have been apart of in a parallel universe where I had an athletic bone in my body, which unfortunately is not this one. But more generally, the 2015 NHL Draft Class is widely regarded as one of the strongest draft classes in NHL history, featuring players such as Connor McDavid, who is widely regarded as the best player in the world. It's also a good balance of being relevant today since most of these players should be in their "prime" age-wise, while simultaneously being far enough out to account for concerns such as players not yet having come over from KHL, or still being used in farm leagues such as the AHL to be developed into NHL starters. It would be extremely rare for a player drafted nearly a decade ago to break into the NHL. Either the player made it at this point, or they didn't and are most likely playing overseas in lesser leagues or currently retired. 

### Project Purpose
My objective is to gather data on every single player who got drafted in the 2015 NHL Draft, and explore the draft class by comparing which nationalities and positions that seem to be the best performers. Data will be extracted through the NHL API with Python, and later transformed into a csv file for data cleaning and exploration in Microsoft Excel. Excel is more than enough for this portion of the project since the dataset I'll be working with is small, as the draft class only consists of a total of 211 players. Finally, an interactive dashboard will be built in Tableau to showcase the gathered insights.

## ETL
This section aims to provide a description of the API used for the analysis with an overview of what data was available for use. I will also explain which data was selected for use and the reasoning behind it, and the exclusion of other data. Python was used with the requests and pandas libraries in order to preview the gathered data and to save it as a csv file to be worked on in Microsoft Excel.

### API Documentation
The NHL player data was accessed through the official NHL APIs. While these APIs are active and open for use, there doesn't seem to be any official API documentation accessible to the public. Instead I used an unofficial NHL API Documentation created by github user Zmalski accessible here: [NHL API Documentation](https://github.com/Zmalski/NHL-API-Reference/blob/main/README.md) 

### Process of Extraction
The APIs features a lot of different information about players, teams, statistics and scheduling. I was hoping for an easy way to access a list of players for any given draft, but was unable to do so. There is a section titled "Draft", containing draft rankings player information for any given year but this only includes information on the players such as their amateur club, height or weight. There is no current information about the statistics of said players in the NHL. Instead this can be found in the "Get Specific Player Info" section. 

Get Specific Player Info -  
Base URL: https://api-web.nhle.com/  
Endpoint: /v1/player/{player}/landing/  
Parameter: {player} (int) - Player ID  
Example: https://api-web.nhle.com/v1/player/8478402/landing/  

This endpoint features all available information about a player. What I'm interested in is the draft class of the players, as I only seek to conduct analysis of the players from the 2015 draft class. Some differentiating factors such as the birth country and position of the players, as well as their points production and games played. I will also gather identifiers such as the players name and unique player ID. 

An issue I ran into was that I could not find a way to only scan for players drafted in 2015, since I needed the unique player ID parameter to use the API, and I was unable to find any API endpoint that would allow me to access all the player ID's for a specific draft class. My solution to circumvent this problem was by looping python through a range of player ID's. While certainly not ideal, the range loop allowed me to capture all players drafted in 2015 by casting a wide enough net to ensure that all players drafted in 2015 would be returned in the results, to then clean the data by removing the players who weren't. I worked under the assumption that players drafted in the same draft would reasonably be entered in the NHL database and be assigned their player_id in close proximity to each other. I tested this by first creating a smaller list of player_id's around the example ID of 8478402 that I have which is Connor McDavid's, a player drafted in 2015. 

The python code for this example can be found in [APIshortlist](APIshortlist.py), and results in this table of five players:

| playerID | firstName | lastName | birth_country | position | draftYear | GamesPlayed | Goals | Assists | Points |
|----------|-----------|----------|---------------|----------|-----------|-------------|-------|---------|--------|
| 8478400  | Colin     | White    | USA           | C        | 2015      | 320         | 44    | 69      | 113    |
| 8478401  | Pavel     | Zacha    | CZE           | C        | 2015      | 546         | 111   | 184     | 295    |
| 8478402  | Connor    | McDavid  | CAN           | C        | 2015      | 645         | 335   | 647     | 982    |
| 8478403  | Jack      | Eichel   | USA           | C        | 2015      | 539         | 211   | 303     | 514    |
| 8478404  | Jeremy    | Bracco   | USA           | R        | 2015      | N/A         | N/A   | N/A     | N/A    |



Sure enough, the surrounding player_id's were all drafted in 2015 which gave me enough confidence to try this strategy to run an iterative range with a large enough range of players surrounding my known player_id to capture all players drafted in 2015. An interesting note is that Connor McDavid was drafted first overall, yet had other players in the 2015 with ID's earlier than his, so they were not created sequentially according to draft order. However, the five players in my featured example were all drafted in the first two rounds so I made the assumption that there are likely more id's of players drafted in 2015 after McDavid's ID than before it.

I decided on the range of 8478000 - 8479200 to give myself a large enough range to account for some missing id's or unexpected entries, while still not being too computationally demanding. The python code to extract the dataset is in [APIfull_list](APIfull_list.py), and the resulting csv file can be found in [nhl2015raw](nhl2015raw.csv).

## Data Cleaning

The first step of my data cleaning process was to verify that my dataset contains all the players from the 2015, so that there are no missing values. I did this by performing a COUNT on all rows that had draftYear: 2015, and checked for any duplicate values. The result showed that my database did contain 211 unique rows of players who got drafted in 2015, which is the correct amount of players for the draft year.

After verifying that my dataset contains all the players drafted in 2015 necessary for my analysis, I removed all rows that contained players drafted in different years or those players that had "N/A" in the draftYear column. Players with this missing value for draftYear were scattered all over the dataset in seemingly random places amongst the 2015 draftees. However, after some investigation it seems that players with "N/A" under their draft year are undrafted players that got signed by an NHL team around the time of the 2015 draft, which is why they got included in the NHL database at that time. These players got removed since the objective is to perform an analysis of players in the 2015 draft. 

Many players are shown with missing values for points scored in the NHL although some players are marked as having 0 points scored in the NHL. It seems that players who scored 0 points in the NHL are marked with "0" under points if they played in NHL games, and "N/A" if they never played an NHL game. I decided to remove all players who never played an NHL game, as that would negatively skew results and not accurately represent average/median performances.

Changed positions "R" to "RW" (Right Winger) and "L" to "LW" (Left Winger) for clarity as that is standard practice. L and R are more commonly used to denote stick position, and has significance in hockey as it is for example widely preferred for defensemen who play on the right side to be left-handed, and thus shoot "R".

Goaltenders are removed since I am not comparing save percentages or goals against averages, which are the two most common metrics to measure the performance of a goaltender apart from advanced statistics such as expected goals against. I am only measuring points, so goaltenders are removed, and only skaters are kept in. While goaltenders can score assists (and sometimes even the rare goalie-goal on an empty net), it is not a performance metric for the position and would negatively skew the analysis.

## Data Exploration
I wanted to add Points per Game (PPG) to the dataset to be used as the primary performance metric in my analysis, but this can be represented in different ways.

The actual Average points per games played (Total Points / Total Games played) gets skewed because the best players from any given draft sticks around the top league, while the worse players struggle to maintain roster spots due to lacklustre performance and end up getting replaced, thus no longer contributing to the total games played by the draft class. High end talent may also start playing in the NHL faster, requiring less time in development before becoming a starting player on the highest level, thus accumulating more games played. Because of this, the "average" points per game can be more reflective of the performance of an elite outlier or two, and not of the "average" player from that given position or nationality especially when working with such a small dataset. 

For example, the top 4 forwards in the draft class measured by Games Played are all in the top 6 when it comes to PPG. But arguably they can be said to all be in the top 5 of PPG if we account for the fact that Kirill Kaprizov (2nd in PPG with 1.187), is a Russian born player. Players who get drafted out of Russia typically take longer to come over than those drafted from other countries due to their contract situations in the KHL, the top division in Russian hockey. The NHL honours the contractual obligations a player already has in foreign leagues, and only permits them to sign an NHL contract after that contract has expired. The KHL tends to try to lock up their impressive young players with lengthy contracts so they can keep them around for longer before losing them to the NHL than other foreign leagues.

**Top 4 forwards Games Played**
| playerID | firstName | lastName | birth_country | position | draftYear | GamesPlayed | Goals | Assists | Points | PPG |
|----------|-----------|----------|---------------|----------|-----------|-------------|-------|---------|--------|---------------|
| 8478402  | Connor    | McDavid  | CAN           | C        | 2015      | 645         | 335   | 647     | 982    | 1.522         |
| 8478427  | Sebastian | Aho      | FIN           | C        | 2015      | 598         | 254   | 303     | 557    | 0.931         |
| 8478483  | Mitch     | Marner   | CAN           | RW       | 2015      | 576         | 194   | 445     | 639    | 1.109         |
| 8478420  | Mikko     | Rantanen | FIN           | RW       | 2015      | 570         | 262   | 355     | 617    | 1.082         |

**Top 6 forwards PPG**
| playerID | firstName  | lastName  | birth_country | position | draftYear | GamesPlayed | Goals | Assists | Points | PPG   |
|----------|------------|-----------|---------------|----------|-----------|-------------|-------|---------|--------|-------|
| 8478402  | Connor     | McDavid   | CAN           | C        | 2015      | 645         | 335   | 647     | 982    | 1.522 |
| 8478864  | Kirill     | Kaprizov  | RUS           | LW       | 2015      | 278         | 160   | 170     | 330    | 1.187 |
| 8478483  | Mitch      | Marner    | CAN           | RW       | 2015      | 576         | 194   | 445     | 639    | 1.109 |
| 8478420  | Mikko      | Rantanen  | FIN           | RW       | 2015      | 570         | 262   | 355     | 617    | 1.082 |
| 8478403  | Jack       | Eichel    | USA           | C        | 2015      | 539         | 211   | 303     | 514    | 0.954 |
| 8478427  | Sebastian  | Aho       | FIN           | C        | 2015      | 598         | 254   | 303     | 557    | 0.931 |


As shown in this scatterplot, the variables Games Played and PPG are positively correlated. The correlation coefficient is 0.71, correlation coefficients whose magnitude are above 0.7 are generally considered to be highly correlated. This graph, and correlation calculation only features players with games played in the NHL in order to not skew the results.

![image](https://github.com/user-attachments/assets/3d279247-6ff3-4547-982e-91a977491bc7)


If we also remove defensemen from the calculation and only include forwards, we can see that correlation is even stronger with a correlation coefficient of 0.77. Although used as the most common performance metric for all skaters, points production is more substanial for forwards, since defensemen can provide more value on the defense side of the game than the average forward can. 
![image](https://github.com/user-attachments/assets/f5e7d5ec-cb3f-499f-be66-0f972d3f4323)

This Weighted PPG will be the highlighted number on the upcoming Tableau dashboard, but the dashboard will also feature the Average PPG in order to provide additional context to the points per game metric which will be further explained in the upcoming chapter.

## Data Visualization
The data visualizations were created in Tableau Public 2024.2 and put together into an interactive dashboard found below. The dashboard allows you to filter the performance metric, which in this case is Weighted PPG as argued for in the Data Exploration chapter.

Link to interactive version: [2015 NHL Draft Performance Dashboard](https://public.tableau.com/app/profile/martin.br.nnstr.m/viz/NHL_2015/2015NHLDraftPerformance)
![image](https://github.com/user-attachments/assets/db6192e9-39ce-4e91-89af-64a161bf0886)

Weighted PPG is represented by the lighter portion of the bar charts, with Average PPG represented by the darker portion. The reason for why it is presented this way and the insights that can be drawn from it, is that of how much the better players drag up the points per game. The average points per game is just the average of all represented players points per game, without taking into account total games played. As previously demonstrated, more games played is positively correlated with a higher points per game. 

As shown in the example below: When filtered to only include Centers, we can see that the largest disparity between the Avg. PPG and the Weighted PPG can be seen for Canadian players. Which is not very surprising since Connor McDavid is a Canadian centreman with the highest PPG in the draft class of 1.522, and the most games played out of all centers with 645, thus being a key driver leading to this large disparity. The numbers of players represented for any given country can be seen in the maps. Latvia, Ukraine and The Netherlands were excluded from the dashboard since those countries only featured one drafted player.
![image](https://github.com/user-attachments/assets/1a18fd60-098b-4e6e-a9c1-ac551fdcf4e0)


## Conclusion
The dashboard successfully completes my purpose of conducting simple data analysis for sports. The steps taken can be followed to perform other data analytics processes to extract data from an API, and to transform it into a functional dashboard. This dashboard should be treated as exploratory, since the sample size used after the data cleaning process only was of 100 players, which gets reduced down when filtering for variables such as nationality and position. I plan on performing a larger scale analysis project following these steps when I find the time, by featuring more draft classes with the purpose of comparing player performance for different positions between countries and would require a larger sample size in order to arrive at some statistical significance.

Some recommendations I have of interesting topics of analysis that can be pursued with similar methods, but through the inclusion of either a larger sample size, and by adding more variables in the specific players API endpoint are as follows:

- Include a larger sample size of multiple draft classes to compare their performances against eachother. For example by including all the players drafted in the 2000's and to rank them by strength of draft class. But I would warn against using recent classes since players that are still active can be expected to still produce more points after the analysis which could bias the results.

- Look at the origin of players and find the best and worst performers. Here I'm not only refering the country of origin of players but an interesting variable to include to use as a focal point of analysis would be the youth league of players before they got drafted. Perhaps some players underperform expectations when drafted from certain leagues. Different youth leagues are going to have different strength of competition, so a player who put up 100 points in a weak youth league, might be a worse offensive producer than a player who put up 40 points in a more competitive league. This analysis could allow us to identify "hidden gems" of undervalued leagues, where players who come from these youth leagues tend to pan out and become NHL players at a higher rate than other leagues.

