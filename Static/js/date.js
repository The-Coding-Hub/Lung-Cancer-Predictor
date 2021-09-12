const date = new Date();
const dateNumber = (date.getDate()).toString();
const monthNumber = (date.getMonth())
console.log(monthNumber)
const yearNumber = (date.getFullYear()).toString();
var monthName = "";

if ((monthNumber+1) === 1) {
  monthName = "January";
} 
else if ((monthNumber+1) === 2) {
  monthName = "February";
} 
else if ((monthNumber+1) === 3) {
  monthName = "March";
}
else if ((monthNumber+1) === 4) {
  monthName = "April";
}
else if ((monthNumber+1) === 5) {
  monthName = "May";
}
else if ((monthNumber+1) === 6) {
  monthName = "June";
}
else if ((monthNumber+1) === 7) {
  monthName = "July";
}
else if ((monthNumber+1) === 8) {
  monthName = "August";
}
else if ((monthNumber+1) === 9) {
  monthName = "September";
}
else if ((monthNumber+1) === 10) {
  monthName = "October";
}
else if ((monthNumber+1) === 11) {
  monthName = "November";
}
else if ((monthNumber+1) === 12) {
  monthName = "December";
}

const dateToday = (dateNumber + " " + monthName + ", " + yearNumber);

const navItem = document.getElementById('date');
navItem.innerHTML = dateToday;