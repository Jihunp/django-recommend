const triggerBtn = document.getElementsByClassName("trigger");
const triggerArray = Array.from(triggerBtn).entries();
const modals = document.getElementsByClassName("modal");
const closeBtn = document.getElementsByClassName("close");

for (let [i, trigger] of triggerArray) {
    toggleModals = function() {
        modals[i].classList.toggle("my-modal");
    };
    trigger.addEventListener("click", toggleModals);
    closeBtn[i].addEventListener("click", toggleModals);
}
// escape all modals with esc key
window.onkeydown = function(event) {
    if(event.key == 'Escape') {
        for(let index of modals) {
            index.style.display = 'none'
        }
    }
}