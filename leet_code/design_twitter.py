# 
# 355. Design Twitter
# 
# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets 
# in the user's news feed.
# 
# Implement the Twitter class:
# 
# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who 
# the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
# 
# https://leetcode.com/problems/design-twitter/
# 
from typing import List

class Twitter:

    def __init__(self):   
        self.users = {}
        self.tweets = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.users.keys():            
            self.tweets[userId].append(tweetId)
        else:
            self.users[userId] = []
            self.tweets[userId] = []
            self.tweets[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        most_recent_tweets = self.tweets[userId][:-10]

        tweets_in_order = []
        while len(most_recent_tweets) > 0:
            tweets_in_order = most_recent_tweets.pop()
            
        return tweets_in_order

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users.keys():
            self.users[followeeId].append(followerId)
        else:
            self.users[followeeId] = []


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users.keys():
            self.users[followeeId].pop(followerId)


# Your Twitter object will be instantiated and called as such:
twitter = Twitter()
twitter.postTweet(1, 5)
param_2 = twitter.getNewsFeed(1)
twitter.follow(1, 2)
twitter.postTweet(2, 6)
twitter.getNewsFeed(1)
twitter.unfollow(1, 2)
twitter.getNewsFeed(1)
