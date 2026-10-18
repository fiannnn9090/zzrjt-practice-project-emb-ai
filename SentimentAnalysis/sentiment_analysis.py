"""Modul analisis sentimen berbasis pustaka Watson NLP (model BERT)."""
import json

import requests


def sentiment_analyzer(text_to_analyse):
    """Menganalisis sentimen sebuah teks.

    Mengembalikan dictionary dengan kunci 'label' dan 'score'.
    Jika teks tidak valid (status 500), keduanya bernilai None.
    """
    # URL layanan analisis sentimen
    url = (
        'https://sn-watson-sentiment-bert.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/SentimentPredict'
    )
    # Membangun payload permintaan dalam format yang diharapkan
    myobj = {"raw_document": {"text": text_to_analyse}}
    # Header kustom yang menentukan ID model untuk layanan analisis sentimen
    header = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }
    # Mengirim permintaan POST ke API analisis sentimen
    response = requests.post(url, json=myobj, headers=header, timeout=10)

    if response.status_code == 200:
        # Respons berhasil: ambil label dan skor
        formatted_response = json.loads(response.text)
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    else:
        # Teks tidak valid (status 500) atau kesalahan lain
        label = None
        score = None

    # Mengembalikan kamus yang berisi hasil analisis sentimen
    return {'label': label, 'score': score}
