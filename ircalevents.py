#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.time.ir/fa/event/list/0/'


async def get_events(year, month, day=None):

    # Base url to get information of events
    if day is None:  # Full list of events in a month
        url = BASE_URL + '{}/{}'.format(year, month)
    else:  # Single day events list
        url = BASE_URL + '{}/{}/{}'.format(year, month, day)

    # Send a request and get all information
    # Why catching exception an printing error is bad?
    # Because maybe user don't want the error to be printed!
    r = requests.get(url)

    # Raises HTTPError exception if response to the request was not ok.
    r.raise_for_status()

    # Parse html
    parsed_html = BeautifulSoup(r.text, 'html.parser')

    # What is going to be returned?
    # Each part of code described in upper comment.
    if day is None:
        events = {}
        #             Day of month       , Event description                 Events list of the month
        for k, v in ((li.contents[1].text, li.contents[2].strip()) for li in parsed_html.ul.find_all('li')):
            k = str(int(k.split()[0]))
            if k in events:
                events[k].append(v)
            else:
                events[k] = [v]
        return events
    else:
        #       Event description                Events list of the day
        return [li.contents[2].strip() for li in parsed_html.ul.find_all('li')]


async def get_day_events(y, m, d):
    return await get_events(y, m, d)


async def get_month_events(y, m):
    return await get_events(y, m)

async def get_year_events(y):
    ret = {}
    for i in range(1, 13):
        ret[str(i)] = await get_month_events(y, i)
    return ret
