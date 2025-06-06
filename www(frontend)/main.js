// Bouncing Part //
$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "bounceIn",
        },
        out:{
            effect: "bounceOut",
        },
    });
    // SiriWave Configuration //
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.10",
        autostart: true,
      });
      // Siri Message Animation // 
      $('.siri-message').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "bounceIn",
        },
        out:{
            effect: "bounceOut",
        },
    });

    //Mic button click event
    $("#MicBtn").click(function () { 
        eel.playAssistantSound();
        $("#oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()();
    });

    //Making shortcut kry for mic button
    function doc_keyUp(e){
        if(e.key === 'a' || e.key === 'A'){
            eel.playAssistantSound();
            $("#oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands()();
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    function PlayAssistant(message){
        if(message != ""){
            $("#oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("");
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        }
    }
    function ShowHideButton(message) {
        if(message.length == 0){
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        }
        else{
            $("#MicBtn").attr("hidden", true);
            $("#SendBtn").attr("hidden", false);
        }
    }
    $("#chatbox").keyup(function () {
        let message = $("#chatbox").val();
        ShowHideButton(message);
    });
    $("#SendBtn").click(function () {
        let message = $("#chatbox").val();
        PlayAssistant(message);
    });
    $("#chatbox").keypress(function (e){
        key = e.which;
        if(key == 13){
            let message = $("#chatbox").val();
            PlayAssistant(message);
        }
    });
    $("#ChatBtn").click(function () {
        var offcanvasElement = document.getElementById('offcanvasLeft')
        var bsOffcanvas = new bootstrap.Offcanvas(offcanvasElement)
        bsOffcanvas.toggle()
    });
});
