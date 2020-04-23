/* this file is meant for various js validations */
/* constants for signup modal */
const signUpForm = document.getElementById('upForm');
const upFirstName = document.getElementById('firstname'); 
const upEmail = document.getElementById('upEmail');
const upPassword = document.getElementById('upPassword');
const errorDiv = document.getElementById('error');
let emailRegex =/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}/igm;
let feedback = [];
/* constants for the signin modal
const signInForm = document.getElementById('inForm');
const inEmail = document.getElementById('inEmail');
const inPassword = document.getElementById('inPassword');
/* listen for submit on the signup modal */
async function getUsers() 
    {
      let response = await fetch(`https://kabucketlist.herokuapp.com/users`);
      let data = await response.json();
      return data;
    }
signUpForm.addEventListener('submit',(e)=>{
    /*
 
    if(upFirstName.value === '' || upFirstName.value == null){
        feedback.push('Enter a name');
        document.getElementById("firstname").style.borderColor = "red";
    }
    if(!upEmail.value.match(emailRegex)||email.value === ""){
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
        e.preventDefault();
        errorDiv.innerText = feedback.join(' , ');
    }

   /* when all else above is true go ahead and signup user 
   fetch('https://kabucketlist.herokuapp.com/users')
  .then(resp => resp.json())
  .then(data => console.log(data))
  .catch((err)=> console.log(err));*/

/*
    
    fetch('https://kabucketlist.herokuapp.com/auth/signup',{
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(signUpData)
      })
      .then((response) => response.json())
      .then((Data)=>{
          console.log(Data);
          /*if(!Status === 201 ){
              console.log('User signup successfully.'+ Data);
              alert(Error);
          }
          else{
              console.log(Error);
              alert('Failed');
          }

      }).catch((error) =>{
          
          alert("An error occured "+ error);
          console.log("This error "+ error);
      });*/
      getUsers()
      .then(data => console.log(data)).catch(error =>{
        console.log('THE FOLLOWING ERROR OCCURED',error);
        alert("Lets see this error");
      });
});


/* listen for submit on the signin form  
signInForm.addEventListener('submit',(e)=>{

    if(!inEmail.value.match(emailRegex)||inEmail.value === ""){
        feedback.push('Enter a valid email');
        document.getElementById("inEmail").style.borderColor = "red";      
    }
    if(inPassword.value.length < 6){
        document.getElementById("inPassword").style.borderColor = "red";
        feedback.push('Password too short!');

    }
    if(inPassword.value.length > 20){
        document.getElementById("inPassword").style.borderColor = "red";
        feedback.push('Password too long!');

    }
    if (feedback.length > 0){
        e.preventDefault();
        errorDiv.innerText = feedback.join(' , ');
    }  
});*/