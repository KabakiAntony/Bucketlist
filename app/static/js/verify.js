/* this file does a fetch to verify the email */
token = localStorage.getItem('user');
fetch(`https://kabucketlist.herokuapp.com/auth/verify?in=`+token,{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    }
  })
.then(response=>response.json())
.then(({data,status,error})=>{
    if(status === 200){
        console.log(data);
        document.getElementById('verified').innerHTML = data;
    }
    else{
        console.log(error, status)
    }
})
.catch((err)=>{
    console.log(err)

});