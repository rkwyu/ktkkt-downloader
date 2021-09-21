# About #
A tool to get anime from [ktkkt.top](https://www.ktkkt.top/) with CLI (Command Line Interface) and GUI (Graphical User Interface).
It currently supports to download one single episode / all episodes in a series.

# Prerequisites #
To running this tool, please make sure the following prerequisites are ready:
* [FFmpeg](https://www.ffmpeg.org/)

# Usage #
Before running the application, required packages need to be installed by following command:
```
$ python -m pip install -r requirements.txt
```

## CLI (Command Line Interface) ##
```
# download single episode
$ python __main__.py -d OUTPUT_DIR -u TARGET_URL

# download all episodes in a series
$ python __main__.py -d OUTPUT_DIR -u TARGET_URL -a
```

### Example ###
鬼滅之刃粵語,  
series URL: https://www.ktkkt.top/movie/index15170.html  
episode 1 URL: https://www.ktkkt.top/play/15170-0-0.html  
```
# download 鬼滅之刃粵語 episode 1 to /home/ktkkt/ by the episode URL
$ python __main__.py -d /home/ktkkt/ -u https://www.ktkkt.top/play/15170-0-0.html

# download 鬼滅之刃粵語 all episodes to /home/ktkkt/ by the episode URL
$ python __main__.py -d /home/ktkkt/ -u https://www.ktkkt.top/play/15170-0-0.html -a

# download 鬼滅之刃粵語 all episodes to /home/ktkkt/ by series URL
$ python __main__.py -d /home/ktkkt/ -u https://www.ktkkt.top/movie/index15170.html -a
```

## GUI (Graphical User Interface) ##
```
# start gui
$ python __main__.py
```
Provide the TARGET_URL, OUTPUT_DIR and then click the buttons to download the single episode / all episodes in a series  

# License #
[GNU GPL v3.0](LICENSE.md)
