import datetime
import math

import praw
import pytz

import settings

def _get_counter():
    event_tz = pytz.timezone(settings.EVENT_TIMEZONE)
    local_tz = pytz.timezone(settings.LOCAL_TIMEZONE)

    event_start = event_tz.localize(datetime.datetime.strptime(
        settings.EVENT_START, settings.TIME_FORMAT))
    event_end = event_tz.localize(datetime.datetime.strptime(
        settings.EVENT_END, settings.TIME_FORMAT))

    now = local_tz.localize(datetime.datetime.now())

    if now < event_start:
        days_left = (event_start - now).days
        if days_left > 1:
            return str(days_left) + " Days"
        elif days_left == 1:
            return "1 Day"
        else:
            hours_left = ((event_start - now).seconds) /  3600

            if hours_left > 1:
                return str(hours_left) + " Hours"
            elif hours_left == 1:
                return "1 Hour"
            else:
                return "<1 Hour"
    elif now >= event_start and now <= event_end:
        return "Now!"
    else:
        return "Over :("

def _get_reddit():
    r = praw.Reddit("Minecon countdown by /u/Hanse00")
    r.config.decode_html_entities = True
    r.login(settings.USERNAME, settings.PASSWORD)

    return r

def main():
    r = _get_reddit()
    time_left = _get_counter()

    for subreddit in settings.SUBREDDITS:
        sidebar = r.get_settings(subreddit)["description"]

        sidebar_start = sidebar[:sidebar.find(START_STRING) + len(START_STRING)]
        sidebar_end = sidebar[sidebar.find(END_STRING):]

        new_sidebar = sidebar_start + time_left + sidebar_end
        r.update_settings(r.get_subreddit(subreddit), description=new_sidebar)

if __name__ == "__main__":
    main()
