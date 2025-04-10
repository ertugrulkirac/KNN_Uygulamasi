Senaryo: Diyabet Teşhisi

Hasta No	   Glikoz Seviyesi	    Vücut Kitle İndeksi (BMI)	    Yaş	      Diyabet Var mı?
   1	            130                       28.1	              45	            Evet
   2               85	                      22.4	              30	            Hayır
   3	            155	                      35.0	              50	            Evet
   4	             90	                      21.0	              25	            Hayır

Şimdi yeni bir hasta geldi ve:

Glikoz: 140

BMI: 30.2

Yaş: 48

Soru: Bu hasta diyabet olabilir mi?
K-NN algoritması ne yapar?

Yeni hastanın verisini alır.

Eğitim verisindeki en yakın K komşuyu bulur (örneğin K=3).

Bu 3 komşudan kaçı “Evet” diyorsa, sonucu o şekilde tahmin eder.

Örneğin, 3 en yakın komşudan 2’si "Evet", 1’i "Hayır" diyorsa:

Tahmin: Evet, bu hasta diyabet olabilir.

