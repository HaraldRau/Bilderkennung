## **Convolutional Neural Networks**

"**Convolutional**" im Kontext eines Convolutional Neural Networks (CNN) bezieht sich auf die Anwendung des mathematischen Vorgangs der **Faltung (Convolution)**, der in den sogenannten **Convolutional Layers** stattfindet. Diese Faltung ist der zentrale Mechanismus, der es CNNs ermöglicht, lokale Muster und Merkmale in Bildern oder anderen mehrdimensionalen Daten zu erkennen.

### Was ist Faltung (Convolution)?

Faltung ist eine mathematische Operation, bei der ein kleinerer Filter (auch **Kern** oder **Kernel** genannt) über ein größeres Eingabebild "faltet" und einen neuen Wert berechnet, indem Werte im Bild mit den entsprechenden Werten im Filter multipliziert und aufsummiert werden. Der Filter extrahiert dabei spezifische Merkmale wie Kanten, Texturen oder andere Muster aus den Daten.

### Wie funktioniert Faltung in CNNs?

Die Faltung in CNNs erfolgt durch das Überlagern eines kleinen **Kernels** (z. B. 3x3 oder 5x5 Matrix) auf das Eingabebild oder eine vorherige Feature Map. Dann wird eine Operation durchgeführt, bei der die Pixelwerte unter dem Filterelement mit den Werten des Filters multipliziert und anschließend summiert werden. Dieses Verfahren wird über das gesamte Bild wiederholt, wobei der Filter "slided" (verschoben) wird, um die lokalen Informationen zu erfassen.

#### Schritte in der Faltung:
1. **Eingabe**: Ein Bild oder eine Feature Map (z. B. 2D-Matrix mit Pixelwerten).
2. **Kernel (Filter)**: Eine kleine Matrix (z. B. 3x3 oder 5x5), die die Faltungsoperation durchführt. Dieser Filter wird auf verschiedene Bereiche des Bildes angewendet.
3. **Berechnung**: An jeder Position des Bildes wird eine elementweise Multiplikation zwischen den Werten im Filter und den entsprechenden Pixelwerten durchgeführt, und die Ergebnisse werden summiert. Dies gibt einen neuen Wert für die Ausgabe-Feature-Map.
4. **Verschiebung (Stride)**: Der Filter wird um eine bestimmte Anzahl von Schritten über das Bild bewegt (z. B. um 1 oder 2 Pixel), um die nächste Berechnung durchzuführen.
5. **Ergebnis**: Eine neue Feature-Map, die die extrahierten Merkmale des Bildes enthält.

### Beispiel für Faltung:
Nehmen wir ein Beispiel mit einem 3x3-Filter und einem 5x5-Bild:

Eingabebild:
```
[1, 0, 1, 2, 1]
[0, 2, 1, 0, 1]
[1, 0, 2, 1, 0]
[2, 1, 0, 2, 1]
[1, 0, 1, 2, 0]
```

3x3-Filter (Kernel):
```
[1, 0, -1]
[1, 0, -1]
[1, 0, -1]
```

Der Filter wird über das Bild geschoben, und an jeder Position werden die Werte unter dem Filter mit dem Filter multipliziert und summiert, um einen neuen Wert zu erzeugen. Wenn wir das für verschiedene Positionen im Bild tun, erhalten wir eine neue Ausgabe (eine sogenannte Feature Map).

### Warum Convolution in CNNs wichtig ist:

1. **Erkennung lokaler Muster**: Convolutional Layers ermöglichen es CNNs, lokale Merkmale in den Daten zu erkennen. Zum Beispiel kann ein Filter Kanten, Linien oder Texturen erkennen.
   
2. **Parameterteilung**: Ein CNN verwendet denselben Filter (Kern) für alle Teile des Bildes, was die Anzahl der zu lernenden Parameter erheblich reduziert. Dies spart Rechenleistung und macht das Netzwerk effizienter.

3. **Translation Invariance**: Da der Filter über das gesamte Bild gleitet, kann das Netzwerk dieselben Merkmale an verschiedenen Positionen im Bild erkennen. Dies macht CNNs robust gegenüber Verschiebungen von Objekten im Bild.

4. **Hierarchische Merkmalsextraktion**: Mehrere Convolutional Layers hintereinander können immer komplexere Merkmale extrahieren. Die ersten Schichten lernen oft einfache Merkmale wie Kanten, während spätere Schichten komplexere Muster wie Formen und Objekte erkennen.

### Fazit:

Das Wort "**Convolutional**" in CNNs verweist auf die zentrale Operation, die Faltung, die es diesen Netzwerken ermöglicht, visuelle Merkmale effizient und skalierbar zu erkennen. Dies macht CNNs besonders gut geeignet für Anwendungen in der Bild- und Videoverarbeitung, da sie lokale Muster erfassen und daraus Merkmale auf unterschiedlichen Abstraktionsebenen lernen können.

## **Pooling**

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
