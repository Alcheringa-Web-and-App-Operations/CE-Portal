const add=document.querySelector("#button1");
const form= document.querySelector("#main");
const count= document.querySelector("#num");

var i=2
add.addEventListener('click',target=>{
    target.preventDefault()
    form.insertAdjacentHTML('beforeend',`<div id="${i}"><div class="row-view" >
    <div id="h${i}" class="member">
        <div >
            <div style="font-size: 120%;" >Member ${i}:</div>
        </div>
        <div>
            <button class="add-member-button" onclick= remove(${i})>
                <i class="fa fa-minus-circle mr-2"></i>Delete member</button> 
        </div>
    </div>
    
</div>
<div class="row-view">
    <div class="sections m-5">
        <div>
            <span class="head-style">Name<span class="red-star"> *</span></span>
            <br>
            <input type="text" name="name${i}" id="name${i}" class="input-text-field " required>
        </div>
        <br><br><br>
        <div>
            <span class="head-style">Contact Number<span class="red-star"> *</span></span>
            <br>
            <input type="number" name="phoneNo${i}" id="phoneNo${i}" class="input-text-field " required>
        </div>
    </div>
    <div class="sections m-5">
        <div>
            <span class="head-style">Gender<span class="red-star"> *</span></span>
            <br>
            <select class="input-text-field " id="gender_m_1">
            <option class="drop-down">Gender</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
            <option value="Other">Other</option>
        </select>
        </div>
        <br><br><br>
        <div>
            <span class="head-style">E-mail<span class="red-star"> *</span></span>
            <br>
            <input type="email" name="email${i}" id="email${i}" class="input-text-field " required>
        </div>
    </div>


</div>
</div>
`);
// <div style="font-size:25px;padding-left: 40px;display: grid;grid-template-columns: 200px 0px;" id = "${i}">
/* <h3 id="h${i}">Candidate ${i}<button onclick= remove(${i})>Remove</button></h3>
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
</div>` */
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
        
        document.getElementById("h"+j).innerHTML=`<div>
        <div style="font-size: 120%;" >Member ${j-1}:</div>
    </div>
    <div>
        <button class="add-member-button" onclick= remove(${j-1})>
            <i class="fa fa-minus-circle mr-2"></i>Delete member</button> 
    </div>`;
        document.getElementById(j).setAttribute("id",j-1)
        document.getElementById("h"+j).setAttribute("id",`h${j-1}`)
        document.getElementById("name"+j).setAttribute("name",`name${j-1}`)
        document.getElementById("phoneNo"+j).setAttribute("name",`phoneNo${j-1}`)
        document.getElementById("email"+j).setAttribute("name",`email${j-1}`)
        document.getElementById("name"+j).setAttribute("id",j-1)
        document.getElementById("phoneNo"+j).setAttribute("id",j-1)
        document.getElementById("email"+j).setAttribute("id",j-1)

    }
    i--
    count.value = i
    
}