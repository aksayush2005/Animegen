# **AnimeGen**  
**Convert stories into anime-style scenes using AI**  

## **Installation**  

### **1. Clone the Repository**  
```sh
git clone https://github.com/ABarpanda/Animegen.git
cd animegen
```

### 2. Install Dependencies
Install the required dependencies from requirements.txt:

```sh
pip install -r requirements.txt
```

### 3. Set Up a Virtual Environment (Optional but Recommended)
To avoid conflicts with other Python projects, you can set up a virtual environment:

```sh
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies within the virtual environment
pip install -r requirements.txt
```

## Usage
#### 1. Prepare Your Story

Write your story in the story.txt file located in the root directory of the project.

#### 2. Run the Script
Run the src/main.py script to generate anime-style scenes from your story:

```sh
python src/main.py
```
#### 3. View the Output
The generated anime-style scenes will be saved in the output/ directory.
```
Project Structure
animegen/
├── story.txt                # Input story file
├── requirements.txt         # List of dependencies
├── src/
│   └── main.py              # Main script to generate anime scenes
├── output/                  # Directory for generated scenes
└── README.md                # Project documentation
```
### Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.

Create a new branch for your feature or bugfix.

Submit a pull request with a detailed description of your changes.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments
Thanks to Hugging Face for providing pre-trained models.

Inspired by the growing interest in AI-generated art and storytelling.
