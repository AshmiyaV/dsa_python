import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followeeMap = defaultdict(set)     

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweetMap[userId].append([self.count, tweetId])       

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followeeMap[userId].add(userId)
        for followeeId in self.followeeMap[userId]:
            if self.tweetMap[followeeId]:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index > 0:
                count, tweetId = self.tweetMap[followeeId][index - 1]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followeeMap[followerId].add(followeeId)   

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followeeMap[followerId] and followeeId != followerId:
            self.followeeMap[followerId].remove(followeeId)

# Simulate input
ops = ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
args = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]

twitter = None
output = []

for op, arg in zip(ops, args):
    if op == "Twitter":
        twitter = Twitter()
        output.append(None)
    elif op == "postTweet":
        twitter.postTweet(arg[0], arg[1])
        output.append(None)
    elif op == "getNewsFeed":
        output.append(twitter.getNewsFeed(arg[0]))
    elif op == "follow":
        twitter.follow(arg[0], arg[1])
        output.append(None)
    elif op == "unfollow":
        twitter.unfollow(arg[0], arg[1])
        output.append(None)

print(output)