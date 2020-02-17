/*
    Hack the North 2020 Front-End Challenge
    Tailai Wang, UW CS/BBA '24
*/

$.getJSON("https://hackthenorth.netlify.com/api/fe-challenge-attendee", function(data){
    console.log(data);
    if (data == null){ //Null Case
        $('.error').attr('class', 'error_active');
        $('.error_pic').attr('src', 'images/astroworld.jpg');
        $('.error_message').append("Houston, We Have a Problem Here!");
    }else{ //Only if the Profile Exists
        /* Organizing Data */
        var id = data.id;
        var name = data.name;
        var ppic = data.profile_pic;
        var bio = data.bio;
        var type = data.type;
        var checked_in = data.checked_in;
        var actions = data.actions;
        if (type == "hacker"){
            var num_workshops_attended = data.num_workshops_attended;
        }
        if (type == "sponsor"){
            var sponsor_company = data.sponsor_company;
            var sponsor_company_link = data.sponsor_company_link;
        }
        if (type == "volunteer"){
            var next_shift = data.next_shift;
        }
        if (type == "organizer"){
            var phone_number = data.phone_number;
        }
        /* End Data Organization */

        $('.main_profile').attr('class', 'main_profile_active');
        $('.profile_pic').attr('src', ppic);
    }
});