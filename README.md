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
  --input STR                   Input graph path.                                 Default is `data/politician_edges.csv`.                                      Default is `output/logs/politician.log`.
  --assignment-output STR       Node-cluster assignment dictionary path.          Default is `output/assignments/politician.json`.
  --initial-learning-rate FLOAT   Initial learning rate.                                        Default is 0.001.
  --minimal-learning-rate FLOAT   Final learning rate.                                          Default is 0.0001.
  --annealing-factor FLOAT        Annealing factor for learning rate.                           Default is 1.0.
  --initial-gamma FLOAT           Initial clustering weight coefficient.                        Default is 0.1.
  --lambd FLOAR                   Smoothness regularization penalty.                            Default is 0.0625.
  --cluster-number INT            Number of clusters.                                           Default is 20.
  --overlap-weighting STR         Weight construction technique for regularization.             Default is `normalized_overlap`.
  --regularization-noise FLOAT    Uniform noise max and min on the feature vector distance.     Default is 10**-8.
```

### Examples

The following commands learn a graph embedding and cluster center and writes them to disk. The node representations are ordered by the ID.

Creating a GEMSEC embedding of the default dataset with the default hyperparameter settings. Saving the embedding, cluster centres and the log file at the default path.

```
python src/embedding_clustering.py
```
Creating a DeepWalk embedding of the default dataset with the default hyperparameter settings. Saving the embedding, cluster centres and the log file at the default path.

```
python src/embedding_clustering.py --model DW
```

Turning off the model saving.

```
python src/embedding_clustering.py --dump-matrices False
```

Creating an embedding of an other dataset the `Facebook Companies`. Saving the output and the log in a custom place.

```
python src/embedding_clustering.py --input data/company_edges.csv  --embedding-output output/embeddings/company_embedding.csv --log-output output/cluster_means/company_means.csv --cluster-mean-output output/logs/company.json
```

Creating a clustered embedding of the default dataset in 32 dimensions, 20 sequences per source node with length 160 and 10 cluster centers.

```
python src/embedding_clustering.py --dimensions 32 --num-of-walks 20 --random-walk-length 160 --cluster-number 10
```
