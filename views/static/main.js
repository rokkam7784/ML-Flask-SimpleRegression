async function validateform() {
    var yrsOfExperience = document.myform.yrsOfExperience.value;
    if (yrsOfExperience == null || yrsOfExperience == "") {
        alert("Years of experience can't be blank");
        return false;
    }
    else if (isNaN(yrsOfExperience)) {
        document.myform.yrsOfExperience.value = '';
        alert("Enter a numerical value as years of experience");
        return false;
    } else {
        fetch(`predict/${yrsOfExperience}`, {
            method: 'GET',
            redirect: 'follow',
        }).then(response => response.json())
        .then(result => {
          alert(`Your predicted salary would be Rs. ${result['Salary']}/-`);
          document.myform.yrsOfExperience.value = '';
        })
        .catch(error => {
          console.error('Error:', error);
        });
        
    }
   
}

