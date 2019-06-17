let buttonUp;
let buttonDown;
let socket;

const enableSocketIO = function() {
	socket = io(`http://${window.location.hostname}:5000`);

	socket.on('connect', function() {
		console.log('Connected');
		stat.innerHTML = 'ON';
	});
};

const listenToButtons = function() {
	buttonUp.addEventListener('click', function() {
		console.log('sending forward to motor');
		socket.emit('forward');
	});

	buttonDown.addEventListener('click', function() {
		console.log('sending backward to motor');
		socket.emit('reverse');
	});
};

const init = function() {
	buttonUp = document.querySelector('.js-button__up');
	buttonDown = document.querySelector('.js-button__down');
	stat = document.querySelector('.js-stat');
	enableSocketIO();
	listenToButtons();
};

document.addEventListener('DOMContentLoaded', init);
