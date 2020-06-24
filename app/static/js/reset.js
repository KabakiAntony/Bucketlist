/* values for sign-up */
let resetForm = document.getElementById('resetForm');
let resetEmail = document.getElementById('resetEmail');

/* signup validations */

resetEmail.addEventListener('input',(e)=>{
    if(isEmail(resetEmail.value)){
        document.getElementById("reset-error-email").innerHTML = ""; 
    }
    else{
        document.getElementById("reset-error-email").innerHTML = "Please enter a valid email address";
    }
});


/* reset instructions function */
function postReset(){
const email = document.getElementById('resetEmail').value;
resetData = {
    email
};
fetch('/auth/send-reset',{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(resetData)
  })
  .then(response => response.json())
  .then(({data,status,error})=>{
    if(status === 202){
        callToast(data);             
    }
    else if(status === 400){
      document.getElementById('reset-error-email').innerHTML = `${error}`;
    }
    else if(status === 404){
      document.getElementById('reset-error-email').innerHTML = `${error}`;
    }
})
.catch(err => console.log(`This error occured :${err}`));
}
/* reset submission */
resetForm.addEventListener('submit',(e)=>{
    e.preventDefault();
    validateData();
    postReset();
});

/* validaition functions */
function isEmail(my_email){
    let emailRegex =/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}/igm;
    return my_email.match(emailRegex);
}
function validateData(){
    if(!isEmail(resetEmail.value)){
        document.getElementById("reset-error-email").innerHTML = "Please enter a valid email address";
        return false;
    }
}
function callToast(data) {
    let snackbar = document.getElementById("signup-success");
    snackbar.innerHTML = `
    <span>${data}</span>&nbsp;
    </br>
    </br>We will now redirect you to the homepage....
    `
    snackbar.className = "show";
    setTimeout(function(){ snackbar.className = snackbar.className.replace("show", "");
    location.href ='/';
    }, 10000);
}


