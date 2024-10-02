In einem Convolutional Neural Network (CNN) beziehen sich "Pooling" und "Max Pooling" auf Techniken zur Reduktion der Dimensionen der Feature Maps (den Ausgabedaten) nach der Anwendung von Convolution-Schichten. Diese Techniken tragen dazu bei, die Berechnungen effizienter zu machen, Überanpassung zu reduzieren und das Netzwerk robuster gegenüber kleinen Variationen in den Daten zu machen.

### 1. **Pooling**
Pooling ist eine Methode zur Reduktion der Größe von Feature Maps, die nach einer Convolution-Schicht in einem CNN entstehen. Es wird auch als "Subsampling" oder "Downsampling" bezeichnet. Der Hauptzweck von Pooling ist:
   - Reduktion der Abmessungen der Feature Maps (Höhe und Breite), während wichtige Informationen beibehalten werden.
   - Verbesserung der Netzwerkleistung, indem die Berechnungen reduziert und Überanpassungen verringert werden.
   - Erhöhung der Translation Invariance, d. h., das Netzwerk wird weniger empfindlich gegenüber leichten Verschiebungen oder Verzerrungen in den Eingabedaten.

Pooling wird normalerweise durch das Definieren eines Fensters (z. B. 2x2 oder 3x3) angewendet, das über die Feature Map gleitet. Innerhalb jedes Fensters wird eine Aggregationsfunktion verwendet, um die Informationen zusammenzufassen.

### 2. **Max Pooling**
Max Pooling ist eine spezifische Art des Pooling, bei der der **Maximalwert** in jedem Pooling-Fenster gewählt wird. Hierbei wird der größte Wert aus jeder Region extrahiert und als repräsentativer Wert für diese Region verwendet.

Beispiel für 2x2 Max Pooling:
- Nehmen wir an, wir haben ein 2x2-Fenster auf der Feature Map. Für jeden Bereich des Fensters wird der maximale Wert ausgewählt.
- Angenommen, eine 4x4-Feature Map hat die Werte:
  ```
  [ [1, 3, 2, 4],
    [5, 6, 1, 2],
    [7, 2, 9, 0],
    [3, 8, 1, 5] ]
  ```
  Nach 2x2 Max Pooling wird die Ausgabematrix (2x2) folgende Werte enthalten:
  ```
  [ [6, 4],
    [8, 9] ]
  ```
  Hier wurde aus jedem 2x2-Bereich der Maximalwert gewählt.

### Zweck von Max Pooling:
   - **Reduktion der Anzahl der Parameter:** Durch Verkleinerung der Feature Map reduziert sich die Anzahl der Neuronen im nächsten Layer.
   - **Überanpassungsvermeidung:** Weniger Parameter bedeuten weniger Risiko, dass das Modell Überanpassungen (Overfitting) auf den Trainingsdaten zeigt.
   - **Robustheit gegenüber Verschiebungen:** Da nur der Maximalwert verwendet wird, ist das Modell weniger anfällig für kleine Verschiebungen oder Transformationen der Eingabedaten.

### Unterschiedliche Pooling-Methoden:
Neben Max Pooling gibt es auch andere Pooling-Methoden:
   - **Average Pooling:** Statt den Maximalwert zu nehmen, wird der Durchschnitt der Werte im Fenster berechnet.
   - **Global Pooling:** Ein Pooling-Fenster, das die gesamte Feature Map abdeckt, wodurch die Ausgabe auf eine einzige Zahl pro Feature reduziert wird (wird häufig in den letzten Schichten von CNNs verwendet).

### Fazit:
- **Pooling** reduziert die Größe der Feature Maps, indem es nur die wichtigsten Informationen extrahiert.
- **Max Pooling** ist eine spezielle Methode, bei der der Maximalwert aus jedem Fenster genommen wird.
