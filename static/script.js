let img = document.getElementsByTagName("img")



function read1() {
    let link1 = new XMLHttpRequest();
    link1.onreadystatechange = function () {
        if (link1.readyState == 4 && link1.status == 200) {
            let data1 = JSON.parse(link1.responseText)

            for (let i = 0; i < 3; i++) {
                document.getElementsByClassName("merit_name")[i].innerHTML = data1.record[i].username;
            }

        }

    }
    link1.open("GET", "data.json", true);
    link1.send();
}



function read2() {
    let link3 = new XMLHttpRequest();
    link3.onreadystatechange = function () {
        if (link3.readyState == 4 && link3.status == 200) {
            let data3 = JSON.parse(link3.responseText)

            for (let i = 0; i < 3; i++) {
                document.getElementsByClassName("merit_points")[i].innerHTML = data3.record[i].points;
            }
        }


    }
    link3.open("GET", "data.json", true);
    link3.send();
}



function readata() {
    let link3 = new XMLHttpRequest();
    link3.onreadystatechange = function () {
        if (link3.readyState == 4 && link3.status == 200) {
            let data3 = JSON.parse(link3.responseText)

            for (let i = 0; i < 3; i++) {
                document.getElementsByTagName("img")[i].src = data3.record[i].profilelink;
                img[i].width = "260"
                img[i].height = "260"
            }
        }


    }
    link3.open("GET", "data.json", true);
    link3.send();
}
function read7() {
    let link3 = new XMLHttpRequest();
    link3.onreadystatechange = function () {
        if (link3.readyState == 4 && link3.status == 200) {
            let data3 = JSON.parse(link3.responseText)

            for (let i = 0; i < 3; i++) {
                document.getElementsByClassName("merit_rank")[i].innerHTML = "#" + data3.record[i].rank;

            }
        }


    }
    link3.open("GET", "data.json", true);
    link3.send();
}






function addclass1(i) {

    const line2 = document.getElementsByClassName("Line2");
    const div = document.createElement("div");
    div.classList.add("Container2");
    line2[0].appendChild(div);


    var container2 = document.getElementsByClassName("Container2");
    let div1 = document.createElement("div");
    div1.classList.add("Card4");
    container2[i].appendChild(div1);

    var card4 = document.getElementsByClassName("Card4");
    let div2 = document.createElement("div");
    div2.classList.add("img2");
    card4[i].appendChild(div2);

    var img2 = document.getElementsByClassName("img2");
    let img = document.createElement("img");
    img2[i].appendChild(img);

    var div3 = document.createElement("div");
    div3.classList.add("Contentbox1");
    card4[i].appendChild(div3);


    var contentbox1 = document.getElementsByClassName("Contentbox1");
    let div4 = document.createElement("h2");
    div4.classList.add("name");
    div4.textContent = "Participant"
    contentbox1[i + 3].appendChild(div4);

    var div5 = document.createElement("div");
    div5.classList.add("rank");
    contentbox1[i + 3].appendChild(div5);

    var rank = document.getElementsByClassName("rank");
    let span1 = document.createElement("span");
    span1.classList.add("srank");
    span1.textContent = "#5";
    rank[i + 3].appendChild(span1);

    var div6 = document.createElement("div");
    div6.classList.add("Points");
    contentbox1[i + 3].appendChild(div6);


    points = document.getElementsByClassName("Points")
    let span2 = document.createElement("span");
    span2.classList.add("spoint");
    span2.textContent = "Points : 100";
    points[i + 3].appendChild(span2);


}



function create() {
    let link3 = new XMLHttpRequest();
    link3.onreadystatechange = function () {
        if (link3.readyState == 4 && link3.status == 200) {
            let data3 = JSON.parse(link3.responseText)

            for (let i = 0; i < data3.record.length - 3; i++) {
                addclass1(i);
            }
        }


    }
    link3.open("GET", "data.json", true);
    link3.send();
}



function read4() {
    let link1 = new XMLHttpRequest();
    link1.onreadystatechange = function () {
        if (link1.readyState == 4 && link1.status == 200) {
            let data1 = JSON.parse(link1.responseText)

            for (let i = 0; i < data1.record.length - 3; i++) {
                document.getElementsByClassName("name")[i].innerHTML = data1.record[i + 3].username;
            }

        }

    }
    link1.open("GET", "data.json", true);
    link1.send();
}


function read5() {
    let link3 = new XMLHttpRequest();
    link3.onreadystatechange = function () {
        if (link3.readyState == 4 && link3.status == 200) {
            let data3 = JSON.parse(link3.responseText)

            for (let i = 0; i < data3.record.length - 3; i++) {
                document.getElementsByClassName("spoint")[i].innerHTML = data3.record[i + 3].points;
            }
        }


    }
    link3.open("GET", "data.json", true);
    link3.send();
}


function read6() {
    let link3 = new XMLHttpRequest();
    link3.onreadystatechange = function () {
        if (link3.readyState == 4 && link3.status == 200) {
            let data3 = JSON.parse(link3.responseText)

            for (let i = 0; i < data3.record.length - 3; i++) {
                document.getElementsByTagName("img")[i + 3].src = data3.record[i + 3].profilelink;
                img[i + 3].width = "250"
                img[i + 3].height = "250"
            }
        }


    }
    link3.open("GET", "data.json", true);
    link3.send();
}


function read8() {
    let link3 = new XMLHttpRequest();
    link3.onreadystatechange = function () {
        if (link3.readyState == 4 && link3.status == 200) {
            let data3 = JSON.parse(link3.responseText)

            for (let i = 0; i < data3.record.length - 3; i++) {
                document.getElementsByClassName("srank")[i].innerHTML = "#" + data3.record[i + 3].rank;

            }
        }

    }
    link3.open("GET", "data.json", true);
    link3.send();
}



read1();
read2();
readata();
read7();
create();
read4();
read5();
read6();
read8();


