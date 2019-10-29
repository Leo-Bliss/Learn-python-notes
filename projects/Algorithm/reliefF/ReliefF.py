#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time    :    2019/10/28 0028 16:26
#@Author  :    tb_youth
#@FileName:    RelifF.py
#@SoftWare:    PyCharm
#@Blog    :    https://blog.csdn.net/tb_youth




from __future__ import print_function
import numpy as np
from sklearn.neighbors import KDTree
from sklearn.preprocessing import minmax_scale
from scipy.spatial.distance import euclidean

class ReliefF1(object):
    """Feature selection using data-mined expert knowledge.

    Based on the ReliefF algorithm as introduced in:

    Kononenko, Igor et al. Overcoming the myopia of inductive learning algorithms with RELIEFF (1997), Applied Intelligence, 7(1), p39-55

    """

    def __init__(self, n_neighbors=100, n_features_to_keep=10):
        """Sets up ReliefF to perform feature selection.
        Parameters
        ----------
        n_neighbors: int (default: 100)
            The number of neighbors to consider when assigning feature importance scores.
            More neighbors results in more accurate scores, but takes longer.
        Returns
        -------
        None
        """

        self.feature_scores = None
        self.top_features = None
        self.tree = None
        self.n_neighbors = n_neighbors
        self.n_features_to_keep = n_features_to_keep

    def fit(self, X, y):
        """Computes the feature importance scores from the training data.
        Parameters
        ----------
        X: array-like {n_samples, n_features}
            Training instances to compute the feature importance scores from
        y: array-like {n_samples}
            Training labels
        Returns
        -------
        None
        """
        self.feature_scores = np.zeros(X.shape[1])
        self.tree = KDTree(X)

        for source_index in range(X.shape[0]):
            distances, indices = self.tree.query(X[source_index].reshape(1, -1), k=self.n_neighbors + 1)

            # First match is self, so ignore it
            for neighbor_index in indices[0][1:]:
                similar_features = X[source_index] == X[neighbor_index]
                label_match = y[source_index] == y[neighbor_index]

                # If the labels match, then increment features that match and decrement features that do not match
                # Do the opposite if the labels do not match
                if label_match:
                    self.feature_scores[similar_features] += 1.
                    self.feature_scores[~similar_features] -= 1.
                else:
                    self.feature_scores[~similar_features] += 1.
                    self.feature_scores[similar_features] -= 1.

        self.top_features = np.argsort(self.feature_scores)[::-1]

    def transform(self, X):
        """Reduces the feature set down to the top `n_features_to_keep` features.
        Parameters
        ----------
        X: array-like {n_samples, n_features}
            Feature matrix to perform feature selection on
        Returns
        -------
        X_reduced: array-like {n_samples, n_features_to_keep}
            Reduced feature matrix
        """
        return X[:, self.top_features[self.n_features_to_keep]]





class ReliefF2(object):
    """Feature selection using data-mined expert knowledge.
    Based on the ReliefF algorithm as introduced in:
    《 机器学习 》 - 周志华 - 第11章 特征选择与稀疏学习
    """

    def __init__(self, n_features_to_keep=10):
        """Sets up ReliefF to perform feature selection.
        Parameters
        ----------
        n_features_to_keep: int (default: 10)
            The number of top features (according to the ReliefF score) to retain after
            feature selection is applied.
        Returns
        -------
        None
        """

        self.feature_scores = None
        self.top_features = None
        self.n_features_to_keep = n_features_to_keep

    def _find_nm(self, sample, X):
        """Find the near-miss of sample

        Parameters
        ----------
        sample: array-like {1, n_features}
            queried sample
        X: array-like {n_samples, n_features}
            The subclass which the label is diff from sample
        Returns
        -------
        idx: int
            index of near-miss in X

        """
        dist = 100000
        idx = None
        for i, s in enumerate(X):
            tmp = euclidean(sample, s)
            if tmp <= dist:
                dist = tmp
                idx = i

        if dist == 100000:
            raise ValueError

        return idx

    def fit(self, X, y, scaled=True):
        """Computes the feature importance scores from the training data.
        Parameters
        ----------
        X: array-like {n_samples, n_features}
            Training instances to compute the feature importance scores from
        y: array-like {n_samples}
            Training labels
        scaled: Boolen
            whether scale X ro not
        Returns
        -------
        self.top_features
        self.feature_scores
        """
        if scaled:
            X = minmax_scale(X, feature_range=(0, 1), axis=0, copy=True)

        self.feature_scores = np.zeros(X.shape[1], dtype=np.float64)

        # The number of labels and its corresponding prior probability
        labels, counts = np.unique(y, return_counts=True)
        Prob = counts / float(len(y))

        for label in labels:
            # Find the near-hit for each sample in the subset with label 'label'
            select = (y == label)
            tree = KDTree(X[select, :])
            nh = tree.query(X[select, :], k=2, return_distance=False)[:, 1:]
            nh = (nh.T[0]).tolist()
            # print(nh)

            # calculate -diff(x, x_nh) for each feature of each sample
            # in the subset with label 'label'
            nh_mat = np.square(np.subtract(X[select, :], X[select, :][nh, :])) * -1

            # Find the near-miss for each sample in the other subset
            nm_mat = np.zeros_like(X[select, :])
            for prob, other_label in zip(Prob[labels != label], labels[labels != label]):
                other_select = (y == other_label)
                nm = []
                for sample in X[select, :]:
                    nm.append(self._find_nm(sample, X[other_select, :]))

                # print(nm)
                # calculate -diff(x, x_nm) for each feature of each sample in the subset
                # with label 'other_label'
                nm_tmp = np.square(np.subtract(X[select, :], X[other_select, :][nm, :])) * prob
                nm_mat = np.add(nm_mat, nm_tmp)

            mat = np.add(nh_mat, nm_mat)
            self.feature_scores += np.sum(mat, axis=0)
        # print(self.feature_scores)

        # Compute indices of top features, cast scores to floating point.
        self.top_features = np.argsort(self.feature_scores)[::-1]
        self.feature_scores = self.feature_scores[self.top_features]

        return self.top_features, self.feature_scores

    def transform(self, X):
        """Reduces the feature set down to the top `n_features_to_keep` features.
        Parameters
        ----------
        X: array-like {n_samples, n_features}
            Feature matrix to perform feature selection on
        Returns
        -------
        X_reduced: array-like {n_samples, n_features_to_keep}
            Reduced feature matrix
        """
        return X[:, self.top_features[:self.n_features_to_keep]]

    def fit_transform(self, X, y):
        """Computes the feature importance scores from the training data, then
        reduces the feature set down to the top `n_features_to_keep` features.
        Parameters
        ----------
        X: array-like {n_samples, n_features}
            Training instances to compute the feature importance scores from
        y: array-like {n_samples}
            Training labels
        Returns
        -------
        X_reduced: array-like {n_samples, n_features_to_keep}
            Reduced feature matrix
        """
        self.fit(X, y)
        return self.transform(X)

if __name__ =='__main__':
    f1 = ReliefF1()
    f2 = ReliefF2()

