/**
 * @file
 * Defines various services for the AngularJS Application "app".
 */

// Sample Service.
app.service('hexafy', function() {
    this.myFunction = function (x) {
        return parseInt(x).toString(16);
    }
});
