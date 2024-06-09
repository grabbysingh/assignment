# SLACK TOKEN

## Pre-requisites:

### 1. Slack account
### 2. Created Workspace

## Building an app to integrate with python code

### 1. Creating an app
Go to https://api.slack.com/apps and click on Create New App button -> From Scratch -> Enter App Name -> Pick the workspace from dropdown -> Click on Create App
![image](https://github.com/grabbysingh/assignment/assets/32235433/6bac9478-432c-45fa-848f-48a00d173936)
![image](https://github.com/grabbysingh/assignment/assets/32235433/1a5dac07-1479-4ba1-ba6d-ae6be4d70126)
![image](https://github.com/grabbysingh/assignment/assets/32235433/1f2a2bb8-4309-4178-89db-def99e8964fd)

### 2. Giving permissions to an App
Go to OAuth & Permissions -> Scroll to Scopes Section -> Inside Bot Token Scopes Section -> Click Add an OAuth Scope and add 4 permissions -> files:read, files:write, chat:write, chat:write.customize
![image](https://github.com/grabbysingh/assignment/assets/32235433/7249e424-f77f-4431-a1b7-215351ee6449)

### 3. Install app to workspace
Scroll up and click on Install to Workspace -> Allow the prompt -> Copy Bot User OAuth Token -> Create a .env file and paste it there named as SLACK_TOKEN = <token>.
![image](https://github.com/grabbysingh/assignment/assets/32235433/c014f942-02e4-4627-8b96-d32ffa127ddb)
![image](https://github.com/grabbysingh/assignment/assets/32235433/28489b72-80eb-43c2-8702-78dd7955b35d)

### 3. Creating channel
Go to https://app.slack.com -> Select Workspace -> Click on channels -> Create channel -> Enter channel name -> Keep Visibility public
![image](https://github.com/grabbysingh/assignment/assets/32235433/4fd5f55d-4f5b-4d5b-bec1-9cf0c00063e8)

### 4. Adding app to created channel
Go to Apps Section on left side -> Click on dropdown -> Click Add this app on a channel -> Select channel name from dropdown -> Click on add
![image](https://github.com/grabbysingh/assignment/assets/32235433/8ba903b2-4d00-49fe-bed9-a83c0d795975)
![image](https://github.com/grabbysingh/assignment/assets/32235433/7eadec3c-4a9c-4537-b855-83661caff9c9)

### 5. Python code for sending text to slack
You can send the text to slack via below python code.
![image](https://github.com/grabbysingh/assignment/assets/32235433/e31edda4-a7b9-4825-9916-32e6525eb33c)
