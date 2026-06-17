# CST8919 Lab 2: Building a Web App with Threat Detection using Azure Monitor and KQL

**Student Name**: Joshua Chen

**Student ID**: 041280453

**Course**: CST8919 DevOps - Security and Compliance

**Semester**: Summer 2026

---

## Demo Video



---

## Technical Analysis

### What I learned during this lab
- how to pass in console logs into Azure
- learned the basic of KQL and its capabilities to filter 
- learned how to create alerts using custom scripts and how the window span works to aggregate the results 

## Challenges faced during the lab 


## Ways to improve detection log in a real world scenario 
- separate based on account trying to log in 
- 

One improvement to the detection log for a real world log in scenario is to have a wau to distinguish which user is trying to login and separate the aggregation for different users. This way it will not attemp to aggregate 5 different users, who might have all failed at least once to login around the same time. Which the curent script would see and think of it as a brute force attack. 

another improvement would possible be adding geo-location to query. Although this would also invovle updating the message being sent by Flask server. Additionally, it should keep historical geo-location information about past login attempts. So it can test to see if they are logging in the same location and if not, stop the login and ask for a 2nd method for authentication.  

TALK ABOUT FOREIGN IP AND NOT GEO LOCGICAL LOCATION 

## KQL query with explanation 
""" 


"""
This is a very basic KQL query, it uses AppServiceConsoleLogs to get the logs from the server and imports them into query editor? Then it feeds it into the following query 

which will look through the messages and filters them to only disply the messages with "Status:401" which is a custom message that I added to the Flask server to represent failed login attempts. 