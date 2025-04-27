$(document).ready(function () {



    eel.expose(DisplayMessage) //displaying message when siri wave is played from the mic button
    function DisplayMessage(message) {

        $(".siri-message li:first").text(message);
        $('.siri-message').textillate('start');

    }


    eel.expose(ShowHood)     //going back to hood
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);

    }
});