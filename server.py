"""Aplikasi web Flask untuk analisis sentimen."""
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Inisialisasi aplikasi Flask
app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """Menerima teks dari antarmuka web dan mengembalikan hasil sentimennya."""
    # Ambil teks dari permintaan GET (nama parameter sesuai mywebscript.js)
    text_to_analyze = request.args.get('textToAnalyze')

    # Panggil aplikasi analisis sentimen
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']

    # Jika input tidak valid, label bernilai None
    if label is None:
        return "Input tidak valid! Coba lagi."

    # 'SENT_POSITIVE' menjadi 'POSITIVE'
    label = label.split('_')[1]

    return f"Teks yang diberikan telah diidentifikasi sebagai {label} dengan skor {score}."


@app.route("/")
def render_index_page():
    """Menampilkan halaman utama."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
