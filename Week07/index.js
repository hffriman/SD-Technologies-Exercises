
// WRITTEN AND COMMENTED BY HENRY FRIMAN 2021

// 1. CREATING VARIABLES THAT IMPORTS
//    THE express LIBRARY AND getPostOffices FUNCTION

const express = require('express');
const { getPostOffices } = require('./api');


// 2. CREATING app VARIABLE THAT USES express LIBRARY
//    IN ORDER TO CREATE A WEB APPLICATION,
//    --> AND PORT variable THAT DEFINES THE SERVER PORT
const app = express();
const PORT = process.env.PORT || 3000;


// 3. CREATING A FUNCTION THAT IS DEFINED TO
//    HAPPEN IN postitoimipaikka ENDPOINT:
//    ----> CREATING numero VARIABLE, WHICH STORES
//          THE VALUE USED AS AN URL PARAMETER

//    ----> CREATING A postoffices LIST THAT CONTAINS
//          THE RESULTS OF A FUNCTION getPostOffices()
//          A.K.A. HAS THE JSON FILE PARSED INSIDE

//    ----> CREATING A postofficekeys ARRAY THAT STORES
//          ALL THE KEYS OF postoffices LIST
    
//    ----> CREATING A NEW EMPTY LIST officelist, WHICH WILL STORE
//          ANY KEY FROM postofficekeys LIST, IF THE CURRENT ELEMENT
//          IN THE postofficekeys LOOP HAS THE SAME VALUE AS numero

//    ----> FINALLY, THE VARIABLE answer IS CREATED TO STORE THE SAVED DATA
//          IN JSON FORM, AND IS PUT INTO THE WEB APPLICATION BY res.json FUNCTION

app.get('/postitoimipaikka/', async function (req, res) {
	let numero = req.query.numero;

	let postoffices = await getPostOffices();

	let postofficekeys = Object.keys(postoffices);

	let officelist = []

	for (key in postofficekeys) {
		
		if (numero == postofficekeys[key]) {

			officelist.push(postoffices[numero]);
		}

	};

	const answer = {postinumero: numero, postitoimipaikka: officelist};
   
	res.json(answer);
});

// THIS PART OF THE CODE FINALIZES THIS PROGRAM'S FUNCTIONALITY
app.listen(PORT, () => console.log(`Palvelin käynnissä portissa ${PORT}`)); // kuunneltava portti
