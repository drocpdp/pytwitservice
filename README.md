
# pytwitservice... what does it do?

## (TLDR): You can be alerted, in real time, of anything in your Twitter feed that you want.
* Configurable, Custom, multiple filters
* Email alerts
* Optional Automatic Retweet (Configurable)

### Use Case 1: Food Trucks Alerts. Which Food Trucks will be at our location today?
#### https://olympicfoodtrucks.wordpress.com/ is a great customer-facing informational gem that I created that helps inform both truck owners and patrons.

* Most food trucks will typically tweet the location where they will be serving lunch.
* pytwitservice automatically RETWEETS such tweets, matching @mention, or custom criteria such as relevant street intersections or company name
	> Example: <sub>"Today we will be slinging burgers at @OlympicTrucks between Centinela Ave and Olympic Blvd..."</sub>
	
	> Typical Filtered keywords: ("@olympictrucks") OR ( ("centinela") OR ("centinela" and ("ave"" OR "avenue") ) )
	
	* Result: 
	  * Filter, and Retweet. 
	     * <sub>Olympic Trucks Retweeted: <B>Truck A:</B> Today we will be slinging burgers at @OlympicTrucks between Centinela Ave and Olympic Blvd...</sub>
	  * Email alert indicating tweet, status of Filter, or Retweet or Both.

### Use Case 2: Tunnel Traffic
* For me, it's the Gotthard Tunnel -- https://twitter.com/TCSGottardo but can be any tunnel that represents the only main hub between 2 crucial points (example https://twitter.com/PANYNJ_HT Holland Tunnel). Definitely useful to warn us of impending traffic/situations. Depending on the Twitter handle, I usually get a series of emails from pytwitservice that serve to effectively communicate a pattern of building traffic or decreasing traffic in my specific tunnel.

### More Suggested Use Cases:
* Keep up to date on Weather, news, stocks, traffic, Famous Court Cases... 
* Follow your favorite Twitter handles and be notified when their tweets contain certain things/labels/names etc.

# Setup and Notes
* Main library used is Tweepy - https://www.tweepy.org/
* You will need a Twitter developer account.
* For emailing, you will need (to run out of the box) a "Gmail App Password", see https://support.google.com/accounts/answer/185833?hl=en#
* Set environment variables as such
```
export PYTWITSERVICE=/opt/services/pytwitservice
export PYTWITSERVICE_CONFIGS=/opt/services/configs/pytwitservice
export PYTWITSERVICE_LOGS=/opt/services/logs/pytwitservice
export EMAILER_GMAIL_PASSWORD=ABCDEFGH
```
* You can run the setup script in /util/etc/
* Note, it will clone this repository. 

# IMPORTANT:
  * see setup_ec2.sh
  * $EXTERNALCONFIGS/pytwitservice/account_info.properties
  ```
	[default]
access_token=111
access_token_secret=111
api_key=111
api_key_secret=111
bearer_token=111
oauth_2_0_client_id=111
oauth_2_0_client_secret=111
```

### Next:
* Simply vi or creating new file, copying contents of ec2_setup.sh and running will setup most everything, including requirements.txt (PIP requirements) setup virtualenv etc.
* $EXTERNALCONFIGS/pytwitservice/place_holder_logs/since_tweet_id.txt is a bit important for first run. It is a sort of "bookmark" for your last processed tweet. It stores tweet id. But after the first run, pytwitservice will serialize as needed.

### To run:
* main.py. It is a one-time run, FYI. To make it practical, I set up a Jenkins project to run main.py every x minutes. I guess it was good for me to not have to worry about the maintenance of an always-running python process. I let Jenkins handle that sort of thing.

### In closing:
* This documentation can be improved, as well as can the code. Feel free to open Pull Requests. I'm sure I'm not the first one to tackle this use case, but it was a great project that 100% had value in my life, was good practice, and fun to see the outcome as well. It also was a great way to meet some of the most awesome, down-to-earth food, kindest, hard-working truck owners.
