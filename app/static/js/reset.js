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

/* validaition functions */
function isEmail(my_email){
    let emailRegex =/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}/igm;
    return my_email.match(emailRegex);
}
function validateData(){
    if(!isEmail(upEmail.value)){
        document.getElementById("error-email").innerHTML = "Please enter a valid email address";
        return false;
    }
}


