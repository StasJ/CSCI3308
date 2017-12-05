$(document).ready(function() {
	setInterval(function() {
		$.get('/livereload/', function(data) {
			if (data == 1)
				location.reload();
		});
	}, 1000);
});
