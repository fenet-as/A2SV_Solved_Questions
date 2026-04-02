import bisect

class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        # Step 1: Sort both arrays
        houses.sort()
        heaters.sort()
        
        radius = 0
        
        # Step 2: For each house, find the nearest heater
        for house in houses:
            # Find insertion point
            ind = bisect.bisect_left(heaters, house)
            
            if ind == 0:
                # House is before all heaters
                closest = heaters[0] - house
            elif ind == len(heaters):
                # House is after all heaters
                closest = house - heaters[-1]
            else:
                # House is between two heaters
                closest = min(house - heaters[ind - 1], heaters[ind] - house)
            
            # Step 3: Update the required radius
            radius = max(radius, closest)
        
        return radius