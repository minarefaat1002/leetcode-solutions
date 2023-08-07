class Solution {
    public int minNumberOfHours(int initialEnergy, int initialExperience, int[] energy, int[] experience) {
        int totalHours = 0;
        for(int i = 0; i<energy.length;i++){
            int en = energy[i];
            int ex = experience[i];
            if(initialEnergy <= en){
                totalHours += en - initialEnergy + 1;
                initialEnergy = en + 1;
            }
            if(initialExperience <= ex){
                totalHours += ex - initialExperience + 1;
                initialExperience = ex + 1;
            }
            initialEnergy -= en;
            initialExperience += ex;
        }
        return totalHours;
    }
}
 // totalHours = 0
 //        for en,ex in zip(energy,experience):
 //            if initialEnergy <= en:
 //                totalHours += en - initialEnergy + 1
 //                initialEnergy = en + 1
 //            if initialExperience <= ex:
 //                totalHours += ex - initialExperience + 1
 //                initialExperience = ex + 1
 //            initialEnergy -= en
 //            initialExperience += ex
 //        return totalHours