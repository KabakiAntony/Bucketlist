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

/* this part acts on the  sign up modal */

document.getElementById("sign-up").addEventListener('click',
function(){
    document.querySelector('.bg-register-modal').style.display = "flex";
});
document.querySelector('.closeb').addEventListener('click',
function(){
    document.querySelector('.bg-register-modal').style.display = "none";
});


signUpForm.addEventListener('submit',(e)=>{
    e.preventDefault();
    validateData();
    postSignUp();
});

function validateData(){
    /* validation on submit during signup goes here */
    let errorDiv = document.getElementById('upError');
    let emailRegex =/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}/igm;
    let feedback = [];
    

    if(upFirstName.value === '' || upFirstName.value == null){
        feedback.push('Enter a name');
        document.getElementById("firstname").style.borderColor = "red";
    }
    if(!upEmail.value.match(emailRegex)||upEmail.value === ""){
        feedback.push('Enter a valid email');
        document.getElementById("upEmail").style.borderColor = "red";    
    }
    if(upPassword.value.length < 6){
        document.getElementById("upPassword").style.borderColor = "red";
        feedback.push('Password too short!');
    }
    if(upPassword.value.length > 20){
        document.getElementById("upPassword").style.borderColor = "red";
        feedback.push('Password too long!');
    }
    if (feedback.length > 0){
        errorDiv.innerText = feedback.join(' , ');
    }
}
function postSignUp(){
    /* when validations are ok  then go ahead and sign up user with entered data */

const email = document.getElementById('upEmail').value;
const password = document.getElementById('upPassword').value;
const firstname = document.getElementById('firstname').value;
signUpData = {
    firstname,
    email,
    password
};
fetch('https://kabucketlist.herokuapp.com/auth/signup',{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(signUpData)
  })
  .then(response => {
    /* 
    Here we get the response from the server
    That is a success or why it is not.
    */ 
    if(response.ok) {
        return response.json();          
    }
    else
    {
        console.log("The server could not service our rekuest due to : ", response.statusText);
    }
})
.then(data => {
    /*
    This returns the data we posted to the server
    */
    console.log(data);
})
/* 
An error here only occurs if there is something that is 
preventing a fetch most of the times it is a network error.
 */
.catch(error => console.log('This error occured :',error));
}