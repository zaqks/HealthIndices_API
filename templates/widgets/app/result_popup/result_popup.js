const capture = document.getElementById("capture");
const result = document.getElementById("result_popup");

const indice_circle = document.getElementById("indice_circle");
const indice_val = document.getElementById("indice_val");
const risk_label = document.getElementById("risk_label");

const grid = document.getElementById("imgs_grid");

function toggle_result() {
  capture.classList.toggle("hide");
  result.classList.toggle("hide");
}

function render_images(data) {
  grid.innerHTML = "";
  //
  let content;
  for (const [name, url] of data) {
    content = `<div class="rslt"><img src="${url}"><h2>${name}</h2></div>`;
    grid.innerHTML += content;
  }
}

function set_bri(val) {
  indice_val.innerText = val;

  // COLORS
  indice_circle.classList.remove("high");
  risk_label.innerText = "low";

  if (val >= 7) {
    indice_circle.classList.add("high");
    risk_label.innerText = "high";
  }

  risk_label.innerText += " risk";
}
