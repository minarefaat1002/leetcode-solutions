/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    const o = Object();
    o.val = val;
    o.toBe = function(val){
        if(this.val === val) return true;
        throw new Error("Not Equal");
    }
    o.notToBe = function(val){
        if(this.val !== val) return true;
        throw new Error("Equal");
    }
    return o;
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */