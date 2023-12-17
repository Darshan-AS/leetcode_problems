from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_cuisine = {}
        self.food_rating = {}
        self.cuisine_foods_rating = defaultdict(SortedSet)

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_cuisine[f] = c
            self.food_rating[f] = r
            self.cuisine_foods_rating[c].add((-r, f))

    def changeRating(self, food: str, new_rating: int) -> None:
        c, r = self.food_cuisine[food], self.food_rating[food]
        self.cuisine_foods_rating[c].remove((-r, food))
        self.food_rating[food] = new_rating
        self.cuisine_foods_rating[c].add((-new_rating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_foods_rating[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
