/**
 * @file
 * Defines various services for the AngularJS Application "app".
 */

// Convert number of base A to number of base B.
app.service('baseShifter', function() {
    this.baseA = 10;
    this.baseB = 16;
    this.setBaseA = function(x) {
        this.baseA = x;
    }
    this.setBaseB = function(x) {
        this.baseB = x;
    }
    this.shift = function(x) {
        return parseInt(x, this.baseA).toString(this.baseB);
    }
});

// Encodes/Decodes text with Base64.
app.service('base64', function() {
    this.encode = function(x) {
        return btoa(x);
    }
    this.decode = function(x) {
        try {
            return atob(x);
        } catch(err) {
            return "NaN";
        }
    }
});

// Manipulates text with Caesar Cipher.
// Only considers alphabetical characters.
app.service('caesar', function() {
    this.alphabetReferenceLow = "abcdefghijklmnopqrstuvwxyz";
    this.alphabetReferenceHigh = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    this.shift = 3;
    this.setShift = function(x) {
        this.shift = x;
    }
    this.encode = function(x) {
        var chars = [];
        for (var i = 0; i < x.length; i++) {
            var charIndexLow = this.alphabetReferenceLow.indexOf(x[i]);
            var charIndexHigh = this.alphabetReferenceLow.indexOf(x[i]);
            var shiftedChar = x[i];
            if (charIndexLow !== -1) {
                shiftedChar = this.alphabetReferenceLow[(charIndexLow + this.shift) % 26];
            } else if (charIndexHigh !== -1) {
                shiftedChar = this.alphabetReferenceHigh[(charIndexHigh + this.shift) % 26];
            }
            chars.push(shiftedChar);
        }
        return chars.join("");
    }
});
