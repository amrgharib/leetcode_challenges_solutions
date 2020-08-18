class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        cand_dist = [0] * num_people
        
        i = 0
        count = 1
        
        while candies:
            cand_dist[i] += count
            candies -= count
            i += 1
            count +=1
            
            if i == num_people:
                i = 0
            if count > candies:
                count = candies
                
        return cand_dist
