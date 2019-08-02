/**
 * @file
 * Defines the controllers for the AngularJS Application "app".
 */

// Sample Controller.
app.controller('TestCtrl', function($scope, hexafy) {
    $scope.userInput = "";
    $scope.userOutput = "NaN";
    $scope.changed = function() {
        $scope.userOutput = hexafy.myFunction($scope.userInput);
    }
});

// Toolbox Controller.
app.controller('ToolboxCtrl', function($scope, hexafy) {
    $scope.frontText = "Toolbox";
    $scope.visible = false;
    $scope.viewOptions = function() {
        //$scope.frontText = "LUL";
        console.log("CLICKED: " + $scope.visible);
        if ($scope.visible == true) {
            console.log("PASS - BEFORE: " + $scope.visible);
            $scope.visible = false;
            console.log("PASS - AFTER: " + $scope.visible);
        } else {
            console.log("FAIL - BEFORE: " + $scope.visible);
            $scope.visible = true;
            console.log("FAIL - AFTER: " + $scope.visible);
        }
    }
});
