import sys
sys.path.append("instabot");

from instabot import Bot
from time import sleep
import random
from datetime import datetime

accounts = [];
accCount = 0;

#Fill this in with your info
myAccount = "not_nang";
myPassword = "oreo12345";

 #fill this out with a starting page
accounts.append("redbir.d");

bot = Bot(filter_users = True, max_follows_per_day = 3840, max_unfollows_per_day = 3840);

bot.login(username = myAccount, password = myPassword	);

for acc in accounts:

	followers = bot.get_user_followers(acc);

	skipped = bot.skipped_file;
	followed = bot.followed_file;
	unfollowed = bot.unfollowed_file;

	followers = list(set(followers) - skipped.set - followed.set - unfollowed.set);
	followCount = 0;

	bot.follow_users(followers);
		
					
	accCount += 1;


			
		 