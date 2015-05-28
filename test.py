from reddit  import client
from reddit.user import User
from reddit.reddits import Subreddit
from reddit.post import Post
from reddit.check import Check

bojohan = client.login('jon55123')


# python = Subreddit("python")
#
# python.hot()

sub = Subreddit("globaloffensive")

p = Post(sub.hot_children()[4])

title = p.title()

check = Check(title)

if check.check_if_vac():
    print "VACATION!!!!!"










