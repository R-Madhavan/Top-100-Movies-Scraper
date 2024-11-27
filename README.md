Here’s a professional and detailed `README.md` for your GitHub project:

---

# 🎥 Top 100 Movies Scraper

This Python project scrapes the **Top 100 Movies** from [Empire's Best Movies List](https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/) and saves them to a text file. It includes error handling for character encoding issues to ensure movie titles are properly displayed.

---

## 🚀 Features
- Scrapes the **Top 100 Movies** from a web page.
- Reverses the movie order to match rankings.
- Fixes character encoding issues (e.g., special characters like `–`).
- Saves the cleaned and sorted list to a `movies.txt` file.

---

## 🛠️ Installation

### Prerequisites
- Python 3.7+
- Required libraries:
  - `requests`
  - `beautifulsoup4`

Install the required libraries with:

```bash
pip install requests beautifulsoup4
```

---

## 📄 Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/top-100-movies-scraper.git
   cd top-100-movies-scraper
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. The list of movies will be saved in a file named `movies.txt` in the project directory.

---

## 📝 Output Example
The script saves the following content to `movies.txt`:

```
1) The Shawshank Redemption
2) The Godfather
3) The Dark Knight
...
59) E.T. – The Extra Terrestrial
...
100) The Wizard of Oz
```

---

## 🌟 Project Structure

```
top-100-movies-scraper/
├── main.py        # Main Python script for scraping and saving movies
├── movies.txt     # Output file containing the top 100 movies (generated after running the script)
└── README.md      # Project documentation
```

---

## 🐛 Known Issues
- This project relies on a web archive URL. If the webpage changes or becomes unavailable, scraping may fail.
- The project assumes all `<h3>` tags with the class `title` contain movie names.

---

## 📚 Learnings
- Web scraping with `requests` and `BeautifulSoup`.
- Handling text encoding issues (`UnicodeEncodeError`).
- File handling and saving data in Python.

---

## 🤝 Contribution
Contributions are welcome! Feel free to open an issue or submit a pull request.

---
