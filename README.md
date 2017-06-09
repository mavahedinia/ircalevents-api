# IrCalEvents API
an api written in japronto which fetches calendar events from time.ir with scraping method!

## Installation
First it is better to have an virtual environment for app to be running! so run
```bash
$ python3 -m venv env
```
in the directory where app is cloned!

Then you should install the dependecies which are:
* `beautifulsoup4`
* `requests`
* `japronto`
and to do that you can simply run
```bash
$ pip3 install -r requirements.txt --upgrade
```

## Running
to run, you can simply run
```bash
$ nohup ./run.sh&
```
or alternatively create a systemd unit (it depends on your own decision!), however donot forget that the `api.py` file should be ran at last.

## Credits
thanks to ** Alireza Omidi ** for `ircalevents.py` from [iran-calendar-events](https://github.com/alirezaomidi/iran-calendar-events) which has been rewritten with async functions and added `get_year_events` functions by me :)
