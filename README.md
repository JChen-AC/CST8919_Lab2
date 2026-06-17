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
Through this lab I learned a few things. The first thing that I learned was how to pass console logs into Azure. Through enabling AppServiceConsoleLogs on the ... I was able to see the logs that I outputted using the Logger library in Azure Logs Analytics. I found this extremely helpful as it allows me to see what is happening within the application and how to debug it. 

The next thing I learned was about to write basic KQL queries and their ability to filter logs out. This is extremely useful especially during debugging as Azure Log Analytics gets a lot of logs and data, so being able to filter them and select specific sources would be useful to debugging to help isolate where the issue is coming from. 

The third thing that I learned was how to create alerts that use custom scripts and how the rolling window works for real time logs and aggregation. 

## Challenges faced during the lab 


## Ways to improve detection log in a real world scenario 

One improvement to the detection log for a real world log in scenario is to have a way to distinguish which user is trying to login and separate/filter the logs based on the user. As separating each user will prevent accidental brute force detection when none is happening. As if all the users' logs are combined into one check, then five different users can fail their login attempt within 5 minutes of one another and the system will think that it is a brute force attack when in reality it was just a coincidence. 

Another improvement would be adding the IP-address or geo-location to the query. Although this would involve updating the log message being sent by Flask server. The reason for this is to add another check for suspicious activity as if one user always logs in at one location and then they suddenly log in at another location then their account might have gotten hacked. Alternatively, it could check the time between logins and their location as if a user logs in at one location, then a few minutes login in another then the user might have gotten hacked. If the user got hacked, then it can automatically notify the user and prompt them for a confirmation or send a 2nd method for authentication. 

## KQL query with explanation 
""" 


"""
This is a very basic KQL query, it uses AppServiceConsoleLogs to get the logs from the server and imports them into query editor? Then it feeds it into the following query 

which will look through the messages and filters them to only disply the messages with "Status:401" which is a custom message that I added to the Flask server to represent failed login attempts. 