function validateform() {
    var yrsOfExperience = document.myform.yrsOfExperience.value;
    if (yrsOfExperience == null || yrsOfExperience == "") {
        alert("Years of experience can't be blank");
        return false;
    }
    else if (isNaN(yrsOfExperience)) {
        document.myform.yrsOfExperience.value = '';
        alert("Enter a numerical value as years of experience");
        return false;
    }
}

