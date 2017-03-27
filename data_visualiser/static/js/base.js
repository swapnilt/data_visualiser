

var app = angular.module('baseApp', []);


app.controller('baseCtrl', function($scope, $http , $q) {
	
	$scope.chart = null;
	$scope.charts_loaded = false;
	$scope.loading = false;
	$scope._data_type = null;
	$scope._region = null;
	$scope._year = null;
	$scope._region2 = null;
	$scope._year2 = null;
	$scope.region1_data = null;
	$scope.region2_data = null;
	
	function drawChart(mydata) {
			
			console.log("drawing chart...");
			if(mydata === null){
				return;
			}
		console.log(mydata);
			
	      var data = new google.visualization.DataTable();
	      data.addColumn('string', 'X');
	      data.addColumn('number', $scope._region);
	      //check if two graphs are to be shown
	      node  = mydata[0];
	      if(node.length == 3 ){
	      	data.addColumn('number', $scope._region2);
	      }
	      
	      

		  data.addRows(mydata);
		  
		

	      var options = {
	        hAxis: {
	          title: 'Month'
	        },
	        vAxis: {
	          title: $scope.data_type
	        },
	        series: {
	          1: {curveType: 'function'}
	        }
	      };

	      $scope.chart = new google.visualization.LineChart(document.getElementById('chart_div'));
	      $scope.chart.draw(data, options);
	    }
	

	
	
	
	$scope.load_complete = function(){
		$scope.charts_loaded = true;
	}
	
	
	$scope.get_region1_data = function(callback){
	
		console.log("in get_region1_data");
		if($scope._data_type === null || $scope._region === null || $scope._year === null){
			
			console.log("unable to fetch data. form is invalid");
			return;
		}
		 var query = "region=" + $scope._region + "&" + "year=" + $scope._year;
		 var url = "/api/v1/" + $scope._data_type + "/?" + query;
		  
		 $http.get(url).
		   
		 success(function(data, status){ 
		 	callback(data, status);
		 
		 }).
		 error(function(data, status){
		 	 $scope.loading = false;
			  console.log(data);
			  console.log(status);
			  alert("Error in fetching data");
		 });
	
	}
	
	$scope.get_region2_data = function(callback){
		
		  console.log("in get_region2_data");
			
		  if($scope._data_type === null || $scope._region2 === null || $scope._year2 === null){
		  	
		  		console.log("unable to fetch data. form is invalid");
		  		return;
		  }
		  
			var query = "region=" + $scope._region2 + "&" + "year=" + $scope._year2;
			var url = "/api/v1/" + $scope._data_type + "/?" + query;
			$http.get(url).
			success(function(data, status){
				callback(data, status);
			}).
			error(function(data, status){
			  	  $scope.loading = false;
				  console.log(data);
				  console.log(status);
				  alert("Error in fetching data");
			});
			
			
	}
	
	$scope.update_data_type = function(){
		
		if($scope.data_type === $scope._data_type){
			// redraw only if there is a change
			return;
			
		}
		
		$scope._data_type = $scope.data_type;
		$scope.loading = true;
		$scope.get_region1_data(function(data, status){
			
			console.log("in sucess of region1 data promise");
			$scope.region1_data = data.objects;
			$scope.get_region2_data(function(data, status){
				
				$scope.region2_data = data.objects;
			  	// send updated data to draw function
				  data = $scope.prepare_chart_data();
				  drawChart(data);
			});
			
		});
		
		  
		  
		
		
	}
	
	
	
	$scope.prepare_chart_data = function(){
	
		var months = ['January', 'February', 'March', 'April', 'May', 'June',
			'July', 'August', 'September', 'October', 'November', 'December'];
			
		console.log("trying to prepare chart data...");
		if($scope.region1_data === null){
			console.log("unable to prepare chart data. region1 data is null");
			return;
		}
			
		if($scope.region2_data !== null){
			
			//var data = [['Month', $scope._region1, $scope._region2]];
			var data = [];
			for(var i=0; i<12; i++){
			
				month = months[i];
				monthly_data1 = $scope.region1_data[i];
				monthly_data2 = $scope.region2_data[i];
				node = [ month, monthly_data1.value, monthly_data2.value ]
				console.log("pushing node:");
				console.log(node)
				data.push(node);
				console.log("data ");
				console.log(data);
			}
			
			console.log("returning data: ");
			console.log(data);
			
			return data;
		
		}else{
		
			//var data = [['Month', $scope._region1]];
			var data = [];
			for(var i=0; i<12; i++){
			
				month = months[i];
				monthly_data1 = $scope.region1_data[i];
				
				node = [ month, monthly_data1.value ];
				console.log("pushing node:");
				console.log(node)
				data.push(node);
				console.log("data ");
				console.log(data);
			}
		
			console.log("returning data: ");
			console.log(data);
			return data;
			
		}
	
	}
	
	$scope.update_region1_chart = function(){
		
		console.log("updating region1 chart");
		$scope.loading = true;
		$scope.get_region1_data(function(data, status){
			
			$scope.loading = false;  
			  $scope.region1_data = data.objects;
			  // send updated data to draw function
			  data = $scope.prepare_chart_data();
			  drawChart(data);
		
		});
	
	}
	
	$scope.update_region2_chart = function(){
		
		console.log("updating region2 chart");
		$scope.loading = true;
		$scope.get_region2_data(function(data, status){
			
			$scope.loading = false;  
			  $scope.region2_data = data.objects;
			  // send updated data to draw function
			  data = $scope.prepare_chart_data();
			  drawChart(data);
		
		});
	
	}
	
	
	$scope.update_region = function(){
		
		console.log("in update region");
		if($scope.region === $scope._region){
			// return if no change
			console.log("no change detected");
			return;
		}
		$scope._region = $scope.region;
		$scope.update_region1_chart();
		
	}

	$scope.update_year = function(){
		
		console.log("in update year");
		if($scope.year === $scope._year){
			// redraw only if there is a change
			console.log("no change detected");
			return;
			
		}
		$scope._year = $scope.year;
		$scope.update_region1_chart();
		
	}
	
	
	
	
	
	$scope.update_region2 = function(){
		
		console.log("in update region2");
		if($scope.region2 === $scope._region2){
			console.log("no change detected");
			// redraw only if there is a change
			return;
			
		}
		$scope._region2 = $scope.region2;
		$scope.update_region2_chart(); 
		
		
	}
	
	$scope.update_year2 = function(){
		console.log("in update year2");
		if($scope.year2 === $scope._year2){
			console.log("no change detected");
			// redraw only if there is a change
			return;
			
		}
		
		$scope._year2 = $scope.year2;
		$scope.update_region2_chart();		
	}
	
	$scope.init = function(){
		console.log("initializing google chart");
		google.charts.load('current', {packages: ['corechart', 'line']});
		//google.charts.setOnLoadCallback($scope.load_complete);
	}
	
	$scope.init();
	
});


$('#refetch-form').submit(function() {
    var res = confirm("All existing data will be deleted. Are you sure?");
    return res; 
});

