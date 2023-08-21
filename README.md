# Pedalbus

Dati di input:
1. gli indirizzi di n bambini (un bambino per indirizzo)
2. l’indirizzo della scuola.
Determinare il numero **minimo** di percorsi che partono dalla casa di un bambino e terminano alla scuola passando da altre case, in modo tale che: ogni bambino i sia parte di ex 1 percorso e la durata del suo percorso tra la propria casa e la scuola sia non superiore a δ volte la sua distanza minima dalla scuola (es. δ=1.5).

*Suggerimento: lavorare sul grafo astratto completo, i cui nodi sono gli indirizzi di casa e il costo degli archi è la durata del percorso minimo nodo-nodo sulla rete stradale.*
## Istruzioni per l'uso

> [!IMPORTANT]
> - Assicurarsi di stare lavorando sempre alla versione corrente del codice 
> - Installare nel proprio ambiente virtuale le dipendenze attraverso il comando
> ```python
> pip install -r requirements.txt
> ```
> - Se sono state aggiunte librerie ricordarsi di fare append nel file `requirements.txt`

Nella cartella [src](src) è presente il codice **definitivo** del progetto.

Nella cartella [test](test) vanno inseriti i file di prova o comunque che non sono legati a qualche chiamata nel main, come ad esempio il [generatore pseudo-casuale di istanze](test/generator.py). 

## TODO

- [ ] Questo è un esempio di TODO

## Authors

- Nicolò Salvi :duck:
- Giacomo Manzoli
