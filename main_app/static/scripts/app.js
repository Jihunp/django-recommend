console.log("insanity check")

const modal = document.getElementById("my-modal");
const btn = document.getElementById("modal-btn");
// span element that closes the modal
const span =  document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.style.display = "block";
}
span.onclick = function() {
    modal.style.display = "none";
}
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none"
    }
}







