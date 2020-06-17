### Parent Control

The origin of this project is due to the inconvenient of the parent control function on my Mac, where I want to set restriction of screen time for my two boys, who are in the age with great desire to computer games.


#### Request

Basic parent control functions as below:
- setup restriction on screen time length each day
- setup restrict login time window for each day 
- log for login/logout for each account
- force quit/logout when time is up or window is closed
- support configration and/or force logout over internet 

Further consideration:
- logs for application/website usage 
- set up restriction of application/website 

#### Technical Solution

- All setup/configeration are stored at AWS ECS
- Setup deman service upon each account login
- Deman service will check restrictions periodically
- Force logout/quit if out of restrictions

#### Key technical employed

- AWS ECS
- Python Flask (server side)
- Shell script (client side)
- REST API 
- Mac user/process management



#### Refences

- log out Mac user  Terminal command
https://superuser.com/questions/40061/what-is-the-mac-os-x-terminal-command-to-log-out-the-current-user

