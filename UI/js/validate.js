/* this file is meant for various js validations */
const singUpForm = document.getElementById('upForm');
const firstname = document.getElementById('firstname'); 
const email = document.getElementById('upEmail');
const password = document.getElementById('upPassword');
const errorDiv = document.getElementById('error');
let emailRegex =/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}/igm;
let feedback = [];

singUpForm.addEventListener('submit',(e)=>{

    if(firstname.value === '' || firstname.value == null){
        feedback.push('Enter a name');
        document.getElementById("firstname").style.borderColor = "red";
    }
    if(!email.value.match(emailRegex)||email.value === ""){
        feedback.push('Enter a valid email');
        document.getElementById("upEmail").style.borderColor = "red";      
    }
    if(password.value.length < 6){
        document.getElementById("upPassword").style.borderColor = "red";
        feedback.push('Password too short!');

    }
    if(password.value.length > 20){
        document.getElementById("upPassword").style.borderColor = "red";
        feedback.push('Password too long!');

    }
    if (feedback.length > 0){
        e.preventDefault();
        errorDiv.innerText = feedback.join(' , ');
    }
    
    
});
