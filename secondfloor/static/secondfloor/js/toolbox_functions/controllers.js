/**
 * @file
 * Defines the controllers for the AngularJS Application "app".
 */

// Number Converter Controller.
app.controller('NumberConverterCtrl', function($scope, baseShifter) {
    $scope.userInput = "";
    $scope.userInputBaseA = 10;
    $scope.userInputBaseB = 16;
    $scope.userOutput = "NaN";

    $scope.baseA = function() {
        baseShifter.setBaseA($scope.userInputBaseA);
        $scope.userOutput = baseShifter.shift($scope.userInput);
    }
    $scope.baseB = function() {
        baseShifter.setBaseB($scope.userInputBaseB);
        $scope.userOutput = baseShifter.shift($scope.userInput);
    }
    $scope.changed = function() {
        $scope.userOutput = baseShifter.shift($scope.userInput);
    }
});

// Toolbox Controller.
app.controller('ToolboxCtrl', function($scope) {
    $scope.frontText = "Toolbox";
    $scope.visible = false;
    $scope.viewOptions = function() {
        if ($scope.visible == true) {
            $scope.visible = false;
        } else {
            $scope.visible = true;
        }
    }
});
