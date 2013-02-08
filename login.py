import twitter

api = twitter.Api(consumer_key='ZR24qjEf6vtZTCGRopVlcA',consumer_secret='wka6zSatoUvq0GhhnrLNU1UZ1K7qfQWESa8uybjlco',access_token_key='69595586-SrH1L9LBK0M7M63nKky4j1QggSE5xv6QhNbrOQk', access_token_secret='gtKp0dZRGMGwJfzmqypSFqsEFn7XbJg3Jgdf5y2HVOc')
i=0
friend = api.GetFriends()
for s in friend:
	print i
	print s.id
	i=i+1
	sta = api.GetFriendsTimeline(s.id)
	#print sta
	print [s.text for s in sta]
