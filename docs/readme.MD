<h3 align="center">Welcome to Project Documention The Socio Platform<h3>
<h6 align="center">

![Project](https://img.shields.io/badge/Project-The%20Socio-blue?style=flat) 
![Version](https://img.shields.io/badge/Version-1.0.0-black?style=flat)
</h6>

<h3>Table of Content ...........</h3>
<h4>
<a href="https://github.com/yeazin/The-Socio/tree/main/docs#-authentication-">. Authentication </a> <br> 
<a href="https://github.com/yeazin/The-Socio/tree/main/docs#-social-profile-">. Social Profile</a> <br>
<a href="https://github.com/yeazin/The-Socio/tree/main/docs#-follow--unfollow-">. Follow / Unfollow </a> <br>
<a href="https://github.com/yeazin/The-Socio/tree/main/docs#-post-features-">. Post Features</a> <br>
<a href="https://github.com/yeazin/The-Socio/tree/main/docs#-api-collection-">. API Collection</a> <br>
</h4> 
    
<h3 align="center"> Authentication </h3>

#### Sign UP 
```bash
    User can Register in the Platform using

    {
        "Full Name", 
        "phone_number",
        "email",
        "Password",
        "Confirm Password"  
    }

    [Behind Logic : After an user sign up . The software will 
    autometically create an username with a role named "SOCIAN" 
    associated.]

```

#### Login & Logout 

```bash 

    All User having an account to the Platform is known as "SOCIAN".
    A SOCIAN user can Login to the platform using 

    {
        "Phone Number / Email ",
        "Password" 
    }

    User also can logout from the platform

```

#### Password Change 

```bash 

    All Socio User can change his/her password by passing 
    
    {
        "Old Password",
        "New Password",
        "Confirm New Password"

    }
```


<h3 align="center"> Social Profile </h3>

#### Social Links 

```bash

    All Socio User can link up their Social Profile link 
    in this platform.
    We have every social link option on our platform.

    All socio User can view or Update their social link any time.

```

#### Self View & Self Update Profile 

```bash 

    All Socio User can see his profile and 
    Update his/her profile 

    [Behind Logic : Some API with "self/" word in it is specially 
    for Logged IN current User]
    
```

#### Socio Profile List 

```bash 

    All Socio User can see other`s Socio User profile 

    [Behind Logic : Single View of user can be seen with Passing 
    Object_ID of Socio User ]

```
<h3 align="center"> Follow / Unfollow </h3>

#### Socio User Followers & Followings 

```bash 

    All Socio User can follow each other. 
    But If an user sent a request to follow other user , that other user 
    do not autometically following the prior user back until that other user
    wants to follow the prior user back or not.

    [ Behind Logic : Followers and Followings is determined with Many to Many to 
    Fields with symmetrical=False. 

    To initate follow and unfollow we need to pass the followings fields 

    {
        "action_name", # pass 'follow' or 'unfollow' based on action 
        "socio_user_id" # socio user id we want to be followed to the logged in user

    } 

    ]

```

<h3 align="center"> Post Features </h3>

#### Show Followers Post 

```bash 

    Socio User can see his/her followers post and also
    can see their profile . 

    [Behind Logic : Two Endpoint was created for 
    One - For all post ,
    Two - For all followers post ]

```

#### Like A POST

```bash 

    Socio User can give a thums up the post they like.

```

#### Comment to A POST

```bash 

    All Socio User can comment to any posts they want.

```

#### Share to A POST

```bash 

    All Socio User can share any post they want.

```

#### Creating Post 

```bash 
    All Socio User can create Post with the followings fields. 

    {
        "Post Title",
        "Post Description",
        "Post Image"
    }

```

#### View & Update the Post

```bash 

    All Socio User can view their post and update their post. 
    
    [Behind Logic : If any user wants to update another user`s post
    Then That will restricted from the system.]

```

<h3 align="center"> API Collection </h3>
