const triggerBtn = document.getElementsByClassName("trigger");
const triggerArray = Array.from(triggerBtn).entries();
const modals = document.getElementsByClassName("modal");
const closeBtn = document.getElementsByClassName("close");

// for of loop that takes each instance of the button and toggles open and close for the modal
for (let [i, trigger] of triggerArray) {
    toggleModals = function() {
        // class named my-modal
        modals[i].classList.toggle("my-modal");
    };
    trigger.addEventListener("click", toggleModals);
    closeBtn[i].addEventListener("click", toggleModals);
}
// escape all modals with esc key
// bug in use
window.onkeydown = function(event) {
    if(event.key == 'Escape') {
        for(let index of modals) {
            index.style.display = 'none'
        }
    }
}