
// WRITTEN AND COMMENTED BY HENRY FRIMAN 2021

// 1. CREATING A VARIABLE fetch THAT IMPORTS 
//    THE FUNCTIONS OF node-fetch LIBRARY

const fetch = require('node-fetch');


// 2. CREATING A FUNCTION WHICH USES THE node-fetch LIBRARY TO 
//    GET THE JSON CONTENT FROM THE SELECTED URL,
//    AND STORES THE DATA INTO THE response VARIABLE
//    ---> THE NEW VARIABLE postoffices IS CREATED 
//         TO PARSE THE JSON CONTENT FROM response,
//         AND IT IS ALSO RETURNED AT THE END OF THE FUNCTION
async function getPostOffices() {
	let response = await fetch('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json');
	let postoffices = await response.json();
	return postoffices;

}

// THIS PROGRAM IS EXPORTED AS A SEPARATE OBJECT getPostOffices,
// WHICH WILL BE REFERRED TO LATER IN THE index.js FILE
module.exports = { getPostOffices }
