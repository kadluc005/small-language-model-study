# Investigating How Small Neural Language Models Learn

<!-- Qu'est-ce que j'essaie de faire ?
Pourquoi je le fais ?
Qu'est-ce que je prédis avant l'expérience ?
Qu'est-ce que l'expérience m'a réellement montré ? -->

## 1. Dataset

The project uses a dataset of 32,033 names, with one name per line.

### Dataset exploration

Initial exploration gave the following results:

- Number of names: 32,033
- Shortest name: `an` (2 characters)
- Longest name: `muhammadibrahim` (15 characters)
- Average name length: 6.12 characters
- Number of unique characters: 26
- Character set: `a-z`

### Vocabulary

To make the data usable by a neural network, characters are mapped to integer IDs.

Two special tokens are added:

- `<start>` — marks the beginning of a name
- `<end>` — marks the end of a name

The resulting vocabulary contains 28 tokens:

- 26 lowercase letters
- 1 start token
- 1 end token

Two mappings are used:

- `stoi`: string → integer
- `itos`: integer → string

## 2. Bigram Dataset

- Definition of a bigram
- X represents the character that we take to predict the next one.
- Y represents the target character, witch is the next character after X
- Example using "emma"
- Number of training examples: 228,146
- Each name produces len(name) + 1 training examples. The reason is that for one name with `len(name)=n`, there are `n+1` transitions.

```python
    <start> → c1
    c1      → c2
    ...
    cn      → <end>
```

### One-hot Encoding

Each token is represented by a vector of 28 values. Only one value is 1 and the others are 0.
Each row will have an output 28 scores.
The 28 scores represents the 28 tokens that its possible to predict.
These scores are called **logits**. The softmax activation function will later convert these logits into probabilities.

### Softmax

The logits values are just random values. They might not be easy to be interpreted. There is where the soft max function comes in.

$$
\operatorname{softmax}(z_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}
$$

The softmax funtion does two things essentially:

- $e^{z_i}$ makes the values positives
- It normalises them so that their sum returns 1.

## 3. Baseline

* Model architecutre:
    * input: one-hot encoded character with 28 dimensions
    * weight matrix: 28 × 28
    * output: 28 logits
    * softmax converts logits into probabilities
    * loss: negative log-likelihood
* Initial loss: 3.8508
* The weights are randomly initialized


