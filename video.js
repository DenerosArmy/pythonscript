
					navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia ||
			navigator.mozGetUserMedia || navigator.msGetUserMedia;
			window.URL = window.URL || window.webkitURL;

			navigator.getUserMedia({video: true}, function(localMediaStream) { 
			var video = document.getElementById("v"); 
			video.autoplay = true;
			video.src = window.URL.createObjectURL(localMediaStream);
				}, function(error) {
				console.log(error);
			});
