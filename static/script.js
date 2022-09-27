const marquee = document.querySelectorAll(".clipped-text");
const gdsc = document.querySelectorAll(".gdsc");
// const tl = gsap.timeline({ default: { duration: 0.75, ease: "power1.out" } });

// tl.fromTo(".gdsc", { scale: 0 }, { scale: 1, duration: 1.5 });
// console.log(marquee);
// added event listener because it doesn't get the right width
addEventListener("load", function () {
  marquee.forEach((el) => {
    console.log(el);
    // set a default rate, the higher the value, the faster it is
    let rate = 200;
    // get the width of the element
    let distance = el.clientWidth;
    // get the margin-right of the element
    let style = window.getComputedStyle(el);
    let marginRight = parseInt(style.marginRight) || 0;
    // get the total width of the element
    let totalDistance = distance + marginRight;
    // get the duration of the animation
    // for a better explanation, see the quoted codepen in the first comment
    let time = totalDistance / rate;
    // get the parent of the element
    let container = el.parentElement;

    tl.to(container, time, {
      repeat: -1,
      x: "-" + totalDistance,
      ease: Linear.easeNone,
    });
  });
});

const rbinary = document.querySelector(".rbinary");
const randomBinary = [
  "11100100",
  "00000001",
  "11100100",
  "00000001",
  "00000010",
  "00000011",
  "00000100",
  "00000101",
  "00000110",
  "00000111",
  "00001000",
  "00001001",
  "00001010",
  "00001011",
  "00001100",
  "00001101",
  "00001110",
  "00001111",
  "00010000",
  "00010001",
  "00010010",
  "00010011",
  "00010100",
  "00010101",
  "00010110",
  "00010111",
  "00011000",
  "00011001",
  "00011010",
  "00011011",
  "00011100",
  "00011101",
  "00011110",
  "00011111",
  "00100000",
  "00100001",
  "00100010",
  "00100011",
  "00100100",
  "00100101",
  "00100110",
  "00100111",
  "00101000",
  "00101001",
  "00101010",
  "00101011",
  "00101100",
  "00101101",
  "00101110",
  "00101111",
  "00110000",
  "00110001",
  "00110010",
];
// console.log(randomBinary.length);

const interval = setInterval(function () {
  // method to be executed;
  arr = [];
  for (i = 0; i < 50; i++) {
    let value = Math.floor(Math.random() * 53);
    arr.push(value);
    // console.log(value);
  }

  let str = "";
  arr.forEach((e) => {
    // console.log(e);
    const r = randomBinary[e].split("");
    // console.log(r);
    r.forEach((z) => {
      str += z;
    });
    str += " ";
  });
  rbinary.textContent = str;
}, 1000);
// clearInterval(interval); // thanks @Luca D'Amico
// const tl = gsap.timeline({ default: { duration: 0.75, ease: "power1.out" } });
// tl.fromTo(
//   ".marquee_content_1",
//   { x: 0 },
//   { x: -100, ease: Linear.easeNone, duration: 1.5, yoyo: true }
// );

// https://codepen.io/lelamanolio/pen/ZEYRJJJ
// Inspired by:
// https://codepen.io/sgorneau/pen/mWEddP
// as described in the above codepen, if we set the value `x` to something like -100% it'll go too fast
// so I took the function to calculate the rate and applied to my code
