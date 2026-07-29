# 🎬 AI Movie Recommendation System

An AI-powered **Movie Recommendation System** built using **Python**, **Machine Learning**, **Scikit-learn**, and **Streamlit**. The application recommends movies based on content similarity and displays real-time movie posters using the **TMDB API**.

---

## 🚀 Live Demo

🌐 **Website:**  
https://ai-movie-recommendation-system-k7qez2kktppy2zhdwzcbrf.streamlit.app/

---

## 💻 GitHub Repository

🔗 **Repository:**  
https://github.com/sharadverma6306/ai-movie-recommendation-system

---

## 📌 Features

- 🎥 Content-Based Movie Recommendation
- 🤖 Machine Learning Powered Recommendations
- 📝 NLP-based Movie Tag Processing
- 📊 Cosine Similarity Recommendation Engine
- 🖼️ Real-Time Movie Posters using TMDB API
- ⚡ Fast and Interactive Streamlit Interface
- 🌐 Fully Deployed on Streamlit Cloud

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Requests
- Pickle
- TMDB API

---

## 📂 Project Structure

```
ai-movie-recommendation-system/
│
├── model/
│   └── movies.pkl
│
├── app.py
├── train.py
├── recommend.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

1. Load the movie dataset.
2. Merge movie metadata into a single feature.
3. Preprocess text using NLP techniques.
4. Convert movie tags into numerical vectors using **CountVectorizer**.
5. Compute similarity using **Cosine Similarity**.
6. Recommend the top 5 most similar movies.
7. Fetch movie posters dynamically using the **TMDB API**.

---

## 📸 Application Preview

### Home Page

Select a movie from the dropdown and click **Recommend** to get similar movie suggestions.

### Recommendation Results

The application displays:

- Movie Poster
- Movie Title
- Top 5 Similar Movies

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/sharadverma6306/ai-movie-recommendation-system.git

cd ai-movie-recommendation-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 🧠 Machine Learning Approach

This project uses a **Content-Based Filtering** recommendation system.

The recommendation model analyzes movie information such as:

- Genres
- Keywords
- Cast
- Crew
- Overview

These features are combined into tags and converted into vectors using **CountVectorizer**. The similarity between movies is then calculated using **Cosine Similarity**, allowing the application to recommend movies with similar content.

---

## 🌐 TMDB API

Movie posters are fetched dynamically using the **The Movie Database (TMDB) API**.

API Documentation:
https://developer.themoviedb.org/docs

---

## 🔮 Future Improvements

- User Authentication
- Search by Actor
- Search by Genre
- Movie Ratings
- Trailer Integration
- Collaborative Filtering
- Hybrid Recommendation System
- Personalized Recommendations

---

## 👨‍💻 Developer

**Sharad Verma**

- GitHub: https://github.com/sharadverma6306
- LinkedIn: https://www.linkedin.com/in/sharadverma6306/

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub!

---

## 📄 License

This project is created for educational and learning purposes.