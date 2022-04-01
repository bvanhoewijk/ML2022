# Grid search outputs
## Linear model
```
Best parameters set found on training set:

{'C': 4, 'kernel': 'linear'}

Grid scores on training set:

0.540 for {'C': 1, 'kernel': 'linear'}
0.540 for {'C': 2, 'kernel': 'linear'}
0.540 for {'C': 3, 'kernel': 'linear'}
0.541 for {'C': 4, 'kernel': 'linear'}
0.541 for {'C': 5, 'kernel': 'linear'}
0.541 for {'C': 6, 'kernel': 'linear'}
0.540 for {'C': 7, 'kernel': 'linear'}
0.541 for {'C': 8, 'kernel': 'linear'}
0.541 for {'C': 9, 'kernel': 'linear'}
0.540 for {'C': 10, 'kernel': 'linear'}
0.541 for {'C': 100, 'kernel': 'linear'}
0.540 for {'C': 1000, 'kernel': 'linear'}
```

```
Detailed classification report:

LINEAR MODEL ACCURACY: 0.5475
```

## kNN model
```
Best parameters set found on training set:

{'n_neighbors': 70}

Grid scores on training set:

0.505 for {'n_neighbors': 1}
0.507 for {'n_neighbors': 2}
0.509 for {'n_neighbors': 3}
0.506 for {'n_neighbors': 4}
0.511 for {'n_neighbors': 5}
0.507 for {'n_neighbors': 6}
0.503 for {'n_neighbors': 7}
0.504 for {'n_neighbors': 8}
0.506 for {'n_neighbors': 9}
0.507 for {'n_neighbors': 10}
0.508 for {'n_neighbors': 11}
0.509 for {'n_neighbors': 12}
0.512 for {'n_neighbors': 13}
0.508 for {'n_neighbors': 14}
0.511 for {'n_neighbors': 15}
0.513 for {'n_neighbors': 16}
0.517 for {'n_neighbors': 17}
0.517 for {'n_neighbors': 18}
0.515 for {'n_neighbors': 19}
0.520 for {'n_neighbors': 20}
0.520 for {'n_neighbors': 21}
0.517 for {'n_neighbors': 22}
0.517 for {'n_neighbors': 23}
0.520 for {'n_neighbors': 24}
0.520 for {'n_neighbors': 25}
0.521 for {'n_neighbors': 26}
0.522 for {'n_neighbors': 27}
0.525 for {'n_neighbors': 28}
0.525 for {'n_neighbors': 29}
0.520 for {'n_neighbors': 30}
0.520 for {'n_neighbors': 31}
0.524 for {'n_neighbors': 32}
0.522 for {'n_neighbors': 33}
0.522 for {'n_neighbors': 34}
0.521 for {'n_neighbors': 35}
0.519 for {'n_neighbors': 36}
0.524 for {'n_neighbors': 37}
0.522 for {'n_neighbors': 38}
0.518 for {'n_neighbors': 39}
0.518 for {'n_neighbors': 40}
0.519 for {'n_neighbors': 41}
0.520 for {'n_neighbors': 42}
0.521 for {'n_neighbors': 43}
0.522 for {'n_neighbors': 44}
0.522 for {'n_neighbors': 45}
0.524 for {'n_neighbors': 46}
0.522 for {'n_neighbors': 47}
0.520 for {'n_neighbors': 48}
0.519 for {'n_neighbors': 49}
0.525 for {'n_neighbors': 50}
0.522 for {'n_neighbors': 51}
0.524 for {'n_neighbors': 52}
0.524 for {'n_neighbors': 53}
0.525 for {'n_neighbors': 54}
0.526 for {'n_neighbors': 55}
0.525 for {'n_neighbors': 56}
0.526 for {'n_neighbors': 57}
0.522 for {'n_neighbors': 58}
0.522 for {'n_neighbors': 59}
0.521 for {'n_neighbors': 60}
0.523 for {'n_neighbors': 61}
0.518 for {'n_neighbors': 62}
0.521 for {'n_neighbors': 63}
0.519 for {'n_neighbors': 64}
0.521 for {'n_neighbors': 65}
0.519 for {'n_neighbors': 66}
0.520 for {'n_neighbors': 67}
0.521 for {'n_neighbors': 68}
0.523 for {'n_neighbors': 69}
0.531 for {'n_neighbors': 70}
0.522 for {'n_neighbors': 71}
0.523 for {'n_neighbors': 72}
0.525 for {'n_neighbors': 73}
0.524 for {'n_neighbors': 74}
0.526 for {'n_neighbors': 75}
0.521 for {'n_neighbors': 76}
0.525 for {'n_neighbors': 77}
0.520 for {'n_neighbors': 78}
0.523 for {'n_neighbors': 79}
0.524 for {'n_neighbors': 80}
0.528 for {'n_neighbors': 81}
0.524 for {'n_neighbors': 82}
0.525 for {'n_neighbors': 83}
0.523 for {'n_neighbors': 84}
0.527 for {'n_neighbors': 85}
0.526 for {'n_neighbors': 86}
0.528 for {'n_neighbors': 87}
0.527 for {'n_neighbors': 88}
0.530 for {'n_neighbors': 89}
0.526 for {'n_neighbors': 90}
0.529 for {'n_neighbors': 91}
0.526 for {'n_neighbors': 92}
0.531 for {'n_neighbors': 93}
0.529 for {'n_neighbors': 94}
0.529 for {'n_neighbors': 95}
0.531 for {'n_neighbors': 96}
0.529 for {'n_neighbors': 97}
0.528 for {'n_neighbors': 98}
0.528 for {'n_neighbors': 99}
0.531 for {'n_neighbors': 100}
0.531 for {'n_neighbors': 101}
```

