# maintenance-send-message

{
    "name": "YoneRobot",
    "description": "Telegram group management bot.",
    "keywords": [
       "telegram",
       "anime",
       "group",
       "manager",
       "yone"
    ],   
 "repository": "https://github.com/noob-kittu/YoneRobot",
 "addons": [
    {
       "options": {
          "version": "12"
       },
       "plan": "heroku-postgresql"
    }
 ],
 "buildpacks": [
    {
      "url": "https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest"
    },
    {
      "url": "heroku/python"
    }
  ],
 "env": {
    "TOKEN": {
       "description": "Your bot token. Get one from @BotFather duh",
       "required": true,
       "value": ""
    },
    "API_ID": {
       "description": "Get API_ID from my.telegram.org, used for telethon based modules.",
       "required": true,
       "value": "3160248"
    },
    "API_HASH": {
       "description": "Get API_HASH from my.telegram.org, used for telethon based modules.",
       "required": true,
       "value": "da866bcad3446898c4d4a20fa10b9d09"
   
    }
    
 }
}
