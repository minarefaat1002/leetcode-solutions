/**
 * @param {number} initialEnergy
 * @param {number} initialExperience
 * @param {number[]} energy
 * @param {number[]} experience
 * @return {number}
 */
var minNumberOfHours = function(initialEnergy, initialExperience, energy, experience) {
        let totalHours = 0;
        for(let i = 0; i<energy.length;i++){
            let en = energy[i];
            let ex = experience[i];
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
};