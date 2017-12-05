$(document).ready(function() {
	function reload(fails) {
		$.get('/livereload/', function(data) {
			if (data == 1) {
				location.reload();
				fails = 0;
			}
			wait = fails <= 10 ? 500 : fails <= 40 ? 1000 : fails <= 100 ? 2000 : 5000;
			setTimeout(function() {reload(fails+1);}, wait);
		});
	}
	reload(0);
	/*
	setInterval(function() {
		$.get('/livereload/', function(data) {
			if (data == 1)
				location.reload();
		});
	}, 1000);
	*/
});
