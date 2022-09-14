const add=document.querySelector("#button1");
const form= document.querySelector("#main");
const count= document.querySelector("#num");

var i=1
add.addEventListener('click',target=>{
    const temp=form.firstElementChild;
    target.preventDefault()
    form.innerHTML+=`<div style="font-size:25px;padding-left: 40px;display: grid;grid-template-columns: 200px 0px;">
    <h3>Candidate ${i+1}</h3>
    <p>
    <div>
        <label for="id_name">Name:</label>
    </div>
    <div>
        <input type="text" name="name${i}" maxlength="50" required="" id="id_name">
    </div>
    <div>
        <label for="id_name">Contact No:</label>

    </div>
    <div>
        <input type="text" name="phoneNo${i}" maxlength="50" required="" id="id_name">

    </div>
    <div>
        <label for="id_email">Email:</label>

    </div>
    <div>
        <input type="email" name="email${i}" maxlength="254" required="" id="id_email">

    </div>
    </p>
</div>`;
    i++;
    count.value = i
})