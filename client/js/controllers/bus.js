'use strict';
 
angular.module('app')
.controller('BusCtrl', ['$scope', '$state', 'Stop', 'Log', function($scope, $state, Stop, Log) {
   $scope.stops = [];
   $scope.logs = [];
   $scope.currentLogs = [];
   $scope.currentStop = {};
   $scope.tableString = []; 

   function getStops() {
     Stop.find()
       .$promise
       .then(function(results) {
         $scope.stops = results;
       });
   }

   getStops();

   function getLogs() {
     Log.find()
       .$promise
       .then(function(results) {
         $scope.logs = results;
       });
   }

   getLogs();

  $scope.plusOne = function() {
    if(!$scope.diff) {
      $scope.diff = 1;
    } else {
      $scope.diff = Number($('#diffValue')[0].value);
    }
    /*$scope.newLog.diff = $scope.newLog.diff + 1;*/
  }

  $scope.minusOne = function() {
    if(!$scope.diff) {
      $scope.diff = 0;
    } else {
      $scope.diff = Number($('#diffValue')[0].value);
    }
    /*$scope.newLog.diff = $scope.newLog.diff - 1;*/
  }

  $scope.addLog = function() {
     Log.create({
        diff: $scope.diff,
        isLate: true,
        date: new Date(),
        stopId: $scope.newLog.stopId
      })
     .$promise
     .then(function(Log) {
       $scope.newLog.diff = '';
       $scope.newLog.stopId = '';
       getLogs();
     });
   };

   $scope.update = function(currentId) {
      var logs = $scope.logs;
      Stop.find({
        filter: {
          where: {
            id: currentId
          }
        }
      })
     .$promise
     .then(function(results) {
       logs.forEach(function(element, index, array) {
          if(element.stopId == results[0].id) {
            $scope.currentLogs.push(element);
          }
        })
        $scope.currentStop = results[0];
        $scope.tableString = buildScheduleTable($scope.currentStop.schedule, $scope.currentLogs);
      });
   }

   
   function buildScheduleTable(schedule, currentLogs) {
      var objects = getOrganizedScheduleObjects(schedule, currentLogs);
      console.log(objects);
      var tableString = [];
      objects.forEach(function(element, index, array) {
        var tdString = "";
        tdString = doubleDigit(element["timeScheduled"][0]) + ":" + doubleDigit(element["timeScheduled"][1]);
        var avgDiff = getAvgDiff(element["actualLog"]);
        if(avgDiff) {
          tdString = tdString + " (normalmente "+ avgDiff +" minutos atrasado)";
        }
        tableString.push(tdString);
      });
      return tableString;
   }

  // Stepper do newLog.diff
  function checkDiff() {
    if (Number($('#diffValue')[0].value) <= Number($('#diffValue')[0].min)) {
      $('#diffValue')[0].value = $('#diffValue')[0].min;
    }
    else if (Number($('#diffValue')[0].value) >= Number($('#diffValue')[0].max)) {
      $('#diffValue')[0].value = $('#diffValue')[0].max;
    }
    else if (isNaN($('#diffValue')[0].value)) {
      $('#diffValue')[0].value = 0;
    }
  }

  $('#diffValue').on("change", function(){
    checkDiff();
  });

  $('#addDiff').click(function(){
    if (Number($('#diffValue')[0].value) < Number($('#diffValue')[0].max)) {
      $('#diffValue')[0].value = Math.floor(Number($('#diffValue')[0].value) + 1);
    }
  });

  $('#subDiff').click(function(){
    if (Number($('#diffValue')[0].value) > Number($('#diffValue')[0].min)) {
      $('#diffValue')[0].value = Math.ceil(Number($('#diffValue')[0].value) - 1);
    }
  });

 }]);