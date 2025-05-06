# Coffee Machine Project

This project was developed as part of the **"100 Days of Code"** Python course. It simulates a virtual coffee machine that manages beverage availability based on ingredient stock levels and handles payments using different currency denominations such as dollars, cents, and pennies.

##  Project Objective

To build a Python program that:
 Offers a selection of coffee drinks (e.g., espresso, latte, cappuccino)
 Tracks and updates ingredient inventory based on orders
 Accepts payment and validates if sufficient funds are provided
 Calculates and returns change when necessary
 Notifies users when ingredients are insufficient for a selected drink

## 🛠 Technologies Used

  **Python** (standard library)
  **Functions** for modular design
  **Dictionaries** for menu and inventory management
  **Conditional Logic** to process user input and control the coffee machine flow

##  Features

- Menu with drink options and their ingredient requirements
- Real-time inventory check before processing orders
- Currency input handling (dollars, quarters, dimes, nickels, pennies)
- Refunds for insufficient payments
- Option to generate a status report of current resources and money collected

##  Sample Program Flow

1. User selects a coffee type
2. Program checks if enough ingredients are available
3. User inserts coins
4. If payment is sufficient:
   - Drink is dispensed
   - Ingredients are deducted
   - Change is returned (if applicable)
5. If not, the money is refunded and the order is canceled
