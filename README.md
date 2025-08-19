#  MediaPipe El Takip Projesi (Hand Tracking Project)

Bu proje, Python'da popüler görüntü işleme kütüphaneleri olan OpenCV ve MediaPipe'i kullanarak gerçek zamanlı el tespiti ve takibi yapar. Kamera akışından anlık olarak elleri algılar, kilit noktalarını (landmarks) belirler ve bunları görsel olarak ekranda gösterir.

##  Özellikler

-   **Gerçek Zamanlı El Tespiti ve Takibi:** Kamera görüntüsündeki elleri anlık olarak algılar ve konumlarını takip eder.
-   **Kilit Noktası Tespiti:** Her bir el için 21 adet anahtar kilit noktasının koordinatlarını bulur.
-   **Görselleştirme:** Tespit edilen el iskeletini, noktalarını ve bu noktaları birleştiren çizgileri kamera görüntüsü üzerine çizer.
-   **Nokta ID Numaraları:** Her bir kilit noktasının üzerine, görsel referans sağlamak için ID numarasını yazar.
-   **Performans Göstergesi:** Uygulamanın anlık işlem hızını (`FPS - Frames Per Second`) ekranda gösterir.

##  Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız vardır:

-   `opencv-python`
-   `mediapipe`

Tüm bağımlılıkları tek bir komutla kurmak için `requirements.txt` dosyasını kullanabilirsiniz.

##  Kurulum

1.  Projeyi indirin veya klonlayın:
    ```bash
    git clone [https://github.com/KullaniciAdiniz/DepoAdiniz.git](https://github.com/KullaniciAdiniz/DepoAdiniz.git)
    cd DepoAdiniz
    ```

2.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

##  Kullanım

Projeyi çalıştırmak için terminalden aşağıdaki komutu girin:

```bash
python main.py
