'use strict';
 
angular.module('app', [
	'lbServices',
	'ui.router'
 ])
.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {
	$stateProvider.state('todo', {
		url: '',
		templateUrl: 'views/bus.html',
		controller: 'BusCtrl'
	});
	$urlRouterProvider.otherwise('todo');
 }]);