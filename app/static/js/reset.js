/* values for sign-up */
let signUpForm = document.getElementById('resetForm');
let upEmail = document.getElementById('upEmail');

/* signup validations */

upEmail.addEventListener('input',(e)=>{
    if(isEmail(upEmail.value)){
        document.getElementById("error-email").innerHTML = ""; 
    }
    else{
        document.getElementById("error-email").innerHTML = "Please enter a valid email address";
    }
});


/* reset instructions function */
function postReset(){
const email = document.getElementById('upEmail').value;
resetData = {
    email
};
fetch('/auth/signup',{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(resetData)
  })
  .then(response => {
    if(response.ok) {
        return response.json();          
    }
    else
    {

        console.log("The server could not service our rekuest due to : ", response.statusText);
    }
})
.then(data => {
    console.log(data);
})
/* 
An error here only occurs if there is something that is 
preventing a fetch most of the times it is a network error.
 */
.catch(error => console.log('This error occured :',error));
}


/* validaition functions */
function isEmail(my_email){
    let emailRegex =/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}/igm;
    return my_email.match(emailRegex);
}
function validateEmailData(){
    if(!isEmail(upEmail.value)){
        document.getElementById("error-email").innerHTML = "Please enter a valid email address";
        return false;
    }
}
/* sign up submission */
signUpForm.addEventListener('submit',(e)=>{
    e.preventDefault();
    validateEmailData();
    postReset();
});

/** everything down here goes for sign up on reset html */
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

