# RPG Project in Python ⚔️  

This is a fully-featured RPG project developed in Python 🐍, leveraging the `pickle` library for data persistence 💾 and adhering to the MVC (Model-View-Controller) architecture 🏗️.  

---

## 📜 Project Description  

This RPG game immerses players in a virtual world 🌍 where they can create characters, explore dungeons, battle bosses, and progress through various challenges. The game automatically saves player data—such as character stats, inventory, and progress—using the `pickle` library, ensuring continuity across sessions 💾.  

The project is structured using the MVC architecture, which separates responsibilities into three distinct layers:  

- **Model (Data Layer)**:  
  Manages the game’s core data and logic, including characters, attributes, inventory, and game mechanics. ⚙️  

- **View (User Interface)**:  
  Provides an interactive user interface using `PySimpleGUI`, allowing players to interact with the game through menus, forms, and visual elements. 🎮  

- **Controller (Logic Layer)**:  
  Acts as the bridge between the model and view, handling game logic, user input, and interactions between components. 🤖  

---

## 🎮 Features  

- **Character Management**:  
  Players can create, customize, and manage their characters, choosing from different classes with unique abilities.  

- **Dungeon Exploration**:  
  Explore dungeons (companies) with varying levels of difficulty, conquer bosses, and earn rewards.  

- **Quizzes and Challenges**:  
  Test your knowledge and skills through quizzes to gain experience and unlock new opportunities.  

- **Ranking System**:  
  Compete with other players by climbing the leaderboard based on levels, dungeons conquered, and courses completed.  

- **Course System**:  
  Enroll in courses to improve your character’s skills and attributes, unlocking new abilities and opportunities.  

- **Battle System**:  
  Engage in strategic battles with bosses, using abilities, items, and tactics to emerge victorious.  

- **Data Persistence**:  
  All progress is saved automatically using the `pickle` library, ensuring a seamless experience across sessions.  

---

## 🛠️ Technologies Used  

- **Python**: Core programming language for the project.  
- **PySimpleGUI**: For creating an intuitive and interactive graphical user interface.  
- **Pickle**: For data serialization and persistence.  

---

## 📂 Project Structure  

The project is organized into the following directories:

acate-rpg/
├── controllers/       # Handles game logic and interactions
├── models/            # Defines data structures and core game logic
├── views/             # Manages the user interface and user output
├── dao/               # Data Access Objects for saving/loading data
├── assets/            # Static assets (images, icons, etc.)
├── exceptions/        # Custom exception classes for better error handling
main.py            # Entry point of the application
README.md          # Project documentation
*.pkl              # Serialized data files for persistence



---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/nickkcj/career-rpg.git
   cd acate-rpg
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game**
   ```bash
   python main.py
   ```