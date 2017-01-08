'use strict';
 
angular.module('app')
.controller('BusCtrl', ['$scope', '$state', 'Stop', 'Log', function($scope, $state, Stop, Log) {
   $scope.stops = [];
   $scope.logs = [];

   function getStops() {
     Stop.find()
       .$promise
       .then(function(results) {
         $scope.stops = results;
       });
   }

   getStops();

   $scope.addStop = function() {
     Stop.create({
        name: $scope.newStop.name,
        coordinates: {
          lat: 0,
          lng: 0
        }
      })
     .$promise
     .then(function(Stop) {
       $scope.newStop.name = '';
       getStops();
     });
   };

   function getLogs() {
     Log.find()
       .$promise
       .then(function(results) {
         $scope.logs = results;
       });
   }

   getLogs();

  $scope.addLog = function() {
     Log.create({
        diff: Math.abs($scope.newLog.diff),
        isLate: true,
        date: new Date(),
        stopID: $scope.newLog.stopId
      })
     .$promise
     .then(function(Log) {
       $scope.newLog.diff = '';
       $scope.newLog.stopId = '';
       getLogs();
     });
   };
 }]);