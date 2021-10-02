//WRITTEN AND COMMENTED BY HENRY FRIMAN 2021

// STEP 1: DEFINING VARIABLES:
// TWO ARRAY VARIABLES THAT STORE THE CONTENT OF JSON FILES (users, posts):
//     ---> users.json AND posts.json ARE STORED INSIDE users and posts
// FOUR ARRAY VARIABLES THAT STORE ONLY ONE ATTRIBUTE OF EITHER users OR posts ARRAYS:
//     ---> usernames STORES name ATTRIBUTES FROM users ARRAY
//     ---> user_userids STORES id ATTRIBUTES FROM users ARRAY
//     ---> titles STORES title ATTRIBUTES FROM posts ARRAY
//     ---> post_userids STORES ALL THE userId ATTRIBUTES FROM post ARRAY
let users = require('./users.json');
let posts = require('./posts.json');
let usernames = users.map(user => user.name);
let user_userids = users.map(user => user.id);
let titles = posts.map(post => post.title);
let post_userids = posts.map(post => post.userId);


// STEP 2: PRINTING THE OUTPUT:
// - THE IDEA OF THE LOOP IS AS FOLLOWS:
//   1. THE FIRST ELEMENT FROM THE usernames ARRAY IS PRINTED
//   2. A NEW LOOP GOES THROUGH EACH ELEMENT OF titles ARRAY
//      ----> THE COMPARISON BEGINS:
//            --> IF THE CURRENT VALUE OF user_userids IS EQUAL
//                TO THE CURRENT VALUE OF post_userids,
//                (A.K.A. IF THE CURRENT POST HAS THE SAME userId AS THE
//                 CURRENT USER'S id), THE CURRENT title IS PRINTED
//   3. AFTER EACH TITLE WRITTEN BY THE CURRENT USER IS PRINTED,
//      THE FIRST LOOP STARTS AGAIN WITH THE NEXT USER AND SO ON...
// 

for (var i = 0; i < usernames.length; i++) {
	
	console.log('\n' + usernames[i]);
	
	for (var j = 0; j < titles.length; j++) {
	
		if (user_userids[i] == post_userids[j]) {
		
			console.log(' - ' + titles[j]);
			
		}	
	
	}

}
