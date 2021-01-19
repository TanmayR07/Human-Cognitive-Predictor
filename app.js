function onClickedBehaviourType() {
    console.log("Estimate Behaviour button clicked");
    var WorkTime = document.getElementById("uiworktime");
    var annortaorAge = document.getElementById("uiage");
    var logTimeSinceEvent = document.getElementById("uilogtime");
    var timeSinceEvent = document.getElementById("uitimeevent");
    var Gender = document.getElementById("uigender");
    var distracted = document.getElementById("uidistracted");
    var frequency = document.getElementById("uifrequency");
    var draining = document.getElementById("uidraining");
    var importance = document.getElementById("uiimportance");
    var stressful = document.getElementById("uistressful");
    var similarity = document.getElementById("uisimilarity");
    var estbehaviour = document.getElementById("uiEstimatedBehaviour");
    var url = "/predict_human_behaviour";

    $.post(
        url,
        {
            worktime: parseFloat(workTime.value),
            annortaorAge: parseFloat(annortaorAge.value),
            logTimeSinceEvent: parseFloat(logTimeSinceEvent.value),
            Gender: Gender.value,
            distracted: distracted.value,
            frequency: frequency.value,
            draining: draining.value,
            importance: importance.value,
            stressful: stressful.value,
        },
        function (data, status) {
            console.log(data.estimated_Human_Behaviour);
            estPrice.innerHTML =
                "<h2>" + data.estimated_Human_Behaviour.toString() + "</h2>";
            console.log(status);
        }
    );
}

function onPageLoad() {
    console.log("document loaded");
    var url = "/get_gender_names";
    $.get(url, function (data, status) {
        console.log("got response for get_gender_names request");
        if (data) {
            var gender = data.gender;
            var uigender = document.getElementById("uigender");
            $("#uigender").empty();
            for (var i in gender) {
                var opt = new Option(gender[i]);
                $("#uigender").append(opt);
            }
        }
    });
    console.log("document loaded");
    var url1 = "/get_distracted";
    $.get(url1, function (data1, status1) {
        console.log("got response for get_distracted request");
        if (data1) {
            var distracted = data1.distraced;
            var uidistracted = document1.getElementById("uidistracted");
            $("#uidistracted").empty();
            for (var i in distracted) {
                var opt1 = new Option(distracted[i]);
                $("#uidistracted").append(opt1);
            }
        }
    });
    console.log("document loaded");
    var url2 = "/get_frequency";
    $.get(url2, function (data2, status) {
        console.log("got response for get_frequency request");
        if (data2) {
            var frequency = data2.frequency;
            var uifrequency = document2.getElementById("uifrequency");
            $("#uifrequency").empty();
            for (var i in gender) {
                var opt2 = new Option(frequency[i]);
                $("#uifrequency").append(opt2);
            }
        }
    });
    console.log("document loaded");
    var url3 = "/get_draining";
    $.get(url3, function (data3, status3) {
        console.log("got response for get_draining request");
        if (data3) {
            var draining = data3.draining;
            var uidraining = document3.getElementById("uidraining");
            $("#uidraining").empty();
            for (var i in gender) {
                var opt3 = new Option(draining[i]);
                $("#uidraining").append(opt3);
            }
        }
    });
    console.log("document loaded");
    var url4 = "/get_importance";
    $.get(url4, function (data4, status4) {
        console.log("got response for get_importance request");
        if (data4) {
            var importance = data4.importance;
            var uiimportance = document4.getElementById("uiimporatnce");
            $("#uiimportance").empty();
            for (var i in gender) {
                var opt4 = new Option(importance[i]);
                $("#uiimportance").append(opt4);
            }
        }
    });
    console.log("document loaded");
    var url5 = "/get_stressful";
    $.get(url5, function (data5, status5) {
        console.log("got response for get_stressful request");
        if (data5) {
            var stressful = data5.stressful;
            var uistressful = document5.getElementById("uistressful");
            $("#uistressful").empty();
            for (var i in gender) {
                var opt5 = new Option(stressful[i]);
                $("#uistressful").append(opt5);
            }
        }
    });
}
window.onload = onPageLoad;