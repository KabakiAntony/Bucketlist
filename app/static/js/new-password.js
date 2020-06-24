/* values for password update */
let newPasswordForm = document.getElementById('newPasswordForm');
let newEmail = document.getElementById('newEmail');
let newPassword = document.getElementById('newPassword');

/*input validations */

newEmail.addEventListener('input',(e)=>{
    if(isEmail(newEmail.value)){
        document.getElementById("new-error-email").innerHTML = ""; 
    }
    else{
        document.getElementById("new-error-email").innerHTML = "Please enter a valid email address";
    }
});
newPassword.addEventListener('input',(e)=>{
    if(isValidPassword(newPassword.value))
    {
        document.getElementById("new-error-password").innerHTML = "";
    }else{
        document.getElementById("new-error-password").innerHTML = 
        `Password should contain atleast 
        1 uppercase character,
        1 lowercase character,
        1 number, 
        1 special character,
        atleast 6 characters
        & not more than 20`;
    }
});

/* set new password function */
function postNewPassword(){
const email = document.getElementById('newEmail').value;
const password = document.getElementById('newPassword').value;
newPasswordData = {
    email,
    password
};
fetch('/auth/newpass',{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(newPasswordData)
  })
  .then(response => response.json())
  .then(({data,status,error})=>{
      if(status === 200){
          callToast(data);          
      }
      else if(status === 400){
        document.getElementById('up-error-email').innerHTML = `${error}`;
      }
  })
  .catch(err => console.log(`This error occured :${err}`));
}

 
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
    if(!isEmail(newEmail.value)){
        document.getElementById("up-error-email").innerHTML = "Please enter a valid email address";
        return false;
    }
    if(!isValidPassword(newPassword.value)){
        document.getElementById("up-error-password").innerHTML = 
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
function callToast(data) {
    let snackbar = document.getElementById("signup-success");
    snackbar.innerHTML = `
    ${data}
    </br>
    </br>We will now redirect you to the homepage....
    `
    snackbar.className = "show";
    setTimeout(function(){ snackbar.className = snackbar.className.replace("show", "");
    location.href ='/';
    }, 10000);
}
/* sign up submission */
newPasswordForm.addEventListener('submit',(e)=>{
    e.preventDefault();
    validateData();
    postNewPassword();
}); 
