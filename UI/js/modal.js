/* this part acts on the sign in modal */

document.getElementById ('sign-in').addEventListener('click',
function(){
    document.querySelector('.bg-sigin-modal').style.display = "flex";
});
document.querySelector('.close').addEventListener('click',
function(){
    document.querySelector('.bg-sigin-modal').style.display = "none";
});

/* this part acts on the  sign up modal */

document.getElementById("sign-up").addEventListener('click',
function(){
    document.querySelector('.bg-register-modal').style.display = "flex";
});
document.querySelector('.closeb').addEventListener('click',
function(){
    document.querySelector('.bg-register-modal').style.display = "none";
});
