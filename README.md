# Track 2: Intent Induction from Conversations for Task-Oriented Dialogue

## People

- TBD

## Task Proposal and Track Website

- Task Proposal: [https://drive.google.com/file/d/1B2YBtWaLJU5X3uudSZEaOyNWQ_QoTZLG/view](https://drive.google.com/file/d/1itlby2Ypq3sRVtOY1alr3ygjPZZdB2TT/view)
- Track Website: [https://chateval.org/dstc10 ](https://github.com/amazon-research/dstc11-track2-intent-induction)

## Metric

### Task 1

- Normalized Mutual Information (NMI)

  - Clustering Metric
  - $NMI = \displaystyle\frac{I(X;Y)}{min(H(X), H(Y))}$
  - where, $X$ denotes Reference labels and $Y$ stands for clustered labels
  - https://process-mining.tistory.com/141


- Accuracy (ACC)

  - Clustering Metric
  - $ACC = \displaystyle\frac{\text{The num of aligned == ref}}{\text{The num of ref}} \text{\(if ref else 0\)}$


### Task 2

- Adjusted Rand Index (ARI)

  - Rand Index: https://taeguu.tistory.com/52
  - Adjusted Rand Index (ARI): 
    - https://taeguu.tistory.com/53?category=829266
    - https://p829911.github.io/2019/01/05/clustering/


- Intent Classification F1-Score (Clustering F1)

  - Prediction-Based Metric
  - Precision: a many-to-one alignment is computed from *cluster* labels to *reference* labels such that the number of correct aligned labels is maximized. 
  - Recall: a many-to-one alignment is computed from *reference* labels to *cluster* labels such that the number of correct aligned labels is maximized.
  - $F1 = \frac{\text{2 * precision * recall}}{\text{precision + recall}}$


- Intent Example Coverage

  - Coverage Metric
  - Example Coverage is defined as percent of examples whose reference intent has a corresponding predicted cluster after performing a many-to-one alignment from predicted clusters to reference clusters.
