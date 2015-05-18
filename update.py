import datetime
import math

import praw
import pytz

import user_info

DEBUG = True

SUBREDDIT = "Mustek"

START_STRING = "[](#countstart)"
END_STRING = "[](#countstop)"

MINECON_TZ = pytz.timezone("Europe/London")
LOCAL_TZ = pytz.timezone("Europe/Copenhagen")

MINECON_START = MINECON_TZ.localize(datetime.datetime(2015, 07, 04, 10))
MINECON_END = MINECON_TZ.localize(datetime.datetime(2015, 07, 05, 18))

def _get_counter():
    now = LOCAL_TZ.localize(datetime.datetime.now())

    if now < MINECON_START:
        days_left = (MINECON_START - now).days
        if days_left > 1:
            return str(days_left) + " Days"
        elif days_left == 1:
            return "1 Day"
        else:
            hours_left = ((MINECON_START - now).seconds) /  3600

            if hours_left > 1:
                return str(hours_left) + " Hours"
            elif hours_left == 1:
                return "1 Hour"
            else:
                return "<1 Hour"
    elif now >= MINECON_START and now <= MINECON_END:
        return "Now!"
    else:
        return "Over :("

def main():
    if DEBUG:
        print _get_counter()
    else:
        r = praw.Reddit("Minecon countdown by /u/Hanse00")
        r.config.decode_html_entities = True
        r.login(user_info.USERNAME, user_info.PASSWORD)
        sidebar = r.get_settings(SUBREDDIT)["description"]

        sidebar_start = sidebar[:sidebar.find(START_STRING) + len(START_STRING)]
        sidebar_end = sidebar[sidebar.find(END_STRING):]

        new_sidebar = sidebar_start + _get_counter() + sidebar_end
        r.update_settings(r.get_subreddit(SUBREDDIT), description=new_sidebar)

if __name__ == "__main__":
    main()
