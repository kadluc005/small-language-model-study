import torch
from src.create_bigram_dataset import X_encoded

# create the Weight matrices with random values

W = torch.randn((28, 28), requires_grad=True)
X = X_encoded

logits = X @ W

print(X.shape)
print(logits.shape)