$(document).ready(function() {
    $('.modal-trigger').leanModal();

    $('.slider').slider({
        // full_width: true,
        interval: 10000
    });

    $(".sideNav").sideNav();
    // $('.collapsible').collapsible();
});

function prev() {
    $('.slider').slider('prev');
}

function next() {
    $('.slider').slider('next');
}

var player;

function onYouTubeIframeAPIReady() {
    player = new YT.Player('video1', {
        width: 400,
        height: 400,
        videoId: 'XVAoaikFFAE',
        // playerVars: {
        //     playlist: 'PT2_F-1esPk,PT2_F-1esPk'
        // },
        events: {
            'onStateChange': onPlayerStateChange
        }
    });
    player = new YT.Player('video2', {
        width: 400,
        height: 400,
        videoId: 'IkGY2PR5qxQ',
        // playerVars: {
        //     playlist: 'NzZgwsZagkU,NzZgwsZagkU'
        // },
        events: {
            'onStateChange': onPlayerStateChange
        }
    });
    player = new YT.Player('video3', {
        width: 400,
        height: 400,
        videoId: 'HvpjU51vbKM',
        // playerVars: {
        //     playlist: 'PT2_F-1esPk,PT2_F-1esPk'
        // },
        events: {
            'onStateChange': onPlayerStateChange
        }
    });
    player = new YT.Player('video4', {
        width: 400,
        height: 400,
        videoId: 'L6Rh0EsUs54',
        // playerVars: {
        //     playlist: 'PT2_F-1esPk,PT2_F-1esPk'
        // },
        events: {
            'onStateChange': onPlayerStateChange
        }
    });
}

function onPlayerStateChange(event) {
    if (event.data === 1) {
        $('.slider').slider('pause');
    } else if (event.data === 2) {
        $('.slider').slider('start');
    }
}