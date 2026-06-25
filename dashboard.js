// Load Complaints

loadComplaints();

function loadComplaints(){

fetch("/complaints")

.then(response=>response.json())

.then(data=>{

let table=document.querySelector("#complaintTable tbody");

table.innerHTML="";

document.getElementById("totalComplaints").innerHTML=data.length;

let pending=0;

let resolved=0;

data.forEach(c=>{

if(c.status==="Pending"){

pending++;

}
else{

resolved++;

}

let row=table.insertRow();

row.insertCell(0).innerHTML=c.id;

row.insertCell(1).innerHTML=c.name;

row.insertCell(2).innerHTML=c.category;

row.insertCell(3).innerHTML=c.description;

row.insertCell(4).innerHTML=

`<span>${c.status}</span>`;

row.insertCell(5).innerHTML=

`
<button class="resolve-btn"
onclick="resolveComplaint(${c.id})">

Resolve

</button>

<button class="delete-btn"
onclick="deleteComplaint(${c.id})">

Delete

</button>

`;

});

document.getElementById("pendingComplaints").innerHTML=pending;

document.getElementById("resolvedComplaints").innerHTML=resolved;

document.getElementById("todayComplaints").innerHTML=Math.floor(Math.random()*10)+1;

document.getElementById("monthlyComplaints").innerHTML=data.length;

});

}

// Resolve Complaint

function resolveComplaint(id){

fetch("/complaints/"+id,{

method:"PUT",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

status:"Resolved"

})

})

.then(response=>response.json())

.then(data=>{

alert("Complaint Resolved Successfully");

loadComplaints();

});

}

// Delete Complaint

function deleteComplaint(id){

if(confirm("Delete this complaint?")){

fetch("/complaints/"+id,{

method:"DELETE"

})

.then(response=>response.json())

.then(data=>{

alert("Complaint Deleted");

loadComplaints();

});

}

}

// Search

document.getElementById("search")

.addEventListener("keyup",function(){

let filter=this.value.toLowerCase();

let rows=document.querySelectorAll("#complaintTable tbody tr");

rows.forEach(row=>{

row.style.display=row.innerText.toLowerCase()

.includes(filter)

? ""

:"none";

});

});