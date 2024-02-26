# Simple Discord Bot with Messaging Functionality

This repository contains a simple Discord bot with a messaging functionality. The bot is designed to showcase a basic implementation of a Discord bot using the `discord.py` library. Additionally, it actively displays its active time online within the bot's Discord description.

## Features

1. **Messaging Functionality:**
   - Responds to specific keywords with predefined messages.
   - Demonstrates the basic structure of handling messages in Discord.

2. **Active Time Display:**
   - The bot actively updates its presence to display the time it has been online.
   - Provides a real-time indication of the bot's activity within the Discord server.

## Getting Started

To run the bot, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/smazurs/basicBot
   ```

2. Install the required dependencies:

   ```bash
   pip install discord
   pip install python-dotenv
   ```

3. Create a `.env` file in the root directory with your Discord bot token:

   ```env
   DISCORD_TOKEN=your_token_here
   ```

## Dependencies

Make sure to install the required dependencies using the following commands:

```bash
pip install discord
pip install python-dotenv
```

## Example Usage

1. Invite the bot to your Discord server.

2. Use the following keyword to trigger a response from the bot:

   ```plaintext
   coin
   ```

   The bot will respond with a number from 1 to 6, using the randint function within responses.py

## Active Time Display

The bot actively updates its presence to display the time it has been online. This information is visible in the Discord server's member list when clickin on the bot.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or additional features you'd like to see, feel free to open an issue or submit a pull request.

## License

This project is licensed under "The Unlicense" License - see the [LICENSE](LICENSE) file for details.
