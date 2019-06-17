// #region Algemeen
//const IP = prompt('geef publiek IP', 'http://127.0.0.1:5000');
const IP = window.location.hostname + ':5000';
const socket = io.connect(IP);

const init = function() {
	document.querySelector('div.power').addEventListener('click', function() {
		socket.emit('power');
	});

	socket.on('poweron', function(data) {
		document.querySelector('div.fancy-bulb').classList.add('active');
	});

	socket.on('poweroff', function(data) {
		document.querySelector('.bulb').classList.remove('active');
	});
};

document.addEventListener('DOMContentLoaded', function() {
	console.info('DOM geladen');
	init();
});

// #endregion
