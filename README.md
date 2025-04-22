# 🐶 Python OOP Challenge: Digital Pet

This project is a solution to the **Python OOP Challenge** where the task was to build a digital pet using Object-Oriented Programming concepts in Python.

## 🧠 Objective

The goal was to implement a `Pet` class with various attributes and methods to simulate interactions with a virtual pet.

---

## ✅ Features Implemented

### Pet Class Attributes
- `name`: Name of the pet
- `hunger`: Integer from 0 (full) to 10 (very hungry)
- `energy`: Integer from 0 (tired) to 10 (fully rested)
- `happiness`: Integer from 0 to 10

### Pet Class Methods
- `eat()`: Reduces hunger by 3 (min 0), increases happiness by 1
- `sleep()`: Increases energy by 5 (max 10)
- `play()`: Decreases energy by 2, increases happiness by 2, increases hunger by 1
- `get_status()`: Displays the pet's current status

### 🎯 Bonus Methods
- `train(trick)`: Teaches the pet a new trick and stores it
- `show_tricks()`: Displays all tricks the pet has learned

---

## 🧪 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Inst3p428/OOP-PYTHONCHALLENGE552.git

   cd OOP-PYTHONCHALLENGE552
2. Run the program:
   ```bash
   python main.py
## 🖥️ Sample Output
```bash
Pet name: Buddy
Hunger: 2
Energy: 7
Happiness: 9
Tricks: ['Sit', 'Roll Over']

