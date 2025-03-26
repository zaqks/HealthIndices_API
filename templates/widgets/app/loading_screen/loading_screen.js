const loader = document.getElementById("loading_screen");
var loading = true;

function set_loading() {
  loader.style.display = "flex";
  loading = true;
}
function clear_loading() {
  loader.style.display = "none";
  loading = false;
}

clear_loading()
// document.addEventListener("DOMContentLoaded", function () {
//   setTimeout(() => {
//     clear_loading();
//   }, 1000);
// });
