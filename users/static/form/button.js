const add=document.querySelector("#button1");
const form= document.querySelector("#main");
const count= document.querySelector("#num");

var i=1
add.addEventListener('click',target=>{
    target.preventDefault()
    form.insertAdjacentHTML('beforeend',`<div style="font-size:25px;padding-left: 40px;display: grid;grid-template-columns: 200px 0px;" id = "${i}">
    <h3 id="h${i}">Candidate ${i+1}<button onclick= remove(${i})>Remove</button></h3>
    <p>
    <div>
        <label for="id_name">Name:</label>
    </div>
    <div>
        <input type="text" name="name${i}" maxlength="50" id="name${i}" required id="id_name">
    </div>
    <div>
        <label for="id_name">Contact No:</label>

    </div>
    <div>
        <input type="text" name="phoneNo${i}" maxlength="50"  id="phoneNo${i}" required id="id_name">

    </div>
    <div>
        <label for="id_email">Email:</label>

    </div>
    <div>
        <input type="email" name="email${i}" id="email${i}" maxlength="254" required id="id_email">

    </div>
    </p>
    </div>`);
    i++
    count.value = i
})

function del(div){
    document.getElementById(div).remove()
    document.getElementById("hidden").insertAdjacentHTML('beforeend',`<input type="hidden" name="name${div}" value=""/>`)
}
function remove(div){
    del(div)
    for(let j=div+1;j<i;j++){
        document.getElementById(j).setAttribute("id",j-1)
        document.getElementById("h"+j).innerHTML=`Candidate ${j} <button onclick= remove(${j-1})>Remove</button>`;
        document.getElementById("h"+j).setAttribute("id",j-1)
        document.getElementById("name"+j).setAttribute("id",j-1)
        document.getElementById("phoneNo"+j).setAttribute("id",j-1)
        document.getElementById("email"+j).setAttribute("id",j-1)
    }
    i--
    count.value = i
    
}