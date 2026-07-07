var words = Array.isArray(window.GAME_WORDS) ? window.GAME_WORDS : [];

function nextWord() {
    if (words.length === 0) {
        document.getElementById('word').innerHTML = 'Aucun mot disponible';
        return;
    }

    var i = Math.floor(Math.random () * words.length);
    var word = words[i];
    document.getElementById('word').innerHTML = word;
}

function initializeClock(id, endtime){
    var clock = document.getElementById(id);
    var t = endtime;
    clock.innerHTML = t + ' sec.';
    var timeinterval = setInterval(function(){
	t = t - 1;
	clock.innerHTML = t + ' sec.';
	if(t<0){
	    clearInterval(timeinterval);
	    alert("Time's up");
	}
    },1000);
}

// initializeClock('clockdiv',100);
nextWord();
