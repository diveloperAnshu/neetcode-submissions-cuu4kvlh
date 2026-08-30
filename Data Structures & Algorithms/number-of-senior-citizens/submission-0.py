class Solution:
    def countSeniors(self, details: List[str]) -> int:
        totalPassengers = 0
        for passenger in details:
            age = passenger[11] + passenger[12]
            newAge = int(age)
            if newAge > 60:
                totalPassengers += 1
        return totalPassengers
        
        