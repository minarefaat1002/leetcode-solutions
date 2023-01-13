class Solution:
    def bestClosingTime(self, customers: str) -> int:
        earliestHour = float('inf')
        minPenalities = float('inf')
        penalitiesTillNow = 0
        comingCustomers = 0
        for state in customers:
            comingCustomers += 1 if state == "Y" else 0
        for i,state in enumerate(customers):
            if minPenalities > 2*penalitiesTillNow - i + comingCustomers:
                minPenalities = 2*penalitiesTillNow - i + comingCustomers
                earliestHour = i
            penalitiesTillNow += 1 if state == "N" else 0 
        return earliestHour if len(customers) - comingCustomers >= minPenalities else len(customers)
