/* values for sign-up */
let signUpForm = document.getElementById('upForm');
let upFirstName = document.getElementById('firstname'); 
let upEmail = document.getElementById('upEmail');
let upPassword = document.getElementById('upPassword');

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
document.getElementById ('sign-up-form').addEventListener('click',
function(){
    document.querySelector('.bg-sigin-modal').style.display = "flex";
});

/* validate on user input */

upEmail.addEventListener('input',(e)=>{
    if(isEmail(upEmail.value)){
        document.getElementById("error-email").innerHTML = ""; 
    }
    else{
        document.getElementById("error-email").innerHTML = "Please enter a valid email address";
    }
});
upPassword.addEventListener('input',(e)=>{
    if(isValidPassword(upPassword.value))
    {
        document.getElementById("error-password").innerHTML = "";
    }else{
        document.getElementById("error-password").innerHTML = 
        `Password should contain atleast 
        1 uppercase character,
        1 lowercase character,
        1 number, 
        1 special character,
        atleast 6 characters
        & not more than 20`;
    }
});
/* sign up function */
function postSignUp(){
const email = document.getElementById('upEmail').value;
const password = document.getElementById('upPassword').value;
const firstname = document.getElementById('firstname').value;
signUpData = {
    firstname,
    email,
    password
};
fetch('/auth/signup',{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(signUpData)
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
signUpForm.addEventListener('submit',(e)=>{
    e.preventDefault();
    validateData();
    postSignUp();
});
