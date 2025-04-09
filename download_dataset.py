import os
import requests
import zipfile
import io

def download_dataset():
    """
    Netflix veri setini Kaggle'dan indirir ve çıkarır.
    """
    print("Veri seti indiriliyor...")
    
    # Kaggle API kimlik bilgileri
    KAGGLE_USERNAME = "KULLANICI_ADINIZ"  # Kaggle kullanıcı adınızı girin
    KAGGLE_KEY = "API_ANAHTARINIZ"  # Kaggle API anahtarınızı girin
    
    # Veri seti URL'si
    dataset_url = "https://www.kaggle.com/datasets/shivamb/netflix-shows/download"
    
    try:
        # İndirme isteği
        response = requests.get(
            dataset_url,
            auth=(KAGGLE_USERNAME, KAGGLE_KEY),
            stream=True
        )
        
        # ZIP dosyasını çıkarma
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(".")
            
        print("Veri seti başarıyla indirildi ve çıkarıldı!")
        
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")
        print("\nAlternatif olarak, veri setini manuel olarak indirebilirsiniz:")
        print("1. https://www.kaggle.com/datasets/shivamb/netflix-shows adresine gidin")
        print("2. 'Download' butonuna tıklayın")
        print("3. İndirilen ZIP dosyasını proje klasörüne çıkarın")

if __name__ == "__main__":
    download_dataset() 