var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    } 
  });
}
var acc = document.getElementsByClassName("accordion2");
var j;

for (j = 0; j < acc.length; j++) {
  acc[j].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel2 = this.nextElementSibling;
    if (panel2.style.maxHeight) {
      panel2.style.maxHeight = null;
    } else {
      panel2.style.maxHeight = panel2.scrollHeight + "px";
    } 
  });
}

function reveal() {
    var reveals = document.querySelectorAll(".reveal");
  
    for (var i = 0; i < reveals.length; i++) {
      var windowHeight = window.innerHeight;
      var elementTop = reveals[i].getBoundingClientRect().top;
      var elementVisible = 150;
  
      if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add("active");
      } else {
        reveals[i].classList.remove("active");
      }
    }
  }
  
  window.addEventListener("scroll", reveal);
  

  function Cv_Strike(object, Width, Height, color, max_range, line_size) {
    const mid_height = Math.random() * 100;
    const main_height = Height;
    const Mainangle = Math.random() * 30 + 10;
    const can = object;
    can.width = Width;
    can.height = Height - 100;
    const c = can.getContext("2d");
    var height_small = main_height / 20;
  
    class part {
      constructor(x, y, angle, height) {
        this.segments = [];
        this.height = Math.random() * height;
        this.startX = x;
        this.startY = y;
        this.angle =
          angle - Math.random() < 0.5 ? Math.random() * 5 : Math.random() * -5;
      }
    }
  
    class segment {
      constructor(maxHeight, angle, x, y) {
        this.height = Math.random() * maxHeight + 25;
        height_small = (main_height - this.height) / 15
        this.angle = angle;
        this.x = x;
        this.y = y;
        this.destX = x - Math.cos(angle) * this.height;
        this.destY = y + Math.abs(Math.sin(angle) * this.height);
      }
    }
    var parts = [];
    var anglee = Math.random() > 0.5 ? Math.random() * 15 * -1 : Math.random() * 15;
  
    for (let b = 0; b < 3; b++) {
      let x_p = parts[b - 1] === undefined ? Math.random() * window.innerWidth / 2 + window.innerWidth / 4 : parts[b - 1].segments[parts[b - 1].segments.length - 1].destX;
      let y_p = parts[b - 1] === undefined ? 0 : parts[b - 1].segments[parts[b - 1].segments.length - 1].destY;
      parts.push(new part(x_p, y_p, Mainangle, main_height));
  
      for (let g = 0; g < 20; g++) {
        anglee -= Math.sin(Math.random() > 0.5 ? Math.random() * -1 : Math.random()) * 2;
        let x = parts[b].segments[g - 1] === undefined ? parts[b].startX : parts[b].segments[g - 1].destX;
        let y = parts[b].segments[g - 1] === undefined ? parts[b].startY : parts[b].segments[g - 1].destY;
        parts[b].segments.push(new segment(height_small, anglee, x, y));
      }
    }
  
  
  
    function draw() {
      c.strokeStyle = ' rgb(239, 245, 16)';
      c.lineWidth = 3.5;
      for (let b = 0; b < 1; b++) {
        for (let a = 0; a < parts[b].segments.length; a++) {
          c.beginPath();
          c.moveTo(parts[b].segments[a].x, parts[b].segments[a].y);
          c.lineTo(parts[b].segments[a].destX, parts[b].segments[a].destY);
          c.stroke();
        }
      }
  
    }
    draw();
  }
  
  
  function animate() {
    (Cv_Strike(document.getElementById("can"), window.innerWidth, 640));
  }
  
  var tab = []
  var l = setInterval(animate, 600);
  tab.push(l);
  


  