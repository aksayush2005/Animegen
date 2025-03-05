# **AnimeGen**  
**Convert stories into anime-style scenes using AI**  

AnimeGen is an AI-powered tool that takes a written story as input, automatically splits it into meaningful scenes, and generates anime-style images for each scene. It then displays these images in a slideshow, creating a visual storytelling experience.  



https://github.com/user-attachments/assets/01dde7e3-760f-4b85-ba0d-cd8a1553d022



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

#### 4. Set Up API Keys
AnimeGen requires Pinecone for scene similarity calculations and Together AI for text-to-image generation.  

 **Create a Pinecone Index**  
1. Sign up at [Pinecone](https://www.pinecone.io/) and create an index named **`animegen`** with the following settings:  
   - **Metric**: Cosine  
   - **Dimension**: 384  
   - **Pod Type**: Starter (or higher)  

2. Get your Pinecone API key from the dashboard.  

**Get a Together AI API Key**  
1. Sign up at [Together AI](https://www.together.ai/) and generate an API key.  

**Store API Keys in `.env`**  
Create a `.env` file in the project root and add:  
```ini
PINECONE_ANIMEGEN_API_KEY=your_pinecone_api_key_here
TOGETHER_AI_API_KEY=your_together_ai_key_here
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
