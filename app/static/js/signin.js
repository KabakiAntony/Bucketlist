/* values for sign-in */
let signInForm = document.getElementById('inForm');
let inEmail = document.getElementById('inEmail');
let inPassword = document.getElementById('inPassword');

/* this part acts on the sign in modal */
document.getElementById ('sign-in').addEventListener('click',
function(){
    document.querySelector('.bg-sigin-modal').style.display = "flex";
});
document.querySelector('.close').addEventListener('click',
function(){
    document.querySelector('.bg-sigin-modal').style.display = "none";
});
document.getElementById ('bottom-sign-in').addEventListener('click',
function(){
    document.querySelector('.bg-sigin-modal').style.display = "flex";
});

/* sign in validations*/

inEmail.addEventListener('input',(e)=>{
    if(isEmail(inEmail.value)){
        document.getElementById("in-error-email").innerHTML = ""; 
    }
    else{
        document.getElementById("in-error-email").innerHTML = "Please enter a valid email address";
    }
});
inPassword.addEventListener('input',(e)=>{
    if(isValidPassword(inPassword.value))
    {
        document.getElementById("in-error-password").innerHTML = "";
    }else{
        document.getElementById("in-error-password").innerHTML = 
        `Password should contain atleast 
        1 uppercase character,
        1 lowercase character,
        1 number, 
        1 special character,
        atleast 6 characters
        & not more than 20`;
    }
});

/* validaition functions */
function isEmail(my_email){
    let emailRegex =/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}/igm;
    return my_email.match(emailRegex);
}
function isValidPassword(my_password){
    let passwordRegex = /^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){6,20}$/igm;
    return my_password.match(passwordRegex);
}
function validateData(){
    if(!isEmail(upEmail.value)){
        document.getElementById("error-email").innerHTML = "Please enter a valid email address";
        return false;
    }
    if(!isValidPassword(upPassword.value)){
        document.getElementById("error-password").innerHTML = 
        `Password should contain atleast 
        1 uppercase character,
        1 lowercase character,
        1 number, 
        1 special character,
        atleast 6 characters
        & not more than 20.`;
        return false;
    }
}
/* sign up submission */
// signInForm.addEventListener('submit',(e)=>{
//     e.preventDefault();
//     validateData();
//     postSignIn();
// });
