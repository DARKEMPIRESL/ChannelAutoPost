# ChannelAutoPost

![Contract-Storing-1155561250](https://user-images.githubusercontent.com/95665347/170169253-4bd788b0-75f7-43d3-bd7d-8ecc8bdee557.jpg)

#A Channel Auto Post (User)Bot To Forward All New Posts Of A Channel To Another!

Make sure to add bot to both/all the channel and promote, if you are using userbot you
just need to be admin in the `TO_CHANNEL`, and just join the `FROM_CHANNEL` channels to forward simple :)

### Session String 
<a href="https://replit.com/@darkempireslbots/DARKCHANNEL?v=1" target="_blank"><img src="https://img.shields.io/badge/run-session.py-red?style=for-the-badge&logo=repl.it" alt="generate_string" /></a>    

You can Also use [@darkStringGenBot](https://t.me/darkStringGenBot) and get a Telethon session

### Installation Guide:
<details>
<summary>Local</summary>
<br>
  
#### The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/DARKEMPIRESL/ChannelAutoPost
cd ChannelAutoPost
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create Config.py with variables as given below>
python3 -m ChannelAutoPost
```

An example `Config.py` file could be:

**Not All of the variables are mandatory**

__The (User)bot should work by setting only the first three variables__

```python3
from heroku_config import Var

class Config(Var):
  APP_ID = 6
  API_HASH = "eb06xxxxxxxxxxxx"
  BOT_TOKE = "1234567890:xxxxxxxxxxxx"  
```
</details>

<details>
<summary>Heroku</summary>
<br>
  
#### Heroku Configuration
  
Simply just leave the Config as it is.

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/DARKEMPIRESL/ChannelAutoPost)

#### Mandatory Vars

- Only three of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
- 
</details>

## Disclaimer:
```
    	Improper use may lead to ban.
    	I am not responsible if you misuse this bot.
      
```
## Credits:
>> [Lonami](https://github.com/LonamiWebs), for [Telethon](https://github.com/LonamiWebs/Telethon)
