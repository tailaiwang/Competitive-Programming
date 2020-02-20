/*
    Hack the North 2020 Front-End Challenge
    Tailai Wang, UW CS/BBA '24
*/
var id;
var name;
var ppic;
var bio;
var type;
var checked_in;
var actions;
var num_workshops_attended;
var sponsor_company;
var sponsor_company_link;
var next_shift;
var phone_number;

$.getJSON("https://hackthenorth.netlify.com/api/fe-challenge-attendee", function(data){
    console.log(data);
    if (data == null){ //Null Case
        $('.error').attr('class', 'error_active');
        $('.error_pic').attr('src', 'images/astroworld.jpg');
        $('.error_message').append("Houston, We Have a Problem Here!");
        $('.error_message2').append("The Profile You Requested Does Not Exist :(")
        $('.main_profile').attr('class', 'main_profile item_invisible');
        $('.login').attr('class', 'login item_invisible');
    }else{ //Only if the Profile Exists
        /* Organizing Data */
        $('.error').attr('class', 'item_invisible');
        id = data.id;
        name = data.name;
        ppic = data.profile_pic;
        bio = data.bio;
        type = data.type;
        checked_in = data.checked_in;
        actions = data.actions;
        login_start(); //Force User to Login
        /* Unique Information by User Type */
        if (type == "hacker"){
            num_workshops_attended = data.num_workshops_attended;
            $('.type_console').append("Astronaut Console (Hacker)");
            $('.num_workshops span').append(num_workshops_attended);
            $('.num_workshops').attr('class', 'num_workshops text-center info_active');
        }
        if (type == "sponsor"){
            sponsor_company = data.sponsor_company;
            sponsor_company_link = data.sponsor_company_link;
            $('.type_console').append("Astronaut Console (Sponsor)");
            $('.sponsor_info span').append(sponsor_company + " (" + sponsor_company_link + ")");
            $('.sponsor_info').attr('class', 'sponsor_info text-center info_active');
        }
        if (type == "volunteer"){
            next_shift = data.next_shift;
            $('.type_console').append("Astronaut Console (Volunteer)");
            $('.next_shift span').append(Date(next_shift));
            $('.next_shift').attr('class', 'next_shift text-center info_active');
        }
        if (type == "organizer"){
            phone_number = data.phone_number;
            $('.type_console').append("Astronaut Console (Organizer)");
            $('.phone_number span').append(phone_number);
            $('.phone_number').attr('class', 'phone_number text-center info_active');
        }
        if (checked_in){ //For Green vs. Red Check-In
            $('.checkin_status span').append("Checked In!");
            $('.checkin_status span').attr('class', 'checked');
            $('.checkin_status').attr('class', 'checkin_status text-center');
        }else{
            $('.checkin_status span').append("Not Checked In!");
            $('.checkin_status span').attr('class', 'not_checked');
            $('.checkin_status').attr('class', 'checkin_status text-center');

        }
        /* End Data Organization */

        /* Displaying to First Section: Primary Information*/
        $('.profile_pic').attr('src', ppic);
        $('.user_id').append(id);
        $('.name').append(name);
        $('.bio').append(bio);


        /*Displaying to Last Section: Action Information */
        if (actions.length == 0){
            $('.action_table').attr('class', 'item_invisible');
        }else{
            var i;
            for (i = 0; i < actions.length; i++){
                if (actions[i] == 'check_in'){
                    var markup = '<tr><td><button onclick = "check_in()">' + 'Check In' + '</button></td></tr>';
                }else if (actions[i] == 'call_phone'){
                    var markup = '<tr><td><button onclick = "call_phone()">' + 'Call Phone' + '</button></td></tr>';
                }else if (actions[i] == 'attend_workshop'){
                    var markup = '<tr><td><button onclick = "attend_workshop()">' + 'Attend Workshop' + '</button></td></tr>';

                }
                $('.action_buttons').append(markup);
            }
        }

    }
}); //end Main Function


/* Action Functions */
function check_in(){
    if(checked_in){
        alert('Already Checked In!');
    }else{
        checked_in = true;
        $('.checkin_status span').text("Checked In!");
        $('.checkin_status span').attr('class', 'checked');
    }
}//end check_in

function call_phone(){
    alert("Called Phone " + phone_number + "!");
}//end call_phone

function attend_workshop(){
    num_workshops_attended += 1;
    $('.num_workshops span').text(num_workshops_attended);
}//end attend_workshop

/* Login Functions */
function login_start(){
    $('.main_profile').attr('class', 'main_profile item_invisible');
    $('.login_pic').attr('src', 'images/astroworld.jpg');
    $('.login').attr('class', 'login_active text-center');
}//end login_start

function login_verification() {
    var user = document.forms["login_form"]["uname"].value;
    var pw = document.forms["login_form"]["pw"].value;
    if (user == "username" && pw == "password") {
        $('.login_active').attr('class', 'item_invisible');
        $('.main_profile').attr('class', 'main_profile_active');
    }else{
        alert("Invalid Login (Pssst username password)");
    }
}//end login_verification