## Auction Program

____

This is a simple Python auction program that allows multiple bidders to submit bids, then determines the winner with the highest bid.

### Features

- Allows users to submit their names and bids.
- Accepts only numeric values for bids.
- Supports multiple bidders.
- Automatically clears the console after each bidder's entry (simulated by adding new lines).
- At the end of the bidding process, it announces the winner with the highest bid.

### Usage

1. When the program starts, the logo (or art) will be displayed.
2. Users will be prompted to enter their name and bid.
3. If the bid is not a numeric value, the program will ask for a valid input.
4. After each bid, the console will be cleared for the next user.
5. Once all bidders have entered their bids, the program will announce the winner with the highest bid.

### Example

Here's an example of how the program works:

```bash
What is your name? Alice
What is your bid? 100
Are there any other bidders? Type 'yes' or 'no': yes
What is your name? Bob
What is your bid? 150
Are there any other bidders? Type 'yes' or 'no': no

The winner is Bob with a bid of 150
```
### Modifying the Logo

You can modify the `logo` by replacing it in the code. It's simply a string of ASCII art that gets printed at the start of the program
