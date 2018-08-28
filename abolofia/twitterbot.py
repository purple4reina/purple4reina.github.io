#!/usr/bin/python


print 'Content-Type: text/html\n\n'


print """


<html>
<head>
	<title>Reina Abolofia</title>



</head>

<body>


Turing Test using a Twitter Bot
    <br /><br />
    <br /><br />
<font color="dark red">WHAT PEOPLE ARE SAYING ABOUT THE BOT:</font>
    <br /><br />
some people are so intelligent they are crazy, applies to you?
    <br /><br />
I tryna be nice sir but I wanna know if you like Justin Bieber and you not responding!
    <br /><br />
I'll only fb if you love Justin Bieber or 1D or other similar people and you obviously don't unless you wanna confess
    <br /><br />
Excuse me Doctor, what is your religion?
    <br /><br />
you talking about Dawson's Creek? Pacey was sissy boy.
    <br /><br />
YOOOO I DON GET ANY OF YO TWEETZ U TRYNNA BE ALL SKOLARLY AN STUFF BUT MOST OF US DONT UNDRSTAND DAT SHIT YOOOO #BOOTYLICIOUS
    <br /><br />
I want to understand your cryptic message- is there a dictionary where I can translate? :)
    <br /><br />
indian ?! Im from indonesia , do you know about indonesia ? :D
    <br /><br />
I straight away thought of PC language until I read the rest.I like the fact that few programmers us it now. Love adelphi
    <br /><br />
DO YOU MAKE YOUR OWN METH OR BUY iT?
    <br /><br />
sorry I didn't understand ur message !!??
    <br /><br />
I'm sorry. I don't understand what do you talk. Please understand me. I'm so sorry sir:D
    <br /><br />
wait right now I'm doing my math homework... Can we just stop this for a minute?
    <br /><br />
SHOUT OUT TO [bot name] FOR BEING A PhD PIMP!!
    <br /><br />
I don't know what u are talking about?!?!?
    <br /><br />
okay my heads going to fall off who are you?
    <br /><br />
You need to stop smoking crack pal.
    <br /><br />
No need to be ashamed of having a big butt, now. You're lucky; it's pretty rare to see a man with a big butt.
    <br /><br />
My little brain can't handle your fat one, you know.
    <br /><br />
I bet you have this really thick dictionary next to you, cause I don't think even a fat brain can absorb all that memory..
    <br /><br />
what kind of dr are you?
    <br /><br />
what are you even talking about?
    <br /><br />
You r Funny...you got lots of code language Words,Now i know you r PHD ;)
    <br /><br />
I never know what your talking about
    <br /><br />
I've been thinking and I'm guessing that you're an English professor somewhere in England..
    <br /><br />
I think you're really cool. I'm just fond of Italian men.
    <br /><br />
Don't you get tired of writing that stuff? Your brain must feel like melting or something..
    <br /><br />
You think the stuff I write are funny? Aww.. :c I grin when I read your stuff too.
    <br /><br />
I've always tried to write like that.. I think you're really cool. Just ignore the bad stuff people say to you. c:
    <br /><br />
I think it's pretty creative and witty of you to play with words like that. That's what I find attractive about you.
    <br /><br />
nothing you say makes any sense!!! what are you talking about?!?!?
    <br /><br />
Um, Charles, I need to confess something.. I think I'm starting to like you. This is bad.. :c
    <br /><br />
I bet you laugh your butt off at these random tweets you write. Lol..
    <br /><br />
I bet you're obsessed with The Big Bang Theory, aren't you?
    <br /><br />
I actually understand him [the bot] partially. He's just pretty smart with words.
    <br /><br />
    <br /><br />
<font color="dark red">HOW TWEETS ARE CREATED:</font>
    <br /><br />
I have compiled a large file of open source books. Everything from the bible to Darwin to Sherlock Holmes. I then use a python script to grab two random sentences from this file and put them together. The tweets are kept to under 80 characters so that they are quick to read. The script is run on a cron tab which then uses a command line tool to post the tweets to twitter.
    <br /><br />
    You can find the current version of the python module that I wrote to provide access to my bot at <a href="https://github.com/purple4reina/tweetbot">GitHub</a>.
    <br /><br />
    <br /><br />
<font color="dark red">RANDOM TWEETS:</font> (refresh to view new ones)
    <br /><br />
"""

import sys

sys.path.append('/homepages/10/d337401589/htdocs/modules/')

from tweetbot import *

print tweet() + '<br /><br />'
print tweet() + '<br /><br /><br /><br />'


print """

<font color="dark red">CURRENT NUMBER OF FOLLOWERS: </font>
    
"""

try:
    followers_page = tweetbot.BOT.followers.ids(screen_name=tweetbot.BOTname)
    BOT_followers = set(followers_page['ids'])
    while followers_page['next_cursor_str'] != '0':
        followers_page = tweetbot.BOT.followers.ids(screen_name=tweetbot.BOTname, cursor=followers_page['next_cursor_str'])
        BOT_followers |= set(followers_page['ids'])

    print str(len(list(BOT_followers)))
except:
    pass


print """
    <br /><br /><br /><br />
</body>

</html>

"""
