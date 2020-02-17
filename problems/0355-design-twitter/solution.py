from collections import defaultdict
import heapq
from time import time

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__tweets_map = defaultdict(list)
        self.__followers_map = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.__tweets_map[userId].append((time(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        feed = self.__tweets_map[userId].copy()
        feed.extend([tweet for followee in self.__followers_map[userId] for tweet in self.__tweets_map[followee]])
        return list(map(lambda x: x[1], heapq.nlargest(10, feed, key=lambda x: x[0])))

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId: return
        self.__followers_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId: return
        self.__followers_map[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
