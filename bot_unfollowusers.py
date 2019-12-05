import sys
sys.path.append("instabot");

from instabot import Bot
from time import sleep
import random
from datetime import datetime

accounts = [];
accCount = 0;

myAccount = "not_nang";
myPassword = "oreo12345";
 #fill this out with a starting page
#accounts.append("masakameme");
accounts.append("swellygotmemes");
accounts.append("masakameme");


bot = Bot(filter_users = True, follow_delay = 30, unfollow_delay = 30, max_follows_per_day = 3840, max_unfollows_per_day = 3840);

bot.login(username = myAccount, password = myPassword);

skipped = bot.skipped_file;
followed = bot.followed_file;
unfollowed = bot.unfollowed_file;

following = bot.get_user_following(myAccount);
whitelist = bot.whitelist_file;
following = list(set(following) - whitelist.set);


bot.unfollow_users(following);

		
		 