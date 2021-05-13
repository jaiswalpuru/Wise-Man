# GURU
<p align="center">
    <img src="https://github.com/jaiswalpuru/discord_bots/blob/main/wise_man/images/guru.png" alt="Logo" width="400" height="200" style="border-radius:10%">
</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
* pip
  ```sh
  python -m pip install -U pip
  ```
* discord
  ```sh
  pip install discord.py
  ```    
* dotenv
  ```sh
  pip install python-dotenv
  ```    
### Installation

1. Get a free TOKEN Key at discord developers portal.
2. Clone the repo
   ```sh
   git clone https://github.com/jaiswalpuru/discord_bots.git
   ```
3. Create a .env file inside the cloned folder
   ```sh
   touch .env
   ```
4. Enter your TOKEN value, and all the Channel ID's which will be used
   ```sh
   TOKEN = 'ENTER YOUR TOKEN'
   TRACKER_CHANNEL_ID = 'VALUE' # Channel where user entering and leaving channel will be tracked.
   WELCOME_CHANNEL_ID = 'VALUE' # Channel for welcoming user.
   ```

### Run 
```sh
   python3 guru.py
   ```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/jaiswalpuru/discord_bots/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.