```
Detailed classification report:

KNN MODEL ACCURACY: 0.528
```

## Decision tree model
```
Best parameters set found on training set:

{'criterion': 'entropy', 'splitter': 'best'}

Grid scores on training set:

0.506 for {'criterion': 'gini', 'splitter': 'best'}
0.506 for {'criterion': 'gini', 'splitter': 'random'}
0.509 for {'criterion': 'entropy', 'splitter': 'best'}
0.506 for {'criterion': 'entropy', 'splitter': 'random'}
```

```
Detailed classification report:

DECISION TREE MODEL ACCURACY: 0.5115
```

# Random forest model
```
Best parameters set found on training set:

{'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 87}

Grid scores on training set:

0.508 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 10}
0.515 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 11}
0.510 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 12}
0.517 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 13}
0.513 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 14}
0.516 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 15}
0.506 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 16}
0.513 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 17}
0.514 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 18}
0.514 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 19}
0.520 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 20}
0.520 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 21}
0.512 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 22}
0.518 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 23}
0.514 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 24}
0.523 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 25}
0.523 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 26}
0.522 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 27}
0.522 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 28}
0.521 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 29}
0.528 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 30}
0.520 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 31}
0.525 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 32}
0.519 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 33}
0.525 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 34}
0.517 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 35}
0.522 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 36}
0.520 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 37}
0.520 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 38}
0.527 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 39}
0.520 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 40}
0.521 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 41}
0.524 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 42}
0.516 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 43}
0.523 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 44}
0.526 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 45}
0.520 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 46}
0.526 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 47}
0.527 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 48}
0.524 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 49}
0.522 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 50}
0.527 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 51}
0.521 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 52}
0.529 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 53}
0.523 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 54}
0.522 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 55}
0.521 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 56}
0.526 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 57}
0.528 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 58}
0.533 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 59}
0.525 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 60}
0.517 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 61}
0.523 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 62}
0.529 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 63}
0.532 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 64}
0.522 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 65}
0.521 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 66}
0.523 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 67}
0.533 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 68}
0.529 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 69}
0.522 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 70}
0.529 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 71}
0.532 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 72}
0.527 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 73}
0.526 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 74}
0.527 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 75}
0.529 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 76}
0.530 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 77}
0.528 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 78}
0.526 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 79}
0.524 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 80}
0.533 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 81}
0.519 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 82}
0.521 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 83}
0.528 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 84}
0.528 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 85}
0.526 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 86}
0.531 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 87}
0.527 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 88}
0.528 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 89}
0.530 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 90}
0.531 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 91}
0.526 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 92}
0.520 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 93}
0.534 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 94}
0.527 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 95}
0.525 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 96}
0.531 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 97}
0.521 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 98}
0.533 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 99}
0.528 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 100}
0.522 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 101}
0.528 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 102}
0.523 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 103}
0.524 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 104}
0.531 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 105}
0.530 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 106}
0.531 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 107}
0.531 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 108}
0.530 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 109}
0.529 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 110}
0.528 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 111}
0.516 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 112}
0.527 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 113}
0.530 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 114}
0.531 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 115}
0.531 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 116}
0.529 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 117}
0.527 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 118}
0.531 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 119}
0.521 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 120}
0.525 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 121}
0.532 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 122}
0.525 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 123}
0.528 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 124}
0.527 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 125}
0.529 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 126}
0.529 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 127}
0.533 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 128}
0.532 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 129}
0.522 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 130}
0.529 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 131}
0.536 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 132}
0.529 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 133}
0.532 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 134}
0.529 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 135}
0.526 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 136}
0.527 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 137}
0.536 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 138}
0.528 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 139}
0.535 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 140}
0.532 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 141}
0.531 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 142}
0.529 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 143}
0.527 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 144}
0.538 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 145}
0.526 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 146}
0.532 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 147}
0.522 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 148}
0.528 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 149}
0.528 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 150}
0.529 for {'bootstrap': True, 'criterion': 'gini', 'n_estimators': 151}
0.516 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 10}
0.521 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 11}
0.521 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 12}
0.520 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 13}
0.524 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 14}
0.510 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 15}
0.525 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 16}
0.523 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 17}
0.512 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 18}
0.522 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 19}
0.526 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 20}
0.521 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 21}
0.516 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 22}
0.522 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 23}
0.526 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 24}
0.521 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 25}
0.520 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 26}
0.524 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 27}
0.517 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 28}
0.530 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 29}
0.521 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 30}
0.526 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 31}
0.517 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 32}
0.514 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 33}
0.520 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 34}
0.521 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 35}
0.527 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 36}
0.517 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 37}
0.525 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 38}
0.526 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 39}
0.520 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 40}
0.525 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 41}
0.524 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 42}
0.524 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 43}
0.521 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 44}
0.527 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 45}
0.524 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 46}
0.514 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 47}
0.513 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 48}
0.532 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 49}
0.520 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 50}
0.519 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 51}
0.530 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 52}
0.527 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 53}
0.523 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 54}
0.525 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 55}
0.532 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 56}
0.529 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 57}
0.528 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 58}
0.527 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 59}
0.524 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 60}
0.528 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 61}
0.526 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 62}
0.528 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 63}
0.528 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 64}
0.534 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 65}
0.523 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 66}
0.523 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 67}
0.524 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 68}
0.525 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 69}
0.533 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 70}
0.531 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 71}
0.525 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 72}
0.529 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 73}
0.528 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 74}
0.531 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 75}
0.524 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 76}
0.527 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 77}
0.526 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 78}
0.526 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 79}
0.526 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 80}
0.526 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 81}
0.530 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 82}
0.526 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 83}
0.524 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 84}
0.529 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 85}
0.529 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 86}
0.539 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 87}
0.528 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 88}
0.523 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 89}
0.535 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 90}
0.529 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 91}
0.525 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 92}
0.529 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 93}
0.525 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 94}
0.529 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 95}
0.529 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 96}
0.528 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 97}
0.530 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 98}
0.531 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 99}
0.528 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 100}
0.524 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 101}
0.536 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 102}
0.530 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 103}
0.523 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 104}
0.535 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 105}
0.526 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 106}
0.528 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 107}
0.527 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 108}
0.526 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 109}
0.527 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 110}
0.529 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 111}
0.528 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 112}
0.526 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 113}
0.533 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 114}
0.531 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 115}
0.528 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 116}
0.527 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 117}
0.530 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 118}
0.529 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 119}
0.529 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 120}
0.530 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 121}
0.527 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 122}
0.521 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 123}
0.534 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 124}
0.530 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 125}
0.528 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 126}
0.537 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 127}
0.530 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 128}
0.535 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 129}
0.532 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 130}
0.527 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 131}
0.531 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 132}
0.532 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 133}
0.529 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 134}
0.528 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 135}
0.531 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 136}
0.528 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 137}
0.531 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 138}
0.533 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 139}
0.522 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 140}
0.529 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 141}
0.530 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 142}
0.532 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 143}
0.534 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 144}
0.531 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 145}
0.533 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 146}
0.537 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 147}
0.537 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 148}
0.528 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 149}
0.529 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 150}
0.532 for {'bootstrap': True, 'criterion': 'entropy', 'n_estimators': 151}
0.510 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 10}
0.527 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 11}
0.518 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 12}
0.518 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 13}
0.519 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 14}
0.511 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 15}
0.525 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 16}
0.513 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 17}
0.528 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 18}
0.518 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 19}
0.518 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 20}
0.517 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 21}
0.514 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 22}
0.519 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 23}
0.520 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 24}
0.520 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 25}
0.524 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 26}
0.525 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 27}
0.527 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 28}
0.526 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 29}
0.523 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 30}
0.519 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 31}
0.522 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 32}
0.531 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 33}
0.526 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 34}
0.518 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 35}
0.527 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 36}
0.518 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 37}
0.528 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 38}
0.521 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 39}
0.525 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 40}
0.526 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 41}
0.522 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 42}
0.531 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 43}
0.521 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 44}
0.521 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 45}
0.517 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 46}
0.523 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 47}
0.525 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 48}
0.517 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 49}
0.526 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 50}
0.525 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 51}
0.532 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 52}
0.527 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 53}
0.525 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 54}
0.533 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 55}
0.522 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 56}
0.521 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 57}
0.527 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 58}
0.531 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 59}
0.527 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 60}
0.532 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 61}
0.529 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 62}
0.526 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 63}
0.523 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 64}
0.524 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 65}
0.530 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 66}
0.531 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 67}
0.525 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 68}
0.521 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 69}
0.520 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 70}
0.533 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 71}
0.534 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 72}
0.527 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 73}
0.522 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 74}
0.530 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 75}
0.530 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 76}
0.535 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 77}
0.521 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 78}
0.530 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 79}
0.532 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 80}
0.528 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 81}
0.530 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 82}
0.528 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 83}
0.534 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 84}
0.526 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 85}
0.527 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 86}
0.526 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 87}
0.533 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 88}
0.522 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 89}
0.528 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 90}
0.532 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 91}
0.531 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 92}
0.523 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 93}
0.524 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 94}
0.523 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 95}
0.529 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 96}
0.528 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 97}
0.528 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 98}
0.527 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 99}
0.525 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 100}
0.530 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 101}
0.523 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 102}
0.532 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 103}
0.533 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 104}
0.529 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 105}
0.527 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 106}
0.534 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 107}
0.524 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 108}
0.530 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 109}
0.523 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 110}
0.532 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 111}
0.527 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 112}
0.528 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 113}
0.532 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 114}
0.530 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 115}
0.534 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 116}
0.529 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 117}
0.524 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 118}
0.530 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 119}
0.522 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 120}
0.525 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 121}
0.533 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 122}
0.530 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 123}
0.527 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 124}
0.523 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 125}
0.530 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 126}
0.534 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 127}
0.529 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 128}
0.536 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 129}
0.532 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 130}
0.529 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 131}
0.531 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 132}
0.530 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 133}
0.527 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 134}
0.539 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 135}
0.527 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 136}
0.529 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 137}
0.534 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 138}
0.532 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 139}
0.531 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 140}
0.530 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 141}
0.530 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 142}
0.531 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 143}
0.527 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 144}
0.528 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 145}
0.527 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 146}
0.520 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 147}
0.528 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 148}
0.531 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 149}
0.531 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 150}
0.535 for {'bootstrap': False, 'criterion': 'gini', 'n_estimators': 151}
0.518 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 10}
0.519 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 11}
0.523 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 12}
0.515 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 13}
0.521 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 14}
0.519 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 15}
0.517 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 16}
0.513 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 17}
0.512 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 18}
0.525 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 19}
0.515 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 20}
0.523 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 21}
0.519 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 22}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 23}
0.527 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 24}
0.520 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 25}
0.524 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 26}
0.516 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 27}
0.519 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 28}
0.522 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 29}
0.524 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 30}
0.523 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 31}
0.529 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 32}
0.533 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 33}
0.521 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 34}
0.525 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 35}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 36}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 37}
0.521 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 38}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 39}
0.522 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 40}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 41}
0.521 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 42}
0.523 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 43}
0.524 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 44}
0.527 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 45}
0.529 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 46}
0.529 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 47}
0.527 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 48}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 49}
0.527 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 50}
0.528 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 51}
0.529 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 52}
0.528 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 53}
0.528 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 54}
0.531 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 55}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 56}
0.524 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 57}
0.525 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 58}
0.527 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 59}
0.522 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 60}
0.538 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 61}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 62}
0.532 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 63}
0.529 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 64}
0.534 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 65}
0.528 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 66}
0.520 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 67}
0.528 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 68}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 69}
0.532 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 70}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 71}
0.537 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 72}
0.529 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 73}
0.530 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 74}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 75}
0.530 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 76}
0.523 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 77}
0.521 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 78}
0.535 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 79}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 80}
0.528 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 81}
0.519 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 82}
0.529 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 83}
0.528 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 84}
0.529 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 85}
0.532 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 86}
0.529 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 87}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 88}
0.530 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 89}
0.525 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 90}
0.525 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 91}
0.531 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 92}
0.532 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 93}
0.531 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 94}
0.532 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 95}
0.532 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 96}
0.533 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 97}
0.531 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 98}
0.532 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 99}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 100}
0.527 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 101}
0.530 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 102}
0.522 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 103}
0.527 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 104}
0.528 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 105}
0.530 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 106}
0.531 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 107}
0.532 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 108}
0.530 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 109}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 110}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 111}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 112}
0.532 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 113}
0.533 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 114}
0.526 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 115}
0.528 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 116}
0.529 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 117}
0.527 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 118}
0.532 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 119}
0.529 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 120}
0.528 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 121}
0.534 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 122}
0.530 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 123}
0.529 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 124}
0.528 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 125}
0.529 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 126}
0.531 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 127}
0.531 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 128}
0.531 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 129}
0.533 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 130}
0.528 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 131}
0.527 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 132}
0.527 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 133}
0.529 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 134}
0.533 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 135}
0.533 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 136}
0.527 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 137}
0.534 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 138}
0.529 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 139}
0.528 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 140}
0.534 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 141}
0.527 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 142}
0.528 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 143}
0.525 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 144}
0.531 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 145}
0.523 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 146}
0.535 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 147}
0.521 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 148}
0.532 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 149}
0.529 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 150}
0.533 for {'bootstrap': False, 'criterion': 'entropy', 'n_estimators': 151}
```

```
Detailed classification report:

RANDOM FOREST MODEL ACCURACY: 0.5285
```

# Baseline model
```
Best parameters set found on training set:

{'strategy': 'most_frequent'}

Grid scores on training set:

0.5 for {'strategy': 'most_frequent'}
```

```
Detailed classification report:

DUMMY MODEL ACCURACY: 0.5
```

# Final linear model
```
LINEAR MODEL ACCURACY: 0.548
```

# PRECISION & RECALL
```
LINEAR MODEL PRECISION: 0.5383159886471145
LINEAR MODEL RECALL: 0.5695695695695696

KNN MODEL PRECISION: 0.5215264187866928
KNN MODEL RECALL: 0.5335335335335335

DECISION TREE MODEL PRECISION: 0.5112474437627812
DECISION TREE MODEL RECALL: 0.5005005005005005

RANDOM FOREST MODEL PRECISION: 0.5271844660194175
RANDOM FOREST MODEL RECALL: 0.5435435435435435

BASELINE MODEL PRECISION: 0.5
BASELINE MODEL RECALL: 1.0

FINAL TEST LINEAR MODEL PRECISION: 0.5402985074626866
FINAL TEST LINEAR MODEL RECALL: 0.5512690355329949
```
