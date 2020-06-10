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
    if(!isEmail(inEmail.value)){
        document.getElementById("in-error-email").innerHTML = "Please enter a valid email address";
        return false;
    }
    if(!isValidPassword(inPassword.value)){
        document.getElementById("in-error-password").innerHTML = 
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

/* sign in submission */
signInForm.addEventListener('submit',(e)=>{
    e.preventDefault();
    validateData();
    signinInfo = {
        email:inEmail.value,
        password:inPassword.value
    }
    postSignIn(signinInfo);
});

function postSignIn(signInData){
    fetch(`/auth/signin`,{
    method : 'POST',
    headers :{
        'Content-Type': 'application/json'
    },
    body:JSON.stringify(signInData)
    
})
.then(response =>response.json())
.then(({data,status,error}) => {
    if (status === 200){
        console.log(data);
        //localStorage.setItem('user',data);
        // callToast();
    }
    else if (status === 401)
    {
        document.getElementById('in-error-password').innerText = error;
    }
    else if(status === 404){
        document.getElementById('in-error-email').innerText = error;
    }
    else if(status === 400){
        document.getElementById('in-error-email').innerText = "An error occurred, please contact administrator!";
    } 
    else {
        document.getElementById('in-error-email').innerText = error;
    }   
})
.catch(err => console.log(err));
}

