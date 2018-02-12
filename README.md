Label Propagation
============================================
<p align="justify">
GEMSEC is a graph embedding algorithm which learns an embedding and clustering jointly. The procedure places nodes in an abstract feature space where the vertex features minimize the negative log likelihood of preserving sampled vertex neighborhoods while the nodes are clustered into a fixed number of groups in this space. GEMSEC is a general extension of earlier work in the domain as it is an augmentation of the core optimization problem of sequence based graph embedding procedures and it is agnostic of the neighborhood sampling strategy
</p>

This repository provides a reference implementation for Label Propagation.

### Requirements

The codebase is implemented in Python 2.7. package versions used for development are just below.
```
networkx          1.11
tqdm              4.19.5
numpy             1.13.3
pandas            0.20.3
jsonschema        2.6.0
```

### Datasets

The code takes an input graph in a csv file. Every row indicates an edge between two nodes separated by a comma. The first row is a header. Nodes should be indexed starting with 0. Sample graphs for the `Facebook Politicians` dataset is included in the  `data/` directory.

### Options

Learning of the embedding is handled by the `src/label_propagation.py` script which provides the following command line arguments.

#### Model options

```
  --input STR                Input graph path.                          Default is `data/politician_edges.csv`.                                     
  --assignment-output STR    Node-cluster assignment dictionary path.   Default is `output/politician.json`.
  --weighing STR             Weighting strategy.                        Default is `overlap`.
  --rounds INT               Number of iteations.                       Default is 30.
  --seed INT                 Initial seed           .                   Default is 42.
```

### Examples

The following commands learn a graph embedding and cluster center and writes them to disk. The node representations are ordered by the ID.

Creating a GEMSEC embedding of the default dataset with the default hyperparameter settings. Saving the embedding, cluster centres and the log file at the default path.

```
python src/label_propagation.py
```
Creating a DeepWalk embedding of the default dataset with the default hyperparameter settings. Saving the embedding, cluster centres and the log file at the default path.

```
python src/label_propagation.py --weighting unit
```

Turning off the model saving.

```
python src/label_propagation.py --seed 32
```

Creating an embedding of an other dataset the `Facebook Companies`. Saving the output and the log in a custom place.

```
python src/embedding_clustering.py --rounds 100
```
