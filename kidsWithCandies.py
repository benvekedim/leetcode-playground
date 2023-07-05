    def kidsWithCandies(candies, extraCandies):
        max_candies = max(candies)
        result = list(map(lambda candy: candy + extraCandies >= max_candies,candies))
        return result
