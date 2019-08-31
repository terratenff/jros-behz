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

// Base64-Cipher Controller.
app.controller('Base64Ctrl', function($scope, base64) {
    $scope.userInputEncode = "";
    $scope.userInputDecode = "";
    $scope.resultEncode = "";
    $scope.resultDecode = "";

    $scope.changedEncode = function() {
        $scope.resultEncode = base64.encode($scope.userInputEncode);
    }

    $scope.changedDecode = function() {
        $scope.resultDecode = base64.decode($scope.userInputDecode);
    }
});

// Caesar Cipher Controller.
app.controller('CaesarCtrl', function($scope, caesar) {
    $scope.userInput = "";
    $scope.userInputShift = 3;
    $scope.result = "NaN";

    $scope.shift = function() {
        caesar.setShift($scope.userInputShift);
        $scope.result = caesar.encode($scope.userInput);
    }

    $scope.changed = function() {
        $scope.result = caesar.encode($scope.userInput);
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
