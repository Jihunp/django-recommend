console.log("insanity check")

const modal = document.getElementsByClassName("modal");
const btn = document.getElementsByClassName("modal-btn");
// span element that closes the modal
const span =  document.getElementsByClassName("close");

[...btn].forEach((btn, i) => {
    btn.onclick = () => (modal[i].style.display ='block');
})


// for (let modalBtn of btn) {
//     modalBtn.onclick = function(event) {
//         modalBtn = document.querySelector(event.target.getAttribute('href')).style.display ="block";
//     }
// }

// for (let close of span) {
//     close.onclick = function(event) {
//         event.target.parentNode.parentNode.style.display = 'none';
//     }
// }
// click outside of the modal exit modal
window.onclick = function(event) {
    if(event.target.classList.contains('modal')) {
        for(let mod of modal) {
            if(typeof mod.style !== 'undefined') {
                mod.style.display = 'none'
            }
        }
    }
}
// escape key exit modal
window.onkeydown = function(event) {
    if(event.key == 'Escape') {
        for(let mod of modal) {
            mod.style.display = 'none'
        }
    }
}





// user clicks button opens specific modal
// for (let i = 0; i < btn.length; i++) {
//     btn[i].onclick = function(e) {
//         e.preventDefault();
//         // we may have to add another name for each class
//         // ele = document.getElementById("open-modal");
//         // ele.classList.add("")
//         mods = document.querySelector(e.target.getAttribute("href"));
//         mods.style.display = "block";
//     }
// }

// for (let i = 0; i < span.length; i++) {
//     span[i].onclick = function() {
//         for (let index in modal) {
//             if (typeof modal[index].style !== 'undefined') modal[index].style.display = "none";
//         }
//     }
// }

// window.onclick = function(event) {
//     if (event.target.classList.contains('modal')) {
//         for(let index in modal) {
//             if (typeof modal[index].style !== 'undefined') modal[index].style.display = "none";
//         }
//     }
// }


// btn.onclick = function() {
//     modal.style.display = "block";
// }
// span.onclick = function() {
//     modal.style.display = "none";
// }
// window.onclick = function(event) {
//     if (event.target == modal) {
//         modal.style.display = "none"
//     }
// }







