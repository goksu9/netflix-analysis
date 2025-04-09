import os
import requests
import zipfile
import io
import json
from pathlib import Path

def setup_kaggle_credentials():
    """
    Kaggle API kimlik bilgilerini ayarlar.
    """
    kaggle_dir = Path.home() / '.kaggle'
    kaggle_dir.mkdir(exist_ok=True)
    
    credentials = {
        "username": "goksuhacolu",
        "key": "b7f3e70c59afd0322f192891cbdb617c"
    }
    
    with open(kaggle_dir / 'kaggle.json', 'w') as f:
        json.dump(credentials, f)
    
    # Dosya izinlerini ayarla
    os.chmod(kaggle_dir / 'kaggle.json', 0o600)

def download_dataset():
    """
    Netflix veri setini Kaggle'dan indirir ve çıkarır.
    """
    print("Veri seti indiriliyor...")
    
    try:
        # Kaggle kimlik bilgilerini ayarla
        setup_kaggle_credentials()
        
        # Kaggle API'yi kullanarak veri setini indir
        os.system('kaggle datasets download -d shivamb/netflix-shows')
        
        # ZIP dosyasını çıkar
        with zipfile.ZipFile('archive.zip', 'r') as zip_ref:
            zip_ref.extractall('.')
            
        print("✅ Veri seti başarıyla indirildi ve çıkarıldı!")
        
    except Exception as e:
        print(f"❌ Hata oluştu: {str(e)}")
        print("\nAlternatif olarak, veri setini manuel olarak indirebilirsiniz:")
        print("1. https://www.kaggle.com/datasets/shivamb/netflix-shows adresine gidin")
        print("2. 'Download' butonuna tıklayın")
        print("3. İndirilen ZIP dosyasını proje klasörüne çıkarın")

if __name__ == "__main__":
    # Gerekli kütüphaneleri kontrol et
    try:
        import kaggle
    except ImportError:
        print("Kaggle API yükleniyor...")
        os.system('pip install kaggle')
    
    download_dataset() 