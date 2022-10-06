const add=document.querySelector("#button1");
const form= document.querySelector("#main");
const count= document.querySelector("#num");
const alert_div= document.querySelector("#alert");
const register_btn= document.querySelector("#register_btn");


console.log(max_participants)
var i=2

var curr_members = 2;
var req_members= min_participants - curr_members;
register_btn.addEventListener("click",e=>{
    var req_members= min_participants - curr_members;

    if(req_members>0){
        alert_div.innerHTML=`Add atleast ${req_members} more members in your Team to register for this competition.`
        register_btn.disabled=true
        }
})


add.addEventListener('click',target=>{
    console.log(max_participants)
    console.log(min_participants)
    target.preventDefault()
    if(count.value>=max_participants){
        add.disabled=true
        console.log(curr_members)
        alert_div.innerHTML=`Maximum number of members added for this competition.`
    }
    if(count.value<max_participants){
        console.log('temp')
        form.insertAdjacentHTML('beforeend',`<div id="${i}"><div class="row-view" >
        <div id="h${i}" class="member" >
            <div >
                <div style="font-size: 120%;font-weight: bold;">Member ${i}:</div>
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
                <input type="text" name="name${i}" id="name${i}" class="input-text-field " required placeholder="Name">
            </div>
            <br><br><br>
            <div>
                <span class="head-style">Contact Number<span class="red-star"> *</span></span>
                <br>
                <div style="display:flex; width: 100%;">
                <input type="text" name="countryCode${i}" class="input-text-field " maxlength="5" required
                  id="id_name_country" style="width: 40px; margin-right: 10px;" placeholder="+12">
                <input type="text" name="phoneNo${i}" class="input-text-field " maxlength="50" required id="id_name" placeholder="Contact Number(e.g. 123456789)">
              </div>
            </div>
            <br><br><br>
            <div>
                <span class="head-style">Program Enrolled<span class="red-star"> *</span></span>
                <br>
                <!-- <input type="email" id="email_m_0" class="input-text-field " required> -->
                <select class="input-text-field" name="degree${i}" required>
                    <option class="drop-down">Program Enrolled</option>
                    <option value="btech">B.Tech</option>
                    <option value="mtech">M.Tech</option>
                    <option value="other">Other</option>
                </select>
                <input type="checkbox" style="margin-top: 12px" name="samedegree${i}" onchange="samefunc(${i})"><label style="margin-left:5px">Same as Leader</label>

            </div>
            <br><br><br>
            <div>
                <span class="head-style">Year of Passing<span class="red-star"> *</span></span>
                <br>
                <!-- <input type="text" id="name_m_1" class="input-text-field " required> -->
                <input type="number" name="year${i}" class="input-text-field " maxlength="4" required id="id_year" placeholder="Year of Passing">
                <input type="checkbox" style="margin-top: 12px" name="sameyear${i}" onchange="samefunc(${i})"><label style="margin-left:5px">Same as Leader</label>
            </div>
        </div>
        <div class="sections m-5">
            <div>
                <span class="head-style">Gender<span class="red-star"> *</span></span>
                <br>
                <select class="input-text-field " name="gender${i}"id="gender_m_1" required>
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
                <input type="email" name="email${i}" id="email${i}" class="input-text-field " required placeholder="Email">
            </div>
            <br><br><br>
            <div>
                <span class="head-style">Institute Name<span class="red-star"> *</span></span>
                <br>
                <!-- <input type="email" id="email_m_0" class="input-text-field " required> -->
                <input type="text" name="collegename${i}" class="input-text-field " maxlength="254" required id="id_collegename" placeholder="Institute Name">
                <input type="checkbox" style="margin-top: 12px" name="samecollege${i}" onchange="samefunc(${i})"><label style="margin-left:5px">Same as Leader</label>

            </div>
        </div>


    </div>
    </div>
    `);
    // req_memebers= min_participants - count.value
    // if(req_memebers>0){
    //     alert_div.innerHTML=`Add atleast ${req_memebers-1} more members in your Team to register for this competition.`
    // }
    // if(req_memebers=0){
    //     alert_div.innerHTML=``
    // }
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
        req_members--
        curr_members++
        // console.log("upated value: " + req_members)
    }
    if(req_members>0){
        alert_div.innerHTML=`Add atleast ${req_members} more members in your Team to register for this competition.`
        console.log(req_members)
        register_btn.disabled=true
        }
    else{
        alert_div.innerHTML=``
        register_btn.disabled=false
        }
})

function del(div) {
    document.getElementById(div).remove()
    document.getElementById("hidden").insertAdjacentHTML('beforeend',`<input type="hidden" name="name${div}" value=""/>`)
    }

function remove(div){
    del(div)
    for (let j = div + 1; j < i; j++) {

        document.getElementById("h" + j).innerHTML = `<div>
        <div style="font-size: 120%;font-weight: bold;" >Member ${j - 1}:</div>
    </div>
    <div>
        <button class="add-member-button" onclick= remove(${j - 1})>
            <i class="fa fa-minus-circle mr-2"></i>Delete member</button> 
    </div>`;
        document.getElementById(j).setAttribute("id", j - 1)
        document.getElementById("h" + j).setAttribute("id", `h${j - 1}`)
        document.getElementById("name" + j).setAttribute("name", `name${j - 1}`)
        document.getElementById("phoneNo" + j).setAttribute("name", `phoneNo${j - 1}`)
        document.getElementById("email" + j).setAttribute("name", `email${j - 1}`)
        document.getElementById("name" + j).setAttribute("id", j - 1)
        document.getElementById("phoneNo" + j).setAttribute("id", j - 1)
        document.getElementById("email" + j).setAttribute("id", j - 1)

    }
    i--
    count.value = i
    req_members++
    curr_members--
    if(curr_members<max_participants){
        add.disabled=false
    }
    if(req_members>0){
        alert_div.innerHTML=`Add atleast ${req_members} more members in your Team to register for this competition.`
        console.log(req_members)
        register_btn.disabled=true
        }
    else{
        alert_div.innerHTML=``
        register_btn.disabled=false
        }
    // console.log("upated value: " + req_members)
}
// console.log(count.value)
