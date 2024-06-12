<h2>KI-Bilderkennung im Unterricht einsetzen</h2>
<h4>Erste Phase</h4>
<p>Es wird an einem einfachen Beispiel die Funktionsweise der Bilderkennung durch ein trainiertes KI-Modell erklärt. Zur Modellbildung wird das Onlinetool  <a href="https://teachablemachine.withgoogle.com/"><b>Teachable Machine</b></a> genutzt. Um das Modell zu trainieren benötigt <b>Teachable Machine</b> Beispielbilder. Ich habe dazu Blätter von 4 Laubbäumen fotogrfiert oder eingescannt. Pro Baumart sollten es mindestens 5 Bilder sein. Weiterhin sollten sich die Bilder der unterschiedlichen Baumsorten deutlich unterscheiden.</p>
<p>Ich habe Bilder von diesen vier Baumarten verwendet.</p>
  <ul>
    <li>Stieleiche</li>
    <li>Kastanie</li>
    <li>Buche</li>
    <li>???</li>
  </ul>
  <p>Die Bilder befinden sich im Ordner: <a href="https://github.com/HaraldRau/Bilderkennung/tree/main/Trainingsbilder"><b>Trainingsbilder</b></a></p>
  <h4>Zweite Phase</h4>
<p>In einer zweiten Phase kann das KI-Modell aus <b>Teachable</b> Machine auf lokalen Systemen offline genutzt werden. Dazu wird mit dem Pythonmodul <a href="https://de.wikipedia.org/wiki/Keras">Keras</a> auf das Framework <a href="https://de.wikipedia.org/wiki/TensorFlow">TensorFlow</a> zugeriffen. Sie müssen nichts programmieren, das relativ übersichtliche Programm <a href="https://github.com/HaraldRau/Bilderkennung/blob/8c23a8d014962fdc6be4e6179d15725e47774308/baumarten.py">baumerkennung.py</a> wurde in Python geschrieben und steht hier mit dem Beispielmodell zum <a href="https://github.com/HaraldRau/Bilderkennung/archive/refs/heads/main.zip">Download</a> bereit.</p>
<h4>Zu installierende Software</h4>
<p>Um den Beispielcode auszuführen, ist folgende Software auf dem PC zu installieren:</p>
<b>Programmiersprache Python</b>
<ul>
<li>Python 3 mit dem Installationsmodul pip</li>
</ul>
<p>Anleitung für Windows: https://learn.microsoft.com/de-de/windows/python/beginners</p>
<b>Python Module über CMD in der Windows Konsole [„Windows-Taste“ + „R“]</b>
<ul>
<li>pip install keras</li>
<li>pip install opencv-python</li>
<li>pip install numpy</li>
</ul>
