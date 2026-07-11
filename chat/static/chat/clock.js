var words = Array.isArray(window.GAME_WORDS) ? window.GAME_WORDS : [];
var timerIntervalId = null;
var roundSeconds = Number(window.ROUND_SECONDS || 100);

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
    if (!clock) return;

    if (timerIntervalId) {
        clearInterval(timerIntervalId);
        timerIntervalId = null;
    }

    var t = endtime;
    clock.innerHTML = t + ' sec.';
    timerIntervalId = setInterval(function(){
	t = t - 1;
	clock.innerHTML = t + ' sec.';
	if(t<0){
	    clearInterval(timerIntervalId);
	    timerIntervalId = null;
	    var coins = typeof window.getCoinCount === 'function' ? window.getCoinCount() : 0;
        var targetMessage = String(window.TIMEOUT_MESSAGE_TARGET || 'Time is up. You collected {coins} coin(s).').replace('{coins}', String(coins));
        var originalMessage = String(window.TIMEOUT_MESSAGE_ORIGINAL || targetMessage).replace('{coins}', String(coins));
        alert(targetMessage + '\n(' + originalMessage + ')');
	    window.location.href = window.LANDING_PAGE_URL || '/';
	}
    },1000);
}

window.restartRoundTimer = function() {
    initializeClock('clockdiv', roundSeconds);
};
