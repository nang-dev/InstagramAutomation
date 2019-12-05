import sys
sys.path.append("instabot");

from instabot import Bot
from time import sleep
import random
from datetime import datetime

accounts = [];
accCount = 0;

myAccount = "not_nang";
 #fill this out with a starting page
accounts.append("meme_greatness1");
accounts.append("crispi_memes");

class IGbot(object):

	errorDelay = 1400;

	def follow(self, bot, followers, followCount, amt):

		lower = followCount;
		#upper = min(followCount + amt, len(followers));
		count = 0;
		actualCount = 0;
		errorCount = 1;
		#follow
		for user in followers[lower:]: 
			print("count", count);
			print("amt", amt);
			if count >= amt or errorCount >= 3:
				return actualCount;
			#username = bot.get_username_from_user_id(user);		
			#print("Attempting to follow:", username);

			followFeedback = bot.follow(user);

			if(followFeedback == 400):
				bot.logout();
				sleep(self.errorDelay);
				bot.login(username = myAccount, password = "");
				errorCount += 1;
				self.errorDelay += 100;
			elif followFeedback:
				print("Followed! -", user);
				count += 1;
			else:
				print("Not Followed! -", user);
			actualCount += 1;
			
		return actualCount;

	def unfollow(self, bot, amt):
		following = bot.get_user_following(myAccount);
		whitelist = bot.whitelist_file;
		following = list(set(following) - whitelist.set);

		count = 0;
		errorCount = 1;
		#lower = followCount;

		for user in following:

			if(count >= amt or errorCount >= 3):
				break;
			#username = bot.get_username_from_user_id(user);
			#print("Attempting to unfollow:", username);


			unfollowFeedback = bot.unfollow(user);

			if(unfollowFeedback == 400):
				bot.logout();
				sleep(self.errorDelay);
				bot.login(username = myAccount, password = "");
				errorCount += 1;
				self.errorDelay += 100;
			elif unfollowFeedback:
				count += 1;
				print("Unfollowed -", user);
			else:
				print("Failed to unfollow -", user);
			
		return True;

	def filter(self, bot, amt):
		following = bot.get_user_following(myAccount);
		whitelist = bot.whitelist_file;
		following = list(set(following) - whitelist.set);

		added = 0;

		for user in following[-amt:]: #file read is stored in reversed stack
			if bot.api.last_response.status_code == 400:
				sys.exit();
			username = bot.get_username_from_user_id(user);
			user_info = bot.get_user_info(user)
			bio = user_info['biography'];
			username = user_info['username'];
			name = user_info['full_name'];
			followers = user_info['follower_count'];
			following = user_info['following_count'];
			if "meme" in bio.lower() or "meme" in name.lower() or "meme" in username.lower():
				if followers > 2500 and followers < 10000:
					if following/followers < 4:
						accounts.append(username);
						print("Added: ", username);
						added += 1;
			if added >= 3:
				return;
			sleep(round(random.uniform(10,15), 2));

	def printUpdate(self, task):
		currTime = datetime.now();
		timeString = currTime.strftime("%Y-%m-%d %H:%M")
		print(task + ": " + timeString);


		with open("times.txt", "a+") as times: 
			times.write(task + ": " + timeString  + "errorDelay" + str(self.errorDelay) + "\r\n");

		"""

		message = client.messages \
		    .create(
		         body= task + ": " + timeString,
		         from_='+18577634660',
		         to='+14088911891'
		     )
		"""

		return currTime;

bot = Bot(filter_users = True, follow_delay = 30, unfollow_delay = 30, max_follows_per_day = 3840, max_unfollows_per_day = 3840);

bot.login(username = myAccount, password = "");	

amt = 159;
delay = 3601;

igBot = IGbot();
#bot.logout();

for acc in accounts:

	followers = bot.get_user_followers(acc);

	skipped = bot.skipped_file;
	followed = bot.followed_file;
	unfollowed = bot.unfollowed_file;

	following = bot.get_user_following(myAccount);
	whitelist = bot.whitelist_file;
	following = list(set(following) - whitelist.set);

	followers = list(set(followers) - set(following) - skipped.set - followed.set - unfollowed.set);
	followCount = 0;

	igBot.printUpdate("Starting Running")

	while followCount < len(followers):

		
		#bot.login(username = myAccount, password = "");

		startTime = igBot.printUpdate("Starting Following")

		followCount += igBot.follow(bot, followers, followCount, amt);

		endTime = igBot.printUpdate("Ending Following")

		#bot.logout();
		secElapsed = (endTime - startTime).total_seconds();
		if secElapsed < delay:
			sleep(delay - secElapsed);


		startTime = igBot.printUpdate("Starting UnFollowing")

		igBot.unfollow(bot, amt//2);

		endTime = igBot.printUpdate("Ending UnFollowing")

		#bot.logout();
		secElapsed = (endTime - startTime).total_seconds();
		if secElapsed < delay:
			sleep(delay - secElapsed);

		#bot.login(username = myAccount, password = "");

		#printUpdate("Starting Approve")
		#bot.approve_pending_follow_requests();
		#printUpdate("Ending Approve")
		"""
		if(len(accounts) - accCount < 2):
			startTime = printUpdate("Starting Filter");
			filter(bot, 400);
			endTime = printUpdate("Ending Filter");
			secElapsed = (endTime - startTime).total_seconds();
			if secElapsed < 3600:
				sleep(3600 - secElapsed);
		"""

	accCount += 1;


		
		 