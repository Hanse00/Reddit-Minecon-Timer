# Reddit Event Timer
This is a python script which allows you to insert a countdown timer to an event, into a subreddit sidebar.

To use the script, download the content of this repository, then run

```
pip install -r requirements.txt
```

This will install the dependencies.

Then edit the ```settings.py``` file, to fit your needs.

The default file looks like this:

```
USERNAME = "Test"
PASSWORD = "Test"

SUBREDDITS = ["Mustek", "MineconAgents"]

START_STRING = "[](#countstart)"
END_STRING = "[](#countstop)"

EVENT_TIMEZONE = "Europe/London"
LOCAL_TIMEZONE = "Europe/Copenhagen"

EVENT_START = "2015-07-04 10:00:00"
EVENT_END = "2015-07-05 18:00:00"

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
```

The settings are:

**USERNAME** The reddit user used for the script

**PASSWORD** The password the script should use to log in

**SUBREDDITS** This is a python list of subreddit names

**START_STRING** This is the string found in the sidebar, after which the script should insert the time left

**END_STRING** This is the string that follows the countdown field

**EVENT_TIMEZONE** The timezone in which the event you are tracking will happen

**LOCAL_TIMEZONE** The timezone of the computer on which the script will run

**EVENT_START** The local time at which the event will start

**EVENT_END** The local time at which the event will end

**TIME_FORMAT** The formatting used for the start and end time
