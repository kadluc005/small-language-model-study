from src.import_data import names
import torch
import torch.nn.functional as F

from src.vocabulary import stoi, itos

X, Y = [], []

for name in names:
    context = [0]

    for ch in (*name , '<end>',):
        ix = stoi[ch]
        X.append(context)
        Y.append(ix)

        context = context[1:] + [ix]
# print(X[:10])
# print(Y[:10])
# print(len(X))
# print(len(Y))

# print(len(X) == len(Y))

# r = sum(len(name) + 1 for name in names)
# print(r == len(X))

X , Y = torch.tensor(X), torch.tensor(Y)


X_encoded = F.one_hot(X, num_classes=28)
X_encoded = torch.squeeze(X_encoded).float()
