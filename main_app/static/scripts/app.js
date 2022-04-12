const triggerBtn = document.getElementsByClassName("trigger");
const triggerArray = Array.from(triggerBtn).entries();
const modals = document.getElementsByClassName("modal");
const closeBtn = document.getElementsByClassName("close");

// for of loop that takes each instance of the button and toggles open and close for the modal
for (let [i, trigger] of triggerArray) {
    toggleModals = function() {
        // class named my-modal
        modals[i].classList.toggle("modal");
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

// modal number two for review
const btnTrigger = document.getElementsByClassName("trigger-2");
const arrayTrigger = Array.from(btnTrigger).entries();
const mods = document.getElementsByClassName("modal-2");
const btnClose = document.getElementsByClassName("close-2");

// for of loop that takes each instance of the button and toggles open and close for the modal
for (let [index, trigun] of arrayTrigger) {
    togglemods = function() {
        // class named my-modal-2
        mods[index].classList.toggle("modal-2");
    };
    trigun.addEventListener("click", togglemods);
    btnClose[index].addEventListener("click", togglemods);
}

// escape all mods with esc key.
// press open/close button once and then escape changes the way we view
window.onkeydown = function(event) {
    if(event.key == 'Escape') {
        for(let i of mods) {
            if (i.style.display === 'none') {
                i.style.display = 'block';
            } else {
                i.style.display = 'none';
            }
        }
    }
}