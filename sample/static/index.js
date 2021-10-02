var img = document.createElement("img");
img.src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXnOr5SRawnyU5oSKYu3gtqxH6ODvHnfXWvw&usqp=CAU"
// let jeet = document.getElementById("i01");
let jeet = document.getElementsByClassName("img2")
for (let i =0; i < 2; i++) {
    jeet[i].appendChild(img);
}
