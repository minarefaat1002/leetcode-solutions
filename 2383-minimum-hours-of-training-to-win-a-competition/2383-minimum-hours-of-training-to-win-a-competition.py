class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        totalHours = 0
        for en,ex in zip(energy,experience):
            if initialEnergy <= en:
                totalHours += en - initialEnergy + 1
                initialEnergy = en + 1
            if initialExperience <= ex:
                totalHours += ex - initialExperience + 1
                initialExperience = ex + 1
            initialEnergy -= en
            initialExperience += ex
        return totalHours